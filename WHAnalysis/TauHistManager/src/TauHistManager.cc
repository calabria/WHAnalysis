// -*- C++ -*-
//
// Package:    TauHistManager
// Class:      TauHistManager
// 
/**\class TauHistManager TauHistManager.cc TauHistManager/TauHistManager/src/TauHistManager.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Tue May 10 17:44:11 CEST 2011
// $Id$
//
//


// system include files
#include <memory>
#include <TMath.h>
#include <stdlib.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "PhysicsTools/JetMCUtils/interface/JetMCTag.h"
#include "PhysicsTools/IsolationAlgos/interface/IsoDepositVetoFactory.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"
#include "DataFormats/TauReco/interface/PFTauDecayMode.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

//
// class declaration
//

class TauHistManager : public edm::EDAnalyzer {
   public:
      explicit TauHistManager(const edm::ParameterSet&);
      ~TauHistManager();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      std::map<std::string,TH1F*> histContainer_; 
      edm::LumiReWeighting LumiWeights_;

      // input tags  
      edm::InputTag tauSrc_;
      edm::InputTag lep2Src_;
      edm::InputTag lep1Src_;
      edm::InputTag vertexSrc_;

      typedef std::vector<double> vdouble;
      vdouble MCDist_f_;
      vdouble TrueDist2011_f_;
      bool isMC_;
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
TauHistManager::TauHistManager(const edm::ParameterSet& iConfig):

  histContainer_(),
  tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc")),
  lep2Src_(iConfig.getUntrackedParameter<edm::InputTag>("lep2Src")),
  lep1Src_(iConfig.getUntrackedParameter<edm::InputTag>("lep1Src")),
  vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc")),
  MCDist_f_(iConfig.getUntrackedParameter<vdouble>("MCDist")),
  TrueDist2011_f_(iConfig.getUntrackedParameter<vdouble>("TrueDist2011")),
  isMC_(iConfig.getUntrackedParameter<bool>("isMC"))
{
   //now do what ever initialization is needed

}


TauHistManager::~TauHistManager()
{
   //clearIsoParam(tauParticleFlowIsoParam_);
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

std::string getTauDecayModeName(int tauDecayMode)
{
  // "translate" from enum defined in DataFormats/TauReco/interface/PFTauDecayMode.h
  // to string ( in format defined in PhysicsTools/JetMCUtils/src/JetMCTag.cc )
  //
  // NOTE: the "unphysical" 2-prong modes take into account
  //       track reconstruction inefficiencies (migration from 3-prong decays),
  //       fake tracks and tracks from the underlying event (migration from 1-prong decays)
  //
  if      ( tauDecayMode == reco::PFTauDecayMode::tauDecaysElectron           ) return std::string("electron");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecayMuon                ) return std::string("muon");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay1ChargedPion0PiZero ) return std::string("oneProng0Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay1ChargedPion1PiZero ) return std::string("oneProng1Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay1ChargedPion2PiZero ) return std::string("oneProng2Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay1ChargedPion3PiZero ) return std::string("oneProng3Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay1ChargedPion4PiZero ) return std::string("oneProng4Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay2ChargedPion0PiZero ) return std::string("twoProng0Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay2ChargedPion1PiZero ) return std::string("twoProng1Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay2ChargedPion2PiZero ) return std::string("twoProng2Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay2ChargedPion3PiZero ) return std::string("twoProng3Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay2ChargedPion4PiZero ) return std::string("twoProng4Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay3ChargedPion0PiZero ) return std::string("threeProng0Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay3ChargedPion1PiZero ) return std::string("threeProng1Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay3ChargedPion2PiZero ) return std::string("threeProng2Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay3ChargedPion3PiZero ) return std::string("threeProng3Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecay3ChargedPion4PiZero ) return std::string("threeProng4Pi0");
  else if ( tauDecayMode == reco::PFTauDecayMode::tauDecayOther               ) return std::string("other");
  else {
    edm::LogError ("getTauDecayModeName")
      << " Invalid tau decay mode = " << tauDecayMode << " !!";
    return std::string("unknown");
  }
}

void setAxisLabel(TAxis* axis, int tauDecayMode)
{
//--- set label for tau decay mode passed as function argument
//   ( same labels to be used for generated and reconstructed tau decay modes,
//     except for 3 bins of generated tau decay mode histogram,
//     which are customized according to the definition in PhysicsTools/JetMCUtils/src/JetMCTag.cc )
//
//    NOTE: bin numbers start at 1 (not 0) !!
//
  axis->SetBinLabel(1 + tauDecayMode, getTauDecayModeName(tauDecayMode).data());
}

void setAxisLabelsRecTauDecayMode(TAxis* axis)
{
//--- set labels for reconstructed tau decay modes

  setAxisLabel(axis, reco::PFTauDecayMode::tauDecaysElectron);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecayMuon);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay1ChargedPion0PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay1ChargedPion1PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay1ChargedPion2PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay1ChargedPion3PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay1ChargedPion4PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay2ChargedPion0PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay2ChargedPion1PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay2ChargedPion2PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay2ChargedPion3PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay2ChargedPion4PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay3ChargedPion0PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay3ChargedPion1PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay3ChargedPion2PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay3ChargedPion3PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecay3ChargedPion4PiZero);
  setAxisLabel(axis, reco::PFTauDecayMode::tauDecayOther);
}


//
// member functions
//

// ------------ method called for each event  ------------
void
TauHistManager::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif

  //std::cout<<"-------------------------------------------------------------------------------"<<std::endl;

/////////////////////////////////////////////////////////////

  double weight = 1;

  if(isMC_){

	  edm::Handle<std::vector< PileupSummaryInfo > >  PupInfo;
	  iEvent.getByLabel(edm::InputTag("addPileupInfo"), PupInfo);

	  std::vector<PileupSummaryInfo>::const_iterator PVI;

	  int npv = -1;
	  int nti = -1;
	  for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI) {

		  int BX = PVI->getBunchCrossing();

		  if(BX == 0) { 
		     	npv = PVI->getPU_NumInteractions();
		     	continue;
		   	}

	  nti = PVI->getTrueNumInteractions();
	  }

	  weight = LumiWeights_.weight( nti );

  }

/////////////////////////////////////////////////////////////

  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);

  Handle<View<reco::Candidate> > leptons1;
  iEvent.getByLabel(lep1Src_,leptons1);

  Handle<View<reco::Candidate> > leptons2;
  iEvent.getByLabel(lep2Src_,leptons2);

  edm::Handle<reco::VertexCollection> pvHandle;
  iEvent.getByLabel(vertexSrc_, pvHandle);

//////////////////////////////////////////////// FR ////////////////////////////////////////////////

  /*std::string nameInputTag = tauSrc_.label();
  size_t found = nameInputTag.find("2");

  if(found != std::string::npos){

	  edm::Handle<edm::View<pat::Tau> > tausFR;
	  iEvent.getByLabel(edm::InputTag("selectedTausEleVeto"),tausFR);

	  for(edm::View<pat::Tau>::const_iterator patTau=tausFR->begin(); patTau!=tausFR->end(); ++patTau){

	   	if(patTau->userFloat("tauWeight")) weight *= patTau->userFloat("tauWeight")/(1-patTau->userFloat("tauWeight"));
		//std::cout<<"weightFromTau1 "<<patTau->userFloat("tauWeight")<<std::endl;

	  }

  }*/

