// -*- C++ -*-
//
// Package:    CompositeCandFilter
// Class:      CompositeCandFilter
// 
/**\class CompositeCandFilter CompositeCandFilter.cc WHAnalysis/CompositeCandFilter/src/CompositeCandFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Mon Jan  2 13:15:21 CET 2012
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

class CompositeCandFilter : public edm::EDFilter {
   public:
      explicit CompositeCandFilter(const edm::ParameterSet&);
      ~CompositeCandFilter();

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

      double etCut_;
      bool applyEMuCharge_;
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
CompositeCandFilter::CompositeCandFilter(const edm::ParameterSet& iConfig):
  CompCandSrc_(iConfig.getUntrackedParameter<edm::InputTag>("CompCandSrc")),
  etCut_(iConfig.getUntrackedParameter<double>("EtCut")),
  applyEMuCharge_(iConfig.getUntrackedParameter<bool>("applyEMuCharge"))
{
   //now do what ever initialization is needed
   produces<reco::CompositeCandidateCollection>("");
}


CompositeCandFilter::~CompositeCandFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
CompositeCandFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;

   bool result = false;

   edm::Handle<edm::View<reco::CompositeCandidate> > CompCandidates;
   iEvent.getByLabel(CompCandSrc_, CompCandidates);

   std::auto_ptr<reco::CompositeCandidateCollection> selectedEleMuTauCompCand(new reco::CompositeCandidateCollection);

   for(edm::View<reco::CompositeCandidate>::const_iterator CompCand=CompCandidates->begin(); CompCand!=CompCandidates->end(); ++CompCand){

   	bool candResult = false;
   	bool resultEt = false;
   	bool resultCharge = false;
	bool massVeto = false;

	const Candidate * WLepCand = CompCand->daughter(0);
	const Candidate * DiTauCand = CompCand->daughter(1);

	double WLepEt = WLepCand->et();
	double DiTauCand1Et = DiTauCand->daughter(0)->et();
	double DiTauCand2tauEt = DiTauCand->daughter(1)->et();

	double TotEt = WLepEt + DiTauCand1Et + DiTauCand2tauEt;
	if(TotEt > etCut_) resultEt = true;

	int WLepCharge = WLepCand->charge();
	int DiTauCand1Charge = DiTauCand->daughter(0)->charge();
	int DiTauCand2Charge = DiTauCand->daughter(1)->charge();

	int DiTauCand1Pt = DiTauCand->daughter(0)->pt();
	int DiTauCand2Pt = DiTauCand->daughter(1)->pt();

	int WLepDiTauCand1Charge = WLepCharge * DiTauCand1Charge;
	int WLepDiTauCand2Charge = WLepCharge * DiTauCand2Charge;

	bool mostEnergetic = DiTauCand1Pt > DiTauCand2Pt ? true : false;
	if(mostEnergetic && WLepDiTauCand2Charge > 0) resultCharge = true;
	else if(WLepDiTauCand1Charge > 0) resultCharge = true;

	double massWLeptonDiTauCand1 = (WLepCand->p4() + DiTauCand->daughter(0)->p4()).M();
	double massWLeptonDiTauCand2 = (WLepCand->p4() + DiTauCand->daughter(1)->p4()).M();

	if(mostEnergetic && massWLeptonDiTauCand1 > 85 && massWLeptonDiTauCand1 < 95) massVeto = true;
	else if(massWLeptonDiTauCand2 > 85 && massWLeptonDiTauCand2 < 95) massVeto = true;

	if(applyEMuCharge_) candResult = resultEt && resultCharge && !massVeto;
	else candResult = resultEt /*&& !massVeto*/;

	if(candResult){
		selectedEleMuTauCompCand->push_back(*CompCand);
		result = true;
	}

   }

   iEvent.put(selectedEleMuTauCompCand);
   return result;
}

// ------------ method called once each job just before starting event loop  ------------
void 
CompositeCandFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CompositeCandFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
CompositeCandFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
CompositeCandFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
CompositeCandFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
CompositeCandFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CompositeCandFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(CompositeCandFilter);
