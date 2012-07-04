#include <map>
#include <string>

#include "TH1.h"
#include "TH2.h"

#include <TMath.h>
#include <cmath>

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/Handle.h"

class DiTauHistManager : public edm::EDAnalyzer {

public:
  explicit DiTauHistManager(const edm::ParameterSet&);
  ~DiTauHistManager();
  
private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  // simple map to contain all histograms; 
  // histograms are booked in the beginJob() 
  // method
  std::map<std::string,TH1F*> histContainer_; 
  std::map<std::string,TH2F*> histContainer2D_; 
  edm::LumiReWeighting LumiWeights_;

  // input tags  
  edm::InputTag DiTauCand_;
  edm::InputTag PFMetTag_;

  double a_;
  double b_;
  //edm::InputTag vertexSrc_;
  typedef std::vector<double> vdouble;
  vdouble MCDist_f_;
  vdouble TrueDist2011_f_;
  bool isMC_;
};


DiTauHistManager::DiTauHistManager(const edm::ParameterSet& iConfig):

  histContainer_(),
  histContainer2D_(),
  DiTauCand_(iConfig.getUntrackedParameter<edm::InputTag>("DiTauCand")),
  PFMetTag_(iConfig.getUntrackedParameter<edm::InputTag> ("PFMetTag")),
  a_(iConfig.getUntrackedParameter<double>("CoeffPzeta")),
  b_(iConfig.getUntrackedParameter<double>("CoeffPzetaVis")),
  //vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc")),
  MCDist_f_(iConfig.getUntrackedParameter<vdouble>("MCDist")),
  TrueDist2011_f_(iConfig.getUntrackedParameter<vdouble>("TrueDist2011")),
  isMC_(iConfig.getUntrackedParameter<bool>("isMC"))
{
}

DiTauHistManager::~DiTauHistManager()
{
}

void
DiTauHistManager::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

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

//FakeRate
if(false){

   double weightLep1 = 0;
   double weightLep2 = 0;
   double weightLep3 = 0;

   edm::Handle<edm::View<reco::Candidate> > objects;
   iEvent.getByLabel(edm::InputTag("selectedTausMuonVeto"), objects);

   for (size_t i = 0; i < objects->size(); ++i) {

    	reco::Candidate * clone = objects->at(i).clone();

    	const pat::Muon* muon = dynamic_cast<const pat::Muon*>(clone);
    	const pat::Electron* electron = dynamic_cast<const pat::Electron*>(clone);
    	const pat::Tau* tau = dynamic_cast<const pat::Tau*>(clone);

	if(muon) weightLep1 = muon->userFloat("muonWeight");
	else if(electron) weightLep1 = electron->userFloat("eleWeight");
	else if(tau) weightLep1 = tau->userFloat("tauWeight");

   }

   edm::Handle<edm::View<reco::Candidate> > objects2;
   iEvent.getByLabel(edm::InputTag("selectedTausMuonVeto2"), objects2);

   for (size_t i = 0; i < objects2->size(); ++i) {

    	reco::Candidate * clone = objects2->at(i).clone();

    	const pat::Muon* muon = dynamic_cast<const pat::Muon*>(clone);
    	const pat::Electron* electron = dynamic_cast<const pat::Electron*>(clone);
    	const pat::Tau* tau = dynamic_cast<const pat::Tau*>(clone);

	if(muon) weightLep2 = muon->userFloat("muonWeight");
	else if(electron) weightLep2 = electron->userFloat("eleWeight");
	else if(tau) weightLep2 = tau->userFloat("tauWeight");

   }

   /*edm::Handle<edm::View<reco::Candidate> > objects3;
   iEvent.getByLabel(edm::InputTag("produceWeightsLep3:patTausWithWeights"), objects3);

   for (size_t i = 0; i < objects3->size(); ++i) {

    	reco::Candidate * clone = objects3->at(i).clone();

    	const pat::Muon* muon = dynamic_cast<const pat::Muon*>(clone);
    	const pat::Electron* electron = dynamic_cast<const pat::Electron*>(clone);
    	const pat::Tau* tau = dynamic_cast<const pat::Tau*>(clone);

	if(muon) weightLep3 = muon->userFloat("muonWeight");
	else if(electron) weightLep3 = electron->userFloat("eleWeight");
	else if(tau) weightLep3 = tau->userFloat("tauWeight");

   }*/

   double totWeight = 1;
   double peso1 = 1;
   double peso2 = 1;
   double peso3 = 1;
   if(weightLep1) peso1 = (weightLep1/(1-weightLep1));
   if(weightLep2) peso2 = (weightLep2/(1-weightLep2));
   if(weightLep3) peso3 = (weightLep3/(1-weightLep3));
   totWeight = peso1 * peso2 * peso3;

   weight *= totWeight;
   //std::cout<<"weightLep1 "<<weightLep1<<" weightLep2 "<<weightLep2<<" weightLep3 "<<weightLep3<<" totWeight "<<totWeight<<std::endl;

   histContainer_["weightLep_1"]->Fill(weightLep1);
   histContainer_["weightLep_2"]->Fill(weightLep2);

}

