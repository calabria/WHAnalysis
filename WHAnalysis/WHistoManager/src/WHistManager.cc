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
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

class WHistManager : public edm::EDAnalyzer {

public:
  explicit WHistManager(const edm::ParameterSet&);
  ~WHistManager();
  
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
  edm::InputTag WCand_;
  edm::InputTag PFMetTag_;
  edm::InputTag elecSrc_;
  //edm::InputTag vertexSrc_;
  typedef std::vector<double> vdouble;
  vdouble MCDist_f_;
  vdouble TrueDist2011_f_;
  bool isMC_;
};


WHistManager::WHistManager(const edm::ParameterSet& iConfig):

  histContainer_(),
  histContainer2D_(),
  WCand_(iConfig.getUntrackedParameter<edm::InputTag>("WCand")),
  PFMetTag_(iConfig.getUntrackedParameter<edm::InputTag> ("PFMetTag")),
  elecSrc_(iConfig.getUntrackedParameter<edm::InputTag>("electronSrc")),
  //vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc")),
  MCDist_f_(iConfig.getUntrackedParameter<vdouble>("MCDist")),
  TrueDist2011_f_(iConfig.getUntrackedParameter<vdouble>("TrueDist2011")),
  isMC_(iConfig.getUntrackedParameter<bool>("isMC"))
{
}

WHistManager::~WHistManager()
{
}

void
WHistManager::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  edm::Handle<edm::View<reco::CompositeCandidate> > WCandidates;
  iEvent.getByLabel(WCand_, WCandidates);

  edm::Handle<pat::METCollection> pfmet;
  iEvent.getByLabel(PFMetTag_, pfmet);

  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(elecSrc_,electrons);

  double metPx = pfmet->front().px();
  double metPy = pfmet->front().py();

  double met = pfmet->front().et();
  histContainer_["MET"]->Fill(met, weight);

  double count = 1.;
  histContainer_["N_eventi"]->Fill(count);
  histContainer_["N_eventi_PU"]->Fill(count, weight);
    
  // loop over WCand
  for(edm::View<reco::CompositeCandidate>::const_iterator WCand=WCandidates->begin(); WCand!=WCandidates->end(); ++WCand){

	histContainer_["VisMass"]->Fill(WCand->mass(), weight);
	histContainer_["Pt_W"]->Fill(WCand->pt(), weight);

        double px1 = 0;
	double py1 = 0;
	double et1 = 0;

        double px2 = 0;
	double py2 = 0;
	double et2 = 0;

	px1 = WCand->daughter(0)->px() + metPx;
	py1 = WCand->daughter(0)->py() + metPy;
	et1 = WCand->daughter(0)->et() + TMath::Sqrt(metPx*metPx + metPy*metPy);
	double mt2_1MET = et1*et1 - (px1*px1 + py1*py1);
	double mt_1MET = 0;
    	if(mt2_1MET > 0) mt_1MET = TMath::Sqrt(mt2_1MET);
	histContainer_["MT_1MET"]->Fill(mt_1MET, weight);

	px2 = WCand->daughter(1)->px() + metPx;
	py2 = WCand->daughter(1)->py() + metPy;
	et2 = WCand->daughter(1)->et() + TMath::Sqrt(metPx*metPx + metPy*metPy);
	double mt2_2MET = et2*et2 - (px2*px2 + py2*py2);
	double mt_2MET = 0;
    	if(mt2_2MET > 0) mt_2MET = TMath::Sqrt(mt2_2MET);
	histContainer_["MT_2MET"]->Fill(mt_2MET, weight);

	double pt1 = WCand->daughter(0)->pt();
	histContainer_["Cand1Pt"]->Fill(pt1, weight);
	double pt2 = WCand->daughter(1)->pt();
	histContainer_["Cand2Pt"]->Fill(pt2, weight);

	double eta1 = WCand->daughter(0)->eta();
	histContainer_["Cand1Eta"]->Fill(eta1, weight);
	double eta2 = WCand->daughter(1)->eta();
	histContainer_["Cand2Eta"]->Fill(eta2, weight);

	double phi1 = WCand->daughter(0)->phi();
	histContainer_["Cand1Phi"]->Fill(phi1, weight);
	double phi2 = WCand->daughter(1)->phi();
	histContainer_["Cand2Phi"]->Fill(phi2, weight);

	double dR = deltaR(eta1, phi1, eta2, phi2); 
	histContainer_["deltaR"]->Fill(dR, weight);

	double dPhi = deltaPhi(phi1, phi2); 
	histContainer_["deltaPhi"]->Fill(dPhi, weight);

	int charge = (WCand->daughter(0)->charge()) + (WCand->daughter(1)->charge());
	histContainer_["pairCharge"]->Fill(charge, weight);
	histContainer2D_["METvsCand1Pt"]->Fill(met,pt1, weight);
	histContainer2D_["METvsCand2Pt"]->Fill(met,pt2, weight);

	for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron){

		double eta3 = electron->eta();
		double phi3 = electron->phi();
		double dRlep = deltaR(eta1, phi1, eta3, phi3); 
		histContainer_["deltaRlep"]->Fill(dRlep, weight);
		double dPhilep = deltaPhi(phi1, phi3); 
		histContainer_["deltaPhilep"]->Fill(dPhilep, weight);

	}

  }

  histContainer_["WCand_mult"]->Fill(WCandidates->size(), weight);

}

