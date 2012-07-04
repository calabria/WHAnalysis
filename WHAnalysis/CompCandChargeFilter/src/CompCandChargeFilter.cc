// -*- C++ -*-
//
// Package:    CompCandChargeFilter
// Class:      CompCandChargeFilter
// 
/**\class CompCandChargeFilter CompCandChargeFilter.cc WHAnalysis/CompCandChargeFilter/src/CompCandChargeFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  
//         Created:  Sat May 26 13:06:20 CEST 2012
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
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

//
// class declaration
//

class CompCandChargeFilter : public edm::EDFilter {
   public:
      explicit CompCandChargeFilter(const edm::ParameterSet&);
      ~CompCandChargeFilter();

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

      edm::InputTag CompCandSrc_;

      bool applyCharge1_;
      bool applyCharge2_;
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
CompCandChargeFilter::CompCandChargeFilter(const edm::ParameterSet& iConfig):
  CompCandSrc_(iConfig.getUntrackedParameter<edm::InputTag>("CompCandSrc")),
  applyCharge1_(iConfig.getUntrackedParameter<bool>("applyCharge1")),
  applyCharge2_(iConfig.getUntrackedParameter<bool>("applyCharge2"))
{
   //now do what ever initialization is needed
   produces<reco::CompositeCandidateCollection>("");

}


CompCandChargeFilter::~CompCandChargeFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
CompCandChargeFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   using namespace edm;
   using namespace reco;

   bool result = false;

   edm::Handle<edm::View<reco::CompositeCandidate> > CompCandidates;
   iEvent.getByLabel(CompCandSrc_, CompCandidates);

   std::auto_ptr<reco::CompositeCandidateCollection> selectedCompCandCharge(new reco::CompositeCandidateCollection);

   for(edm::View<reco::CompositeCandidate>::const_iterator CompCand=CompCandidates->begin(); CompCand!=CompCandidates->end(); ++CompCand){

	const Candidate * WLepCand = CompCand->daughter(0);
	const Candidate * DiTauCand = CompCand->daughter(1);

	int WLepCharge = WLepCand->charge();
	int DiTauCand1Charge = DiTauCand->daughter(0)->charge();
	int DiTauCand2Charge = DiTauCand->daughter(1)->charge();

	int WLepDiTauCand1Charge = WLepCharge * DiTauCand1Charge;
	int WLepDiTauCand2Charge = WLepCharge * DiTauCand2Charge;

	if(applyCharge1_ && WLepDiTauCand1Charge > 0) result = true;
	else if(applyCharge2_ && WLepDiTauCand2Charge > 0) result = true;

   }

   iEvent.put(selectedCompCandCharge);
   return result;

}

// ------------ method called once each job just before starting event loop  ------------
void 
CompCandChargeFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CompCandChargeFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
CompCandChargeFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
CompCandChargeFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
CompCandChargeFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
CompCandChargeFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CompCandChargeFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(CompCandChargeFilter);
