// -*- C++ -*-
//
// Package:    MuonIdSelector
// Class:      MuonIdSelector
// 
/**\class MuonIdSelector MuonIdSelector.cc WHAnalysis/MuonIdSelector/src/MuonIdSelector.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Thu Nov 24 08:36:45 CET 2011
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include <vector> 
#include <TMath.h>
#include <string>
//
// class declaration
//

class MuonIdSelector : public edm::EDProducer {
   public:
      explicit MuonIdSelector(const edm::ParameterSet&);
      ~MuonIdSelector();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag srcBeamSpot_;
      edm::InputTag srcVertex_;
      edm::InputTag muonSrc_;

      bool applyGlobalMuonPromptTight_;
      bool applyAllArbitrated_;

      double maxIPxy_; // max. transverse impact parameter of muon track
      double maxIPz_; // max. longitudinal impact parameter of muon track

      int IPtrackType_; // compute impact parameters for inner/global track of muon
      int IPrefType_; // compute impact parameters wrt. beam spot/reconstructed event vertex

      double maxChi2red_; // max. (normalized) chi^2 of global muon track fit per degree of freedom
      double maxDptOverPt_; // max. relative error on muon momentum (computed for inner track)

      unsigned minTrackerHits_; // min. number of hits in SiStrip + Pixel detectors
      unsigned minPixelHits_; // min. number of hits in Pixel detector

      unsigned minMuonStations_; // min. number of hits in Muon chambers
      unsigned minMatchedSegments_; // min. number of segments in Muon stations matched to inner track 

};

   template<typename T>
   bool isValidRef(const edm::Ref<T>& ref)
   {
	return ( (ref.isAvailable() || ref.isTransient()) && ref.isNonnull() );
   }

//
// constants, enums and typedefs
//

   enum { InnerTrack, GlobalTrack };
   enum { BeamSpot, Vertex };

   bool defaultApplyGlobalMuonPromptTight_ = true;
   bool defaultApplyAllArbitrated_ = true;

   double defaultMaxIPxy_ = 0.02; // cm
   double defaultMaxIPz_ = 1.e+3;

   int defaultIPtrackType_ = InnerTrack;
   int defaultIPrefType_ = Vertex;

   double defaultMaxChi2red_ = 10.; // chi^2/nDoF
   double defaultMaxDptOverPt_ = 0.10;

   unsigned defaultMinTrackerHits_ = 10;
   unsigned defaultMinPixelHits_ = 1;

   unsigned defaultMinMuonStations_ = 2;
   unsigned defaultMinMatchedSegments_ = 1;

//
// static data member definitions
//

//
// constructors and destructor
//
MuonIdSelector::MuonIdSelector(const edm::ParameterSet& iConfig):
   srcBeamSpot_(iConfig.getParameter<edm::InputTag>("beamSpotSource")),
   srcVertex_(iConfig.getParameter<edm::InputTag>("vertexSource")),
   muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc")),
   applyGlobalMuonPromptTight_(iConfig.getParameter<bool>("applyGlobalMuonPromptTight")),
   applyAllArbitrated_(iConfig.getParameter<bool>("applyAllArbitrated")),
   maxIPxy_(iConfig.getParameter<double>("maxIPxy")),
   maxIPz_(iConfig.getParameter<double>("maxIPz")),
   maxChi2red_(iConfig.getParameter<double>("maxChi2red")),
   maxDptOverPt_(iConfig.getParameter<double>("maxDptOverPt")),
   minTrackerHits_(iConfig.getParameter<unsigned>("minTrackerHits")),
   minPixelHits_(iConfig.getParameter<unsigned>("minPixelHits")),
   minMuonStations_(iConfig.getParameter<unsigned>("minMuonStations")),
   minMatchedSegments_(iConfig.getParameter<unsigned>("minMatchedSegments"))
{
   //register your products
/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
 
   //if you want to put into the Run
   produces<ExampleData2,InRun>();
*/
   //now do what ever other initialization is needed

   produces<pat::MuonCollection>("selectedMuonsByID").setBranchAlias("selectedMuonsByID");
   produces<pat::MuonCollection>("badMuonsByID").setBranchAlias("badMuonsByID");
}


