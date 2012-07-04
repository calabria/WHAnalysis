// -*- C++ -*-
//
// Package:    CompositeCandHistManager
// Class:      CompositeCandHistManager
// 
/**\class CompositeCandHistManager CompositeCandHistManager.cc WHAnalysis/CompositeCandHistManager/src/CompositeCandHistManager.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Sun Dec 18 15:51:35 CET 2011
// $Id$
//
//


// system include files
#include <memory>
#include <map>
#include <string>
#include <TMath.h>
#include <cmath>
// user include files
#include "TH1.h"
#include "TH2.h"


#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

//
// class declaration
//

class CompositeCandHistManager : public edm::EDAnalyzer {
   public:
      explicit CompositeCandHistManager(const edm::ParameterSet&);
      ~CompositeCandHistManager();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------

      std::map<std::string,TH1F*> histContainer_; 
      std::map<std::string,TH2F*> histContainer2D_; 
      edm::LumiReWeighting LumiWeights_;

      // input tags  
      edm::InputTag CompCandSrc_;
      //edm::InputTag muonSrc_;
      //edm::InputTag eleSrc_;
      //edm::InputTag tauSrc_;
      edm::InputTag PFMetTag_;

      typedef std::vector<double> vdouble;
      vdouble MCDist_f_;
      vdouble TrueDist2011_f_;
      bool isMC_;
      bool isFR_;
};

//
// constants, enums and typedefs
//


double tightIsoFR(double pt){
	//double mpv = -17.31;
    	//double sigma = 4.828;
    	//double costante = 0.002873;  

	double mpv = -4.90507 ;
	double sigma = 4.84749;
	double costante = 1.32257e-04;
   
    	double fakeTau = ((TMath::Landau(pt,mpv,sigma))+costante);  
	double w = fakeTau/(1-fakeTau);

	return w;
}

double mediumIsoFR(double pt){
 	//double mpv = -10.4;
    	//double sigma = 4.42;
    	//double costante = 0.002845;

	double mpv = -2.57312;
	double sigma = 4.68848;
	double costante = 1.67789e-03;

     	double fakeTau = ((TMath::Landau(pt,mpv,sigma))+costante);
	double w = fakeTau/(1-fakeTau);

	return w;
}

///////////// For AntiEleMVA

double tightIsoFRMVA(double pt){

	double mpv = -1.30342e+01 ;
	double sigma = 6.02648e+00;
	double costante = -1.78456e-03;
   
    	double fakeTau = ((TMath::Landau(pt,mpv,sigma))+costante);  
	double w = fakeTau/(1-fakeTau);

	return w;
}

double mediumIsoFRMVA(double pt){

	double mpv = -7.72228e+00;
	double sigma = 5.54539e+00;
	double costante = -6.12401e-04;

     	double fakeTau = ((TMath::Landau(pt,mpv,sigma))+costante);
	double w = fakeTau/(1-fakeTau);

	return w;
}

//
// static data member definitions
//

//
// constructors and destructor
//
CompositeCandHistManager::CompositeCandHistManager(const edm::ParameterSet& iConfig):
  histContainer_(),
  histContainer2D_(),
  CompCandSrc_(iConfig.getUntrackedParameter<edm::InputTag>("CompCandSrc")),
  //muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
  //eleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("eleSrc")),
  //tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc")),
  PFMetTag_(iConfig.getUntrackedParameter<edm::InputTag> ("PFMetTag")),
  MCDist_f_(iConfig.getUntrackedParameter<vdouble>("MCDist")),
  TrueDist2011_f_(iConfig.getUntrackedParameter<vdouble>("TrueDist2011")),
  isMC_(iConfig.getUntrackedParameter<bool>("isMC")),
  isFR_(iConfig.getUntrackedParameter<bool>("isFR",false))
{
   //now do what ever initialization is needed

}


CompositeCandHistManager::~CompositeCandHistManager()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
CompositeCandHistManager::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;

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

  edm::Handle<edm::View<reco::CompositeCandidate> > CompCandidates;
  iEvent.getByLabel(CompCandSrc_, CompCandidates);

///////////////////////////////////////////////////////////// FR /////////////////////////////////////////////////////////////

  if(isFR_){

	  double weightPU = 0;

	  for(edm::View<reco::CompositeCandidate>::const_iterator CompCand=CompCandidates->begin(); CompCand!=CompCandidates->end(); ++CompCand){

		const Candidate * WLeptonCand = CompCand->daughter(0); //Candidato leptone dal W
		const Candidate * DiTauCand = CompCand->daughter(1); //Candidato composito DiTau

		int DiTauCand1Charge = DiTauCand->daughter(0)->charge(); //Carica del primo membro della coppia DiTau
		int DiTauCand2Charge = DiTauCand->daughter(1)->charge(); //Carica del secondo membro della coppia DiTau
		int WLeptonCandCharge = WLeptonCand->charge();

		int WLeptonDiTauCand1ChargeProd = WLeptonCandCharge * DiTauCand1Charge;
		int WLeptonDiTauCand2ChargeProd = WLeptonCandCharge * DiTauCand2Charge;

		double DiTauCand1Pt = DiTauCand->daughter(0)->pt(); //Carica del primo membro della coppia DiTau
		double DiTauCand2Pt = DiTauCand->daughter(1)->pt(); //Carica del secondo membro della coppia DiTau
		double WLeptonCandPt = WLeptonCand->pt();

		if(WLeptonDiTauCand1ChargeProd > 0){
			weightPU += tightIsoFR(DiTauCand1Pt);
			histContainer_["weightLep_1"]->Fill(tightIsoFR(DiTauCand1Pt));
			std::cout<<"PT1: "<<DiTauCand1Pt<<" chargeProd1: "<<WLeptonDiTauCand1ChargeProd<<" weight1: "<<tightIsoFRMVA(DiTauCand1Pt)<<std::endl;
		}
		else if(WLeptonDiTauCand2ChargeProd > 0){
		 	weightPU += mediumIsoFR(DiTauCand2Pt);
	   		histContainer_["weightLep_2"]->Fill(mediumIsoFR(DiTauCand2Pt));
			std::cout<<"PT2: "<<DiTauCand2Pt<<" chargeProd2: "<<WLeptonDiTauCand2ChargeProd<<" weight2: "<<mediumIsoFRMVA(DiTauCand2Pt)<<std::endl;
		}

	  }

	  if(weightPU) weight *= weightPU;
	  std::cout<<"Tot Weight: "<<weightPU<<std::endl;

  }

///////////////////////////////////////////////////////////// FR /////////////////////////////////////////////////////////////

  edm::Handle<pat::METCollection> pfmet;
  iEvent.getByLabel(PFMetTag_, pfmet);

  double met = pfmet->front().et();

  for(edm::View<reco::CompositeCandidate>::const_iterator CompCand=CompCandidates->begin(); CompCand!=CompCandidates->end(); ++CompCand){

	const Candidate * WLeptonCand = CompCand->daughter(0); //Candidato leptone dal W
	const Candidate * DiTauCand = CompCand->daughter(1); //Candidato composito DiTau

	double DiTauCand1Et = DiTauCand->daughter(0)->et(); //Et primo membro della coppia DiTau
	double DiTauCand2Et = DiTauCand->daughter(1)->et(); //Et secondo membro della coppia DiTau
	double WLeptonCandEt = WLeptonCand->et();
	double TotEt = WLeptonCandEt + DiTauCand1Et + DiTauCand2Et;
	histContainer_["hLt"]->Fill(TotEt, weight);

	int DiTauCand1Charge = DiTauCand->daughter(0)->charge(); //Carica del primo membro della coppia DiTau
	int DiTauCand2Charge = DiTauCand->daughter(1)->charge(); //Carica del secondo membro della coppia DiTau
	int WLeptonCandCharge = WLeptonCand->charge();
	int WLeptonDiTauCand1Charge = WLeptonCandCharge + DiTauCand1Charge;
	int WLeptonDiTauCand2Charge = WLeptonCandCharge + DiTauCand2Charge;

	double DiTauCand1Pt = DiTauCand->daughter(0)->pt(); //Carica del primo membro della coppia DiTau
	double DiTauCand2Pt = DiTauCand->daughter(1)->pt(); //Carica del secondo membro della coppia DiTau
	double WLeptonCandPt = WLeptonCand->pt();
	bool mostEnergetic = DiTauCand1Pt > DiTauCand2Pt ? true : false;

	double DiTauCand1Eta = DiTauCand->daughter(0)->eta(); //Carica del primo membro della coppia DiTau
	double DiTauCand2Eta = DiTauCand->daughter(1)->eta(); //Carica del secondo membro della coppia DiTau
	double WLeptonCandEta = WLeptonCand->eta();

	double DiTauCand1Phi = DiTauCand->daughter(0)->phi(); //Carica del primo membro della coppia DiTau
	double DiTauCand2Phi = DiTauCand->daughter(1)->phi(); //Carica del secondo membro della coppia DiTau
	double WLeptonCandPhi = WLeptonCand->phi();

	double massWLeptonDiTauCand1 = (WLeptonCand->p4() + DiTauCand->daughter(0)->p4()).M();
	double massWLeptonDiTauCand2 = (WLeptonCand->p4() + DiTauCand->daughter(1)->p4()).M();
	double massHiggs = (DiTauCand->daughter(0)->p4() + DiTauCand->daughter(1)->p4()).M();

	double higgsPt = DiTauCand->pt(); //Pt of the Higgs candidate

        double scalarSumPt = (WLeptonCand->p4()).Et() + ((*pfmet)[0].p4()).Et();
        double vectorSumPt = (WLeptonCand->p4() + (*pfmet)[0].p4()).Pt() ;
        double Mt = TMath::Sqrt( scalarSumPt*scalarSumPt - vectorSumPt*vectorSumPt );

	histContainer2D_["hMtMet"]->Fill(Mt, met, weight);

	double phiTau1 = deltaPhi(DiTauCand1Phi,WLeptonCandPhi);
	double cosTau1 = cos(phiTau1);
	double phiTau2 = deltaPhi(DiTauCand2Phi,WLeptonCandPhi);
	double cosTau2 = cos(phiTau2);

	//double metPt = (*pfmet)[0].pt();
	//double metPhi = (*pfmet)[0].phi();
	//double metEt = (*pfmet)[0].et();
	//double Mt2 = TMath::Sqrt((2*WLeptonCandPt*metEt)*(1-TMath::Cos(deltaPhi(metPhi,WLeptonCandPhi))));
	//std::cout<<"lepPt: "<<WLeptonCandPt<<" lepEt: "<<WLeptonCandEt<<std::endl; 
	//std::cout<<"metPt: "<<metPt<<" metEt: "<<metEt<<std::endl; 
	//std::cout<<"Mt: "<<Mt<<" Mt2: "<<Mt2<<std::endl; 

	histContainer_["hWLeptonTau1Charge"]->Fill(WLeptonDiTauCand1Charge, weight);
	histContainer_["hWLeptonTau2Charge"]->Fill(WLeptonDiTauCand2Charge, weight);

	if(mostEnergetic){ 
		histContainer_["hWLeptonLeadTauCharge"]->Fill(WLeptonDiTauCand1Charge, weight);
		histContainer_["hWLeptonSubLeadTauCharge"]->Fill(WLeptonDiTauCand2Charge, weight);

		histContainer_["hMassWLeptonLeadTau"]->Fill(massWLeptonDiTauCand1, weight);
		histContainer_["hMassWLeptonSubLeadTau"]->Fill(massWLeptonDiTauCand2, weight);

		histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]->Fill(massWLeptonDiTauCand1, higgsPt, weight);
		histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]->Fill(massWLeptonDiTauCand2, higgsPt, weight);

		histContainer2D_["hMassWLeptonLeadTauVsMET"]->Fill(massWLeptonDiTauCand1, met, weight);
		histContainer2D_["hMassWLeptonSubLeadTauVsMET"]->Fill(massWLeptonDiTauCand2, met, weight);

		histContainer_["hCosDPhiELeadTau"]->Fill(cosTau1, weight);
		histContainer2D_["hCosDPhiELeadTauVsMT"]->Fill(Mt, cosTau1, weight);
		histContainer_["hCosDPhiESubLeadTau"]->Fill(cosTau2, weight);
		histContainer2D_["hCosDPhiESubLeadTauVsMT"]->Fill(Mt, cosTau2, weight);
	}
	else{
 		histContainer_["hWLeptonLeadTauCharge"]->Fill(WLeptonDiTauCand2Charge, weight);
 		histContainer_["hWLeptonSubLeadTauCharge"]->Fill(WLeptonDiTauCand1Charge, weight);

		histContainer_["hMassWLeptonLeadTau"]->Fill(massWLeptonDiTauCand2, weight);
		histContainer_["hMassWLeptonSubLeadTau"]->Fill(massWLeptonDiTauCand1, weight);

		histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]->Fill(massWLeptonDiTauCand2, higgsPt, weight);
		histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]->Fill(massWLeptonDiTauCand1, higgsPt, weight);

		histContainer2D_["hMassWLeptonLeadTauVsMET"]->Fill(massWLeptonDiTauCand2, met, weight);
		histContainer2D_["hMassWLeptonSubLeadTauVsMET"]->Fill(massWLeptonDiTauCand1, met, weight);

		histContainer_["hCosDPhiELeadTau"]->Fill(cosTau2, weight);
		histContainer2D_["hCosDPhiELeadTauVsMT"]->Fill(Mt, cosTau2, weight);
		histContainer_["hCosDPhiESubLeadTau"]->Fill(cosTau1, weight);
		histContainer2D_["hCosDPhiESubLeadTauVsMT"]->Fill(Mt, cosTau1, weight);
	}

   	histContainer_["hDiTauCand1Pt"]->Fill(DiTauCand1Pt, weight);
   	histContainer_["hDiTauCand1Eta"]->Fill(DiTauCand1Eta, weight);
   	histContainer_["hDiTauCand1Phi"]->Fill(DiTauCand1Phi, weight);

   	histContainer_["hDiTauCand2Pt"]->Fill(DiTauCand2Pt, weight);
   	histContainer_["hDiTauCand2Eta"]->Fill(DiTauCand2Eta, weight);
   	histContainer_["hDiTauCand2Phi"]->Fill(DiTauCand2Phi, weight);

   	histContainer_["hWLepCandPt"]->Fill(WLeptonCandPt, weight);
   	histContainer_["hWLepCandEta"]->Fill(WLeptonCandEta, weight);
   	histContainer_["hWLepCandPhi"]->Fill(WLeptonCandPhi, weight);

   	histContainer_["VisMass"]->Fill(massHiggs, weight);
	histContainer_["MTeMET"]->Fill(Mt, weight);

	histContainer_["hCosDPhiETau1"]->Fill(cosTau1, weight);
	histContainer_["hCosDPhiETau2"]->Fill(cosTau2, weight);

  }

  histContainer_["MET"]->Fill(met, weight);

  double count = 1.;
  histContainer_["N_eventi"]->Fill(count);
  histContainer_["N_eventi_PU"]->Fill(count, weight);

  histContainer_["CompCand_mult"]->Fill(CompCandidates->size(), weight);

}


// ------------ method called once each job just before starting event loop  ------------
void 
CompositeCandHistManager::beginJob()
{
  // register to the TFileService
  edm::Service<TFileService> fs;
  TH1::SetDefaultSumw2();

  histContainer_["N_eventi"]=fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
  histContainer_["N_eventi_PU"]=fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);
  histContainer_["CompCand_mult"]=fs->make<TH1F>("CompCand_mult", "size", 20, 0.5,  20.5);

  histContainer_["weightLep_1"]=fs->make<TH1F>("weightLep_1", "weightLep_1", 50, 0., 0.1);
  histContainer_["weightLep_2"]=fs->make<TH1F>("weightLep_2", "weightLep_2", 50, 0., 0.1);

  histContainer_["hDiTauCand1Pt"]=fs->make<TH1F>("DiTauCand1Pt", "DiTauCand1Pt", 25, 0, 100);
  histContainer_["hDiTauCand1Eta"]=fs->make<TH1F>("DiTauCand1Eta", "DiTauCand1Eta",  100, -5,  5);
  histContainer_["hDiTauCand1Phi"]=fs->make<TH1F>("DiTauCand1Phi", "DiTauCand1Phi",  36,   -TMath::Pi(), +TMath::Pi());

  histContainer_["hDiTauCand2Pt"]=fs->make<TH1F>("DiTauCand2Pt", "DiTauCand2Pt", 25, 0, 100);
  histContainer_["hDiTauCand2Eta"]=fs->make<TH1F>("DiTauCand2Eta", "DiTauCand2Eta",  100, -5,  5);
  histContainer_["hDiTauCand2Phi"]=fs->make<TH1F>("DiTauCand2Phi", "DiTauCand2Phi",  36,   -TMath::Pi(), +TMath::Pi());

  histContainer_["hWLepCandPt"]=fs->make<TH1F>("WLepCandPt", "WLepCandPt", 25, 0, 100);
  histContainer_["hWLepCandEta"]=fs->make<TH1F>("WLepCandEta", "WLepCandEta",  100, -5,  5);
  histContainer_["hWLepCandPhi"]=fs->make<TH1F>("WLepCandPhi", "WLepCandPhi",  36,   -TMath::Pi(), +TMath::Pi());

  histContainer_["VisMass"]=fs->make<TH1F>("VisMass", "mass", 30, 0., 300.);
  histContainer_["MTeMET"]=fs->make<TH1F>("MTeMET", "MTeMET", 25, 0., 200.);

  histContainer_["hCosDPhiETau1"]=fs->make<TH1F>("cosTau1", "cosTau1", 50, -1, 1);
  histContainer_["hCosDPhiETau2"]=fs->make<TH1F>("cosTau2", "cosTau2", 50, -1, 1);
  histContainer_["hCosDPhiELeadTau"]=fs->make<TH1F>("cosLeadTau", "cosLeadTau", 50, -1, 1);
  histContainer_["hCosDPhiESubLeadTau"]=fs->make<TH1F>("cosSubLeadTau", "cosSubLeadTau2", 50, -1, 1);
  histContainer2D_["hCosDPhiELeadTauVsMT"]=fs->make<TH2F>("CosDPhiELeadTauVsMT", "CosDPhiELeadTauVsMT", 25, 0., 200., 50, -1, 1);
  histContainer2D_["hCosDPhiESubLeadTauVsMT"]=fs->make<TH2F>("CosDPhiESubLeadTauVsMT", "CosDPhiESubLeadTauVsMT", 25, 0., 200., 50, -1, 1);

  histContainer2D_["hMtMet"]=fs->make<TH2F>("MtMet", "MtMet", 25, 0., 200., 40, 0., 200.);

  histContainer_["MET"]=fs->make<TH1F>("MET", "met",    40,   0., 200.);
  histContainer_["hLt"]=fs->make<TH1F>("Lt", "Lt",50, 0,200);

  histContainer_["hWLeptonLeadTauCharge"]=fs->make<TH1F>("WLeptonLeadTauCharge", "WLeptonLeadTauCharge", 7, -3.5, +3.5);
  histContainer_["hWLeptonSubLeadTauCharge"]=fs->make<TH1F>("WLeptonSubLeadTauCharge", "WLeptonSubLeadTauCharge", 7, -3.5, +3.5);
  histContainer_["hWLeptonTau1Charge"]=fs->make<TH1F>("WLeptonTau1Charge", "WLeptonTau1Charge", 7, -3.5, +3.5);
  histContainer_["hWLeptonTau2Charge"]=fs->make<TH1F>("WLeptonTau2Charge", "WLeptonTau2Charge", 7, -3.5, +3.5);
  //histContainer_["hVertexChi2NDOF"]=fs->make<TH1F>("VertexChi2NDOF", "VertexChi2NDOF",20, 0, 30);
  histContainer_["hMassWLeptonLeadTau"]=fs->make<TH1F>("MassWLeptonLeadTau", "MassWLeptonLeadTau", 30, 0., 300.);
  histContainer_["hMassWLeptonSubLeadTau"]=fs->make<TH1F>("MassWLeptonSubLeadTau", "MassWLeptonSubLeadTau", 30, 0., 300.);

  histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]=fs->make<TH2F>("MassWLeptonLeadTauVsPtHiggs", "MassWLeptonLeadTauVsPtHiggs", 30, 0., 300., 50, 0., 200.);
  histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]=fs->make<TH2F>("MassWLeptonSubLeadTauPtVsHiggs", "MassWLeptonSubLeadTauVsPtHiggs", 30, 0., 300., 50, 0., 200.);

  histContainer2D_["hMassWLeptonLeadTauVsMET"]=fs->make<TH2F>("MassWLeptonLeadTauVsMET", "MassWLeptonLeadTauVsMET", 30, 0., 300., 40, 0., 200.);
  histContainer2D_["hMassWLeptonSubLeadTauVsMET"]=fs->make<TH2F>("MassWLeptonSubLeadTauVsMET", "MassWLeptonSubLeadTauVsMET", 30, 0., 300., 40, 0., 200.);

///////////////////////////////////////////////////////////// X axis

  histContainer_["N_eventi"]->GetXaxis()->SetTitle("Events");
  histContainer_["N_eventi_PU"]->GetXaxis()->SetTitle("Events");

  histContainer_["hDiTauCand1Pt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hDiTauCand1Eta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hDiTauCand1Phi"]->GetXaxis()->SetTitle("#phi");

  histContainer_["hDiTauCand2Pt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hDiTauCand2Eta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hDiTauCand2Phi"]->GetXaxis()->SetTitle("#phi");

  histContainer_["hWLepCandPt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hWLepCandEta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hWLepCandPhi"]->GetXaxis()->SetTitle("#phi");

  histContainer_["VisMass"]->GetXaxis()->SetTitle("Vis.Mass [GeV/c^{2}]");
  histContainer_["MTeMET"]->GetXaxis()->SetTitle("M_{T} (l_{W}, MET) [GeV/c^{2}]");

  histContainer_["MET"]->GetXaxis()->SetTitle("MET [GeV]");
  histContainer_["hLt"]->GetXaxis()->SetTitle("#sum_{All leptons} E_{T} [GeV]");

  histContainer_["hCosDPhiETau1"]->GetXaxis()->SetTitle("cos#Delta#phi(#tau_{1},e)");
  histContainer_["hCosDPhiETau2"]->GetXaxis()->SetTitle("cos#Delta#phi(#tau_{2},e)");
  histContainer_["hCosDPhiELeadTau"]->GetXaxis()->SetTitle("cos#Delta#phi(#tau_{lead},e)");
  histContainer_["hCosDPhiESubLeadTau"]->GetXaxis()->SetTitle("cos#Delta#phi(#tau_{sublead},e)");
  histContainer2D_["hCosDPhiELeadTauVsMT"]->GetXaxis()->SetTitle("M_{T} (l_{W}, MET) [GeV/c^{2}]");
  histContainer2D_["hCosDPhiESubLeadTauVsMT"]->GetXaxis()->SetTitle("M_{T} (l_{W}, MET) [GeV/c^{2}]");

  histContainer2D_["hMtMet"]->GetXaxis()->SetTitle("M_{T} (l_{W}, MET) [GeV/c^{2}]");

  histContainer_["hWLeptonLeadTauCharge"]->GetXaxis()->SetTitle("Charge (l_{W},#tau_{lead})");
  histContainer_["hWLeptonSubLeadTauCharge"]->GetXaxis()->SetTitle("Charge (l_{W},#tau_{sublead})");
  histContainer_["hWLeptonTau1Charge"]->GetXaxis()->SetTitle("Charge (l_{W},#tau_{1})");
  histContainer_["hWLeptonTau2Charge"]->GetXaxis()->SetTitle("Charge (l_{W},#tau_{2})");
  //histContainer_["hVertexChi2NDOF"]->GetXaxis()->SetTitle("Vertex #chi^{2}/NDOF");

  histContainer_["hMassWLeptonLeadTau"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{lead}) [GeV/c^{2}]");
  histContainer_["hMassWLeptonSubLeadTau"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{sublead}) [GeV/c^{2}]");

  histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{lead}) [GeV/c^{2}]");
  histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{sublead}) [GeV/c^{2}]");
  histContainer2D_["hMassWLeptonLeadTauVsMET"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{lead}) [GeV/c^{2}]");
  histContainer2D_["hMassWLeptonSubLeadTauVsMET"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{sublead}) [GeV/c^{2}]");

///////////////////////////////////////////////////////////// Y axis

  histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]->GetYaxis()->SetTitle("HiggsCand p_{T} [GeV/c]");
  histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]->GetYaxis()->SetTitle("HiggsCand p_{T} [GeV/c]");
  histContainer2D_["hMassWLeptonLeadTauVsMET"]->GetYaxis()->SetTitle("MET [GeV]");
  histContainer2D_["hMassWLeptonSubLeadTauVsMET"]->GetYaxis()->SetTitle("MET [GeV]");

  histContainer2D_["hMtMet"]->GetYaxis()->SetTitle("MET [GeV]");

  histContainer2D_["hCosDPhiELeadTauVsMT"]->GetYaxis()->SetTitle("cos#Delta#phi(#tau_{lead},e)");
  histContainer2D_["hCosDPhiESubLeadTauVsMT"]->GetYaxis()->SetTitle("cos#Delta#phi(#tau_{sublead},e)");

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
CompositeCandHistManager::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
CompositeCandHistManager::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
CompositeCandHistManager::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
CompositeCandHistManager::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
CompositeCandHistManager::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CompositeCandHistManager::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CompositeCandHistManager);
