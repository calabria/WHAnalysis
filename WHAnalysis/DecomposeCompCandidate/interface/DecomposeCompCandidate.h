// -*- C++ -*-
//
// Package:    DecomposeCompCandidate
// Class:      DecomposeCompCandidate
// 
/**\class DecomposeCompCandidate DecomposeCompCandidate.cc WHAnalysis/DecomposeCompCandidate/src/DecomposeCompCandidate.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Thu Mar 15 20:04:47 CET 2012
// $Id$
//
//

#ifndef WHAnalysis_DecomposeCompCandidate_DecomposeCompCandidate_h
#define WHAnalysis_DecomposeCompCandidate_DecomposeCompCandidate_h

// user include files
#include <memory>
#include <map>
#include <string>
#include <cmath>
#include <vector>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/GeometryVector/interface/VectorUtil.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"

//
// class declaration
//
template<typename T>
class DecomposeCompCandidate : public edm::EDProducer {
   public:
      explicit DecomposeCompCandidate(const edm::ParameterSet&);
      ~DecomposeCompCandidate();

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

      edm::InputTag obj1Src_;
      edm::InputTag obj2Src_;
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
DecomposeCompCandidate<T>::DecomposeCompCandidate(const edm::ParameterSet& iConfig):
  obj1Src_(iConfig.getUntrackedParameter<edm::InputTag>("obj1Src")),
  obj2Src_(iConfig.getUntrackedParameter<edm::InputTag>("obj2Src"))
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

   produces<TCollection>("");
  
}

template<typename T>
DecomposeCompCandidate<T>::~DecomposeCompCandidate()
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
DecomposeCompCandidate<T>::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;

  edm::Handle<TView> objects1;
  iEvent.getByLabel(obj1Src_,objects1);

  edm::Handle<View<reco::Candidate> > objects2;
  iEvent.getByLabel(obj2Src_,objects2);

  int sizeObj1 = objects1->size();
  int sizeObj2 = objects2->size();

  std::auto_ptr<TCollection> sameSignObj1(new TCollection() );

  for(int i = 0; i < sizeObj1; i++){

	bool result = false;

	TPtr obj1 = objects1->ptrAt(i);

	T object1( *obj1 );

	int charge1 = obj1->charge();

    	View<reco::Candidate>::const_iterator obj2; 
    	for (obj2 = objects2->begin(); obj2 != objects2->end(); ++obj2) {

		bool resultTMP = false;

		int charge2 = obj2->charge();

		if(charge1*charge2 > 0) resultTMP = true;

		result = result | resultTMP;

		//std::cout<<"charge1 "<<charge1<<" charge2 "<<charge2<<" result "<<result<<std::endl;

	}

  if(result) sameSignObj1->push_back(object1); 

  }

  iEvent.put(sameSignObj1);

}

// ------------ method called once each job just before starting event loop  ------------
template<typename T>
void 
DecomposeCompCandidate<T>::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
template<typename T>
void 
DecomposeCompCandidate<T>::endJob() {
}

// ------------ method called when starting to processes a run  ------------
template<typename T>
void 
DecomposeCompCandidate<T>::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
template<typename T>
void 
DecomposeCompCandidate<T>::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
template<typename T>
void 
DecomposeCompCandidate<T>::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
template<typename T>
void 
DecomposeCompCandidate<T>::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
template<typename T>
void
DecomposeCompCandidate<T>::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

#endif
