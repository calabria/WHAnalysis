// -*- C++ -*-
//
// Package:    PuDistribution
// Class:      PuDistribution
// 
/**\class PuDistribution PuDistribution.cc WHAnalysis/PuDistribution/src/PuDistribution.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Tue Sep 13 14:52:13 CEST 2011
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

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
//
// class declaration
//

class PuDistribution : public edm::EDAnalyzer {
   public:
      explicit PuDistribution(const edm::ParameterSet&);
      ~PuDistribution();

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
PuDistribution::PuDistribution(const edm::ParameterSet& iConfig):
    histContainer_()
{
   //now do what ever initialization is needed

}


PuDistribution::~PuDistribution()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
PuDistribution::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  Handle<std::vector< PileupSummaryInfo > >  PupInfo;
  iEvent.getByLabel(edm::InputTag("addPileupInfo"), PupInfo);

  std::vector<PileupSummaryInfo>::const_iterator PVI;

  int npv = -1;
  int trueInt = -1;
  int trueInt_BX = -1;
  for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI) {

	  int BX = PVI->getBunchCrossing();
	  trueInt = PVI->getTrueNumInteractions();
	  histContainer_["nti"]->Fill(trueInt);

	  if(BX == 0) { 
	     	npv = PVI->getPU_NumInteractions();
		histContainer_["npv"]->Fill(npv);
	  	trueInt_BX = PVI->getTrueNumInteractions();
	        histContainer_["nti_BX"]->Fill(trueInt_BX);
	     	continue;
	   	}

  }

}


// ------------ method called once each job just before starting event loop  ------------
void 
PuDistribution::beginJob()
{

  edm::Service<TFileService> fs;

  histContainer_["npv"]=fs->make<TH1F>("npv", "npv", 50, -0.5, 49.5);
  histContainer_["nti"]=fs->make<TH1F>("nti", "nti", 50, -0.5, 49.5);
  histContainer_["nti_BX"]=fs->make<TH1F>("nti_BX", "nti_BX", 50, -0.5, 49.5);

}

// ------------ method called once each job just after ending the event loop  ------------
void 
PuDistribution::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
PuDistribution::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PuDistribution::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PuDistribution::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PuDistribution::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PuDistribution::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PuDistribution);
