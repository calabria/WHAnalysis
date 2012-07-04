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
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Common/interface/Ref.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

#include "DataFormats/Common/interface/ValueMap.h"

class MuonHistManager : public edm::EDAnalyzer {

public:
  explicit MuonHistManager(const edm::ParameterSet&);
  ~MuonHistManager();
  
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

MuonHistManager::MuonHistManager(const edm::ParameterSet& iConfig):

  histContainer_(),
  histContainer2D_(),
  muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
  vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc")),
  MCDist_f_(iConfig.getUntrackedParameter<vdouble>("MCDist")),
  TrueDist2011_f_(iConfig.getUntrackedParameter<vdouble>("TrueDist2011")),
  isMC_(iConfig.getUntrackedParameter<bool>("isMC"))
{
}

MuonHistManager::~MuonHistManager()
{
}

void
MuonHistManager::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  // get muon collection
  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

    
  // loop over muons
  for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon){

   if(muon->userFloat("muonWeight")) weight *= muon->userFloat("muonWeight");

   histContainer_["hMuonPt"]->Fill(muon->pt(), weight);
   histContainer_["hMuonJetPt"]->Fill(muon->pt()*(1+muon->userFloat("PFRelIsoDB04v2")), weight);
   histContainer_["hMuonEta"]->Fill(muon->eta(), weight);
   histContainer_["hMuonPhi"]->Fill(muon->phi(), weight);

   bool GlobalMuonPromptTight = false;
   bool AllArbitrated = false;
   double Chi2red = -1;
   double DptOverPt = -1;
   int TrackerHits = -1;
   int PixelHits = -1;
   int numMuonStations = -1;
   int MatchedSegments = -1;
   if(isValidRef(muon->globalTrack()) && isValidRef(muon->innerTrack())){
   	GlobalMuonPromptTight = muon::isGoodMuon(*muon, muon::GlobalMuonPromptTight);
   	AllArbitrated = muon::isGoodMuon(*muon, muon::AllArbitrated);
	Chi2red = muon->globalTrack()->normalizedChi2();
	double ptInnerTrack = muon->innerTrack()->pt();
 	if(ptInnerTrack) DptOverPt = muon->innerTrack()->ptError() / ptInnerTrack;
	const reco::HitPattern& innerTrackHitPattern = muon->innerTrack()->hitPattern();
	TrackerHits = innerTrackHitPattern.numberOfValidTrackerHits();
	PixelHits = innerTrackHitPattern.numberOfValidPixelHits();
   
	unsigned int theStationMask = (unsigned int)muon->stationMask(reco::Muon::SegmentAndTrackArbitration);
	for( int i = 0; i < 8; ++i ){ // eight stations, eight bits
   		if ( theStationMask & (1<<i) ) ++numMuonStations;
	}
     	MatchedSegments = muon->numberOfMatches();
   }

   histContainer_["hGlobalMuonPromptTight"]->Fill(GlobalMuonPromptTight,weight);
   histContainer_["hAllArbitrated"]->Fill(AllArbitrated,weight);
   histContainer_["hChi2red"]->Fill(Chi2red,weight);
   histContainer_["hDptOverPt"]->Fill(DptOverPt,weight);
   histContainer_["hTrackerHits"]->Fill(TrackerHits,weight);
   histContainer_["hPixelHits"]->Fill(PixelHits,weight);
   histContainer_["hNumMuonStations"]->Fill(numMuonStations,weight);
   histContainer_["hMatchedSegments"]->Fill(MatchedSegments,weight);

   //std::cout<<"muonID: "<<muon->userInt("muonID")<<std::endl;

   // Which type of muons in the collection?
   if(muon->isStandAloneMuon())
      if(muon->isGlobalMuon())
	if(muon->isTrackerMuon()) histContainer_["hMuonType"]->Fill(1, weight); // STA + GLB + TM
	else histContainer_["hMuonType"]->Fill(2, weight); // STA + GLB
      else 
	if(muon->isTrackerMuon()) histContainer_["hMuonType"]->Fill(3, weight);  // STA + TM
	else histContainer_["hMuonType"]->Fill(5, weight); // STA
    else
      if(muon->isTrackerMuon()) histContainer_["hMuonType"]->Fill(4, weight); // TM

    // Muon in CMS are usually MIP. What is the compatibility of a muon HP using only claorimeters?
    if(muon->isCaloCompatibilityValid())
      histContainer_["hMuonCaloCompatibility"]->Fill(muon->caloCompatibility(), weight);

    // The muon system can also be used just as only for ID. What is the compatibility of a muon HP using only calorimeters?
    histContainer_["hMuonSegCompatibility"]->Fill(muon::segmentCompatibility(*muon), weight);

    histContainer2D_["SegCompatibilityVsCaloCompatibility"]->Fill(muon->caloCompatibility(),muon::segmentCompatibility(*muon), weight);


    // How many chambers have been associated to a muon track?
    histContainer_["hMuonChamberMatched"]->Fill(muon->numberOfChambers(), weight);
    // If you look at MuonSegmentMatcher class you will see a lot of interesting quantities to look at!
    // you can get the list of matched info using matches()

    histContainer_["hMuonRelIso"]->Fill(muon->userFloat("PFRelIsoDB04v2"), weight);

    if(isValidRef(muon->track())){
      if ( vertexSrc_.label() != "" ) {
	edm::Handle<std::vector<reco::Vertex> > recoVertices;
	iEvent.getByLabel(vertexSrc_, recoVertices);
	if ( recoVertices->size() >= 1 ) {
	  const reco::Vertex& thePrimaryEventVertex = (*recoVertices->begin());
	  histContainer_["hMuonIPxy"]->Fill(muon->track()->dxy(thePrimaryEventVertex.position()), weight);
	  histContainer_["hMuonIPz"]->Fill(muon->track()->dz(thePrimaryEventVertex.position()), weight);
	  if(muon->track()->dxyError()){
		  double IPxySig = (muon->track()->dxy(thePrimaryEventVertex.position())) / (muon->track()->dxyError());
		  histContainer_["hMuonIPxySig"]->Fill(IPxySig, weight);}
	}
      }
    }

  }//Fine loop sui mu


  // Multiplicity
  histContainer_["hMuonMult"]->Fill(muons->size(), weight);

}

