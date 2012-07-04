// -*- C++ -*-
//
// Package:    MuonsUserEmbedded
// Class:      MuonsUserEmbedded
// 
/**\class MuonsUserEmbedded MuonsUserEmbedded.cc WHAnalysis/MuonsUserEmbedded/src/MuonsUserEmbedded.cc

 Description: [one line class summary]

 Implementation: 
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Tue Nov 22 12:02:59 CET 2011
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"


//
// class declaration
//

class MuonsUserEmbedded : public edm::EDProducer {
   public:
      explicit MuonsUserEmbedded(const edm::ParameterSet&);
      ~MuonsUserEmbedded();

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

     edm::InputTag muonTag_;
     edm::InputTag vertexTag_;

     reco::isodeposit::AbsVetos vetos2010Charged_;
     reco::isodeposit::AbsVetos vetos2010Neutral_;  
     reco::isodeposit::AbsVetos vetos2010Photons_;

     reco::isodeposit::AbsVetos vetos2011Charged_; 
     reco::isodeposit::AbsVetos vetos2011Neutral_;  
     reco::isodeposit::AbsVetos vetos2011Photons_;
};

   template<typename T>
   bool isValidRef(const edm::Ref<T>& ref)
   {
	return ( (ref.isAvailable() || ref.isTransient()) && ref.isNonnull() );
   }

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
MuonsUserEmbedded::MuonsUserEmbedded(const edm::ParameterSet& iConfig)
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

  muonTag_ = iConfig.getParameter<edm::InputTag>("muonTag");
  vertexTag_ = iConfig.getParameter<edm::InputTag>("vertexTag");
 
  produces<pat::MuonCollection>("");
  
}


MuonsUserEmbedded::~MuonsUserEmbedded()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
MuonsUserEmbedded::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  edm::Handle<pat::MuonCollection> muonsHandle;
  iEvent.getByLabel(muonTag_,muonsHandle);
  const pat::MuonCollection* muons = muonsHandle.product();

  edm::Handle<reco::VertexCollection> vertexHandle;
  iEvent.getByLabel(vertexTag_,vertexHandle);
  const reco::VertexCollection* vertexes = vertexHandle.product();

  std::auto_ptr< pat::MuonCollection > muonsUserEmbeddedColl( new pat::MuonCollection() ) ;

  for(unsigned int i = 0; i < muons->size(); i++){
    pat::Muon aMuon( (*muons)[i] );
   
    double dxyWrtPV =  -99.;
    double dzWrtPV  =  -99.;

    if(vertexes->size()!=0 && aMuon.isGlobalMuon()){
      dxyWrtPV = (aMuon.globalTrack())->dxy( (*vertexes)[0].position() ) ;
      dzWrtPV  = (aMuon.globalTrack())->dz( (*vertexes)[0].position() ) ;
    }
    else if (vertexes->size()!=0 && aMuon.isTrackerMuon()){
      dxyWrtPV = (aMuon.innerTrack())->dxy( (*vertexes)[0].position() ) ;
      dzWrtPV  = (aMuon.innerTrack())->dz( (*vertexes)[0].position() ) ;
    }

    aMuon.addUserFloat("dxyWrtPV",dxyWrtPV);
    aMuon.addUserFloat("dzWrtPV",dzWrtPV);

    int isGlobalMuon_ = 1;
    int isTrackerMuon_ = 1;
    int globalMuonPromptTight_ = 1;
    int allArbitrated_ = 1;
    double normalizeChi2_ = -99;
    double ptError_ = -99;
    int innerTrackHitPattern_ = 99;
    int numberOfValidPixelHits_ = 99;
    int numMuonStations_ = 99;
    int numberOfMatches_ = 99;

    isGlobalMuon_ = aMuon.isGlobalMuon();
    isTrackerMuon_ = aMuon.isTrackerMuon();

    bool validRefGlob = isValidRef(aMuon.globalTrack());
    bool validRefInn = isValidRef(aMuon.innerTrack());

    if(validRefGlob && validRefInn){

	globalMuonPromptTight_ = muon::isGoodMuon(aMuon, muon::GlobalMuonPromptTight);
	allArbitrated_ =  muon::isGoodMuon(aMuon, muon::AllArbitrated);

	reco::TrackRef muonTrack;
	if (isValidRef(muonTrack)) {

		normalizeChi2_ = aMuon.globalTrack()->normalizedChi2();
		ptError_ = (aMuon.innerTrack()->ptError())/(aMuon.innerTrack()->pt()); 

		const reco::HitPattern& innerTrackHitPattern = aMuon.innerTrack()->hitPattern();
		innerTrackHitPattern_ = innerTrackHitPattern.numberOfValidTrackerHits();
		numberOfValidPixelHits_ = innerTrackHitPattern.numberOfValidPixelHits();

	      	int numMuonStations = 0;
		unsigned int theStationMask = (unsigned int)aMuon.stationMask(reco::Muon::SegmentAndTrackArbitration);
		for( int i = 0; i < 8; ++i ){ // eight stations, eight bits
			if ( theStationMask & (1<<i) ) ++numMuonStations;
		}

		numMuonStations_ = numMuonStations;
		numberOfMatches_ = aMuon.numberOfMatches();

	}
    }

    int muonID = isGlobalMuon_ && isTrackerMuon_ && globalMuonPromptTight_ && allArbitrated_ && (fabs(dxyWrtPV) < 0.02) && (fabs(dzWrtPV) < 0.2) && (normalizeChi2_ < 10) && (ptError_ < 0.1) && (innerTrackHitPattern_ >= 10) && (numberOfValidPixelHits_ >= 1) && (numMuonStations_ >= 2) && (numberOfMatches_ >= 1);

    //std::cout<<"isGlobal: "<< isGlobalMuon_<<" isTracker: "<<isTrackerMuon_<<" globalMuonPromptTight: "<<globalMuonPromptTight_<<" allArbitrated"<< allArbitrated_<<" dxyWrtPV: "<<dxyWrtPV<<" dzWrtPV: "<<dzWrtPV<<" normalizeChi2: "<<normalizeChi2_<<" ptError: "<<ptError_<<" innerTrackHitPattern: "<<innerTrackHitPattern_<<" numberOfValidPixelHits: "<<numberOfValidPixelHits_<<" numMuonStations: "<<numMuonStations_<<" numberOfMatches: "<<numberOfMatches_<<std::endl;

    //std::cout<<"Total ID: "<<muonID<<std::endl;

    aMuon.addUserInt("isGlobalMuon",isGlobalMuon_);
    aMuon.addUserInt("isTrackerMuon",isTrackerMuon_);
    aMuon.addUserInt("globalMuonPromptTight",globalMuonPromptTight_);
    aMuon.addUserInt("allArbitrated",allArbitrated_);
    aMuon.addUserFloat("normalizeChi2",normalizeChi2_);
    aMuon.addUserFloat("ptError",ptError_);
    aMuon.addUserInt("innerTrackHitPattern",innerTrackHitPattern_);
    aMuon.addUserInt("numberOfValidPixelHits",numberOfValidPixelHits_);
    aMuon.addUserInt("numMuonStations",numMuonStations_);
    aMuon.addUserInt("numberOfMatches",numberOfMatches_);
    aMuon.addUserInt("muonID",muonID);

    // iso deposits
    reco::isodeposit::AbsVetos vetos2010Charged;
    reco::isodeposit::AbsVetos vetos2010Neutral;  
    reco::isodeposit::AbsVetos vetos2010Photons;
    reco::isodeposit::AbsVetos vetos2011Charged; 
    reco::isodeposit::AbsVetos vetos2011Neutral;  
    reco::isodeposit::AbsVetos vetos2011Photons;

    vetos2010Charged.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aMuon.eta(),aMuon.phi()),0.01));
    vetos2010Charged.push_back(new reco::isodeposit::ThresholdVeto(0.5));
    vetos2010Neutral.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aMuon.eta(),aMuon.phi()),0.08));
    vetos2010Neutral.push_back(new reco::isodeposit::ThresholdVeto(1.0));
    vetos2010Photons.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aMuon.eta(),aMuon.phi()),0.05));
    vetos2010Photons.push_back(new reco::isodeposit::ThresholdVeto(1.0));
    
    vetos2011Charged.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aMuon.eta(),aMuon.phi()),0.01));
    vetos2011Charged.push_back(new reco::isodeposit::ThresholdVeto(0.5));//it was 0.0
    vetos2011Neutral.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aMuon.eta(),aMuon.phi()),0.01));
    vetos2011Neutral.push_back(new reco::isodeposit::ThresholdVeto(0.5));
    vetos2011Photons.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aMuon.eta(),aMuon.phi()),0.01));
    vetos2011Photons.push_back(new reco::isodeposit::ThresholdVeto(0.5));

    float chIso03v1 = 
      aMuon.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.3, vetos2010Charged).first;
    float nhIso03v1 = 
      aMuon.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.3, vetos2010Neutral).first;
    float phIso03v1 = 
      aMuon.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.3, vetos2010Photons).first;
    float nhIsoPU03v1 = 
      aMuon.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2010Neutral).first;
    float phIsoPU03v1 = 
      aMuon.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2010Photons).first;

    float chIso04v1 = 
      aMuon.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.4, vetos2010Charged).first;
    float nhIso04v1 = 
      aMuon.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2010Neutral).first;
    float phIso04v1 = 
      aMuon.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2010Photons).first;
    float nhIsoPU04v1 = 
      aMuon.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2010Neutral).first;
    float phIsoPU04v1 = 
      aMuon.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2010Photons).first;

    float chIso03v2 = 
      aMuon.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.3, vetos2011Charged).first;
    float nhIso03v2 = 
      aMuon.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.3, vetos2011Neutral).first;
    float phIso03v2 = 
      aMuon.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.3, vetos2011Photons).first;
    float nhIsoPU03v2 = 
      aMuon.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2011Neutral).first;
    float phIsoPU03v2 = 
      aMuon.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2011Photons).first;

    float chIso04v2 = 
      aMuon.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.4, vetos2011Charged).first;
    float nhIso04v2 = 
      aMuon.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2011Neutral).first;
    float phIso04v2 = 
      aMuon.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2011Photons).first;
    float nhIsoPU04v2 = 
      aMuon.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2011Neutral).first;
    float phIsoPU04v2 = 
      aMuon.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2011Photons).first;


    aMuon.addUserFloat("PFRelIso04v1",(chIso04v1+nhIso04v1+phIso04v1)/aMuon.pt());
    aMuon.addUserFloat("PFRelIso03v1",(chIso03v1+nhIso03v1+phIso03v1)/aMuon.pt());
    aMuon.addUserFloat("PFRelIsoDB04v1",(chIso04v1+std::max(nhIso04v1+phIso04v1-0.5*0.5*(nhIsoPU04v1+phIsoPU04v1),0.0))/aMuon.pt());
    aMuon.addUserFloat("PFRelIsoDB03v1",(chIso03v1+std::max(nhIso03v1+phIso03v1-0.5*0.5*(nhIsoPU03v1+phIsoPU03v1),0.0))/aMuon.pt());

    aMuon.addUserFloat("PFRelIso04v2",(chIso04v2+nhIso04v2+phIso04v2)/aMuon.pt());
    aMuon.addUserFloat("PFRelIso03v2",(chIso03v2+nhIso03v2+phIso03v2)/aMuon.pt());
    aMuon.addUserFloat("PFRelIsoDB04v2",(chIso04v2+std::max(nhIso04v2+phIso04v2-0.5*0.5*(nhIsoPU04v2+phIsoPU04v2),0.0))/aMuon.pt());
    aMuon.addUserFloat("PFRelIsoDB03v2",(chIso03v2+std::max(nhIso03v2+phIso03v2-0.5*0.5*(nhIsoPU03v2+phIsoPU03v2),0.0))/aMuon.pt());

    // cleaning
    for(unsigned int i = 0; i <vetos2010Charged.size(); i++){
      delete vetos2010Charged[i];
    }
    for(unsigned int i = 0; i <vetos2010Neutral.size(); i++){
      delete vetos2010Neutral[i];
      delete vetos2010Photons[i];
    }
    for(unsigned int i = 0; i <vetos2011Charged.size(); i++){
      delete vetos2011Charged[i];
    }
    for(unsigned int i = 0; i <vetos2011Neutral.size(); i++){
      delete vetos2011Neutral[i];
      delete vetos2011Photons[i];
    }

    aMuon.addUserFloat("isInRun",iEvent.run());

    muonsUserEmbeddedColl->push_back(aMuon);

  }


  iEvent.put( muonsUserEmbeddedColl );
  return;
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
MuonsUserEmbedded::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MuonsUserEmbedded::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
MuonsUserEmbedded::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
MuonsUserEmbedded::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
MuonsUserEmbedded::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
MuonsUserEmbedded::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MuonsUserEmbedded::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MuonsUserEmbedded);