//////////////////////////////////////////////// FR //////////////////////////////////////////////// 

  double count = 1.;
  histContainer_["N_eventi"]->Fill(count);
  histContainer_["N_eventi_PU"]->Fill(count, weight);

  //std::cout<<weight<<std::endl;

  for(edm::View<pat::Tau>::const_iterator patTau=taus->begin(); patTau!=taus->end(); ++patTau){

   //std::cout<<"TauWeight: "<<patTau->userFloat("tauWeight")<<std::endl;
   if(patTau->userFloat("tauWeight")) weight *= patTau->userFloat("tauWeight")/(1-patTau->userFloat("tauWeight"));

   double etaTau = patTau->eta();
   double phiTau = patTau->phi();
   double ptTau = patTau->pt();

   histContainer_["hTauPt"]->Fill(patTau->pt(), weight);
   histContainer_["hTauEta"]->Fill(patTau->eta(), weight);
   histContainer_["hTauPhi"]->Fill(patTau->phi(), weight);
   histContainer_["hTauCharge"]->Fill(patTau->charge(), weight);
   histContainer_["hTauVisMass"]->Fill(patTau->mass(), weight);

	if (!pvHandle->empty()) {
		const reco::Vertex &pv = (*pvHandle)[0];
		double dZ = patTau->vz() - pv.z();
		histContainer_["hTauDz"]->Fill(dZ, weight);
	}

        edm::View<reco::Candidate>::const_iterator lepton1;
   	for(lepton1=leptons1->begin(); lepton1!=leptons1->end(); ++lepton1){
   		double etaLep1 = lepton1->eta();
   		double phiLep1 = lepton1->phi();
   		double deltaR_Lep1Tau = deltaR(etaTau, phiTau, etaLep1, phiLep1);
  	 	histContainer_["deltaR_Lep1Tau"]->Fill(deltaR_Lep1Tau, weight);
		//std::cout<<"DRTauLep1 "<<deltaR_Lep1Tau<<std::endl;
   	}
        edm::View<reco::Candidate>::const_iterator lepton2;
	for(lepton2=leptons2->begin(); lepton2!=leptons2->end(); ++lepton2){
   		double etaLep2 = lepton2->eta();
   		double phiLep2 = lepton2->phi();
   		double deltaR_Lep2Tau = deltaR(etaTau, phiTau, etaLep2, phiLep2);
   		histContainer_["deltaR_Lep2Tau"]->Fill(deltaR_Lep2Tau, weight);
	}

   /*if ( isValidRef(patTau->leadPFChargedHadrCand()) && isValidRef(patTau->leadPFChargedHadrCand()->trackRef()) ) {
      	histContainer_["hTauLeadTrkPt"]->Fill(patTau->leadPFChargedHadrCand()->trackRef()->pt(), weight);
      	histContainer_["hTauLeadTrkEta"]->Fill(patTau->leadPFChargedHadrCand()->trackRef()->eta(), weight);
      	histContainer_["hTauLeadTrkPhi"]->Fill(patTau->leadPFChargedHadrCand()->trackRef()->phi(), weight);

      if ( vertexSrc_.label() != "" ) {
	edm::Handle<std::vector<reco::Vertex> > recoVertices;
	iEvent.getByLabel(vertexSrc_, recoVertices);
	if ( recoVertices->size() >= 1 ) {
	  const reco::Vertex& thePrimaryEventVertex = (*recoVertices->begin());
	  histContainer_["hTauLeadTrkIPxy"]->Fill(patTau->leadPFChargedHadrCand()->trackRef()->dxy(thePrimaryEventVertex.position()), weight);
	  histContainer_["hTauLeadTrkIPz"]->Fill(patTau->leadPFChargedHadrCand()->trackRef()->dz(thePrimaryEventVertex.position()), weight);
	}
      }

      	const reco::HitPattern& hitPattern = patTau->leadPFChargedHadrCand()->trackRef()->hitPattern();
      	histContainer_["hTauLeadTrkNumHits"]->Fill(hitPattern.numberOfValidTrackerHits(), weight);
      	histContainer_["hTauLeadTrkNumPixelHits"]->Fill(hitPattern.numberOfValidPixelHits(), weight);
      	histContainer_["hTauLeadTrkNumStripHits"]->Fill(hitPattern.numberOfValidStripHits(), weight);
   }*/

   //std::cout<<"Tau1 "<<patTau->pt()<<" IsoL "<<patTau->tauID("byTightCombinedIsolationDeltaBetaCorr")<<" AntiMuT "<<patTau->tauID("againstMuonTight")<<" AntiEleL "<<patTau->tauID("againstElectronLoose")<<std::endl;
   //std::cout<<"Tau2 "<<patTau->pt()<<" IsoM "<<patTau->tauID("byMediumCombinedIsolationDeltaBetaCorr")<<" AntiMuT "<<patTau->tauID("againstMuonTight")<<" AntiEleM "<<patTau->tauID("againstElectronMedium")<<"\n"<<std::endl;

   histContainer_["hTauDiscriminatorByLooseIsolation"]->Fill(patTau->tauID("byLooseIsolation"), weight);
   histContainer_["hTauDiscriminatorByMediumIsolation"]->Fill(patTau->tauID("byMediumIsolation"), weight);
   histContainer_["hTauDiscriminatorByTightIsolation"]->Fill(patTau->tauID("byTightIsolation"), weight);

   histContainer_["hTauDiscriminatorByVLooseIsolation"]->Fill(patTau->tauID("byVLooseIsolation"), weight);
   histContainer_["hTauDiscriminatorByVLooseIsolationDeltaBetaCorr"]->Fill(patTau->tauID("byVLooseIsolationDeltaBetaCorr"), weight);
   histContainer_["hTauDiscriminatorByLooseIsolationDeltaBetaCorr"]->Fill(patTau->tauID("byLooseIsolationDeltaBetaCorr"), weight);
   histContainer_["hTauDiscriminatorByMediumIsolationDeltaBetaCorr"]->Fill(patTau->tauID("byMediumIsolationDeltaBetaCorr"), weight);
   histContainer_["hTauDiscriminatorByTightIsolationDeltaBetaCorr"]->Fill(patTau->tauID("byTightIsolationDeltaBetaCorr"), weight);
   histContainer_["hTauDiscriminatorByVLooseCombinedIsolationDeltaBetaCorr"]->Fill(patTau->tauID("byVLooseCombinedIsolationDeltaBetaCorr"), weight);
   histContainer_["hTauDiscriminatorByLooseCombinedIsolationDeltaBetaCorr"]->Fill(patTau->tauID("byLooseCombinedIsolationDeltaBetaCorr"), weight);
   histContainer_["hTauDiscriminatorByMediumCombinedIsolationDeltaBetaCorr"]->Fill(patTau->tauID("byMediumCombinedIsolationDeltaBetaCorr"), weight);
   histContainer_["hTauDiscriminatorByTightCombinedIsolationDeltaBetaCorr"]->Fill(patTau->tauID("byTightCombinedIsolationDeltaBetaCorr"), weight);

   histContainer_["hTauDiscriminatorAgainstElectronsLoose"]->Fill(patTau->tauID("againstElectronLoose"), weight);
   histContainer_["hTauDiscriminatorAgainstElectronsMedium"]->Fill(patTau->tauID("againstElectronMedium"), weight);
   histContainer_["hTauDiscriminatorAgainstElectronsTight"]->Fill(patTau->tauID("againstElectronTight"), weight);
   histContainer_["hTauDiscriminatorAgainstElectronMVA"]->Fill(patTau->tauID("againstElectronMVA"), weight);
   histContainer_["hTauDiscriminatorAgainstMuonsLoose"]->Fill(patTau->tauID("againstMuonLoose"), weight);
   histContainer_["hTauDiscriminatorAgainstMuonMedium"]->Fill(patTau->tauID("againstMuonMedium"), weight);
   histContainer_["hTauDiscriminatorAgainstMuonsTight"]->Fill(patTau->tauID("againstMuonTight"), weight);

   histContainer_["hTauParticleFlowIsoPt"]->Fill(patTau->particleIso(), weight);
   histContainer_["hTauPFChargedHadronIsoPt"]->Fill(patTau->chargedHadronIso(), weight);
   histContainer_["hTauPFNeutralHadronIsoPt"]->Fill(patTau->neutralHadronIso(), weight);
   histContainer_["hTauPFGammaIsoPt"]->Fill(patTau->photonIso(), weight);

   int recTauDecayMode = patTau->decayMode();
   histContainer_["hTauRecDecayMode"]->Fill(recTauDecayMode, weight);
   setAxisLabelsRecTauDecayMode(histContainer_["hTauRecDecayMode"]->GetXaxis());

   double jetRadius = TMath::Sqrt(patTau->etaetaMoment() + patTau->phiphiMoment());
   if ( !TMath::IsNaN(jetRadius) ) histContainer_["hTauJetRadius"]->Fill(jetRadius, weight);

   histContainer_["hNumChargedHadronsSignalCone"]->Fill(patTau->signalPFChargedHadrCands().size(), weight);
   histContainer_["hNumNeutralHadronsSignalCone"]->Fill(patTau->signalPFNeutrHadrCands().size(), weight);
   histContainer_["hNumPhotonsSignalCone"]->Fill(patTau->signalPFGammaCands().size(), weight);
   histContainer_["hNumParticlesSignalCone"]->Fill(patTau->signalPFCands().size(), weight);
      
   histContainer_["hNumChargedHadronsIsoCone"]->Fill(patTau->isolationPFChargedHadrCands().size(), weight);
   histContainer_["hNumNeutralHadronsIsoCone"]->Fill(patTau->isolationPFNeutrHadrCands().size(), weight);
   histContainer_["hNumPhotonsIsoCone"]->Fill(patTau->isolationPFGammaCands().size(), weight);
   histContainer_["hNumParticlesIsoCone"]->Fill(patTau->isolationPFCands().size(), weight);
      
   histContainer_["hPtSumPFChargedHadronsIsoCone"]->Fill(patTau->isolationPFChargedHadrCandsPtSum(), weight);
   histContainer_["hPtSumPhotonsIsoCone"]->Fill(patTau->isolationPFGammaCandsEtSum(), weight);

  }

  // Multiplicity
  histContainer_["hTauMult"]->Fill(taus->size(), weight);

}


