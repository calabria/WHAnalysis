// -*- C++ -*-
//
// Package:    ElectronsUserEmbedder
// Class:      ElectronsUserEmbedder
// 
/**\class ElectronsUserEmbedder ElectronsUserEmbedder.cc WHAnalysis/ElectronsUserEmbedder/src/ElectronsUserEmbedder.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Tue Nov 22 17:00:17 CET 2011
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
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"

#include "HiggsAnalysis/HiggsToWW2Leptons/interface/ElectronIDMVA.h"

#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/Scalers/interface/DcsStatus.h"
#include "RecoEgamma/EgammaTools/interface/ConversionFinder.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHit.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"

using namespace edm;
using namespace std;
using namespace reco;

//
// class declaration
//

class ElectronsUserEmbedder : public edm::EDProducer {
   public:
      explicit ElectronsUserEmbedder(const edm::ParameterSet&);
      ~ElectronsUserEmbedder();

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

      edm::InputTag electronTag_;
      edm::InputTag vertexTag_;
      bool isMC_;
      bool doMVA_;
      ElectronIDMVA* fMVA_;
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
ElectronsUserEmbedder::ElectronsUserEmbedder(const edm::ParameterSet& iConfig)
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

  electronTag_ = iConfig.getParameter<edm::InputTag>("electronTag");
  vertexTag_   = iConfig.getParameter<edm::InputTag>("vertexTag");
  isMC_        = iConfig.getParameter<bool>("isMC");
  doMVA_       = iConfig.getParameter<bool>("doMVA");

  edm::FileInPath inputFileName0 = iConfig.getParameter<edm::FileInPath>("inputFileName0");
  edm::FileInPath inputFileName1 = iConfig.getParameter<edm::FileInPath>("inputFileName1");
  edm::FileInPath inputFileName2 = iConfig.getParameter<edm::FileInPath>("inputFileName2");
  edm::FileInPath inputFileName3 = iConfig.getParameter<edm::FileInPath>("inputFileName3");
  edm::FileInPath inputFileName4 = iConfig.getParameter<edm::FileInPath>("inputFileName4");
  edm::FileInPath inputFileName5 = iConfig.getParameter<edm::FileInPath>("inputFileName5");

  if(doMVA_){
    fMVA_ = new ElectronIDMVA();
    fMVA_->Initialize("BDTG method",
		      inputFileName0.fullPath().data(),
		      inputFileName1.fullPath().data(),
		      inputFileName2.fullPath().data(),
		      inputFileName3.fullPath().data(),
		      inputFileName4.fullPath().data(),
		      inputFileName5.fullPath().data(),                
		      ElectronIDMVA::kNoIPInfo);
  }

  produces<pat::ElectronCollection>("");
  
}


ElectronsUserEmbedder::~ElectronsUserEmbedder()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

  if(doMVA_) delete fMVA_;

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
ElectronsUserEmbedder::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  edm::Handle<pat::ElectronCollection> electronsHandle;
  iEvent.getByLabel(electronTag_,electronsHandle);
  const pat::ElectronCollection* electrons = electronsHandle.product();

  edm::Handle<reco::VertexCollection> vertexHandle;
  iEvent.getByLabel(vertexTag_,vertexHandle);
  const reco::VertexCollection* vertexes = vertexHandle.product();

  edm::Handle<reco::BeamSpot> bsHandle;
  iEvent.getByLabel("offlineBeamSpot", bsHandle);
  const reco::BeamSpot &thebs = *bsHandle.product();

  edm::Handle<reco::ConversionCollection> hConversions;
  iEvent.getByLabel("allConversions", hConversions);

  edm::Handle<DcsStatusCollection> dcsHandle;
  iEvent.getByLabel("scalersRawToDigi", dcsHandle);
  float evt_bField;

  if (!isMC_) {
    // scale factor = 3.801/18166.0 which are
    // average values taken over a stable two
    // week period
    float currentToBFieldScaleFactor = 2.09237036221512717e-04;
    float current = -9999/currentToBFieldScaleFactor;
    if( dcsHandle.isValid() && (*dcsHandle).size() > 0 ) {
      current = (*dcsHandle)[0].magnetCurrent();
    }
      
    evt_bField = current*currentToBFieldScaleFactor;
  }
  else {
    edm::ESHandle<MagneticField> magneticField;
    iSetup.get<IdealMagneticFieldRecord>().get(magneticField);
    evt_bField = magneticField->inTesla(GlobalPoint(0.,0.,0.)).z();
  }

  //Get the CTF tracks
  Handle<reco::TrackCollection> tracks_h;
  iEvent.getByLabel("generalTracks", tracks_h);
  
  //get GSF Tracks
  Handle<reco::GsfTrackCollection> gsftracks_h;
  iEvent.getByLabel("electronGsfTracks", gsftracks_h);
  
  std::auto_ptr< pat::ElectronCollection > electronsUserEmbeddedColl( new pat::ElectronCollection() ) ;

  for(unsigned int i = 0; i < electrons->size(); i++){

    pat::Electron aElectron( (*electrons)[i] );
    const reco::GsfElectron* aGsf = static_cast<reco::GsfElectron*>(&aElectron); 

    const reco::Track *el_track = (const reco::Track*)((aElectron).gsfTrack().get());  
    const reco::HitPattern& p_inner = el_track->trackerExpectedHitsInner(); 
    float nHits = p_inner.numberOfHits();

    ConversionFinder convFinder;
    vector<ConversionInfo> v_convInfos = convFinder.getConversionInfos(*(aElectron.core()), tracks_h, gsftracks_h, evt_bField);
    ConversionInfo convInfo  = convFinder.getConversionInfo(*aGsf, tracks_h, gsftracks_h, evt_bField);
    double els_conv_dist     = convInfo.dist();
    double els_conv_dcot     = convInfo.dcot();
    //double els_conv_radius   = convInfo.radiusOfConversion();
    math::XYZPoint els_conv_Point = convInfo.pointOfConversion(); 
    TrackRef els_conv_ctfRef = convInfo.conversionPartnerCtfTk(); 
    GsfTrackRef els_conv_gsfRef = convInfo.conversionPartnerGsfTk();
    //double els_conv_delMissHits =  convInfo.deltaMissingHits();

    float dPhi  = aElectron.deltaPhiSuperClusterTrackAtVtx();
    float dEta  = aElectron.deltaEtaSuperClusterTrackAtVtx();
    float sihih = aElectron.sigmaIetaIeta();
    float HoE   = aElectron.hadronicOverEm();
    //cout << "dEta " << dEta << " dPhi " << dPhi << " -- dcot " << els_conv_dcot << " -- nHits " << nHits << endl;

    aElectron.addUserFloat("nHits",nHits);
    aElectron.addUserFloat("dist",fabs(els_conv_dist));
    aElectron.addUserFloat("dcot",fabs(els_conv_dcot));
    aElectron.addUserFloat("dPhi",fabs(dPhi));
    aElectron.addUserFloat("dEta",fabs(dEta));
    aElectron.addUserFloat("sihih",sihih);
    aElectron.addUserFloat("HoE",HoE);

    int passconversionveto = 
      int(!ConversionTools::hasMatchedConversion(*aGsf,hConversions,thebs.position(),true,2.0,1e-06,0));
    aElectron.addUserInt("antiConv",passconversionveto);

    //edm::Handle< EcalRecHitCollection > reducedEBRecHits;
    //edm::Handle< EcalRecHitCollection > reducedEERecHits;
    //iEvent.getByLabel( edm::InputTag("reducedEcalRecHitsEB"), reducedEBRecHits );
    //iEvent.getByLabel( edm::InputTag("reducedEcalRecHitsEE"), reducedEERecHits ) ;
    //const EcalRecHitCollection * reducedRecHits = 0 ;
    //if (aElectron.isEB())  
    //  reducedRecHits = reducedEBRecHits.product() ; 
    //else 
    //  reducedRecHits = reducedEERecHits.product() ;
  
    double dxyWrtPV = -99.;
    double dzWrtPV =  -99.;

    if(vertexes->size()!=0 && (aElectron.gsfTrack()).isNonnull() ){
      dxyWrtPV = (aElectron.gsfTrack())->dxy( (*vertexes)[0].position() ) ;
      dzWrtPV  = (aElectron.gsfTrack())->dz(  (*vertexes)[0].position() ) ;
    }
    else if (vertexes->size()!=0 && (aElectron.track()).isNonnull() ){
      dxyWrtPV = (aElectron.track())->dxy( (*vertexes)[0].position() ) ;
      dzWrtPV  = (aElectron.track())->dz(  (*vertexes)[0].position() ) ;
    }

    aElectron.addUserFloat("dxyWrtPV",dxyWrtPV);
    aElectron.addUserFloat("dzWrtPV",dzWrtPV);

   EcalClusterLazyTools lazyTools(iEvent,iSetup,
				   edm::InputTag("reducedEcalRecHitsEB"),
				   edm::InputTag("reducedEcalRecHitsEE"));
    float mva = -99;    
    int mvaPreselection = passconversionveto && nHits<=0 && dxyWrtPV<0.02 && dzWrtPV<0.1 &&
      ((aElectron.isEB() && sihih < 0.01 
	&& fabs(dEta) < 0.007
	&& fabs(dPhi) < 0.15
	&& HoE < 0.12
	&& aElectron.dr03TkSumPt()/aElectron.pt() < 0.20
	&& (TMath::Max(aElectron.dr03EcalRecHitSumEt() - 1.0, 0.0))/aElectron.pt() < 0.20
	&& aElectron.dr03HcalTowerSumEt()/aElectron.pt() < 0.20

	) ||
       (aElectron.isEE() && sihih < 0.03 
	&& fabs(dEta) < 0.009
	&& fabs(dPhi) < 0.10
	&& HoE < 0.10
	&& aElectron.dr03TkSumPt()/aElectron.pt() < 0.20
	&& (TMath::Max(aElectron.dr03EcalRecHitSumEt() - 1.0, 0.0))/aElectron.pt() < 0.20
	&& aElectron.dr03HcalTowerSumEt()/aElectron.pt() < 0.20
	));
    if(doMVA_)
      mva = fMVA_->MVAValue(aGsf, lazyTools);
    aElectron.addUserFloat("mva",mva);
    aElectron.addUserInt("mvaPreselection",mvaPreselection);


    // iso deposits
    reco::isodeposit::AbsVetos vetos2010Charged;
    reco::isodeposit::AbsVetos vetos2010Neutral;  
    reco::isodeposit::AbsVetos vetos2010Photons;
    reco::isodeposit::AbsVetos vetos2011Charged; 
    reco::isodeposit::AbsVetos vetos2011Neutral;  
    reco::isodeposit::AbsVetos vetos2011Photons;
    reco::isodeposit::AbsVetos vetos2011EECharged; 
    reco::isodeposit::AbsVetos vetos2011EENeutral;  
    reco::isodeposit::AbsVetos vetos2011EEPhotons;

    vetos2010Charged.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aElectron.eta(),aElectron.phi()),0.01));
    vetos2010Charged.push_back(new reco::isodeposit::ThresholdVeto(0.5));
    vetos2010Neutral.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aElectron.eta(),aElectron.phi()),0.08));
    vetos2010Neutral.push_back(new reco::isodeposit::ThresholdVeto(1.0));
    vetos2010Photons.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aElectron.eta(),aElectron.phi()),0.05));
    vetos2010Photons.push_back(new reco::isodeposit::ThresholdVeto(1.0));

    vetos2011Charged.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aElectron.eta(),aElectron.phi()),0.03));//0.01
    vetos2011Charged.push_back(new reco::isodeposit::ThresholdVeto(0.5));//0.0
    vetos2011Neutral.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aElectron.eta(),aElectron.phi()),0.08));//0.01
    vetos2011Neutral.push_back(new reco::isodeposit::ThresholdVeto(0.5));
    vetos2011Photons.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aElectron.eta(),aElectron.phi()),0.05));//0.01
    vetos2011Photons.push_back(new reco::isodeposit::ThresholdVeto(0.5));

    vetos2011EECharged.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aElectron.eta(),aElectron.phi()),0.03));//0.015
    vetos2011EECharged.push_back(new reco::isodeposit::ThresholdVeto(0.5));//0.0
    vetos2011EENeutral.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aElectron.eta(),aElectron.phi()),0.08));//0.01
    vetos2011EENeutral.push_back(new reco::isodeposit::ThresholdVeto(0.5));
    vetos2011EEPhotons.push_back(new reco::isodeposit::ConeVeto(reco::isodeposit::Direction(aElectron.eta(),aElectron.phi()),0.05));//0.08
    vetos2011EEPhotons.push_back(new reco::isodeposit::ThresholdVeto(0.5));
  
  
    float chIso03v1 = 
      aElectron.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.3, vetos2010Charged).first;
    float nhIso03v1 = 
      aElectron.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.3, vetos2010Neutral).first;
    float phIso03v1 = 
      aElectron.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.3, vetos2010Photons).first;
    float nhIsoPU03v1 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2010Neutral).first;
    float phIsoPU03v1 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2010Photons).first;
    
    float chIso04v1 = 
      aElectron.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.4, vetos2010Charged).first;
    float nhIso04v1 = 
      aElectron.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2010Neutral).first;
    float phIso04v1 = 
      aElectron.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2010Photons).first;
    float nhIsoPU04v1 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2010Neutral).first;
    float phIsoPU04v1 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2010Photons).first;

    float chIso03v2 = 
      aElectron.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.3, vetos2011Charged).first;
    float nhIso03v2 = 
      aElectron.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.3, vetos2011Neutral).first;
    float phIso03v2 = 
      aElectron.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.3, vetos2011Photons).first;
    float nhIsoPU03v2 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2011Neutral).first;
    float phIsoPU03v2 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2011Photons).first;

    float chIso04v2 = 
      aElectron.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.4, vetos2011Charged).first;
    float nhIso04v2 = 
      aElectron.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2011Neutral).first;
    float phIso04v2 = 
      aElectron.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2011Photons).first;
    float nhIsoPU04v2 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2011Neutral).first;
    float phIsoPU04v2 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2011Photons).first;

    float chIso03EEv2 = 
      aElectron.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.3, vetos2011EECharged).first;
    float nhIso03EEv2 = 
      aElectron.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.3, vetos2011EENeutral).first;
    float phIso03EEv2 = 
      aElectron.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.3, vetos2011EEPhotons).first;
    float nhIsoPU03EEv2 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2011EENeutral).first;
    float phIsoPU03EEv2 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.3, vetos2011EEPhotons).first;

    float chIso04EEv2 = 
      aElectron.isoDeposit(pat::PfChargedHadronIso)->depositAndCountWithin(0.4, vetos2011EECharged).first;
    float nhIso04EEv2 = 
      aElectron.isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2011EENeutral).first;
    float phIso04EEv2 = 
      aElectron.isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2011EEPhotons).first;
    float nhIsoPU04EEv2 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2011EENeutral).first;
    float phIsoPU04EEv2 = 
      aElectron.isoDeposit(pat::PfAllParticleIso)->depositAndCountWithin(0.4, vetos2011EEPhotons).first;


    aElectron.addUserFloat("PFRelIso04v1",(chIso04v1+nhIso04v1+phIso04v1)/aElectron.pt());
    aElectron.addUserFloat("PFRelIso03v1",(chIso03v1+nhIso03v1+phIso03v1)/aElectron.pt());
    aElectron.addUserFloat("PFRelIsoDB04v1",(chIso04v1+std::max(nhIso04v1+phIso04v1-0.5*0.5*(nhIsoPU04v1+phIsoPU04v1),0.0))/aElectron.pt());
    aElectron.addUserFloat("PFRelIsoDB03v1",(chIso03v1+std::max(nhIso03v1+phIso03v1-0.5*0.5*(nhIsoPU03v1+phIsoPU03v1),0.0))/aElectron.pt());

    aElectron.addUserFloat("PFRelIso04v2",(chIso04v2+nhIso04v2+phIso04v2)/aElectron.pt());
    aElectron.addUserFloat("PFRelIso03v2",(chIso03v2+nhIso03v2+phIso03v2)/aElectron.pt());
    aElectron.addUserFloat("PFRelIsoDB04v2",(chIso04v2+std::max(nhIso04v2+phIso04v2-0.5*0.5*(nhIsoPU04v2+phIsoPU04v2),0.0))/aElectron.pt());
    aElectron.addUserFloat("PFRelIsoDB03v2",(chIso03v2+std::max(nhIso03v2+phIso03v2-0.5*0.5*(nhIsoPU03v2+phIsoPU03v2),0.0))/aElectron.pt());
    aElectron.addUserFloat("PFRelIsoDB04v3",
			   (aElectron.isEB())*(chIso04v2+std::max(nhIso04v2+phIso04v2-0.5*0.5*(nhIsoPU04v2+phIsoPU04v2),0.0))/aElectron.pt()+
			   (aElectron.isEE())*(chIso04EEv2+std::max(nhIso04EEv2+phIso04EEv2-0.5*0.5*(nhIsoPU04EEv2+phIsoPU04EEv2),0.0))/aElectron.pt()
			   );
    aElectron.addUserFloat("PFRelIsoDB03v3",
			   (int(aElectron.isEB()))*(chIso03v2+std::max(nhIso03v2+phIso03v2-0.5*0.5*(nhIsoPU03v2+phIsoPU03v2),0.0))/aElectron.pt()+
			   (int(aElectron.isEE()))*(chIso03EEv2+std::max(nhIso03EEv2+phIso03EEv2-0.5*0.5*(nhIsoPU03EEv2+phIsoPU03EEv2),0.0))/aElectron.pt()
			   );

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
    for(unsigned int i = 0; i <vetos2011EECharged.size(); i++){
      delete vetos2011EECharged[i];
    }
    for(unsigned int i = 0; i <vetos2011EENeutral.size(); i++){
      delete vetos2011EENeutral[i];
      delete vetos2011EEPhotons[i];
    }

    aElectron.addUserFloat("isInRun",iEvent.run());

    electronsUserEmbeddedColl->push_back(aElectron);
    
  }


  iEvent.put( electronsUserEmbeddedColl );
  return;
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
ElectronsUserEmbedder::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ElectronsUserEmbedder::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
ElectronsUserEmbedder::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
ElectronsUserEmbedder::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
ElectronsUserEmbedder::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
ElectronsUserEmbedder::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ElectronsUserEmbedder::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ElectronsUserEmbedder);
