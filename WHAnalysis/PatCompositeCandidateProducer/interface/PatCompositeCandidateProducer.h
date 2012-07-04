// -*- C++ -*-
//
// Package:    PatCompositeCandidateProducer
// Class:      PatCompositeCandidateProducer
// 
/**\class PatCompositeCandidateProducer PatCompositeCandidateProducer.cc WHAnalysis/PatCompositeCandidateProducer/src/PatCompositeCandidateProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Wed Jan 25 11:24:14 CET 2012
// $Id$
//
//

#ifndef WHAnalysis_PatCompositeCandidateProducer_PatCompositeCandidateProducer_h
#define WHAnalysis_PatCompositeCandidateProducer_PatCompositeCandidateProducer_h

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"


//
// class declaration
//

template<typename T1, typename T2, typename T3>
class PatCompositeCandidateProducer : public edm::EDProducer {
   public:
      explicit PatCompositeCandidateProducer(const edm::ParameterSet&);
      ~PatCompositeCandidateProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

      typedef edm::Ptr<T1> TPtr1;
      typedef edm::View<T1> TView1;
      typedef std::vector<T1> TCollection1;

      typedef edm::Ptr<T2> TPtr2;
      typedef edm::View<T2> TView2;
      typedef std::vector<T2> TCollection2;

      typedef edm::Ptr<T3> TPtr3;
      typedef edm::View<T3> TView3;
      typedef std::vector<T3> TCollection3;

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag lep1Src_;
      edm::InputTag lep2Src_;
      edm::InputTag lep3Src_;
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
template<typename T1, typename T2, typename T3>
PatCompositeCandidateProducer<T1,T2,T3>::PatCompositeCandidateProducer(const edm::ParameterSet& iConfig):
  lep1Src_(iConfig.getUntrackedParameter<edm::InputTag>("lep1Src")),
  lep2Src_(iConfig.getUntrackedParameter<edm::InputTag>("lep2Src")),
  lep3Src_(iConfig.getUntrackedParameter<edm::InputTag>("lep3Src"))
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

   produces< pat::CompositeCandidateCollection >("");
  
}

template<typename T1, typename T2, typename T3>
PatCompositeCandidateProducer<T1,T2,T3>::~PatCompositeCandidateProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
template<typename T1, typename T2, typename T3>
void
PatCompositeCandidateProducer<T1,T2,T3>::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  edm::Handle<TView1> leptons1;
  iEvent.getByLabel(lep1Src_,leptons1);

  edm::Handle<TView2> leptons2;
  iEvent.getByLabel(lep2Src_,leptons2);

  edm::Handle<TView3> leptons3;
  iEvent.getByLabel(lep3Src_,leptons3);

  int sizeLep1 = leptons1->size();
  int sizeLep2 = leptons2->size();
  int sizeLep3 = leptons3->size();

  std::auto_ptr< pat::CompositeCandidateCollection > patCompositeCandidateL1L2L3( new pat::CompositeCandidateCollection );

  for(int i = 0; i < sizeLep1; i++){

	TPtr1 lepton1 = leptons1->ptrAt(i);

	for(int j = 0; j < sizeLep2; j++){

		TPtr2 lepton2 = leptons2->ptrAt(j);

		for(int k = 0; k < sizeLep3; k++){

			TPtr3 lepton3 = leptons3->ptrAt(k);
			
			pat::CompositeCandidate L1L2L3;
			L1L2L3.addDaughter(*lepton1, "L1");
			L1L2L3.addDaughter(*lepton2, "L2");
			L1L2L3.addDaughter(*lepton3, "L3");

			patCompositeCandidateL1L2L3->push_back(L1L2L3);

		}
	}
  }

  iEvent.put( patCompositeCandidateL1L2L3 );
 
}

// ------------ method called once each job just before starting event loop  ------------
template<typename T1, typename T2, typename T3>
void 
PatCompositeCandidateProducer<T1,T2,T3>::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
template<typename T1, typename T2, typename T3>
void 
PatCompositeCandidateProducer<T1,T2,T3>::endJob() {
}

// ------------ method called when starting to processes a run  ------------
template<typename T1, typename T2, typename T3>
void 
PatCompositeCandidateProducer<T1,T2,T3>::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
template<typename T1, typename T2, typename T3>
void 
PatCompositeCandidateProducer<T1,T2,T3>::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
template<typename T1, typename T2, typename T3>
void 
PatCompositeCandidateProducer<T1,T2,T3>::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
template<typename T1, typename T2, typename T3>
void 
PatCompositeCandidateProducer<T1,T2,T3>::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
template<typename T1, typename T2, typename T3>
void
PatCompositeCandidateProducer<T1,T2,T3>::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

#endif

