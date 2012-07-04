// -*- C++ -*-
//
// Package:    VertexProducer
// Class:      VertexProducer
// 
/**\class VertexProducer VertexProducer.cc WHAnalysis/VertexProducer/src/VertexProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Thu Jul 28 13:59:43 CEST 2011
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Common/interface/Handle.h"

#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <iomanip>

//
// class declaration
//

class VertexProducer : public edm::EDProducer {
   public:
      explicit VertexProducer(const edm::ParameterSet&);
      ~VertexProducer();

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

      edm::InputTag vertexSrc_;
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
VertexProducer::VertexProducer(const edm::ParameterSet& iConfig):
   vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag> ("vertexSrc"))
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

   produces<reco::VertexCollection>();
  
}


VertexProducer::~VertexProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
VertexProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  edm::Handle<reco::VertexCollection> pvHandle; 
  iEvent.getByLabel(vertexSrc_, pvHandle);

  std::auto_ptr<reco::VertexCollection> selectedVerticesSumPT(new reco::VertexCollection);

/*  
  double sumPt = 0;
  double prevSumPt = 0;
  double sumPtNew = 0;

  if(pvHandle.isValid()) {

	  const reco::VertexCollection & vertices = *pvHandle.product();
	  for(reco::VertexCollection::const_iterator it=vertices.begin() ; it!=vertices.end() ; ++it){

			sumPt = it->p4().pt();
			//std::cout<<"sumPt "<<sumPt<<std::endl;
			if(sumPt >= prevSumPt) prevSumPt = sumPt;

		}
  }

  //std::cout<<"Final sumPt "<<prevSumPt<<std::endl;

  if(pvHandle.isValid()) {

	  const reco::VertexCollection & vertices = *pvHandle.product();
	  for(reco::VertexCollection::const_iterator it=vertices.begin() ; it!=vertices.end() ; ++it){

			sumPtNew = it->p4().pt();
			if(sumPtNew == prevSumPt){
				//std::cout<<"Selected sumPt "<<sumPtNew<<std::endl;
				selectedVerticesSumPT->push_back(*it);}

		}
  }*/

  if (!pvHandle->empty()) {

	const reco::Vertex &pv = (*pvHandle)[0];
	selectedVerticesSumPT->push_back(pv);
  }

  iEvent.put(selectedVerticesSumPT);
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
VertexProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
VertexProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
VertexProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
VertexProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
VertexProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
VertexProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
VertexProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(VertexProducer);
