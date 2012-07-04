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
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

class ElectronHistManager : public edm::EDAnalyzer {

public:
  explicit ElectronHistManager(const edm::ParameterSet&);
  ~ElectronHistManager();
  
private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  // simple map to contain all histograms; 
  // histograms are booked in the beginJob() 
  // method
  std::map<std::string,TH1F*> histContainer_; 
  edm::LumiReWeighting LumiWeights_;

  // input tags  
  edm::InputTag elecSrc_;
  edm::InputTag muonSrc_;
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

ElectronHistManager::ElectronHistManager(const edm::ParameterSet& iConfig):

  histContainer_(),
  elecSrc_(iConfig.getUntrackedParameter<edm::InputTag>("electronSrc")),
  muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
  vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc")),
  MCDist_f_(iConfig.getUntrackedParameter<vdouble>("MCDist")),
  TrueDist2011_f_(iConfig.getUntrackedParameter<vdouble>("TrueDist2011")),
  isMC_(iConfig.getUntrackedParameter<bool>("isMC"))
{
}

ElectronHistManager::~ElectronHistManager()
{
}

void
ElectronHistManager::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

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

  double count = 1.;
  histContainer_["N_eventi"]->Fill(count);
  histContainer_["N_eventi_PU"]->Fill(count, weight);

  double electronEtaMaxBarrel_ = 1.442;
  double electronEtaMinEndcap_ = 1.560;

  // get electron collection
  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(elecSrc_,electrons);

  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

  //std::cout<<electrons->size()<<std::endl;

