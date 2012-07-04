// -*- C++ -*-
//
// Package:    LeptonHighestPt
// Class:      LeptonHighestPt
// 
/**\class LeptonHighestPt LeptonHighestPt.cc WHAnalysis/LeptonHighestPt/src/LeptonHighestPt.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Tue Oct 11 15:19:44 CEST 2011
// $Id$
//
//


// system include files
#include <memory>
#include <map>
#include <string>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

//
// class declaration
//

class LeptonHighestPt : public edm::EDProducer {
   public:
      explicit LeptonHighestPt(const edm::ParameterSet&);
      ~LeptonHighestPt();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag tauSrc_;
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
LeptonHighestPt::LeptonHighestPt(const edm::ParameterSet& iConfig):
  tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc"))
{
   //register your products
/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
 
   //if you want to put into the Run
   produces<ExampleData2,InRun>();
*/
   //now do what ever other initialization is needed

  produces<pat::TauCollection>("");
  
}


LeptonHighestPt::~LeptonHighestPt()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
LeptonHighestPt::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
/* This is an event example
   //Read 'ExampleData' from the Event
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   std::auto_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
   iEvent.put(pOut);
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/

  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);

  double tempPt = 0;

  std::auto_ptr<pat::TauCollection> TauHighestPt(new pat::TauCollection);

  for(edm::View<pat::Tau>::const_iterator tau = taus->begin(); tau != taus->end(); ++tau){

	double pt = tau->pt();
	if(pt > tempPt) tempPt = pt;

  }

  for(edm::View<pat::Tau>::const_iterator tau = taus->begin(); tau != taus->end(); ++tau){

	double pt = tau->pt();
	if(pt == tempPt) TauHighestPt->push_back(*tau);
	//std::cout<<"high pt = "<<tempPt<<" pt = "<<pt<<" result = "<<(pt == tempPt)<<std::endl;

  }

  iEvent.put(TauHighestPt);
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
LeptonHighestPt::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
LeptonHighestPt::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
LeptonHighestPt::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
LeptonHighestPt::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
LeptonHighestPt::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
LeptonHighestPt::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LeptonHighestPt::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(LeptonHighestPt);
