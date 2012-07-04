// -*- C++ -*-
//
// Package:    TriggerFilter
// Class:      TriggerFilter
// 
/**\class TriggerFilter TriggerFilter.cc WHAnalysis/TriggerFilter/src/TriggerFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Thu Jan 12 11:16:03 CET 2012
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

#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <boost/foreach.hpp>

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Utilities/interface/RegexMatch.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/ESWatcher.h"
#include "HLTrigger/HLTcore/interface/HLTFilter.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Provenance/interface/ParameterSetID.h"
#include <DataFormats/Provenance/interface/EventRange.h>
// needed for trigger bits from EventSetup as in ALCARECO paths
#include "CondFormats/HLTObjects/interface/AlCaRecoTriggerBits.h"
#include "CondFormats/DataRecord/interface/AlCaRecoTriggerBitsRcd.h"


//
// class declaration
//

class TriggerFilter : public edm::EDFilter {
   public:
      explicit TriggerFilter(const edm::ParameterSet&);
      ~TriggerFilter();

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

      typedef std::vector<std::string> vstring;
      typedef std::vector<edm::EventRange> VEventRange;

      edm::InputTag src_;
      vstring triggerPaths_;
      std::string defaultTrigger_;
      VEventRange hltEventRanges_;
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
TriggerFilter::TriggerFilter(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed

  src_ = iConfig.getParameter<edm::InputTag>("TriggerResultsTag"); 
  triggerPaths_ = iConfig.getParameter<vstring>("HLTPaths");
  defaultTrigger_ = iConfig.getParameter<std::string>("defaultTrigger");
  hltEventRanges_ = iConfig.getParameter<VEventRange>("hltEventRanges");

}


TriggerFilter::~TriggerFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

//
// member functions
//

// ------------ method called on each new Event  ------------
bool
TriggerFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   std::string triggerPath;
   bool result = false;

   int runNumber = iEvent.id().run();
   //int lumiSectionNumber = iEvent.id().luminosityBlock();
   //int eventNumber = iEvent.id().event();

   int triggerPathsSize = triggerPaths_.size();
   //int runRangesSize = hltEventRanges_.size();

   for(int i = 0; i < triggerPathsSize; i++){

	edm::EventRange range;
	range = hltEventRanges_[i];
	int startRun = range.startRun();
	int endRun = range.endRun();
	if(runNumber >= startRun && runNumber <= endRun && runNumber != 1) triggerPath = triggerPaths_[i];
	else if(runNumber == 1) triggerPath = defaultTrigger_;
	else continue;
	//std::cout<<"InRun: "<<startRun<<" EndRun: "<<endRun<<" Trigger: "<<triggerPath<<std::endl;
	//std::cout<<"ActualRun: "<<runNumber<<std::endl;

   }

   if(triggerPath == "") result = true;
   else{

	   if ( src_.label() != "" ) {

		edm::Handle<edm::TriggerResults> hltResults;
		iEvent.getByLabel(src_, hltResults);

		const edm::TriggerNames& triggerNames = iEvent.triggerNames(*hltResults);

		//std::cout<<triggerNames.triggerName(1)<<std::endl;

		std::string goodPath;
		for(int i = 0; i < (int)triggerNames.size(); i++){
			
			std::string storedName = triggerNames.triggerName(i);
			size_t found = storedName.find(triggerPath);
			if(found != std::string::npos) {
				goodPath = storedName;
				//std::cout<<storedName<<" "<<triggerPath<<" "<<found<<std::endl;
			}
		}

		unsigned int index = triggerNames.triggerIndex(goodPath);

		//std::cout<<index<<" "<<goodPath<<std::endl;

		if ( index < triggerNames.size() ) {

			bool isTriggered = ( hltResults->accept(index) ) ? true : false;
			result = isTriggered;
			//std::cout<<isTriggered<<std::endl;

		}
		else {

			// HLT path not present in event
			std::cout<<" Undefined HLT path --> skipping !!"<<std::endl;

		}
		
	   }

   }

   return result;

}

// ------------ method called once each job just before starting event loop  ------------
void 
TriggerFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
TriggerFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
TriggerFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
TriggerFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
TriggerFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(TriggerFilter);