void 
MuonHistManager::beginJob()
{
  // register to the TFileService
  edm::Service<TFileService> fs;
  TH1::SetDefaultSumw2();

  // ID
  histContainer_["hMuonMult"]=fs->make<TH1F>("muonMult",   "muon multiplicity", 20, 0.5, 20.5);
  histContainer_["hMuonPt"]=fs->make<TH1F>("muonPt",   "muon Pt", 100, 0, 200);
  histContainer_["hMuonJetPt"]=fs->make<TH1F>("muonJetPt",   "muon JetPt", 100, 0, 200);
  histContainer_["hMuonEta"]=fs->make<TH1F>("muonEta",   "muon Eta",  100, -5,  5);
  histContainer_["hMuonPhi"]=fs->make<TH1F>("muonPhi",   "muon Phi",     100, -3.5, 3.5);
  histContainer_["hMuonType"] = fs->make<TH1F>("MuonType", "Type of Muons", 5, 1, 6);
  histContainer_["hMuonCaloCompatibility"] = fs->make<TH1F>("CaloCompatibility","Muon HP using Calorimeters only",100,0,1);
  histContainer_["hMuonSegCompatibility"] = fs->make<TH1F>("SegmentCompatibility","Muon HP using segments only",100,0,1);
  histContainer_["hMuonChamberMatched"] = fs->make<TH1F>("NumMatchedChamber", "Number of matched chambers", 7, 0, 7);
  histContainer2D_["SegCompatibilityVsCaloCompatibility"] = fs->make<TH2F>("SegCompatibilityVsCaloCompatibility","Seg. Compatibility vs. Calo Compatibility",100,0,1,100,0,1);

  // Isolation
  histContainer_["hMuonRelIso"] = fs->make<TH1F>("MuRelIso","MuRelIso",200,0,10);
  histContainer_["hMuonIPxy"] = fs->make<TH1F>("MuIPxy","MuIPxy",400,-1.,+1.);
  histContainer_["hMuonIPxySig"] = fs->make<TH1F>("MuIPxySig","MuIPxySig",400,-40.,+40.);
  histContainer_["hMuonIPz"] = fs->make<TH1F>("MuIPz","MuIPz",400,-1.,+1.);
  histContainer_["N_eventi"]=fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
  histContainer_["N_eventi_PU"]=fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);

  histContainer_["hGlobalMuonPromptTight"] = fs->make<TH1F>("GlobalMuonPromptTight","GlobalMuonPromptTight",2,0,2);
  histContainer_["hAllArbitrated"] = fs->make<TH1F>("AllArbitrated","AllArbitrated",2,0,2);
  histContainer_["hChi2red"] = fs->make<TH1F>("Chi2red","Chi2red",30,0,15);
  histContainer_["hDptOverPt"] = fs->make<TH1F>("DptOverPt","DptOverPt",50,0,1);
  histContainer_["hTrackerHits"] = fs->make<TH1F>("TrackerHits","TrackerHits",30,0,30);
  histContainer_["hPixelHits"] = fs->make<TH1F>("PixelHits","PixelHits",20,0,20);
  histContainer_["hNumMuonStations"] = fs->make<TH1F>("NumMuonStations","NumMuonStations",20,0,20);
  histContainer_["hMatchedSegments"] = fs->make<TH1F>("MatchedSegments","MatchedSegments",20,0,20);

  histContainer_["hMuonMult"]->GetXaxis()->SetTitle("# Muons");
  histContainer_["hMuonPt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hMuonJetPt"]->GetXaxis()->SetTitle("Jet p_{T} [GeV/c]");
  histContainer_["hMuonEta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hMuonPhi"]->GetXaxis()->SetTitle("#phi");
  histContainer_["hMuonType"]->GetXaxis()->SetTitle("Muon type");
  histContainer_["hMuonType"]->GetXaxis()->SetBinLabel(1, "STA + GLB + TM");
  histContainer_["hMuonType"]->GetXaxis()->SetBinLabel(2, "STA + GLB");
  histContainer_["hMuonType"]->GetXaxis()->SetBinLabel(3, "STA + TM");
  histContainer_["hMuonType"]->GetXaxis()->SetBinLabel(4, "TM");
  histContainer_["hMuonType"]->GetXaxis()->SetBinLabel(5, "STA");
  histContainer_["hMuonCaloCompatibility"] ->GetXaxis()->SetTitle("Calo Compatibility");
  histContainer_["hMuonSegCompatibility"] ->GetXaxis()->SetTitle("Segment Compatibility");
  histContainer_["hMuonChamberMatched"] ->GetXaxis()->SetTitle("NumMatchedChamber");

  histContainer_["hMuonRelIso"]->GetXaxis()->SetTitle("Muon Iso/p_{T}");
  histContainer_["hMuonIPxy"]->GetXaxis()->SetTitle("IP_{xy} [cm]");
  histContainer_["hMuonIPxySig"]->GetXaxis()->SetTitle("IP_{xy}/#sigma_{IP_{xy}} [cm]");
  histContainer_["hMuonIPz"]->GetXaxis()->SetTitle("IP_{z} [cm]");
  histContainer_["N_eventi"]->GetXaxis()->SetTitle("Events");
  histContainer_["N_eventi_PU"]->GetXaxis()->SetTitle("Events");
  histContainer2D_["SegCompatibilityVsCaloCompatibility"]->GetXaxis()->SetTitle("Calo Compatibility");
  histContainer2D_["SegCompatibilityVsCaloCompatibility"]->GetYaxis()->SetTitle("Seg. Compatibility");

  histContainer_["hGlobalMuonPromptTight"]->GetXaxis()->SetTitle("GlobalMuonPromptTight");
  histContainer_["hAllArbitrated"]->GetXaxis()->SetTitle("AllArbitrated");
  histContainer_["hChi2red"]->GetXaxis()->SetTitle("#Chi^{2}/ndof");
  histContainer_["hDptOverPt"]->GetXaxis()->SetTitle("#delta p_{T}/p_{T}");
  histContainer_["hTrackerHits"]->GetXaxis()->SetTitle("TrackerHits");
  histContainer_["hPixelHits"]->GetXaxis()->SetTitle("PixelHits");
  histContainer_["hNumMuonStations"]->GetXaxis()->SetTitle("NumMuonStations");
  histContainer_["hMatchedSegments"]->GetXaxis()->SetTitle("MatchedSegments");

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
MuonHistManager::endJob() 
{
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(MuonHistManager);
