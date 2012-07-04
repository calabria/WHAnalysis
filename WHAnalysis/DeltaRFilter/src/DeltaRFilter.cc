// -*- C++ -*-
//
// Package:    DeltaRFilter
// Class:      DeltaRFilter
// 
/**\class DeltaRFilter DeltaRFilter.cc DeltaRFilter/DeltaRFilter/src/DeltaRFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Sat May  7 11:22:07 CEST 2011
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

#include "FWCore/Utilities/interface/InputTag.h"

#include "TH1D.h"
#include "TH2D.h"
#include "TH3D.h"
#include "TMath.h"
#include "TTree.h"
#include "TH1F.h"
#include "TFile.h"
#include "TAxis.h"
#include <TROOT.h>
#include <TSystem.h>
#include <TCanvas.h>
#include <cmath>
#include "TStyle.h"
#include <string>
#include <vector>
#include <set>
#include <Math/VectorUtil.h>
#include "TLorentzVector.h"
#include <algorithm>
#include "Math/GenVector/VectorUtil.h"
#include "Math/GenVector/PxPyPzE4D.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/Common/interface/Handle.h"

#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/GeometryVector/interface/Phi.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h" 
#include "DataFormats/Candidate/interface/Candidate.h" 
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METFwd.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "TMath.h"
#include "DataFormats/Math/interface/deltaR.h"

#include <iostream>
#include <iomanip>


using namespace edm;
using namespace pat;
using namespace std;
using namespace reco;
using namespace ROOT::Math::VectorUtil ;

//
// class declaration
//

class DeltaRFilter : public edm::EDFilter {
   public:
      explicit DeltaRFilter(const edm::ParameterSet&);
      ~DeltaRFilter();

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

     edm::InputTag DiTauTag_;
     double DeltaRCut_;

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
DeltaRFilter::DeltaRFilter(const edm::ParameterSet& iConfig):
     DiTauTag_(iConfig.getUntrackedParameter<edm::InputTag> ("DiTauTag")),
     DeltaRCut_(iConfig.getUntrackedParameter<double>("DeltaRCut"))
{
   //now do what ever initialization is needed
  	produces<reco::CompositeCandidateCollection>("selectedCand1Cand2PairsDeltaR").setBranchAlias("selectedCand1Cand2PairsDeltaR");
}


DeltaRFilter::~DeltaRFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
DeltaRFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

     Handle<reco::CompositeCandidateCollection> diTau;
     iEvent.getByLabel(DiTauTag_, diTau);  

     std::auto_ptr<reco::CompositeCandidateCollection> selectedCand1Cand2PairsDeltaR(new reco::CompositeCandidateCollection);

     unsigned int diTauCollectionSize = diTau->size();
     for (unsigned int i=0; i<diTauCollectionSize; ++i) {
	reco::CompositeCandidate pair = diTau->at(i);

	double eta1 = pair.daughter(0)->eta();
	double eta2 = pair.daughter(1)->eta();
	double phi1 = pair.daughter(0)->phi();
	double phi2 = pair.daughter(1)->phi();

	double dR = deltaR(eta1, phi1, eta2, phi2); 

	//std::cout<<"dR: "<<dR<<std::endl;

	if(dR > DeltaRCut_){
		selectedCand1Cand2PairsDeltaR->push_back(pair);
		result = true;}
     }

   iEvent.put(selectedCand1Cand2PairsDeltaR, "selectedCand1Cand2PairsDeltaR");

   //std::cout<<"Bool: "<<result<<std::endl;
   return result;
}

// ------------ method called once each job just before starting event loop  ------------
void 
DeltaRFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DeltaRFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
DeltaRFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
DeltaRFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
DeltaRFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
DeltaRFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DeltaRFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(DeltaRFilter);
