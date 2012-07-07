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
#include "DataFormats/MuonReco/interface/Muon.h"

#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"

#include "Muon/MuonAnalysisTools/interface/MuonMVAEstimator.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/TransientTrack/plugins/TransientTrackBuilderESProducer.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/GeometryVector/interface/VectorUtil.h"

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

     bool doMuIdMVA_;
     bool doMuIsoMVA_;
     bool doMuIsoRingsRadMVA_;
     bool doMuIdIsoCombMVA_;
     std::string target;
     MuonEffectiveArea::MuonEffectiveAreaTarget target_;

     MuonMVAEstimator* fMuonIDMVA_;
     MuonMVAEstimator* fMuonIsoMVA_;
     MuonMVAEstimator* fMuonIsoRingsRadMVA_;
     MuonMVAEstimator* fMuonIDIsoCombinedMVA_;

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

  muonTag_ = iConfig.getParameter<edm::InputTag>("muonTag");
  vertexTag_ = iConfig.getParameter<edm::InputTag>("vertexTag");

  doMuIdMVA_ = iConfig.getParameter<bool>("doMuIdMVA");
  doMuIsoMVA_ = iConfig.getParameter<bool>("doMuIsoMVA");
  doMuIsoRingsRadMVA_ = iConfig.getParameter<bool>("doMuIsoRingsRadMVA");
  doMuIdIsoCombMVA_ = iConfig.getParameter<bool>("doMuIdIsoCombMVA");
  target = iConfig.getParameter<std::string>("target");

  if( doMuIdMVA_ ){

   fMuonIDMVA_ = new MuonMVAEstimator();
   edm::FileInPath inputFileName0 = iConfig.getParameter<edm::FileInPath>("inputFileName0");
   edm::FileInPath inputFileName1 = iConfig.getParameter<edm::FileInPath>("inputFileName1");
   edm::FileInPath inputFileName2 = iConfig.getParameter<edm::FileInPath>("inputFileName2");
   edm::FileInPath inputFileName3 = iConfig.getParameter<edm::FileInPath>("inputFileName3");
   edm::FileInPath inputFileName4 = iConfig.getParameter<edm::FileInPath>("inputFileName4");
   edm::FileInPath inputFileName5 = iConfig.getParameter<edm::FileInPath>("inputFileName5");   

   vector<string> muonid_weightfiles;
   muonid_weightfiles.push_back(inputFileName0.fullPath().data());
   muonid_weightfiles.push_back(inputFileName1.fullPath().data());
   muonid_weightfiles.push_back(inputFileName2.fullPath().data());
   muonid_weightfiles.push_back(inputFileName3.fullPath().data());
   muonid_weightfiles.push_back(inputFileName4.fullPath().data());
   muonid_weightfiles.push_back(inputFileName5.fullPath().data());  

   fMuonIDMVA_->initialize("MuonID_BDTG",
                           MuonMVAEstimator::kID,
                           kTRUE,
                           muonid_weightfiles); 
  }

  if( doMuIsoMVA_ ){

   fMuonIsoMVA_ = new MuonMVAEstimator();
   edm::FileInPath inputFileName0v2 = iConfig.getParameter<edm::FileInPath>("inputFileName0v2");
   edm::FileInPath inputFileName1v2 = iConfig.getParameter<edm::FileInPath>("inputFileName1v2");
   edm::FileInPath inputFileName2v2 = iConfig.getParameter<edm::FileInPath>("inputFileName2v2");
   edm::FileInPath inputFileName3v2 = iConfig.getParameter<edm::FileInPath>("inputFileName3v2");
   edm::FileInPath inputFileName4v2 = iConfig.getParameter<edm::FileInPath>("inputFileName4v2");
   edm::FileInPath inputFileName5v2 = iConfig.getParameter<edm::FileInPath>("inputFileName5v2");   

   vector<string> muoniso_weightfiles;
   muoniso_weightfiles.push_back(inputFileName0v2.fullPath().data());
   muoniso_weightfiles.push_back(inputFileName1v2.fullPath().data());
   muoniso_weightfiles.push_back(inputFileName2v2.fullPath().data());
   muoniso_weightfiles.push_back(inputFileName3v2.fullPath().data());
   muoniso_weightfiles.push_back(inputFileName4v2.fullPath().data());
   muoniso_weightfiles.push_back(inputFileName5v2.fullPath().data());   
   fMuonIsoMVA_->initialize("MuonIso_BDTG_IsoRings",
	    		    MuonMVAEstimator::kIsoRings,
 	    		    kTRUE,
 	    		    muoniso_weightfiles);
  }

  if( doMuIsoRingsRadMVA_ ){

   fMuonIsoRingsRadMVA_ = new MuonMVAEstimator();
   edm::FileInPath inputFileName0v3 = iConfig.getParameter<edm::FileInPath>("inputFileName0v3");
   edm::FileInPath inputFileName1v3 = iConfig.getParameter<edm::FileInPath>("inputFileName1v3");
   edm::FileInPath inputFileName2v3 = iConfig.getParameter<edm::FileInPath>("inputFileName2v3");
   edm::FileInPath inputFileName3v3 = iConfig.getParameter<edm::FileInPath>("inputFileName3v3");
   edm::FileInPath inputFileName4v3 = iConfig.getParameter<edm::FileInPath>("inputFileName4v3");
   edm::FileInPath inputFileName5v3 = iConfig.getParameter<edm::FileInPath>("inputFileName5v3");   

   vector<string> muonisoRingsRad_weightfiles;
   muonisoRingsRad_weightfiles.push_back(inputFileName0v3.fullPath().data());
   muonisoRingsRad_weightfiles.push_back(inputFileName1v3.fullPath().data());
   muonisoRingsRad_weightfiles.push_back(inputFileName2v3.fullPath().data());
   muonisoRingsRad_weightfiles.push_back(inputFileName3v3.fullPath().data());
   muonisoRingsRad_weightfiles.push_back(inputFileName4v3.fullPath().data());
   muonisoRingsRad_weightfiles.push_back(inputFileName5v3.fullPath().data());   
   fMuonIsoRingsRadMVA_->initialize("MuonIso_BDTG_IsoRingsRad",
                                    MuonMVAEstimator::kIsoRingsRadial,
                                    kTRUE,
                                    muonisoRingsRad_weightfiles);
  }

  if( doMuIdIsoCombMVA_ ){

   fMuonIDIsoCombinedMVA_ = new MuonMVAEstimator();
   edm::FileInPath inputFileName0v4 = iConfig.getParameter<edm::FileInPath>("inputFileName0v4");
   edm::FileInPath inputFileName1v4 = iConfig.getParameter<edm::FileInPath>("inputFileName1v4");
   edm::FileInPath inputFileName2v4 = iConfig.getParameter<edm::FileInPath>("inputFileName2v4");
   edm::FileInPath inputFileName3v4 = iConfig.getParameter<edm::FileInPath>("inputFileName3v4");
   edm::FileInPath inputFileName4v4 = iConfig.getParameter<edm::FileInPath>("inputFileName4v4");  

   vector<string> muonidiso_weightfiles;
   muonidiso_weightfiles.push_back(inputFileName0v4.fullPath().data());
   muonidiso_weightfiles.push_back(inputFileName1v4.fullPath().data());
   muonidiso_weightfiles.push_back(inputFileName2v4.fullPath().data());
   muonidiso_weightfiles.push_back(inputFileName3v4.fullPath().data());
   muonidiso_weightfiles.push_back(inputFileName4v4.fullPath().data());   
   fMuonIDIsoCombinedMVA_->initialize("MuonIso_BDTG_IsoRings",
                                      MuonMVAEstimator::kIDIsoRingsCombined,
                                      kTRUE,
                                      muonidiso_weightfiles);
  }
 
  produces<pat::MuonCollection>("");
  
}