  // loop over electrons
  for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron){

   if(electron->userFloat("eleWeight")) weight *= electron->userFloat("eleWeight");

   //std::cout<<electron->pt()<<std::endl;

   histContainer_["hElePt"]->Fill(electron->pt(), weight);
   histContainer_["hEleJetPt"]->Fill(electron->pt()*(1 + electron->userFloat("PFRelIsoDB04v2")), weight);
   histContainer_["hEleEta"]->Fill(electron->eta(), weight);
   histContainer_["hElePhi"]->Fill(electron->phi(), weight);

   float MtValue = electron->userFloat("Mt");
   histContainer_["hEleMetMt"]->Fill(MtValue, weight);
   //std::cout<<"Mt "<<MtValue<<std::endl;

   histContainer_["hElePFRelIsoDeltaBeta"]->Fill(electron->userFloat("PFRelIsoDB04v2"), weight);

   for(edm::View<pat::Muon>::const_iterator muon = muons->begin(); muon != muons->end(); ++muon){
	double etaMu = muon->eta();
	double phiMu = muon->phi();
	double deltaRmuEle = deltaR(electron->eta(),electron->phi(), etaMu, phiMu );
	histContainer_["deltaRmuEle"]->Fill(deltaRmuEle, weight);    
   }

   if(electron->pt() < 20) histContainer_["EleIDWP70cIso"]->Fill(electron->electronID("simpleEleId70cIso"), weight);
   if(electron->pt() > 20)histContainer_["EleIDWP80cIso"]->Fill(electron->electronID("simpleEleId80cIso"), weight);

   histContainer_["hNHits"]->Fill(electron->userFloat("nHits"), weight);
   histContainer_["hDist"]->Fill(electron->userFloat("dist"), weight);
   histContainer_["hDCot"]->Fill(electron->userFloat("dcot"), weight);
   histContainer_["hMVA"]->Fill(electron->userFloat("mva"), weight);

   //std::cout<<"ElePt: "<<electron->pt()<<" EleSCEta: "<<electron->superClusterPosition().eta()<<" Mva: "<<electron->userFloat("mva")<<std::endl; 
   //std::cout<<"ElePt: "<<electron->pt()<<" EleEta: "<<electron->eta()<<std::endl; 
   //std::cout<<"dxy "<<electron->userFloat("dxyWrtPV")<<" dz "<<electron->userFloat("dzWrtPV")<<std::endl;

   if(electron->pt() < 20 && TMath::Abs(electron->superClusterPosition().eta()) >= 0.0 && TMath::Abs(electron->superClusterPosition().eta()) < 1.0) histContainer_["hMVA_R1"]->Fill(electron->userFloat("mva"), weight);
   else if(electron->pt() < 20 && TMath::Abs(electron->superClusterPosition().eta()) >= 1.0 && TMath::Abs(electron->superClusterPosition().eta()) < 1.5) histContainer_["hMVA_R2"]->Fill(electron->userFloat("mva"), weight);
   else if(electron->pt() < 20 && TMath::Abs(electron->superClusterPosition().eta()) >= 1.5 && TMath::Abs(electron->superClusterPosition().eta()) < 2.5) histContainer_["hMVA_R3"]->Fill(electron->userFloat("mva"), weight);
   else if(electron->pt() > 20 && TMath::Abs(electron->superClusterPosition().eta()) >= 0.0 && TMath::Abs(electron->superClusterPosition().eta()) < 1.0) histContainer_["hMVA_R4"]->Fill(electron->userFloat("mva"), weight);
   else if(electron->pt() > 20 && TMath::Abs(electron->superClusterPosition().eta()) >= 1.0 && TMath::Abs(electron->superClusterPosition().eta()) < 1.5) histContainer_["hMVA_R5"]->Fill(electron->userFloat("mva"), weight);
   else if(electron->pt() > 20 && TMath::Abs(electron->superClusterPosition().eta()) >= 1.5 && TMath::Abs(electron->superClusterPosition().eta()) < 2.5) histContainer_["hMVA_R6"]->Fill(electron->userFloat("mva"), weight);
   //else std::cout<<"No histograms filled"<<std::endl;

   histContainer_["hConvVeto"]->Fill(electron->userInt("antiConv"), weight);

   //std::cout<<"sigmaLor "<<electron->userFloat("sihih")<<" SigmaPat "<<electron->sigmaIetaIeta()<<std::endl;

   /*if ( TMath::Abs(electron->eta()) < electronEtaMaxBarrel_ && electron->pt() < 20) {
	std::cout<<"LowPtBarrel: sigma = "<<electron->userFloat("sihih")<<" dPhi = "<<electron->userFloat("dPhi")<< " dEta = "<<electron->userFloat("dEta")<<" HoE = "<<electron->userFloat("HoE")<<" fbrem = "<<electron->fbrem()<<" antiConVeto = "<<electron->userInt("antiConv")<<" Nhits = "<<electron->userFloat("nHits")<<" PreID = "<<electron->userInt("mvaPreselection")<<std::endl;
	//std::cout<<"sigmaPat = "<<electron->sigmaIetaIeta()<<" dEtaPat "<<TMath::Abs(electron->deltaEtaSuperClusterTrackAtVtx())<<std::endl;
   }
   if ( TMath::Abs(electron->eta()) > electronEtaMinEndcap_ && electron->pt() < 20) {
	std::cout<<"LowPtEndcap: sigma = "<<electron->userFloat("sihih")<<" dPhi = "<<electron->userFloat("dPhi")<< " dEta = "<<electron->userFloat("dEta")<<" HoE = "<<electron->userFloat("HoE")<<" fbrem = "<<electron->fbrem()<<" antiConVeto = "<<electron->userInt("antiConv")<<" Nhits = "<<electron->userFloat("nHits")<<" PreID = "<<electron->userInt("mvaPreselection")<<std::endl;
	//std::cout<<"sigmaPat = "<<electron->sigmaIetaIeta()<<" dEtaPat "<<TMath::Abs(electron->deltaEtaSuperClusterTrackAtVtx())<<std::endl;
   }
   if ( TMath::Abs(electron->eta()) < electronEtaMaxBarrel_ && electron->pt() > 20) {
	std::cout<<"HighPtBarrel: sigma = "<<electron->userFloat("sihih")<<" dPhi = "<<electron->userFloat("dPhi")<< " dEta = "<<electron->userFloat("dEta")<<" HoE = "<<electron->userFloat("HoE")<<" fbrem = "<<electron->fbrem()<<" antiConVeto = "<<electron->userInt("antiConv")<<" Nhits = "<<electron->userFloat("nHits")<<" PreID = "<<electron->userInt("mvaPreselection")<<std::endl;
	//std::cout<<"sigmaPat = "<<electron->sigmaIetaIeta()<<" dEtaPat "<<TMath::Abs(electron->deltaEtaSuperClusterTrackAtVtx())<<std::endl;
   }
   if ( TMath::Abs(electron->eta()) > electronEtaMinEndcap_ && electron->pt() > 20) {
	std::cout<<"HighPtEndcap: sigma = "<<electron->userFloat("sihih")<<" dPhi = "<<electron->userFloat("dPhi")<< " dEta = "<<electron->userFloat("dEta")<<" HoE = "<<electron->userFloat("HoE")<<" fbrem = "<<electron->fbrem()<<" antiConVeto = "<<electron->userInt("antiConv")<<" Nhits = "<<electron->userFloat("nHits")<<" PreID = "<<electron->userInt("mvaPreselection")<<std::endl;
	//std::cout<<"sigmaPat = "<<electron->sigmaIetaIeta()<<" dEtaPat "<<TMath::Abs(electron->deltaEtaSuperClusterTrackAtVtx())<<std::endl;
   }*/

   if ( TMath::Abs(electron->eta()) < electronEtaMaxBarrel_ ) {
      double EleIso_Barrel = ( electron->dr03TkSumPt() + std::max(0., electron->dr03EcalRecHitSumEt() - 1.) + electron->dr03HcalTowerSumEt() ) / electron->p4().Pt();
      histContainer_["hEleRelIso_Barrel"]->Fill(EleIso_Barrel, weight);
      histContainer_["hEleEnOverPBarrel"]->Fill(electron->eSuperClusterOverP(), weight);
      histContainer_["hEleHadEnOverEmEnBarrel"]->Fill(electron->hcalOverEcal(), weight); 
      histContainer_["hEleSigmaIEtaIEtaBarrel"]->Fill(electron->sigmaIetaIeta(), weight); 
      histContainer_["hEleAbsDeltaPhiBarrel"]->Fill(TMath::Abs(electron->deltaPhiSuperClusterTrackAtVtx()), weight); 
      histContainer_["hEleAbsDeltaEtaBarrel"]->Fill(TMath::Abs(electron->deltaEtaSuperClusterTrackAtVtx()), weight);
      histContainer_["hEleTrkIso03OverPtBarrel"]->Fill( electron->dr03TkSumPt() / electron->pt(), weight );
      histContainer_["hEleEMIso03OverPtBarrel"]->Fill( TMath::Max(electron->dr03EcalRecHitSumEt() - 1.0, 0.0) / electron->pt(), weight );
      histContainer_["hEleHadIso03OverPtBarrel"]->Fill( electron->dr03HcalTowerSumEt() / electron->pt(), weight);
   }
   if ( TMath::Abs(electron->eta()) > electronEtaMinEndcap_ ) {
      double EleIso_Endcap = ( electron->dr03TkSumPt() + electron->dr03EcalRecHitSumEt() + electron->dr03HcalTowerSumEt() ) / electron->p4().Pt();
      histContainer_["hEleRelIso_Endcap"]->Fill(EleIso_Endcap, weight);
      histContainer_["hEleEnOverPEndcap"]->Fill(electron->eSuperClusterOverP(), weight);
      histContainer_["hEleHadEnOverEmEnEndcap"]->Fill(electron->hcalOverEcal(), weight); 
      histContainer_["hEleSigmaIEtaIEtaEndcap"]->Fill(electron->sigmaIetaIeta(), weight); 
      histContainer_["hEleAbsDeltaPhiEndcap"]->Fill(TMath::Abs(electron->deltaPhiSuperClusterTrackAtVtx()), weight); 
      histContainer_["hEleAbsDeltaEtaEndcap"]->Fill(TMath::Abs(electron->deltaEtaSuperClusterTrackAtVtx()), weight);
      histContainer_["hEleTrkIso03OverPtEndcap"]->Fill( electron->dr03TkSumPt() / electron->pt(), weight );
      histContainer_["hEleEMIso03OverPtEndcap"]->Fill( TMath::Max(electron->dr03EcalRecHitSumEt() - 1.0, 0.0) / electron->pt(), weight );
      histContainer_["hEleHadIso03OverPtEndcap"]->Fill( electron->dr03HcalTowerSumEt() / electron->pt(), weight);
   }

   if(isValidRef(electron->gsfTrack())){
     if ( vertexSrc_.label() != "" ) {
	edm::Handle<std::vector<reco::Vertex> > recoVertices;
	iEvent.getByLabel(vertexSrc_, recoVertices);
	if ( recoVertices->size() >= 1 ) {
	  const reco::Vertex& thePrimaryEventVertex = (*recoVertices->begin());
	  histContainer_["hEleIPxy"]->Fill(electron->gsfTrack()->dxy(thePrimaryEventVertex.position()), weight);
	  histContainer_["hEleIPz"]->Fill(electron->gsfTrack()->dz(thePrimaryEventVertex.position()), weight);
	  //std::cout<<"IPz "<<electron->gsfTrack()->dz(thePrimaryEventVertex.position())<<std::endl;
	  if(electron->gsfTrack()->dxyError()){
		  double IPxySig = (electron->gsfTrack()->dxy(thePrimaryEventVertex.position())) / (electron->gsfTrack()->dxyError());
		  histContainer_["hEleIPxySig"]->Fill(IPxySig, weight);}
	}
     }
   }

  }

  // Multiplicity
  histContainer_["hEleMult" ]->Fill(electrons->size(), weight);

}

