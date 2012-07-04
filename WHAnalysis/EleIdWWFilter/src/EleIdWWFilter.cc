// -*- C++ -*-
//
// Package:    EleIdWWFilter
// Class:      EleIdWWFilter
// 
/**\class EleIdWWFilter EleIdWWFilter.cc WHAnalysis/EleIdWWFilter/src/EleIdWWFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Sat Oct 22 17:12:46 CEST 2011
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

class EleIdWWFilter : public edm::EDFilter {
   public:
      explicit EleIdWWFilter(const edm::ParameterSet&);
      ~EleIdWWFilter();

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

      edm::InputTag electronSrc_;
      double separationPt_;
      std::string eleIdWP1_;
      std::string eleIdWP2_;
      double output1_;
      double output2_;

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
EleIdWWFilter::EleIdWWFilter(const edm::ParameterSet& iConfig):
   electronSrc_(iConfig.getUntrackedParameter<edm::InputTag> ("electronSrc")),
   separationPt_(iConfig.getUntrackedParameter<double> ("separationPt")),
   eleIdWP1_(iConfig.getUntrackedParameter<std::string> ("eleIdWP1")),
   eleIdWP2_(iConfig.getUntrackedParameter<std::string> ("eleIdWP2")),
   output1_(iConfig.getUntrackedParameter<double> ("output1")),
   output2_(iConfig.getUntrackedParameter<double> ("output2"))
{
   //now do what ever initialization is needed
   produces<pat::ElectronCollection>("selectedElectronsByEleIdWW").setBranchAlias("selectedElectronsByEleIdWW");
   produces<pat::ElectronCollection>("selectedElectronsByEleIdWW1").setBranchAlias("selectedElectronsByEleIdWW1");
   produces<pat::ElectronCollection>("selectedElectronsByEleIdWW2").setBranchAlias("selectedElectronsByEleIdWW2");

}


EleIdWWFilter::~EleIdWWFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
EleIdWWFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
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
  bool eleResult = false;

  edm::Handle<edm::View<pat::Electron> > patElectronCollection;
  iEvent.getByLabel(electronSrc_,patElectronCollection);

  std::auto_ptr<pat::ElectronCollection> selectedElectronsByEleIdWW(new pat::ElectronCollection);
  std::auto_ptr<pat::ElectronCollection> selectedElectronsByEleIdWW1(new pat::ElectronCollection);
  std::auto_ptr<pat::ElectronCollection> selectedElectronsByEleIdWW2(new pat::ElectronCollection);

  for ( edm::View<pat::Electron>::const_iterator patElectron = patElectronCollection->begin(); patElectron != patElectronCollection->end(); ++patElectron ) {

	double outputWP1 = patElectron->electronID(eleIdWP1_.c_str());
	double outputWP2 = patElectron->electronID(eleIdWP2_.c_str());
	double pt = patElectron->pt();
	bool case1 = (pt < separationPt_) && (outputWP1 > output1_);
	bool case2 = (pt >= separationPt_) && (outputWP2 > output2_);

	//std::cout<<"pt "<<pt<<" outputWP1 "<<outputWP1<<" outputWP2 "<<outputWP2<<" case1 "<<case1<<" case2 "<<case2<<std::endl;

	if(case1) selectedElectronsByEleIdWW1->push_back(*patElectron);  
	else if(case2) selectedElectronsByEleIdWW2->push_back(*patElectron);      

	if(case1 || case2){
		
		result = true;
		eleResult = true;

	}
	else eleResult = false;
	if(eleResult) selectedElectronsByEleIdWW->push_back(*patElectron);    

  }

   iEvent.put(selectedElectronsByEleIdWW, "selectedElectronsByEleIdWW");
   iEvent.put(selectedElectronsByEleIdWW1, "selectedElectronsByEleIdWW1");
   iEvent.put(selectedElectronsByEleIdWW2, "selectedElectronsByEleIdWW2");
   return result;

}

// ------------ method called once each job just before starting event loop  ------------
void 
EleIdWWFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
EleIdWWFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
EleIdWWFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
EleIdWWFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
EleIdWWFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
EleIdWWFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
EleIdWWFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(EleIdWWFilter);
