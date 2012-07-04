// -*- C++ -*-
//
// Package:    TauDzFilter
// Class:      TauDzFilter
// 
/**\class TauDzFilter TauDzFilter.cc WHAnalysis/TauDzFilter/src/TauDzFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Sat Oct 22 16:39:54 CEST 2011
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
#include "DataFormats/PatCandidates/interface/Tau.h"


//
// class declaration
//

class TauDzFilter : public edm::EDFilter {
   public:
      explicit TauDzFilter(const edm::ParameterSet&);
      ~TauDzFilter();

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
      edm::InputTag tauSrc_;
      double dzCutMax_;
      double dzCutMin_;

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
TauDzFilter::TauDzFilter(const edm::ParameterSet& iConfig):
   vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag> ("vertexSrc")),
   tauSrc_(iConfig.getUntrackedParameter<edm::InputTag> ("tauSrc")),
   dzCutMax_(iConfig.getUntrackedParameter<double> ("dzCutMax")),
   dzCutMin_(iConfig.getUntrackedParameter<double> ("dzCutMin"))
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
   produces<pat::TauCollection>("selectedTausByDz").setBranchAlias("selectedTausByDz");
  
}


TauDzFilter::~TauDzFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
bool
TauDzFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
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
  bool tauResult = false;

  edm::Handle<reco::VertexCollection> primaryEventVertexCollection;
  iEvent.getByLabel(vertexSrc_, primaryEventVertexCollection);

  edm::Handle<edm::View<pat::Tau> > patTauCollection;
  iEvent.getByLabel(tauSrc_,patTauCollection);

  std::auto_ptr<pat::TauCollection> selectedTausByDz(new pat::TauCollection);

  if ( primaryEventVertexCollection->size() < 1 ) {
    return false;
  } 

  const reco::Vertex& thePrimaryEventVertex = (*primaryEventVertexCollection->begin());

  for ( edm::View<pat::Tau>::const_iterator patTau = patTauCollection->begin(); patTau != patTauCollection->end(); ++patTau ) {

      	double dz = patTau->vz() - thePrimaryEventVertex.z();

	if ( dz > dzCutMin_ && dz < dzCutMax_ ) {
		result = true;
		tauResult = true;
	      	}
	else tauResult = false;
	//if(dz > dzCutMin_ && dz < dzCutMax_) std::cout<<"dz "<<dz<<" result "<<result<<" tauResult "<<tauResult<<std::endl;

	if(tauResult) selectedTausByDz->push_back(*patTau);    

  }

   iEvent.put(selectedTausByDz, "selectedTausByDz");
   return result;
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
TauDzFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TauDzFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
TauDzFilter::beginRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
TauDzFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
TauDzFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
TauDzFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TauDzFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TauDzFilter);