// ------------ method called once each job just before starting event loop  ------------
void 
TauHistManager::beginJob()
{

  // register to the TFileService
  edm::Service<TFileService> fs;
  TH1::SetDefaultSumw2();

  // ID
  histContainer_["hTauMult"]=fs->make<TH1F>("TauMult", "Tau multiplicity", 20, 0.5,  20.5);
  histContainer_["hTauPt"]=fs->make<TH1F>("TauPt",   "Tau Pt", 100, 0, 200);
  histContainer_["hTauEta"]=fs->make<TH1F>("TauEta",   "Tau Eta",  100, -5,  5);
  histContainer_["hTauPhi"]=fs->make<TH1F>("TauPhi",   "Tau Phi",  36,   -TMath::Pi(), +TMath::Pi());
  histContainer_["hTauCharge"] = fs->make<TH1F>("TauCharge", "Tau Charge (#Sigma Tracks in Signal Cone)", 11, -5.5, +5.5);
  histContainer_["hTauVisMass"] = fs->make<TH1F>("TauVisMass", "TauVisMass", 100, 0., 2.5);
  histContainer_["hTauDz"] = fs->make<TH1F>("TauDz", "TauDz", 50, -1.0, 1.0);
  histContainer_["deltaR_Lep1Tau"]=fs->make<TH1F>("deltaR_Lep1Tau", "deltaR_Lep1Tau", 100, 0., 5.);
  histContainer_["deltaR_Lep2Tau"]=fs->make<TH1F>("deltaR_Lep2Tau", "deltaR_Lep2Tau", 100, 0., 5.);

  histContainer_["hTauDiscriminatorAgainstElectronsLoose"]=fs->make<TH1F>("TauDiscriminatorAgainstElectronsLoose", "Discriminator against Electrons (Loose)", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorAgainstElectronsMedium"]=fs->make<TH1F>("TauDiscriminatorAgainstElectronsMedium", "Discriminator against Electrons (Medium)", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorAgainstElectronsTight"]=fs->make<TH1F>("TauDiscriminatorAgainstElectronsTight", "Discriminator against Electrons (Tight)", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorAgainstElectronMVA"]=fs->make<TH1F>("TauDiscriminatorAgainstElectronMVA", "TauDiscriminatorAgainstElectronMVA", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorAgainstMuonsLoose"]=fs->make<TH1F>("TauDiscriminatorAgainstMuonsLoose", "Discriminator against Muons (Loose)", 2, -0.5, 1.55);
   histContainer_["hTauDiscriminatorAgainstMuonMedium"]=fs->make<TH1F>("TauDiscriminatorAgainstMuonMedium", "TauDiscriminatorAgainstMuonMedium", 2, -0.5, 1.55);
  histContainer_["hTauDiscriminatorAgainstMuonsTight"]=fs->make<TH1F>("TauDiscriminatorAgainstMuonsTight", "Discriminator against Muons (Tight)", 2, -0.5, 1.55);

  histContainer_["hTauDiscriminatorByVLooseIsolation"]=fs->make<TH1F>("TauDiscriminatorByVLooseIsolation","TauDiscriminatorByVLooseIsolation", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByVLooseIsolationDeltaBetaCorr"]=fs->make<TH1F>("TauDiscriminatorByVLooseIsolationDeltaBetaCorr", "TauDiscriminatorByVLooseIsolationDeltaBetaCorr", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByLooseIsolationDeltaBetaCorr"]=fs->make<TH1F>("TauDiscriminatorByLooseIsolationDeltaBetaCorr", "TauDiscriminatorByLooseIsolationDeltaBetaCorr", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByMediumIsolationDeltaBetaCorr"]=fs->make<TH1F>("TauDiscriminatorByMediumIsolationDeltaBetaCorr", "TauDiscriminatorByMediumIsolationDeltaBetaCorr", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByTightIsolationDeltaBetaCorr"]=fs->make<TH1F>("TauDiscriminatorByTightIsolationDeltaBetaCorr", "TauDiscriminatorByTightIsolationDeltaBetaCorr", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByVLooseCombinedIsolationDeltaBetaCorr"]=fs->make<TH1F>("TauDiscriminatorByVLooseCombinedIsolationDeltaBetaCorr", "TauDiscriminatorByVLooseCombinedIsolationDeltaBetaCorr", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByLooseCombinedIsolationDeltaBetaCorr"]=fs->make<TH1F>("TauDiscriminatorByLooseCombinedIsolationDeltaBetaCorr", "TauDiscriminatorByLooseCombinedIsolationDeltaBetaCorr", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByMediumCombinedIsolationDeltaBetaCorr"]=fs->make<TH1F>("TauDiscriminatorByMediumCombinedIsolationDeltaBetaCorr", "TauDiscriminatorByMediumCombinedIsolationDeltaBetaCorr", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByTightCombinedIsolationDeltaBetaCorr"]=fs->make<TH1F>("TauDiscriminatorByTightCombinedIsolationDeltaBetaCorr", "TauDiscriminatorByTightCombinedIsolationDeltaBetaCorr", 2, -0.5, 1.5);

  /*histContainer_["hTauLeadTrkPt"]=fs->make<TH1F>("TauLeadPt",   "Tau Lead Pt", 100, 0, 200);
  histContainer_["hTauLeadTrkEta"]=fs->make<TH1F>("TauLeadEta",   "Tau Lead Eta",  100, -5,  5);
  histContainer_["hTauLeadTrkPhi"]=fs->make<TH1F>("TauLeadPhi",   "Tau Lead Phi",     36, -TMath::Pi(), +TMath::Pi());
  histContainer_["hTauLeadTrkNumHits"]=fs->make<TH1F>("TauLeadTrkNumHits", "Lead Track Number of Pixel + Strip Hits", 25, -0.5, 24.5);
  histContainer_["hTauLeadTrkNumPixelHits"]=fs->make<TH1F>("TauLeadTrkNumPixelHits", "Lead Track Number of Pixel Hits", 5, -0.5, 4.5);
  histContainer_["hTauLeadTrkNumStripHits"]=fs->make<TH1F>("TauLeadTrkNumStripHits", "Lead Track Number of Strip Hits", 20, -0.5, 19.5);
  histContainer_["hTauLeadTrkIPxy"]=fs->make<TH1F>("TauLeadTrkIPxy", "Lead Track Impact Parameter (xy)", 100, -0.100, 0.100);
  histContainer_["hTauLeadTrkIPz"]=fs->make<TH1F>("TauLeadTrkIPz", "Lead Track Impact Parameter (z)", 100, -1.0, 1.0);*/

  histContainer_["hTauDiscriminatorByLooseIsolation"]=fs->make<TH1F>("TauDiscriminatorByLooseIsolation", "Discriminator by Loose Isolation", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByMediumIsolation"]=fs->make<TH1F>("TauDiscriminatorByMediumIsolation", "Discriminator by Medium Isolation", 2, -0.5, 1.5);
  histContainer_["hTauDiscriminatorByTightIsolation"]=fs->make<TH1F>("TauDiscriminatorByTightIsolation", "Discriminator by Tight Isolation", 2, -0.5, 1.5);

  histContainer_["hTauRecDecayMode"]=fs->make<TH1F>("TauRecDecayMode", "rec. Tau decay mode", 20, -0.5, 19.5);
  histContainer_["hTauJetRadius"]=fs->make<TH1F>("TauJetRadius", "Tau jet-Radius", 51, -0.005, +0.505);

  histContainer_["hTauParticleFlowIsoPt"]=fs->make<TH1F>("TauParticleFlowIsoPt", "Particle Flow Isolation P_{T}", 100, 0., 10.);    
  histContainer_["hTauPFChargedHadronIsoPt"]=fs->make<TH1F>("TauPFChargedHadronIsoPt", "Particle Flow (Charged Hadron) Isolation P_{T}", 100, 0., 10.);   
  histContainer_["hTauPFNeutralHadronIsoPt"]=fs->make<TH1F>("TauPFNeutralHadronIsoPt", "Particle Flow (Neutral Hadron) Isolation P_{T}", 100, 0., 10.);   
  histContainer_["hTauPFGammaIsoPt"]=fs->make<TH1F>("TauPFGammaIsoPt", "Particle Flow (Photon) Isolation P_{T}", 100, 0., 10.);  

  histContainer_["N_eventi"]=fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
  histContainer_["N_eventi_PU"]=fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);

  histContainer_["hNumChargedHadronsSignalCone"]=fs->make<TH1F>("NumChargedHadronsSignalCone", "NumChargedHadronsSignalCone", 10, -0.5, 9.5);
  histContainer_["hNumNeutralHadronsSignalCone"]=fs->make<TH1F>("NumNeutralHadronsSignalCone", "NumNeutralHadronsSignalCone", 10, -0.5, 9.5);
  histContainer_["hNumPhotonsSignalCone"]=fs->make<TH1F>("NumPhotonsSignalCone", "NumPhotonsSignalCone", 10, -0.5, 9.5);
  histContainer_["hNumParticlesSignalCone"]=fs->make<TH1F>("NumParticlesSignalCone", "NumParticlesSignalCone", 10, -0.5, 9.5);
      
  histContainer_["hNumChargedHadronsIsoCone"]=fs->make<TH1F>("NumChargedHadronsIsoCone", "NumChargedHadronsIsoCone", 10, -0.5, 9.5);
  histContainer_["hNumNeutralHadronsIsoCone"]=fs->make<TH1F>("NumNeutralHadronsIsoCone", "NumNeutralHadronsIsoCone", 10, -0.5, 9.5);
  histContainer_["hNumPhotonsIsoCone"]=fs->make<TH1F>("NumPhotonsIsoCone", "NumPhotonsIsoCone", 10, -0.5, 9.5);
  histContainer_["hNumParticlesIsoCone"]=fs->make<TH1F>("NumParticlesIsoCone", "NumParticlesIsoCone", 10, -0.5, 9.5);
      
  histContainer_["hPtSumPFChargedHadronsIsoCone"]=fs->make<TH1F>("PtSumPFChargedHadronsIsoCone", "PtSumPFChargedHadronsIsoCone", 100, 0., 10.);
  histContainer_["hPtSumPhotonsIsoCone"]=fs->make<TH1F>("PtSumPhotonsIsoCone", "PtSumPhotonsIsoCone", 100, 0., 10.);

  histContainer_["hTauMult"]->GetXaxis()->SetTitle("# Taus");
  histContainer_["hTauPt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hTauEta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hTauPhi"]->GetXaxis()->SetTitle("#phi");
  histContainer_["hTauCharge"]->GetXaxis()->SetTitle("Charge");
  histContainer_["hTauVisMass"]->GetXaxis()->SetTitle("Vis. Mass [GeV/c^{2}]");
  histContainer_["hTauDz"]->GetXaxis()->SetTitle("Tau dZ [cm]");
  histContainer_["deltaR_Lep1Tau"]->GetXaxis()->SetTitle("#Delta R(l_{1}, #tau)");
  histContainer_["deltaR_Lep2Tau"]->GetXaxis()->SetTitle("#Delta R(l_{2}, #tau)");

  histContainer_["hTauDiscriminatorAgainstElectronsLoose"]->GetXaxis()->SetTitle("Discriminator Output");
  histContainer_["hTauDiscriminatorAgainstMuonsLoose"]->GetXaxis()->SetTitle("Discriminator Output");
  histContainer_["hTauDiscriminatorAgainstElectronsMedium"]->GetXaxis()->SetTitle("Discriminator Output");
  histContainer_["hTauDiscriminatorAgainstElectronsTight"]->GetXaxis()->SetTitle("Discriminator Output");
  histContainer_["hTauDiscriminatorAgainstMuonsTight"]->GetXaxis()->SetTitle("Discriminator Output");

  /*histContainer_["hTauLeadTrkPt"]->GetXaxis()->SetTitle("p_{T}^{lead} [GeV/c]");
  histContainer_["hTauLeadTrkEta"]->GetXaxis()->SetTitle("#eta^{lead}");
  histContainer_["hTauLeadTrkPhi"]->GetXaxis()->SetTitle("#phi^{lead}");
  histContainer_["hTauLeadTrkNumHits"]->GetXaxis()->SetTitle("Tau LeadTrk NumHits");
  histContainer_["hTauLeadTrkNumPixelHits"]->GetXaxis()->SetTitle("Tau LeadTrk NumPixelHits");
  histContainer_["hTauLeadTrkNumStripHits"]->GetXaxis()->SetTitle("Tau LeadTrk NumStripHits");
  histContainer_["hTauLeadTrkIPxy"]->GetXaxis()->SetTitle("IP_{xy}^{lead} [cm]");
  histContainer_["hTauLeadTrkIPz"]->GetXaxis()->SetTitle("IP_{z}^{lead} [cm]");*/

  histContainer_["hTauDiscriminatorByLooseIsolation"]->GetXaxis()->SetTitle("Discriminator Output");
  histContainer_["hTauDiscriminatorByMediumIsolation"]->GetXaxis()->SetTitle("Discriminator Output");
  histContainer_["hTauDiscriminatorByTightIsolation"]->GetXaxis()->SetTitle("Discriminator Output");

  histContainer_["hTauRecDecayMode"]->GetXaxis()->SetTitle("Tau Decay Mode");
  histContainer_["hTauJetRadius"]->GetXaxis()->SetTitle("#Delta R_{#tau -jet}");

  histContainer_["hTauParticleFlowIsoPt"]->GetXaxis()->SetTitle("Particle Flow Isolation p_{T}");    
  histContainer_["hTauPFChargedHadronIsoPt"]->GetXaxis()->SetTitle("Particle Flow (Charged Hadron) Isolation p_{T}");   
  histContainer_["hTauPFNeutralHadronIsoPt"]->GetXaxis()->SetTitle("Particle Flow (Neutral Hadron) Isolation p_{T}");   
  histContainer_["hTauPFGammaIsoPt"]->GetXaxis()->SetTitle("Particle Flow (Photon) Isolation p_{T}");  

  histContainer_["N_eventi"]->GetXaxis()->SetTitle("Events");
  histContainer_["N_eventi_PU"]->GetXaxis()->SetTitle("Events");

  histContainer_["hNumChargedHadronsSignalCone"]->GetXaxis()->SetTitle("Num Charged Hadrons in Signal Cone");
  histContainer_["hNumNeutralHadronsSignalCone"]->GetXaxis()->SetTitle("Num Neutral Hadrons in Signal Cone");
  histContainer_["hNumPhotonsSignalCone"]->GetXaxis()->SetTitle("Num Photons in Signal Cone");
  histContainer_["hNumParticlesSignalCone"]->GetXaxis()->SetTitle("Num Particles in Signal Cone");
      
  histContainer_["hNumChargedHadronsIsoCone"]->GetXaxis()->SetTitle("Num Charged Hadrons in Iso Cone");
  histContainer_["hNumNeutralHadronsIsoCone"]->GetXaxis()->SetTitle("Num Neutral Hadrons in Iso Cone");
  histContainer_["hNumPhotonsIsoCone"]->GetXaxis()->SetTitle("Num Photons in Iso Cone");
  histContainer_["hNumParticlesIsoCone"]->GetXaxis()->SetTitle("Num Particles in Iso Cone");
      
  histContainer_["hPtSumPFChargedHadronsIsoCone"]->GetXaxis()->SetTitle("PtSumPFChargedHadronsIsoCone");
  histContainer_["hPtSumPhotonsIsoCone"]->GetXaxis()->SetTitle("PtSumPhotonsIsoCone");

/////////////////////////////////////////////////////////////

  if(isMC_){

	  std::vector< float > MCDist ;
	  std::vector< float > TrueDist2011;

	  int sizeMCDist_f_ = MCDist_f_.size();

	  for( int i=0; i<sizeMCDist_f_; ++i) {
	      TrueDist2011.push_back(TrueDist2011_f_[i]);
	      MCDist.push_back(MCDist_f_[i]);
	    }

	  LumiWeights_ = edm::LumiReWeighting(MCDist, TrueDist2011);

  }

/////////////////////////////////////////////////////////////

}

// ------------ method called once each job just after ending the event loop  ------------
void 
TauHistManager::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
TauHistManager::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
TauHistManager::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
TauHistManager::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
TauHistManager::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TauHistManager::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TauHistManager);
