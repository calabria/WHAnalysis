// -*- C++ -*-
//
// Package:    BTagFilter
// Class:      BTagFilter
// 
/**\class BTagFilter BTagFilter.cc WHAnalysis/BTagFilter/src/BTagFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Mon Aug  1 18:27:09 CEST 2011
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
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

//
// class declaration
//

class BTagFilter : public edm::EDFilter {
   public:
      explicit BTagFilter(const edm::ParameterSet&);
      ~BTagFilter();

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

      edm::InputTag jetSrc_;
      std::string bTaggingDiscriminator_;
      double bTagThreshold_;
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
BTagFilter::BTagFilter(const edm::ParameterSet& iConfig):
  jetSrc_(iConfig.getUntrackedParameter<edm::InputTag>("jetSrc")),
  bTaggingDiscriminator_(iConfig.getUntrackedParameter<std::string>("bTaggingDiscriminator")),
  bTagThreshold_(iConfig.getUntrackedParameter<double>("bTagThreshold"))
{
   //now do what ever initialization is needed

}


BTagFilter::~BTagFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
BTagFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  double bJetNumber = 0.;
  bool result = false;

  edm::Handle<pat::JetCollection> patJets;
  iEvent.getByLabel(jetSrc_, patJets);

  for(std::vector<pat::Jet>::const_iterator patJet = patJets->begin(); patJet != patJets->end(); ++patJet){

	if(patJet->bDiscriminator(bTaggingDiscriminator_.c_str()) > bTagThreshold_) ++bJetNumber;

  }

   if(bJetNumber == 0) result = true;
   //std::cout<<bJetNumber<<" "<<result<<std::endl;
   return result;
}

// ------------ method called once each job just before starting event loop  ------------
void 
BTagFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
BTagFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
BTagFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
BTagFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
BTagFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
BTagFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
BTagFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(BTagFilter);