MuonIdSelector::~MuonIdSelector()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
MuonIdSelector::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
/* This is an event example
   //Read 'ExampleData' from the Event
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   std::auto_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
   iEvent.put(pOut);
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/

   //--- define default muon selection criteria used by WW cross-section analysis,
   // as documented in CMS AN-10/344
   // (to be used in case selection criteria are not specified explicitely)

   edm::Handle<edm::View<pat::Muon> > muons;
   iEvent.getByLabel(muonSrc_,muons);

   std::auto_ptr<pat::MuonCollection> selectedMuonsByID(new pat::MuonCollection);
   std::auto_ptr<pat::MuonCollection> badMuonsByID(new pat::MuonCollection);

   reco::TrackBase::Point IPrefPoint;
   bool IPrefPoint_initialized = false;

   IPrefType_ = Vertex;
   IPtrackType_ = InnerTrack;

   if(true){
    	edm::Handle<reco::VertexCollection> recoVertices;
	iEvent.getByLabel(srcVertex_, recoVertices);
	for(reco::VertexCollection::const_iterator recoVertex = recoVertices->begin(); recoVertex != recoVertices->end(); ++recoVertex){
		if(recoVertex->tracksSize() > 0){
			IPrefPoint = recoVertex->position();
			IPrefPoint_initialized = true;
			break;
		}
	}
   }

   if(false){
	edm::Handle<reco::BeamSpot> beamSpot;
	iEvent.getByLabel(srcBeamSpot_, beamSpot);
	IPrefPoint = beamSpot->position();
   }

   for( edm::View<pat::Muon>::const_iterator patMuon=muons->begin(); patMuon!=muons->end(); ++patMuon ) {

	if ( !patMuon->isGlobalMuon() ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if ( !patMuon->isTrackerMuon() ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if ( !isValidRef(patMuon->globalTrack()) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if ( !isValidRef(patMuon->innerTrack()) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}

	if ( applyGlobalMuonPromptTight_ && !muon::isGoodMuon(*patMuon, muon::GlobalMuonPromptTight) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if ( applyAllArbitrated_ && !muon::isGoodMuon(*patMuon, muon::AllArbitrated) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}

	reco::TrackRef muonTrack;
	if ( IPtrackType_ == InnerTrack ) muonTrack = patMuon->innerTrack();
	else if ( IPtrackType_ == GlobalTrack ) muonTrack = patMuon->globalTrack();
	if ( !isValidRef(muonTrack) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if ( !(TMath::Abs(muonTrack->dxy(IPrefPoint)) < maxIPxy_) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if ( !(TMath::Abs(muonTrack->dz(IPrefPoint)) < maxIPz_) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}

	if ( !(patMuon->globalTrack()->normalizedChi2() < maxChi2red_) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if ( !(patMuon->innerTrack()->ptError() < (maxDptOverPt_*patMuon->innerTrack()->pt())) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}

	const reco::HitPattern& innerTrackHitPattern = patMuon->innerTrack()->hitPattern();
	if ( !(innerTrackHitPattern.numberOfValidTrackerHits() >= (int)minTrackerHits_) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if ( !(innerTrackHitPattern.numberOfValidPixelHits() >= (int)minPixelHits_) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}

	//---------------------------------------------------------------------------
	// compute numbers of muon stations with matched segments
	//
	// CV: code copied from version 1.41 of DataFormats/MuonReco/src/Muon.cc
	// (not included in CMSSW_3_8_x yet)
	//
	int numMuonStations = 0;
	
	unsigned int theStationMask = (unsigned int)patMuon->stationMask(reco::Muon::SegmentAndTrackArbitration);
	for( int i = 0; i < 8; ++i ){ // eight stations, eight bits
		if ( theStationMask & (1<<i) ) ++numMuonStations;
	}
	//---------------------------------------------------------------------------

	if ( !(numMuonStations >= (int)minMuonStations_) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if ( !(patMuon->numberOfMatches() >= (int)minMatchedSegments_) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	
	selectedMuonsByID->push_back(*patMuon);

	if ( !(patMuon->userFloat("PFRelIsoDB04v2") < 0.3) ) {
		badMuonsByID->push_back(*patMuon);
		continue;}
	if( !(TMath::Abs(patMuon->eta()) < 2.1) ) {
		badMuonsByID->push_back(*patMuon);
		continue;} 
   } 

   iEvent.put(selectedMuonsByID, "selectedMuonsByID");
   iEvent.put(badMuonsByID, "badMuonsByID");
}

// ------------ method called once each job just before starting event loop  ------------
void 
MuonIdSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MuonIdSelector::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
MuonIdSelector::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
MuonIdSelector::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
MuonIdSelector::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
MuonIdSelector::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MuonIdSelector::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MuonIdSelector);
