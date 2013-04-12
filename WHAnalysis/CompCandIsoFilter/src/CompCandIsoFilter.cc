// -*- C++ -*-
//
// Package:    CompCandIsoFilter
// Class:      CompCandIsoFilter
// 
/**\class CompCandIsoFilter CompCandIsoFilter.cc WHAnalysis/CompCandIsoFilter/src/CompCandIsoFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
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

class CompCandIsoFilter : public edm::EDFilter {
   public:
      explicit CompCandIsoFilter(const edm::ParameterSet&);
      ~CompCandIsoFilter();

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
      typedef std::vector<double> vdouble;
      //std::string osTauCut_;
      //std::string ssTauCut_;
      bool isFR_;
      vdouble condVec_;

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
CompCandIsoFilter::CompCandIsoFilter(const edm::ParameterSet& iConfig):
  CompCandSrc_(iConfig.getUntrackedParameter<edm::InputTag>("CompCandSrc")),
  //osTauCut_(iConfig.getUntrackedParameter<std::string>("osTauCut")),
  //ssTauCut_(iConfig.getUntrackedParameter<std::string>("ssTauCut")),
  isFR_(iConfig.getUntrackedParameter<bool>("isFR")),
  condVec_(iConfig.getUntrackedParameter<vdouble>("condVec"))
{
   //now do what ever initialization is needed
   produces<reco::CompositeCandidateCollection>("");

}


CompCandIsoFilter::~CompCandIsoFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
CompCandIsoFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   using namespace edm;
   using namespace reco;

   bool result = false;

   edm::Handle<edm::View<reco::CompositeCandidate> > CompCandidates;
   iEvent.getByLabel(CompCandSrc_, CompCandidates);

   std::auto_ptr<reco::CompositeCandidateCollection> selectedCompCandIso(new reco::CompositeCandidateCollection);

   for(edm::View<reco::CompositeCandidate>::const_iterator CompCand=CompCandidates->begin(); CompCand!=CompCandidates->end(); ++CompCand){

	const Candidate * WLepCand = CompCand->daughter(0);
	const Candidate * DiTauCand = CompCand->daughter(1);

	const reco::Candidate * dau1 = DiTauCand->daughter(0); 
	const reco::Candidate * dau2 = DiTauCand->daughter(1);

 	const pat::Tau & tau1 = dynamic_cast<const pat::Tau&>(*dau1->masterClone());
 	const pat::Tau & tau2 = dynamic_cast<const pat::Tau&>(*dau2->masterClone());

	int WLepCharge = WLepCand->charge();
	int DiTauCand1Charge = DiTauCand->daughter(0)->charge();
	int DiTauCand2Charge = DiTauCand->daughter(1)->charge();

	int WLepDiTauCand1Charge = WLepCharge * DiTauCand1Charge;
	int WLepDiTauCand2Charge = WLepCharge * DiTauCand2Charge;

	if(WLepDiTauCand1Charge < 0){//Tau1 real, Tau2 fakeable

		int trigMatch1 = tau1.triggerObjectMatchByPath("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*") || tau1.triggerObjectMatchByPath("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*");
		int trigMatch2 = tau2.triggerObjectMatchByPath("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*") || tau1.triggerObjectMatchByPath("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*");
		int isoTau1 = tau1.tauID("byTightCombinedIsolationDeltaBetaCorr");
		int isoTau2 = tau2.tauID("byMediumCombinedIsolationDeltaBetaCorr");

		if(isFR_){

			if(trigMatch1 == 1 && isoTau1 == condVec_[0] && isoTau2 == condVec_[1]){

				result = true;
				selectedCompCandIso->push_back(*CompCand);

			}

		}
		else{

			if(trigMatch1 == 1 && isoTau1 == condVec_[0] && isoTau2 == condVec_[1]){

				result = true;
				selectedCompCandIso->push_back(*CompCand);

			}

		}

	}
	else{//Tau2 real, Tau1 fakeable

		int trigMatch1 = tau1.triggerObjectMatchByPath("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*") || tau1.triggerObjectMatchByPath("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*");
		int trigMatch2 = tau2.triggerObjectMatchByPath("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*") || tau1.triggerObjectMatchByPath("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*");
		int isoTau1 = tau1.tauID("byTightCombinedIsolationDeltaBetaCorr");
		int isoTau2 = tau2.tauID("byMediumCombinedIsolationDeltaBetaCorr");

		if(isFR_){

			if(trigMatch2 == 1 && isoTau1 == condVec_[1] && isoTau2 == condVec_[0]){

				result = true;
				selectedCompCandIso->push_back(*CompCand);

			}

		}
		else{

			if(trigMatch2 == 1 && isoTau1 == condVec_[1] && isoTau2 == condVec_[0]){

				result = true;
				selectedCompCandIso->push_back(*CompCand);

			}

		}

	}

   }

   iEvent.put(selectedCompCandIso);
   return result;

}

// ------------ method called once each job just before starting event loop  ------------
void 
CompCandIsoFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CompCandIsoFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
CompCandIsoFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
CompCandIsoFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
CompCandIsoFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
CompCandIsoFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CompCandIsoFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(CompCandIsoFilter);