void 
WHistManager::beginJob()
{
  // register to the TFileService
  edm::Service<TFileService> fs;
  TH1::SetDefaultSumw2();

  histContainer_["N_eventi"]=fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
  histContainer_["N_eventi_PU"]=fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);
  histContainer_["MET"]=fs->make<TH1F>("MET", "met",    40,   0., 120.);
  histContainer_["VisMass"]=fs->make<TH1F>("VisMass", "mass",    40,   0., 120.);
  histContainer_["MT_1MET"]=fs->make<TH1F>("MT_1MET", "MT_1MET",    40,   0., 200.);
  histContainer_["MT_2MET"]=fs->make<TH1F>("MT_2MET", "MT_2MET",    40,   0., 200.);
  histContainer_["Cand1Pt"]=fs->make<TH1F>("Cand1Pt", "Cand1Pt",    100,   0., 200.);
  histContainer_["Cand2Pt"]=fs->make<TH1F>("Cand2Pt", "Cand2Pt",    100,   0., 200.);
  histContainer_["Cand1Eta"]=fs->make<TH1F>("Cand1Eta", "Cand1Eta",    100, -5., +5.);
  histContainer_["Cand2Eta"]=fs->make<TH1F>("Cand2Eta", "Cand2Eta",    100, -5., +5.);
  histContainer_["Cand1Phi"]=fs->make<TH1F>("Cand1Phi", "Cand1Phi",    36, -TMath::Pi(), +TMath::Pi());
  histContainer_["Cand2Phi"]=fs->make<TH1F>("Cand2Phi", "Cand2Phi",    36, -TMath::Pi(), +TMath::Pi());
  histContainer_["deltaR"]=fs->make<TH1F>("deltaR", "deltaR",51, -0.1, 10.1);
  histContainer_["deltaPhi"]=fs->make<TH1F>("deltaPhi", "deltaPhi",   36, -TMath::Pi(), +TMath::Pi());
  histContainer_["deltaRlep"]=fs->make<TH1F>("deltaRlep", "deltaRlep",51, -0.1, 10.1);
  histContainer_["deltaPhilep"]=fs->make<TH1F>("deltaPhilep", "deltaPhilep",   36, -TMath::Pi(), +TMath::Pi());
  histContainer_["pairCharge"]=fs->make<TH1F>("pairCharge", "pairCharge",7, -3.5, +3.5);
  histContainer_["WCand_mult"]=fs->make<TH1F>("WCand_mult", "size", 100, 0., 10.);
  histContainer_["Pt_W"]=fs->make<TH1F>("Pt_W", "p_{T}^{W}",100, 0., 200.);
  histContainer2D_["METvsCand1Pt"]=fs->make<TH2F>("METvsCand1Pt",  "MET vs. Cand_{1} p_{T}", 40, 0,  120, 40, 0,  120);
  histContainer2D_["METvsCand2Pt"]=fs->make<TH2F>("METvsCand2Pt",  "MET vs. Cand_{2} p_{T}", 40, 0,  120, 40, 0,  120);

  histContainer_["N_eventi"]->GetXaxis()->SetTitle("Events");
  histContainer_["N_eventi_PU"]->GetXaxis()->SetTitle("Events");
  histContainer_["MET"]->GetXaxis()->SetTitle("MET [GeV]");
  histContainer_["VisMass"]->GetXaxis()->SetTitle("Vis.Mass [GeV/c^{2}]");
  histContainer_["MT_1MET"]->GetXaxis()->SetTitle("M_{T} (Cand_{1}, MET) [GeV/c^{2}]");
  histContainer_["MT_2MET"]->GetXaxis()->SetTitle("M_{T} (Cand_{2}, MET) [GeV/c^{2}]");
  histContainer_["Cand1Pt"]->GetXaxis()->SetTitle("Cand_1 p_{T} [GeV/c]");
  histContainer_["Cand2Pt"]->GetXaxis()->SetTitle("Cand_2 p_{T} [GeV/c]");
  histContainer_["Cand1Eta"]->GetXaxis()->SetTitle("Cand_{1} #eta");
  histContainer_["Cand2Eta"]->GetXaxis()->SetTitle("Cand_{2} #eta");
  histContainer_["Cand1Phi"]->GetXaxis()->SetTitle("Cand_{1} #phi");
  histContainer_["Cand2Phi"]->GetXaxis()->SetTitle("Cand_{2} #phi");
  histContainer_["deltaR"]->GetXaxis()->SetTitle("#Delta R(Cand_{1}, Cand_{2})");
  histContainer_["deltaPhi"]->GetXaxis()->SetTitle("#Delta#phi (Cand_{1}, Cand_{2})");
  histContainer_["deltaRlep"]->GetXaxis()->SetTitle("#Delta R (e, #mu)");
  histContainer_["deltaPhilep"]->GetXaxis()->SetTitle("#Delta#phi (e, #mu)");
  histContainer_["pairCharge"]->GetXaxis()->SetTitle("Pair Charge");
  histContainer_["WCand_mult"]->GetXaxis()->SetTitle("# W pairs");
  histContainer_["Pt_W"]->GetXaxis()->SetTitle("p_{T}^{W} [GeV/c]");
  histContainer2D_["METvsCand1Pt"]->GetXaxis()->SetTitle("Cand_{1} p_{T} [GeV/c]");
  histContainer2D_["METvsCand1Pt"]->GetYaxis()->SetTitle("MET [GeV]");
  histContainer2D_["METvsCand2Pt"]->GetXaxis()->SetTitle("Cand_{2} p_{T} [GeV/c]");
  histContainer2D_["METvsCand2Pt"]->GetYaxis()->SetTitle("MET [GeV]");

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
WHistManager::endJob() 
{
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(WHistManager);