/////////////////////////////////////////////////////////////

  edm::Handle<edm::View<reco::CompositeCandidate> > DiTauCandidates;
  iEvent.getByLabel(DiTauCand_, DiTauCandidates);

  edm::Handle<pat::METCollection> pfmet;
  iEvent.getByLabel(PFMetTag_, pfmet);

  double metPx = pfmet->front().px();
  double metPy = pfmet->front().py();

  double met = pfmet->front().et();
    
  // loop over DiTau
  for(edm::View<reco::CompositeCandidate>::const_iterator DiTau=DiTauCandidates->begin(); DiTau!=DiTauCandidates->end(); ++DiTau){

	//std::cout<<"VisMass "<<DiTau->mass()<<std::endl;
	histContainer_["VisMass"]->Fill(DiTau->mass(), weight);

        double px1 = 0;
	double py1 = 0;
	double et1 = 0;

        double px2 = 0;
	double py2 = 0;
	double et2 = 0;

	px1 = DiTau->daughter(0)->px() + metPx;
	py1 = DiTau->daughter(0)->py() + metPy;
	et1 = DiTau->daughter(0)->et() + TMath::Sqrt(metPx*metPx + metPy*metPy);
	double mt2_1MET = et1*et1 - (px1*px1 + py1*py1);
	double mt_1MET = 0;
    	if(mt2_1MET > 0) mt_1MET = TMath::Sqrt(mt2_1MET);
	histContainer_["MT_1MET"]->Fill(mt_1MET, weight);

	px2 = DiTau->daughter(1)->px() + metPx;
	py2 = DiTau->daughter(1)->py() + metPy;
	et2 = DiTau->daughter(1)->et() + TMath::Sqrt(metPx*metPx + metPy*metPy);
	double mt2_2MET = et2*et2 - (px2*px2 + py2*py2);
	double mt_2MET = 0;
    	if(mt2_2MET > 0) mt_2MET = TMath::Sqrt(mt2_2MET);
	histContainer_["MT_2MET"]->Fill(mt_2MET, weight);

	double pt1 = DiTau->daughter(0)->pt();
	histContainer_["Cand1Pt"]->Fill(pt1, weight);
	double pt2 = DiTau->daughter(1)->pt();
	histContainer_["Cand2Pt"]->Fill(pt2, weight);

	double ptAsym = fabs((pt1 - pt2) / (pt1 + pt2));
	histContainer_["ptAsymmetry"]->Fill(ptAsym, weight);
	histContainer2D_["MassVsPtAsymmetry"]->Fill(DiTau->mass(), ptAsym, weight);

	double eta1 = DiTau->daughter(0)->eta();
	histContainer_["Cand1Eta"]->Fill(eta1, weight);
	double eta2 = DiTau->daughter(1)->eta();
	histContainer_["Cand2Eta"]->Fill(eta2, weight);

	double phi1 = DiTau->daughter(0)->phi();
	histContainer_["Cand1Phi"]->Fill(phi1, weight);
	double phi2 = DiTau->daughter(1)->phi();
	histContainer_["Cand2Phi"]->Fill(phi2, weight);

	double dR = deltaR(eta1, phi1, eta2, phi2); 
	histContainer_["deltaR"]->Fill(dR, weight);

	double dPhi = deltaPhi(phi1, phi2); 
	histContainer_["deltaPhi"]->Fill(dPhi, weight);

	int charge = (DiTau->daughter(0)->charge()) + (DiTau->daughter(1)->charge());

   	if (TMath::Abs(charge) != 0) histContainer_["VisMass_SS"]->Fill(DiTau->mass(), weight);

	histContainer_["Pt_Ditau"]->Fill(DiTau->pt(), weight);
	histContainer_["pairCharge"]->Fill(charge, weight);
	histContainer2D_["METvsCand1Pt"]->Fill(met, pt1, weight);
	histContainer2D_["METvsCand2Pt"]->Fill(met, pt2, weight);

	//Pzeta

	double leg1x = cos(DiTau->daughter(0)->phi());
    	double leg1y = sin(DiTau->daughter(0)->phi());
    	double leg2x = cos(DiTau->daughter(1)->phi());
    	double leg2y = sin(DiTau->daughter(1)->phi());
    	double zetaX = leg1x + leg2x;
    	double zetaY = leg1y + leg2y;
    	double zetaR = TMath::Sqrt(zetaX*zetaX + zetaY*zetaY);
    	if ( zetaR > 0. ) {
      		zetaX /= zetaR;
      		zetaY /= zetaR;
    	}

    	double visPx = DiTau->daughter(0)->px() + DiTau->daughter(1)->px();
    	double visPy = DiTau->daughter(0)->py() + DiTau->daughter(1)->py();
    	double pZetaVis = visPx*zetaX + visPy*zetaY;

    	double px = visPx + metPx;
    	double py = visPy + metPy;
    	double pZeta = px*zetaX + py*zetaY;

	double PzetaDiscr = a_*pZeta + b_*pZetaVis;
	histContainer_["PzetaDiscr"]->Fill(PzetaDiscr, weight);
	histContainer2D_["PzetaVsPzetaVis"]->Fill(pZetaVis, pZeta, weight);
	
  }

  /*for(edm::View<reco::CompositeCandidate>::const_iterator MuEle=MuEleCandidates->begin(); MuEle!=MuEleCandidates->end(); ++MuEle){
    	int chargeMuEle = MuEle->charge();
   	histContainer_["hChargeMuEle"]->Fill(chargeMuEle, weight);
   	double massMuEle = MuEle->mass();
   	double etaMu = MuEle->daughter(0)->eta();
   	double etaEle = MuEle->daughter(1)->eta() ;
   	double phiMu = MuEle->daughter(0)->phi();
   	double phiEle = MuEle->daughter(1)->phi() ;
   	double dR_MuEle = deltaR(etaMu, phiMu, etaEle, phiEle);
   	histContainer_["deltaR_MuEle"]->Fill(dR_MuEle, weight);
  	histContainer2D_["CompCand_DeltaR(MuEle)vsCharge(MuEle)"]->Fill(dR_MuEle,chargeMuEle, weight );
   	histContainer2D_["CompCand_VisMass(MuEle)vsCharge(MuEle)"]->Fill(massMuEle,chargeMuEle, weight );
   	histContainer_["CompCand_VisMass_MuEle"]->Fill(massMuEle, weight);
   	if (TMath::Abs(chargeMuEle) != 0) histContainer_["VisMass_MuEle_SameSign"]->Fill(massMuEle, weight);
   	if (TMath::Abs(chargeMuEle) == 0) histContainer_["VisMass_MuEle_OppositeSign"]->Fill(massMuEle, weight);
  }*/

  histContainer_["DiTau_mult"]->Fill(DiTauCandidates->size(), weight);

  histContainer_["MET"]->Fill(met, weight);

  double count = 1.;
  histContainer_["N_eventi"]->Fill(count);
  histContainer_["N_eventi_PU"]->Fill(count, weight);

}