void 
ElectronHistManager::beginJob()
{
  // register to the TFileService
  edm::Service<TFileService> fs;
  TH1::SetDefaultSumw2();
  
  //Electron Section

  histContainer_["N_eventi"]=fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
  histContainer_["N_eventi_PU"]=fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);
  histContainer_["hEleMult"]=fs->make<TH1F>("eleMult",   "electron multiplicity", 20, 0.5, 20.5);
  histContainer_["hElePt"]=fs->make<TH1F>("elePt",   "electron Pt", 100, 0,  200);
  histContainer_["hEleJetPt"]=fs->make<TH1F>("eleJetPt",   "electron JetPt", 100, 0,  200);
  histContainer_["hEleEta"]=fs->make<TH1F>("eleEta",   "electron Eta",100, -5,  5);
  histContainer_["hElePhi"]=fs->make<TH1F>("elePhi",   "electron Phi", 100, -3.5, 3.5);
  histContainer_["hEleMetMt"]=fs->make<TH1F>("EleMetMt",   "EleMetMt", 50, 0, 200);
  histContainer_["deltaRmuEle"]=fs->make<TH1F>("deltaRmuEle",   "deltaRmuEle", 100, 0., 5.);

  histContainer_["EleIDWP70cIso"]=fs->make<TH1F>("EleIDWP70cIso", "EleIDWP70cIso",    8,   -0.5, 7.5);
  histContainer_["EleIDWP80cIso"]=fs->make<TH1F>("EleIDWP80cIso", "EleIDWP80cIso",    8,   -0.5, 7.5);

  histContainer_["hNHits"]=fs->make<TH1F>("nHits","MissingExpInnerHits",5,0,5);
  histContainer_["hDist"]=fs->make<TH1F>("dist", "Distance Of Closest Approach", 50,0,1);
  histContainer_["hDCot"]=fs->make<TH1F>("dcot", "DeltaCotTheta", 50,0,0.5);
  histContainer_["hMVA"]=fs->make<TH1F>("mva", "mva", 30,-1.5,+1.5);
  histContainer_["hMVA_R1"]=fs->make<TH1F>("mva_R1", "mva (pt < 20 && 0.0 < superClusterPosition.Eta < 1.0)", 30,-1.5,+1.5);
  histContainer_["hMVA_R2"]=fs->make<TH1F>("mva_R2", "mva (pt < 20 && 1.0 < superClusterPosition.Eta < 1.5)", 30,-1.5,+1.5);
  histContainer_["hMVA_R3"]=fs->make<TH1F>("mva_R3", "mva (pt < 20 && 1.5 < superClusterPosition.Eta < 2.5)", 30,-1.5,+1.5);
  histContainer_["hMVA_R4"]=fs->make<TH1F>("mva_R4", "mva (pt > 20 && 0.0 < superClusterPosition.Eta < 1.0)", 30,-1.5,+1.5);
  histContainer_["hMVA_R5"]=fs->make<TH1F>("mva_R5", "mva (pt > 20 && 1.0 < superClusterPosition.Eta < 1.5)", 30,-1.5,+1.5);
  histContainer_["hMVA_R6"]=fs->make<TH1F>("mva_R6", "mva (pt > 20 && 1.5 < superClusterPosition.Eta < 2.5)", 30,-1.5,+1.5);
  histContainer_["hConvVeto"]=fs->make<TH1F>("antiConv","antiConv", 2,0,2);

  histContainer_["hEleRelIso_Barrel"] = fs->make<TH1F>("EleRelIso_Barrel","EleRelIso_Barrel",200,0,10);
  histContainer_["hEleRelIso_Endcap"] = fs->make<TH1F>("EleRelIso_Endcap","EleRelIso_Endcap",200,0,10);
  histContainer_["hElePFRelIsoDeltaBeta"] = fs->make<TH1F>("ElePFRelIsoDeltaBeta","ElePFRelIsoDeltaBeta",200,0,10);

  histContainer_["hEleTrkIso03OverPtBarrel"] = fs->make<TH1F>("EleTrkIso03OverPtBarrel","EleTrkIso03OverPtBarrel",200,0,10);
  histContainer_["hEleEMIso03OverPtBarrel"] = fs->make<TH1F>("hEleEMIso03OverPtBarrel","hEleEMIso03OverPtBarrel",200,0,10);
  histContainer_["hEleHadIso03OverPtBarrel"] = fs->make<TH1F>("hEleHadIso03OverPtBarrel","hEleHadIso03OverPtBarrel",200,0,10);
  histContainer_["hEleTrkIso03OverPtEndcap"] = fs->make<TH1F>("EleTrkIso03OverPtEndcap","EleTrkIso03OverPtEndcap",200,0,10);
  histContainer_["hEleEMIso03OverPtEndcap"] = fs->make<TH1F>("hEleEMIso03OverPtEndcap","hEleEMIso03OverPtEndcap",200,0,10);
  histContainer_["hEleHadIso03OverPtEndcap"] = fs->make<TH1F>("hEleHadIso03OverPtEndcap","hEleHadIso03OverPtEndcap",200,0,10);

  histContainer_["hEleIPxy"] = fs->make<TH1F>("EleIPxy","EleIPxy",400,-1.,+1.);
  histContainer_["hEleIPxySig"] = fs->make<TH1F>("EleIPxySig","EleIPxySig",400,-40.,+40.);
  histContainer_["hEleIPz"] = fs->make<TH1F>("EleIPz","EleIPz",400,-1.,+1.);

  histContainer_["hEleEnOverPBarrel"] = fs->make<TH1F>("EleEnOverPBarrel","EleEnOverPBarrel",50, 0., 5.);
  histContainer_["hEleHadEnOverEmEnBarrel"] = fs->make<TH1F>("EleHadEnOverEmEnBarrel","EleHadEnOverEmEnBarrel", 102, -0.01, 1.01); 
  histContainer_["hEleSigmaIEtaIEtaBarrel"] = fs->make<TH1F>("EleSigmaIEtaIEtaBarrel","EleSigmaIEtaIEtaBarrel", 102, -0.001, 0.101); 
  histContainer_["hEleAbsDeltaPhiBarrel"] = fs->make<TH1F>("EleAbsDeltaPhiBarrel","EleAbsDeltaPhiBarrel", 82, -0.001, 0.081); 
  histContainer_["hEleAbsDeltaEtaBarrel"] = fs->make<TH1F>("EleAbsDeltaEtaBarrel","EleAbsDeltaEtaBarrel", 102, -0.001, 0.101);

  histContainer_["hEleEnOverPEndcap"] = fs->make<TH1F>("EleEnOverPEndcap","EleEnOverPEndcap",50, 0., 5.);
  histContainer_["hEleHadEnOverEmEnEndcap"] = fs->make<TH1F>("EleHadEnOverEmEnEndcap","EleHadEnOverEmEnEndcap", 102, -0.01, 1.01); 
  histContainer_["hEleSigmaIEtaIEtaEndcap"] = fs->make<TH1F>("EleSigmaIEtaIEtaEndcap","EleSigmaIEtaIEtaEndcap", 102, -0.001, 0.101); 
  histContainer_["hEleAbsDeltaPhiEndcap"] = fs->make<TH1F>("EleAbsDeltaPhiEndcap","EleAbsDeltaPhiEndcap", 82, -0.001, 0.081); 
  histContainer_["hEleAbsDeltaEtaEndcap"] = fs->make<TH1F>("EleAbsDeltaEtaEndcap","EleAbsDeltaEtaEndcap", 102, -0.001, 0.101);

  histContainer_["N_eventi"]->GetXaxis()->SetTitle("Events");
  histContainer_["N_eventi_PU"]->GetXaxis()->SetTitle("Events");
  histContainer_["hEleMult"]->GetXaxis()->SetTitle("# Electrons");
  histContainer_["hElePt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hEleJetPt"]->GetXaxis()->SetTitle("Jet p_{T} [GeV/c]");
  histContainer_["hEleEta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hElePhi"]->GetXaxis()->SetTitle("#phi");
  histContainer_["hEleMetMt"]->GetXaxis()->SetTitle("M_{T}(p_{T}^{e},MET)");
  histContainer_["deltaRmuEle"]->GetXaxis()->SetTitle("#Delta R(#mu, e)");

  histContainer_["EleIDWP70cIso"]->GetXaxis()->SetTitle("EleIDWP70cIso");
  histContainer_["EleIDWP80cIso"]->GetXaxis()->SetTitle("EleIDWP80cIso");

  histContainer_["hNHits"]->GetXaxis()->SetTitle("MissingExpInnerHits");
  histContainer_["hDist"]->GetXaxis()->SetTitle("Distance Of Closest Approach");
  histContainer_["hDCot"]->GetXaxis()->SetTitle("DeltaCotTheta");
  histContainer_["hMVA"]->GetXaxis()->SetTitle("mva");
  histContainer_["hMVA_R1"]->GetXaxis()->SetTitle("mva");
  histContainer_["hMVA_R2"]->GetXaxis()->SetTitle("mva");
  histContainer_["hMVA_R3"]->GetXaxis()->SetTitle("mva");
  histContainer_["hMVA_R4"]->GetXaxis()->SetTitle("mva");
  histContainer_["hMVA_R5"]->GetXaxis()->SetTitle("mva");
  histContainer_["hMVA_R6"]->GetXaxis()->SetTitle("mva");
  histContainer_["hConvVeto"]->GetXaxis()->SetTitle("AntiConvVeto");

  histContainer_["hEleRelIso_Barrel"]->GetXaxis()->SetTitle("Ele Iso/p_{T}");
  histContainer_["hEleRelIso_Endcap"]->GetXaxis()->SetTitle("Ele Iso/p_{T}");
  histContainer_["hElePFRelIsoDeltaBeta"]->GetXaxis()->SetTitle("Ele Iso^{#Delta#beta}_{PF}/p_{T}");

  histContainer_["hEleTrkIso03OverPtBarrel"]->GetXaxis()->SetTitle("EleTrkIso03OverPtBarrel");
  histContainer_["hEleEMIso03OverPtBarrel"]->GetXaxis()->SetTitle("hEleEMIso03OverPtBarrel");
  histContainer_["hEleHadIso03OverPtBarrel"]->GetXaxis()->SetTitle("hEleHadIso03OverPtBarrel");
  histContainer_["hEleTrkIso03OverPtEndcap"]->GetXaxis()->SetTitle("EleTrkIso03OverPtEndcap");
  histContainer_["hEleEMIso03OverPtEndcap"]->GetXaxis()->SetTitle("hEleEMIso03OverPtEndcap");
  histContainer_["hEleHadIso03OverPtEndcap"]->GetXaxis()->SetTitle("hEleHadIso03OverPtEndcap");

  histContainer_["hEleIPxy"]->GetXaxis()->SetTitle("IP_{xy} [cm]");
  histContainer_["hEleIPxySig"]->GetXaxis()->SetTitle("IP_{xy}/#sigma_{IP_{xy}}");
  histContainer_["hEleIPz"]->GetXaxis()->SetTitle("IP_{z} [cm]");

  histContainer_["hEleIPxy"]->GetXaxis()->SetTitle("IP_{xy} [cm]");
  histContainer_["hEleIPz"]->GetXaxis()->SetTitle("IP_{z} [cm]");

  histContainer_["hEleEnOverPBarrel"]->GetXaxis()->SetTitle("E/p");
  histContainer_["hEleHadEnOverEmEnBarrel"]->GetXaxis()->SetTitle("H/E"); 
  histContainer_["hEleSigmaIEtaIEtaBarrel"]->GetXaxis()->SetTitle("#sigma_{i#eta i#eta}"); 
  histContainer_["hEleAbsDeltaPhiBarrel"]->GetXaxis()->SetTitle("#Delta#phi"); 
  histContainer_["hEleAbsDeltaEtaBarrel"]->GetXaxis()->SetTitle("#Delta#eta");

  histContainer_["hEleEnOverPEndcap"]->GetXaxis()->SetTitle("E/p");
  histContainer_["hEleHadEnOverEmEnEndcap"]->GetXaxis()->SetTitle("H/E"); 
  histContainer_["hEleSigmaIEtaIEtaEndcap"]->GetXaxis()->SetTitle("#sigma_{i#eta i#eta}"); 
  histContainer_["hEleAbsDeltaPhiEndcap"]->GetXaxis()->SetTitle("#Delta#phi"); 
  histContainer_["hEleAbsDeltaEtaEndcap"]->GetXaxis()->SetTitle("#Delta#eta");

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
ElectronHistManager::endJob() 
{
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(ElectronHistManager);
