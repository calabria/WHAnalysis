// -*- C++ -*-
//
// Package:    FinalVertexFitter
// Class:      FinalVertexFitter
// 
/**\class FinalVertexFitter FinalVertexFitter.cc WHAnalysis/FinalVertexFitter/src/FinalVertexFitter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Tue Jan 10 10:22:40 CET 2012
// $Id$
//
//


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
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
//
// class declaration
//

namespace {
  reco::TransientTrack getTracks(
      const reco::Candidate* cand, const TransientTrackBuilder* builder) {
    const pat::Muon* muon = dynamic_cast<const pat::Muon*>(cand);
    const pat::Electron* electron = dynamic_cast<const pat::Electron*>(cand);
    const pat::Tau* tau = dynamic_cast<const pat::Tau*>(cand);
    if (muon) {
      if (muon->innerTrack().isNonnull())
        return (builder->build(muon->innerTrack()));
    } else if (electron) {
      if (electron->gsfTrack().isNonnull())
        return (builder->build(electron->gsfTrack()));
    } else if (tau) {
      if (tau->signalPFChargedHadrCands()[0]->trackRef().isNonnull())
        return (builder->build(
              tau->signalPFChargedHadrCands()[0]->trackRef()));
      else
        if (tau->signalPFChargedHadrCands()[0]->gsfTrackRef().isNonnull())
          return (builder->build(
                tau->signalPFChargedHadrCands()[0]->gsfTrackRef()));
    }
    return reco::TransientTrack();
  }
}

class FinalVertexFitter : public edm::EDProducer {
   public:
      explicit FinalVertexFitter(const edm::ParameterSet&);
      ~FinalVertexFitter();

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

      edm::InputTag src_;
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
FinalVertexFitter::FinalVertexFitter(const edm::ParameterSet& iConfig)
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

   src_ = iConfig.getParameter<edm::InputTag>("src");
   produces<reco::CompositeCandidateCollection>("");
  
}


FinalVertexFitter::~FinalVertexFitter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
FinalVertexFitter::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

   std::auto_ptr<reco::CompositeCandidateCollection> output(new reco::CompositeCandidateCollection);

   edm::Handle<edm::View<reco::CompositeCandidate> > finalStates;
   iEvent.getByLabel(src_, finalStates);

   edm::ESHandle<TransientTrackBuilder> trackBuilderHandle;
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", trackBuilderHandle);

   for (size_t i = 0; i < finalStates->size(); ++i) {
    	reco::CompositeCandidate * clone = finalStates->at(i).clone();
    	std::vector<reco::TransientTrack> tracks;
    	for (size_t d = 0; d < clone->numberOfDaughters(); ++d) {
      		reco::TransientTrack transtrack = getTracks(clone->daughter(d),trackBuilderHandle.product());
      		if (transtrack.isValid()) tracks.push_back(transtrack);
    	}

    	double vtxChi2 = -1;
    	double vtxNDOF = -1;
    	if (tracks.size() > 1) {
      		KalmanVertexFitter kvf(true);
      		TransientVertex vtx = kvf.vertex(tracks);
      		vtxChi2 = vtx.totalChiSquared();
      		vtxNDOF = vtx.degreesOfFreedom();
    	}

    	//clone->addUserFloat("vtxChi2", vtxChi2);
    	//clone->addUserFloat("vtxNDOF", vtxNDOF);
    	//output->push_back(clone);
  }

  //iEvent.put(output);
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
FinalVertexFitter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
FinalVertexFitter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
FinalVertexFitter::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
FinalVertexFitter::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
FinalVertexFitter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
FinalVertexFitter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
FinalVertexFitter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(FinalVertexFitter);