void 
DiTauHistManager::beginJob()
{
  // register to the TFileService
  edm::Service<TFileService> fs;
  TH1::SetDefaultSumw2();

  histContainer_["weightLep_1"]=fs->make<TH1F>("weightLep_1", "weightLep_1", 500, 0., 1.);
  histContainer_["weightLep_2"]=fs->make<TH1F>("weightLep_2", "weightLep_2", 500, 0., 1.);

  histContainer_["N_eventi"]=fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
  histContainer_["N_eventi_PU"]=fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);
  histContainer_["MET"]=fs->make<TH1F>("MET", "met",    40,   0., 200.);
  histContainer_["VisMass"]=fs->make<TH1F>("VisMass", "mass",    30,   0., 300.);
  histContainer_["VisMass_SS"]=fs->make<TH1F>("VisMass_SS", "mass_SS",    30,   0., 300.);
  histContainer_["MT_1MET"]=fs->make<TH1F>("MT_1MET", "MT_1MET",    25,   0., 200.);
  histContainer_["MT_2MET"]=fs->make<TH1F>("MT_2MET", "MT_2MET",    25,   0., 200.);
  histContainer_["Cand1Pt"]=fs->make<TH1F>("Cand1Pt", "Cand1Pt",    50,   0., 200.);
  histContainer_["Cand2Pt"]=fs->make<TH1F>("Cand2Pt", "Cand2Pt",    50,   0., 200.);

  histContainer_["ptAsymmetry"]=fs->make<TH1F>("ptAsymmetry", "ptAsymmetry", 50, 0., 1.);
  histContainer2D_["MassVsPtAsymmetry"]=fs->make<TH2F>("MassVsPtAsymmetry", "MassVsPtAsymmetry", 30, 0., 300., 50, 0., 1.);

  histContainer_["Cand1Eta"]=fs->make<TH1F>("Cand1Eta", "Cand1Eta",    30, -3., +3.);
  histContainer_["Cand2Eta"]=fs->make<TH1F>("Cand2Eta", "Cand2Eta",    30, -3., +3.);
  histContainer_["Cand1Phi"]=fs->make<TH1F>("Cand1Phi", "Cand1Phi",    36, -TMath::Pi(), +TMath::Pi());
  histContainer_["Cand2Phi"]=fs->make<TH1F>("Cand2Phi", "Cand2Phi",    36, -TMath::Pi(), +TMath::Pi());
  histContainer_["deltaR"]=fs->make<TH1F>("deltaR", "deltaR", 51, -0.1, 10.1);
  histContainer_["deltaPhi"]=fs->make<TH1F>("deltaPhi", "deltaPhi",   36, -TMath::Pi(), +TMath::Pi());
  histContainer_["pairCharge"]=fs->make<TH1F>("pairCharge", "pairCharge", 7, -3.5, +3.5);
  //histContainer_["hChargeMuEle"]=fs->make<TH1F>("ChargeMuEle", "ChargeMuEle", 7, -3.5, +3.5);
  histContainer_["PzetaDiscr"]=fs->make<TH1F>("PzetaDiscr", "PzetaDiscr", 25, -100., +100.);
  histContainer_["DiTau_mult"]=fs->make<TH1F>("DiTau_mult", "size", 20, 0.5,  20.5);
  histContainer_["Pt_Ditau"]=fs->make<TH1F>("Pt_Ditau", "DiTau Vis. p_{T}",100, 0., 200.);
  histContainer2D_["METvsCand1Pt"]=fs->make<TH2F>("METvsCand1Pt",  "MET vs. Cand_{1} p_{T}", 40, 0,  120,  40, 0,  120);
  histContainer2D_["METvsCand2Pt"]=fs->make<TH2F>("METvsCand2Pt",  "MET vs. Cand_{2} p_{T}", 40, 0,  120,  40, 0,  120);
  histContainer2D_["PzetaVsPzetaVis"]=fs->make<TH2F>("PzetaVsPzetaVis",  "P_{#zeta} vs. P_{#zeta}^{Vis}", 40, 0,  120, 40, 0,  120);
  //histContainer2D_["CompCand_VisMass(MuEle)vsCharge(MuEle)"]=fs->make<TH2F>("CompCand_VisMass(MuEle)vsCharge(MuEle)",  "CompCand_VisMass(MuEle)vsCharge(MuEle)", 40, 0,  200,  20, -2,  2);
  //histContainer_["CompCand_VisMass_MuEle"]=fs->make<TH1F>("CompCand_VisMass_MuEle", "CompCand_VisMass_MuEle",40, 0,200);
  //histContainer_["deltaR_MuEle"]=fs->make<TH1F>("deltaR_MuEle", "deltaR_MuEle", 50, -0.1, 10.);
  //histContainer2D_["CompCand_DeltaR(MuEle)vsCharge(MuEle)"]=fs->make<TH2F>("CompCand_DeltaR(MuEle)vsCharge(MuEle)",  "CompCand_DeltaR(MuEle)vsCharge(MuEle)",50, -0.1, 10., 20, -2,  2);
  //histContainer_["VisMass_MuEle_SameSign"]=fs->make<TH1F>("VisMass_MuEle_SameSign", "VisMass_MuEle_SameSign",40, 0,200);
  //histContainer_["VisMass_MuEle_OppositeSign"]=fs->make<TH1F>("VisMass_MuEle_OppositeSign", "VisMass_MuEle_OppositeSign",40, 0,200);