MuonsUserEmbedded::~MuonsUserEmbedded()
{
 
   if(doMuIdMVA_) delete fMuonIDMVA_;
   if(doMuIsoMVA_) delete fMuonIsoMVA_;
   if(doMuIsoRingsRadMVA_) delete fMuonIsoRingsRadMVA_;
   if(doMuIdIsoCombMVA_) delete fMuonIDIsoCombinedMVA_;

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
MuonsUserEmbedded::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;

  edm::Handle<pat::MuonCollection> muonsHandle;
  iEvent.getByLabel(muonTag_,muonsHandle);
  const pat::MuonCollection* muons = muonsHandle.product();

  edm::Handle<reco::MuonCollection> recoMuonsHandle;
  iEvent.getByLabel("muons",recoMuonsHandle);
  const reco::MuonCollection* recoMuons = recoMuonsHandle.product();

  edm::Handle<reco::VertexCollection> vertexHandle;
  iEvent.getByLabel(vertexTag_,vertexHandle);
  const reco::VertexCollection* vertexes = vertexHandle.product();

  edm::Handle<reco::PFCandidateCollection> pfHandle;
  iEvent.getByLabel("particleFlow",pfHandle);
  if( !pfHandle.isValid() )  
    edm::LogError("DataNotAvailable")
      << "No pf particles label available \n";
  const reco::PFCandidateCollection* pfCandidates = pfHandle.product();

  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  edm::Handle<reco::VertexCollection> hVertex;
  iEvent.getByLabel("offlinePrimaryVertices", hVertex);
  const reco::VertexCollection *pvCol = hVertex.product();

  Handle<double> hRho;
  edm::InputTag tag("kt6PFJets","rho");
  iEvent.getByLabel(tag,hRho);
  double Rho = *hRho;

  Handle<reco::PFCandidateCollection> hPfCandProduct;
  iEvent.getByLabel("particleFlow", hPfCandProduct);
  const reco::PFCandidateCollection &inPfCands = *(hPfCandProduct.product());

  reco::MuonCollection IdentifiedMuons;

  InputTag gsfEleLabel(string("gsfElectrons"));
  Handle<reco::GsfElectronCollection> theEGammaCollection;
  iEvent.getByLabel(gsfEleLabel,theEGammaCollection);
  const reco::GsfElectronCollection inElectrons = *(theEGammaCollection.product());

  reco::GsfElectronCollection IdentifiedElectrons;

  for (reco::GsfElectronCollection::const_iterator iE = inElectrons.begin(); 
       iE != inElectrons.end(); ++iE) {

    double electronTrackZ = 0;
    if (iE->gsfTrack().isNonnull()) {
      electronTrackZ = iE->gsfTrack()->dz(pvCol->at(0).position());
    } else if (iE->closestCtfTrackRef().isNonnull()) {
      electronTrackZ = iE->closestCtfTrackRef()->dz(pvCol->at(0).position());
    }    
    if(fabs(electronTrackZ) > 0.2)  continue;

    
    if(fabs(iE->superCluster()->eta())<1.479) {     
      if(iE->pt() > 20) {
        if(iE->sigmaIetaIeta()       > 0.01)  continue;
        if(fabs(iE->deltaEtaSuperClusterTrackAtVtx()) > 0.007) continue;
        if(fabs(iE->deltaPhiSuperClusterTrackAtVtx()) > 0.8)  continue;
        if(iE->hadronicOverEm()       > 0.15)  continue;    
      } else {
        if(iE->sigmaIetaIeta()       > 0.012)  continue;
        if(fabs(iE->deltaEtaSuperClusterTrackAtVtx()) > 0.007) continue;
        if(fabs(iE->deltaPhiSuperClusterTrackAtVtx()) > 0.8)  continue;
        if(iE->hadronicOverEm()       > 0.15) continue;    
      } 
    } else {     
      if(iE->pt() > 20) {
        if(iE->sigmaIetaIeta()       > 0.03)  continue;
        if(fabs(iE->deltaEtaSuperClusterTrackAtVtx()) > 0.010) continue;
        if(fabs(iE->deltaPhiSuperClusterTrackAtVtx()) > 0.8)  continue;
      } else {
        if(iE->sigmaIetaIeta()       > 0.032)  continue;
        if(fabs(iE->deltaEtaSuperClusterTrackAtVtx()) > 0.010) continue;
        if(fabs(iE->deltaPhiSuperClusterTrackAtVtx()) > 0.8)  continue;
      }
    }
    IdentifiedElectrons.push_back(*iE);
  }

  if(target == "2011Data") {
    	target_ = MuonEffectiveArea::kMuEAData2011;
  } else if(target == "2012Data") {
    	target_ = MuonEffectiveArea::kMuEAData2012;
  } else if(target == "Fall11MC") {
    	target_ = MuonEffectiveArea::kMuEAFall11MC;
  } else if(target == "Summer11MC") {
    	target_ = MuonEffectiveArea::kMuEASummer11MC;
  } else{
	 throw cms::Exception("UnknownTarget")
	 << "Bad eff. area option for muons: " << target
	 << " options are: 2011Data, 2012Data, Fall11MC, Summer11MC" << std::endl;
  }

  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  std::auto_ptr< pat::MuonCollection > muonsUserEmbeddedColl( new pat::MuonCollection() ) ;

  for(unsigned int i = 0; i < muons->size(); i++){
    pat::Muon aMuon( (*muons)[i] );

    const reco::Muon* aRecoMuon = 0;
    for(unsigned int j = 0; j < recoMuons->size(); j++){
      if( Geom::deltaR( (*recoMuons)[j].p4() , aMuon.p4()) < 1e-03 ) { 
	aRecoMuon = &((*recoMuons)[j]);
	//std::cout << "Match to recoMuon" << std::endl;
      }
    }

    //std::cout << "@@@@@@@@ recoMuon: " << aMuon.px() << ", " << aMuon.py() << ", " << aMuon.pz() << std::endl;
    int isPFMuon = 0;
    for(unsigned int j = 0; j < pfCandidates->size(); j++){
      if( (*pfCandidates)[j].particleId() == reco::PFCandidate::mu ) { 
	reco::MuonRef muonRefToPFMuon = (*pfCandidates)[j].muonRef();
	//if( muonRefToPFMuon.isNonnull() ){
	//std::cout << j << ": muonRefToPFMuon: " << muonRefToPFMuon->px() << ", " 
	//    << muonRefToPFMuon->py() << ", " << muonRefToPFMuon->pz() << std::endl;
	//}
	if( muonRefToPFMuon.isNonnull() && 
	    Geom::deltaR( muonRefToPFMuon->p4() , aMuon.p4()) < 1e-04 &&
	    (muonRefToPFMuon->isGlobalMuon() || muonRefToPFMuon->isTrackerMuon() ) )
	  isPFMuon = 1;
      }
    }
   
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
    aMuon.addUserInt("isPFMuon",isPFMuon);

    int isGlobalMuon_ = 0;
    int isTrackerMuon_ = 0;
    int globalMuonPromptTight_ = 0;
    int allArbitrated_ = 0;
    double normalizeChi2_ = 99;
    double ptError_ = 99;
    int innerTrackHitPattern_ = -99;
    int numberOfValidPixelHits_ = -99;
    int numMuonStations_ = -99;
    int numberOfMatches_ = -99;

    isGlobalMuon_ = aMuon.isGlobalMuon();
    isTrackerMuon_ = aMuon.isTrackerMuon();

    bool validRefGlob = isValidRef(aMuon.globalTrack());
    bool validRefInn = isValidRef(aMuon.innerTrack());

    if(validRefGlob && validRefInn){

	globalMuonPromptTight_ = muon::isGoodMuon(aMuon, muon::GlobalMuonPromptTight);
	allArbitrated_ =  muon::isGoodMuon(aMuon, muon::AllArbitrated);

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

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    float idmva = -99;
    float isomva = -99;
    float isoringsradmva = -99; 
    float idisomva = -99;

    if(doMuIdMVA_){

	    idmva = fMuonIDMVA_->mvaValue( aMuon, pvCol->at(0), 
					inPfCands, Rho, 
		                    	target_, 
					IdentifiedElectrons, IdentifiedMuons);}

    if(doMuIsoMVA_){

	    isomva = fMuonIsoMVA_->mvaValue( aMuon, pvCol->at(0), 
					inPfCands, Rho, 
					target_, 
					IdentifiedElectrons, IdentifiedMuons);}

    if(doMuIsoRingsRadMVA_){

	    isoringsradmva = fMuonIsoRingsRadMVA_->mvaValue( aMuon, pvCol->at(0), 
					inPfCands, Rho, 
					target_, 
					IdentifiedElectrons, IdentifiedMuons);}

    if(doMuIdIsoCombMVA_){

	    idisomva = fMuonIDIsoCombinedMVA_->mvaValue( aMuon, pvCol->at(0), 
					inPfCands, Rho, 
					target_, 
					IdentifiedElectrons, IdentifiedMuons);}

    //std::cout<<"MVA "<<idmva<<" "<<isomva<<" "<<isoringsradmva<<" "<<idisomva<<std::endl;

    aMuon.addUserFloat("muonIdMVA",idmva);
    aMuon.addUserFloat("muonIsoRingsMVA",isomva);
    aMuon.addUserFloat("muonIsoRingsRadMVA",isoringsradmva);
    aMuon.addUserFloat("muonIdIsoCombMVA",idisomva);

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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
