// -*- C++ -*-
//
// Package:    LeptonIPSelector
// Class:      LeptonIPSelector
// 
/**\class LeptonIPSelector LeptonIPSelector.cc WHAnalysis/LeptonIPSelector/src/LeptonIPSelector.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Mon Sep 19 11:29:52 CEST 2011
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
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

//
// class declaration
//

class LeptonIPSelector : public edm::EDFilter {
   public:
      explicit LeptonIPSelector(const edm::ParameterSet&);
      ~LeptonIPSelector();

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
      edm::InputTag leptonSrc_;
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
LeptonIPSelector::LeptonIPSelector(const edm::ParameterSet& iConfig):
   vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag> ("vertexSrc")),
   leptonSrc_(iConfig.getUntrackedParameter<edm::InputTag> ("leptonSrc")),
   IPmin_(iConfig.getUntrackedParameter<double> ("IPmin")),
   IPmax_(iConfig.getUntrackedParameter<double> ("IPmax"))
{
   //now do what ever initialization is needed
   produces<pat::MuonCollection>("selectedMuonsByIP").setBranchAlias("selectedMuonsByIP");
}


LeptonIPSelector::~LeptonIPSelector()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
LeptonIPSelector::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  bool result = false;
  bool leptonResult = false;

  edm::Handle<reco::VertexCollection> primaryEventVertexCollection;
  iEvent.getByLabel(vertexSrc_, primaryEventVertexCollection);

  edm::Handle<edm::View<pat::Muon> > patLeptonCollection;
  iEvent.getByLabel(leptonSrc_,patLeptonCollection);

  std::auto_ptr<pat::MuonCollection> selectedMuonsByIP(new pat::MuonCollection);

  if ( primaryEventVertexCollection->size() < 1 ) {
    return false;
  } 

  const reco::Vertex& thePrimaryEventVertex = (*primaryEventVertexCollection->begin());

  for ( edm::View<pat::Muon>::const_iterator patLepton = patLeptonCollection->begin(); patLepton != patLeptonCollection->end(); ++patLepton ) {

	  if(isValidRef(patLepton->track())){
      		double ip = patLepton->track()->dxy(thePrimaryEventVertex.position());

	      	if ( ip > IPmin_ && ip < IPmax_ ) {
			result = true;
			leptonResult = true;
	      	}
	      	else leptonResult = false;
		//if(ip < -0.02 && ip > -0.04) std::cout<<"ip "<<ip<<" result "<<result<<" leptonResult "<<leptonResult<<std::endl;

	    	if(leptonResult) selectedMuonsByIP->push_back(*patLepton);    

	  }

  }

   iEvent.put(selectedMuonsByIP, "selectedMuonsByIP");
   return result;
}

// ------------ method called once each job just before starting event loop  ------------
void 
LeptonIPSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
LeptonIPSelector::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
LeptonIPSelector::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
LeptonIPSelector::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
LeptonIPSelector::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
LeptonIPSelector::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LeptonIPSelector::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(LeptonIPSelector);
