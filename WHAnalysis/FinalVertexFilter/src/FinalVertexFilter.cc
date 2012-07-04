// -*- C++ -*-
//
// Package:    FinalVertexFilter
// Class:      FinalVertexFilter
// 
/**\class FinalVertexFilter FinalVertexFilter.cc WHAnalysis/FinalVertexFilter/src/FinalVertexFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Tue Jan 10 13:09:13 CET 2012
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
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
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

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

class FinalVertexFilter : public edm::EDFilter {
   public:
      explicit FinalVertexFilter(const edm::ParameterSet&);
      ~FinalVertexFilter();

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

      edm::InputTag muonSrc_;
      edm::InputTag eleSrc_;
      edm::InputTag tauSrc_;
      double vertexChi2NDOF_;
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
FinalVertexFilter::FinalVertexFilter(const edm::ParameterSet& iConfig):
  muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
  eleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("eleSrc")),
  tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc")),
  vertexChi2NDOF_(iConfig.getUntrackedParameter<double>("vertexChi2NDOF"))
{
   //now do what ever initialization is needed
}


FinalVertexFilter::~FinalVertexFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
FinalVertexFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  bool result = false;
  double vtxChi2NDOF = 0;

  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);

  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(eleSrc_,electrons);

  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

  edm::ESHandle<TransientTrackBuilder> trackBuilderHandle;
  iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", trackBuilderHandle);

  for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon){

	for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron){

	 	for(edm::View<pat::Tau>::const_iterator patTau=taus->begin(); patTau!=taus->end(); ++patTau){

			const reco::Candidate * MuonCand = muon->clone();
			const reco::Candidate * TauCand = patTau->clone();
			const reco::Candidate * EleCand = electron->clone();
    			std::vector<reco::TransientTrack> tracks;

        		reco::TransientTrack transtrackMuon = getTracks(MuonCand,trackBuilderHandle.product());
        		if (transtrackMuon.isValid()) tracks.push_back(transtrackMuon);

        		reco::TransientTrack transtrackTau = getTracks(TauCand,trackBuilderHandle.product());
        		if (transtrackTau.isValid()) tracks.push_back(transtrackTau);

        		reco::TransientTrack transtrackEle = getTracks(EleCand,trackBuilderHandle.product());
        		if (transtrackEle.isValid()) tracks.push_back(transtrackEle);

			//std::cout<<transtrackMuon.isValid()<<" "<<transtrackTau.isValid()<<" "<<transtrackEle.isValid()<<std::endl;
    	
    			double vtxChi2 = -1;
    			double vtxNDOF = -1;

			//std::cout<<tracks.size()<<std::endl;

    			if (tracks.size() > 1) {
      				KalmanVertexFitter kvf(true);
      				TransientVertex vtx = kvf.vertex(tracks);
      				vtxChi2 = vtx.totalChiSquared();
      				vtxNDOF = vtx.degreesOfFreedom();

			}

			//std::cout<<"Chi2 "<<vtxChi2<<" NDOF "<<vtxNDOF<<std::endl;
			if(vtxNDOF) vtxChi2NDOF = vtxChi2/vtxNDOF;
			if(vtxChi2NDOF < vertexChi2NDOF_) result = true;

		}
	}
  }

  return result;

}

// ------------ method called once each job just before starting event loop  ------------
void 
FinalVertexFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
FinalVertexFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
FinalVertexFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
FinalVertexFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
FinalVertexFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
FinalVertexFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
FinalVertexFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(FinalVertexFilter);
