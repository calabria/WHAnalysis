// -*- C++ -*-
//
// Package:    SelectedEvents
// Class:      SelectedEvents
// 
/**\class SelectedEvents SelectedEvents.cc WHAnalysis/SelectedEvents/src/SelectedEvents.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Sun Jul 10 18:27:48 CEST 2011
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Common/interface/Ref.h"


#include <fstream>
#include <sstream>
//
// class declaration
//

class SelectedEvents : public edm::EDAnalyzer {
   public:
      explicit SelectedEvents(const edm::ParameterSet&);
      ~SelectedEvents();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      std::string path_;
      edm::InputTag muonSrc_;
      edm::InputTag eleSrc_;
      edm::InputTag tauSrc_;

      // ----------member data ---------------------------
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
SelectedEvents::SelectedEvents(const edm::ParameterSet& iConfig):
	path_(iConfig.getUntrackedParameter<std::string>("path","/cmshome/calabria/")),
      	muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
      	eleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("eleSrc")),
      	tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc"))
{
   //now do what ever initialization is needed

}


SelectedEvents::~SelectedEvents()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
SelectedEvents::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  std::ofstream selEvents;
  std::stringstream txtName;
  int run = iEvent.id().run();
  int event = iEvent.id().event();
  txtName<<path_<<"run_"<<run<<"__event_"<<event<<".txt";
  std::string txt = txtName.str();
  selEvents.open(txt.c_str());
  selEvents<<iEvent.id()<<std::endl;
  selEvents.close();

  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);
  for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon){

	double muonpt = muon->pt();
	//double muonphi = muon->phi();
	double muoneta = muon->eta();
	double muoniso = muon->userFloat("PFRelIsoDB03v2");
	//std::cout<<"muon pt: "<<muonpt<<" muon eta: "<<muoneta<<" muon iso: "<<muoniso<<std::endl;
  }

  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(eleSrc_,electrons);
  for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron){

	double elept = electron->pt();
	//double elephi = electron->phi();
	double eleeta = electron->eta();
	double eleiso = electron->userFloat("PFRelIsoDB03v3");
	//std::cout<<"electron pt: "<<elept<<" electron eta: "<<eleeta<<" electron iso: "<<eleiso<<std::endl;
  }

  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);
  for(edm::View<pat::Tau>::const_iterator patTau=taus->begin(); patTau!=taus->end(); ++patTau){

	double taupt = patTau->pt();
	//double tauphi = patTau->phi();
	double taueta = patTau->eta();
	int tauiso = patTau->tauID("byLooseIsolation");
	int tauisoDB = patTau->tauID("byLooseCombinedIsolationDeltaBetaCorr");
	int tauID = patTau->tauID("decayModeFinding");
	//std::cout<<"patTau pt: "<<taupt<<" patTau eta: "<<taueta<<" tauID: "<<tauID<<" patTau iso: "<<tauiso<<" patTau isoDB: "<<tauisoDB<<std::endl;

  }

}


// ------------ method called once each job just before starting event loop  ------------
void 
SelectedEvents::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SelectedEvents::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
SelectedEvents::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SelectedEvents::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SelectedEvents::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SelectedEvents::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SelectedEvents::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SelectedEvents);
