// -*- C++ -*-
//
// Package:    LeadLeptonsProducer
// Class:      LeadLeptonsProducer
// 
/**\class LeadLeptonsProducer LeadLeptonsProducer.cc WHAnalysis/LeadLeptonsProducer/src/LeadLeptonsProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Wed Oct 26 16:52:28 CEST 2011
// $Id$
//
//

#ifndef WHAnalysis_LeadLeptonsProducer_LeadLeptonsProducer_h
#define WHAnalysis_LeadLeptonsProducer_LeadLeptonsProducer_h

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"


//
// class declaration
//

template<typename T>
class LeadLeptonsProducer : public edm::EDProducer {
   public:
      explicit LeadLeptonsProducer(const edm::ParameterSet&);
      ~LeadLeptonsProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

      typedef edm::Ptr<T> TPtr;
      typedef edm::View<T> TView;
      typedef std::vector<T> TCollection;

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag lepSrc_;

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
template<typename T>
LeadLeptonsProducer<T>::LeadLeptonsProducer(const edm::ParameterSet& iConfig):
  lepSrc_(iConfig.getUntrackedParameter<edm::InputTag> ("lepSrc"))
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

   produces<TCollection>("leadingLeptons");
   produces<TCollection>("subleadingLeptons");

}

template<typename T>
LeadLeptonsProducer<T>::~LeadLeptonsProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
template<typename T>
void
LeadLeptonsProducer<T>::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  using namespace pat;

  double leadPt = 0;
  double subleadPt = 0;

  edm::Handle<TView> leptons;
  iEvent.getByLabel(lepSrc_,leptons);

  double size = leptons->size();

  std::auto_ptr<TCollection> leadingLeptons(new TCollection() );
  std::auto_ptr<TCollection> subleadingLeptons(new TCollection() );

  for(int i = 0; i < size; i++){

	TPtr patLepton = leptons->ptrAt(i);

	double pt = patLepton->pt();
        //std::cout<<"pt "<<pt<<std::endl;

  }

  if(size){

	  TPtr patLepton1 = leptons->ptrAt(0);
          T object1( *patLepton1 );

	  leadingLeptons->push_back(object1);
	  leadPt = patLepton1->pt();

	  if(size > 1){

	  	TPtr patLepton2 = leptons->ptrAt(1);
          	T object2( *patLepton2 );
		
	 	subleadingLeptons->push_back(*patLepton2);
	  	subleadPt = patLepton2->pt();
	  }

  }

  //std::cout<<"lead "<<leadPt<<" sublead "<<subleadPt<<std::endl;

  iEvent.put(leadingLeptons, "leadingLeptons");
  iEvent.put(subleadingLeptons, "subleadingLeptons");
 
}

// ------------ method called once each job just before starting event loop  ------------
template<typename T>
void 
LeadLeptonsProducer<T>::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
template<typename T>
void 
LeadLeptonsProducer<T>::endJob() {
}

// ------------ method called when starting to processes a run  ------------
template<typename T>
void 
LeadLeptonsProducer<T>::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
template<typename T>
void 
LeadLeptonsProducer<T>::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
template<typename T>
void 
LeadLeptonsProducer<T>::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
template<typename T>
void 
LeadLeptonsProducer<T>::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
template<typename T>
void
LeadLeptonsProducer<T>::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

#endif