///////////////////////////////////////////////////////////// Axis Labels

  histContainer_["N_eventi"]->GetXaxis()->SetTitle("Events");
  histContainer_["N_eventi_PU"]->GetXaxis()->SetTitle("Events");
  histContainer_["MET"]->GetXaxis()->SetTitle("MET [GeV]");
  histContainer_["VisMass"]->GetXaxis()->SetTitle("Vis.Mass [GeV/c^{2}]");
  histContainer_["VisMass_SS"]->GetXaxis()->SetTitle("Vis.Mass SS [GeV/c^{2}]");
  histContainer_["MT_1MET"]->GetXaxis()->SetTitle("M_{T} (Cand_{1}, MET) [GeV/c^{2}]");
  histContainer_["MT_2MET"]->GetXaxis()->SetTitle("M_{T} (Cand_{2}, MET) [GeV/c^{2}]");
  histContainer_["Cand1Pt"]->GetXaxis()->SetTitle("Cand_{1} p_{T} [GeV/c]");
  histContainer_["Cand2Pt"]->GetXaxis()->SetTitle("Cand_{2} p_{T} [GeV/c]");

  histContainer_["ptAsymmetry"]->GetXaxis()->SetTitle("p_{T} Asymmetry");
  histContainer2D_["MassVsPtAsymmetry"]->GetXaxis()->SetTitle("Vis.Mass [GeV/c^{2}]");
  histContainer2D_["MassVsPtAsymmetry"]->GetYaxis()->SetTitle("p_{T} Asymmetry");

  histContainer_["Cand1Eta"]->GetXaxis()->SetTitle("Cand_{1} #eta");
  histContainer_["Cand2Eta"]->GetXaxis()->SetTitle("Cand_{2} #eta");
  histContainer_["Cand1Phi"]->GetXaxis()->SetTitle("Cand_{1} #phi");
  histContainer_["Cand2Phi"]->GetXaxis()->SetTitle("Cand_{2} #phi");
  histContainer_["deltaR"]->GetXaxis()->SetTitle("#Delta R(Cand_{1}, Cand_{2})");
  histContainer_["deltaPhi"]->GetXaxis()->SetTitle("#Delta#phi (Cand_{1}, Cand_{2})");
  histContainer_["pairCharge"]->GetXaxis()->SetTitle("Pair Charge");
  //histContainer_["hChargeMuEle"]->GetXaxis()->SetTitle("Charge (#mu-e)");
  histContainer_["PzetaDiscr"]->GetXaxis()->SetTitle("P_{#zeta} Discr. [GeV/c]");
  histContainer_["DiTau_mult"]->GetXaxis()->SetTitle("# pairs");
  histContainer_["Pt_Ditau"]->GetXaxis()->SetTitle("DiTau Vis. p_{T} [GeV/c]");
  histContainer2D_["METvsCand1Pt"]->GetXaxis()->SetTitle("Cand_{1} p_{T} [GeV/c]");
  histContainer2D_["METvsCand1Pt"]->GetYaxis()->SetTitle("MET [GeV]");
  histContainer2D_["METvsCand2Pt"]->GetXaxis()->SetTitle("Cand_{2} p_{T} [GeV/c]");
  histContainer2D_["METvsCand2Pt"]->GetYaxis()->SetTitle("MET [GeV]");
  histContainer2D_["PzetaVsPzetaVis"]->GetXaxis()->SetTitle("P_{#zeta}^{Vis} [GeV/c]");
  histContainer2D_["PzetaVsPzetaVis"]->GetYaxis()->SetTitle("P_{#zeta} [GeV/c]");
  //histContainer2D_["CompCand_VisMass(MuEle)vsCharge(MuEle)"]->GetXaxis()->SetTitle("Vis. Mass (#mu, e)");
  //histContainer2D_["CompCand_VisMass(MuEle)vsCharge(MuEle)"]->GetYaxis()->SetTitle("Charge (#mu, e)");
  //histContainer_["CompCand_VisMass_MuEle"]->GetXaxis()->SetTitle("Vis. Mass (#mu, e)");
  //histContainer_["deltaR_MuEle"]->GetXaxis()->SetTitle("#Delta R(#mu, e)");
  //histContainer2D_["CompCand_DeltaR(MuEle)vsCharge(MuEle)"]->GetXaxis()->SetTitle("#Delta R(#mu, e)");
  //histContainer2D_["CompCand_DeltaR(MuEle)vsCharge(MuEle)"]->GetYaxis()->SetTitle("Charge (#mu, e)");
  //histContainer_["VisMass_MuEle_SameSign"]->GetXaxis()->SetTitle("Vis. Mass^{SS} (#mu, e)");
  //histContainer_["VisMass_MuEle_OppositeSign"]->GetXaxis()->SetTitle("Vis. Mass^{OS} (#mu, e)");

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

void 
DiTauHistManager::endJob() 
{
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DiTauHistManager);
