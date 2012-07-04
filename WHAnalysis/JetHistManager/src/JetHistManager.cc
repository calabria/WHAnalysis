// -*- C++ -*-
//
// Package:    JetHistManager
// Class:      JetHistManager
// 
/**\class JetHistManager JetHistManager.cc WHAnalysis/JetHistManager/src/JetHistManager.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Thu Jul 28 15:14:52 CEST 2011
// $Id$
//
//


// system include files
#include <memory>
#include <map>
#include <string>

#include "TH1.h"
#include "TH2.h"

#include <TMath.h>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
//
// class declaration
//

class JetHistManager : public edm::EDAnalyzer {
   public:
      explicit JetHistManager(const edm::ParameterSet&);
      ~JetHistManager();

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
      edm::LumiReWeighting LumiWeights_;

      edm::InputTag jetSrc_;
      std::string bTaggingDiscriminator_;
      double bTagThreshold_;
      //edm::InputTag vertexSrc_;
      typedef std::vector<double> vdouble;
      vdouble MCDist_f_;
      vdouble TrueDist2011_f_;
      bool isMC_;

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
JetHistManager::JetHistManager(const edm::ParameterSet& iConfig):
  histContainer_(),
  jetSrc_(iConfig.getUntrackedParameter<edm::InputTag>("jetSrc")),
  bTaggingDiscriminator_(iConfig.getUntrackedParameter<std::string>("bTaggingDiscriminator")),
  bTagThreshold_(iConfig.getUntrackedParameter<double>("bTagThreshold")),
  //vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc")),
  MCDist_f_(iConfig.getUntrackedParameter<vdouble>("MCDist")),
  TrueDist2011_f_(iConfig.getUntrackedParameter<vdouble>("TrueDist2011")),
  isMC_(iConfig.getUntrackedParameter<bool>("isMC"))
{
   //now do what ever initialization is needed

}


JetHistManager::~JetHistManager()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
JetHistManager::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  // get jet collection

  edm::Handle<pat::JetCollection> patJets;
  iEvent.getByLabel(jetSrc_, patJets);

  double sumJetEt = 0.;
  double bJetNumber = 0.;

  // loop over electrons
  for(std::vector<pat::Jet>::const_iterator patJet = patJets->begin(); patJet != patJets->end(); ++patJet){

   	histContainer_["hJetPt"]->Fill(patJet->pt(), weight);
   	histContainer_["hJetEt"]->Fill(patJet->et(), weight);
   	histContainer_["hJetEta"]->Fill(patJet->eta(), weight);
   	histContainer_["hJetPhi"]->Fill(patJet->phi(), weight);

	histContainer_["hBTagDiscr"]->Fill(patJet->bDiscriminator(bTaggingDiscriminator_.c_str()));
	if(patJet->bDiscriminator(bTaggingDiscriminator_.c_str()) > bTagThreshold_){
 		histContainer_["hPtBJets"]->Fill(patJet->pt(), weight);
		histContainer_["hNumBJets"]->Fill(1, weight);
		++bJetNumber;
		}
	else histContainer_["hNumBJets"]->Fill(0);

    	sumJetEt += patJet->et();
  }

  histContainer_["hBJetNumber"]->Fill(bJetNumber, weight);
  histContainer_["hJetMult" ]->Fill(patJets->size(), weight);
  histContainer_["hSumEtJets"]->Fill(sumJetEt, weight);
}


// ------------ method called once each job just before starting event loop  ------------
void 
JetHistManager::beginJob()
{

  // register to the TFileService
  edm::Service<TFileService> fs;
  TH1::SetDefaultSumw2();

  histContainer_["N_eventi"]=fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
  histContainer_["N_eventi_PU"]=fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);
  histContainer_["hJetMult"]=fs->make<TH1F>("JetMult", "Jet multiplicity", 20, 0.5,  20.5);
  histContainer_["hJetPt"]=fs->make<TH1F>("JetPt",   "Jet p_{T}", 100, 0,  200);
  histContainer_["hJetEt"]=fs->make<TH1F>("JetEt",   "Jet E_{T}", 100, 0,  200);
  histContainer_["hJetEta"]=fs->make<TH1F>("JetEta",   "Jet Eta",100, -5,  5);
  histContainer_["hJetPhi"]=fs->make<TH1F>("JetPhi",   "Jet Phi", 100, -3.5, 3.5);

  histContainer_["hBTagDiscr"]=fs->make<TH1F>("bDiscr", "bDiscriminator",    100,   -25., 25.);
  histContainer_["hPtBJets"]=fs->make<TH1F>("bTaggedJetPt",   "bTagged Jet p_{T}", 100, 0,  200);
  histContainer_["hNumBJets"]=fs->make<TH1F>("NumBJets",   "Number of bJets", 2, 0,  2);
  histContainer_["hSumEtJets"]=fs->make<TH1F>("JetSumPt",   " Jet SumPt", 100, 0,  200);
  histContainer_["hBJetNumber"]=fs->make<TH1F>("bJetNumber","bJetNumber",10,0,10);

  histContainer_["N_eventi"]->GetXaxis()->SetTitle("Events");
  histContainer_["N_eventi_PU"]->GetXaxis()->SetTitle("Events");
  histContainer_["hJetMult"]->GetXaxis()->SetTitle("# Jets");
  histContainer_["hJetPt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hJetEt"]->GetXaxis()->SetTitle("E_{T} [GeV]");
  histContainer_["hJetEta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hJetPhi"]->GetXaxis()->SetTitle("#phi");

  histContainer_["hBTagDiscr"]->GetXaxis()->SetTitle("bDiscriminator");
  histContainer_["hPtBJets"]->GetXaxis()->SetTitle("bTagged Jet p_{T} [GeV/c]");
  histContainer_["hSumEtJets"]->GetXaxis()->SetTitle("JetSumP_{T} [GeV/c]");
  histContainer_["hBJetNumber"]->GetXaxis()->SetTitle("bJet Number");

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
JetHistManager::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
JetHistManager::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
JetHistManager::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
JetHistManager::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
JetHistManager::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetHistManager::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetHistManager);
