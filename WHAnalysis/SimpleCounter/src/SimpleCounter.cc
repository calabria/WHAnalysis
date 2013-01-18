// -*- C++ -*-
//
// Package:    SimpleCounter
// Class:      SimpleCounter
// 
/**\class SimpleCounter SimpleCounter.cc DTandCSCSegmentsinTracks/SimpleCounter/src/SimpleCounter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Sat Jun  2 15:56:01 CEST 2012
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/Common/interface/MergeableCounter.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
//
// class declaration
//

class SimpleCounter : public edm::EDAnalyzer {
   public:
      explicit SimpleCounter(const edm::ParameterSet&);
      ~SimpleCounter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(const edm::LuminosityBlock &, const edm::EventSetup &);
      virtual void endLuminosityBlock(const edm::LuminosityBlock &, const edm::EventSetup &);

      // ----------member data ---------------------------

      int nEventsTotal;
      int nEventsFiltered;
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
SimpleCounter::SimpleCounter(const edm::ParameterSet& iConfig):
  histContainer_()
{
   //now do what ever initialization is needed

}


SimpleCounter::~SimpleCounter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
SimpleCounter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
  using namespace edm;

  double count = 1.;
  histContainer_["N_eventi"]->Fill(count);

}


// ------------ method called once each job just before starting event loop  ------------
void 
SimpleCounter::beginJob()
{

  nEventsTotal = 0;
  nEventsFiltered = 0;

  // register to the TFileService
  edm::Service<TFileService> fs;

  histContainer_["N_eventi"]=fs->make<TH1F>("N_eventi", "count", 2, 0., 2.);
  histContainer_["N_eventi_Tot"]=fs->make<TH1F>("N_eventi_Tot", "N_eventi_Tot", 2, 0., 2.);
  histContainer_["N_eventi_Filtered"]=fs->make<TH1F>("N_eventi_Filtered", "N_eventi_Filtered", 2, 0., 2.);

}

// ------------ method called once each job just after ending the event loop  ------------
void 
SimpleCounter::endJob() 
{

  histContainer_["N_eventi_Tot"]->SetBinContent(1,nEventsTotal);
  histContainer_["N_eventi_Filtered"]->SetBinContent(1,nEventsFiltered);

}

// ------------ method called when starting to processes a run  ------------
void 
SimpleCounter::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SimpleCounter::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SimpleCounter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SimpleCounter::endLuminosityBlock(const edm::LuminosityBlock & lumi, const edm::EventSetup & setup)
{

// Total number of events is the sum of the events in each of these luminosity blocks
  edm::Handle<edm::MergeableCounter> nEventsTotalCounter;
  lumi.getByLabel("nEventsTotal", nEventsTotalCounter);
  nEventsTotal += nEventsTotalCounter->value;

  edm::Handle<edm::MergeableCounter> nEventsFilteredCounter;
  lumi.getByLabel("nEventsFiltered", nEventsFilteredCounter);
  nEventsFiltered += nEventsFilteredCounter->value;

  std::cout<<"Eventi "<<nEventsTotal<<" "<<nEventsFiltered<<std::endl;

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SimpleCounter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SimpleCounter);
