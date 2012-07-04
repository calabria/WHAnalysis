// -*- C++ -*-
//
// Package:    ElectronIPSelector
// Class:      ElectronIPSelector
// 
/**\class ElectronIPSelector ElectronIPSelector.cc WHAnalysis/ElectronIPSelector/src/ElectronIPSelector.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Sat Oct 22 14:06:02 CEST 2011
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/Electron.h"


//
// class declaration
//

class ElectronIPSelector : public edm::EDFilter {
   public:
      explicit ElectronIPSelector(const edm::ParameterSet&);
      ~ElectronIPSelector();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual bool beginRun(edm::Run&, edm::EventSetup const&);
      virtual bool endRun(edm::Run&, edm::EventSetup const&);
      virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag vertexSrc_;
      edm::InputTag electronSrc_;
      double IPmin_;
      double IPmax_;

};

template<typename T>
bool isValidRef(const edm::Ref<T>& ref)
{
  return ( (ref.isAvailable() || ref.isTransient()) && ref.isNonnull() );  
}

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
ElectronIPSelector::ElectronIPSelector(const edm::ParameterSet& iConfig):
   vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag> ("vertexSrc")),
   electronSrc_(iConfig.getUntrackedParameter<edm::InputTag> ("electronSrc")),
   IPmin_(iConfig.getUntrackedParameter<double> ("IPmin")),
   IPmax_(iConfig.getUntrackedParameter<double> ("IPmax"))
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
   produces<pat::ElectronCollection>("selectedElectronsByIP").setBranchAlias("selectedElectronsByIP");
  
}


ElectronIPSelector::~ElectronIPSelector()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
bool
ElectronIPSelector::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  bool result = false;
  bool eleResult = false;

  edm::Handle<reco::VertexCollection> primaryEventVertexCollection;
  iEvent.getByLabel(vertexSrc_, primaryEventVertexCollection);

  edm::Handle<edm::View<pat::Electron> > patElectronCollection;
  iEvent.getByLabel(electronSrc_,patElectronCollection);

  std::auto_ptr<pat::ElectronCollection> selectedElectronsByIP(new pat::ElectronCollection);

  if ( primaryEventVertexCollection->size() < 1 ) {
    return false;
  } 

  const reco::Vertex& thePrimaryEventVertex = (*primaryEventVertexCollection->begin());

  for ( edm::View<pat::Electron>::const_iterator patElectron = patElectronCollection->begin(); patElectron != patElectronCollection->end(); ++patElectron ) {

	  if(isValidRef(patElectron->gsfTrack())){
      		double ip = patElectron->gsfTrack()->dxy(thePrimaryEventVertex.position());

	      	if ( ip > IPmin_ && ip < IPmax_ ) {
			result = true;
			eleResult = true;
	      	}
	      	else eleResult = false;
		//if(ip > IPmin_ && ip < IPmax_) std::cout<<"ip "<<ip<<" result "<<result<<" eleResult "<<eleResult<<std::endl;

	    	if(eleResult) selectedElectronsByIP->push_back(*patElectron);    

	  }

  }

   iEvent.put(selectedElectronsByIP, "selectedElectronsByIP");
   return result;
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
ElectronIPSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ElectronIPSelector::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
ElectronIPSelector::beginRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
ElectronIPSelector::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
ElectronIPSelector::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
ElectronIPSelector::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ElectronIPSelector::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(ElectronIPSelector);
