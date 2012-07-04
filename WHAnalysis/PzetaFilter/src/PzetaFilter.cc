// -*- C++ -*-
//
// Package:    PzetaFilter
// Class:      PzetaFilter
// 
/**\class PzetaFilter PzetaFilter.cc PzetaFilter/PzetaFilter/src/PzetaFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Sat May  7 11:22:35 CEST 2011
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

class PzetaFilter : public edm::EDFilter {
   public:
      explicit PzetaFilter(const edm::ParameterSet&);
      ~PzetaFilter();

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
     edm::InputTag PFMetTag_;
     double PzetaCut_;
     double a_;
     double b_;
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
PzetaFilter::PzetaFilter(const edm::ParameterSet& iConfig):
     DiTauTag_(iConfig.getUntrackedParameter<edm::InputTag> ("DiTauTag")),
     PFMetTag_(iConfig.getUntrackedParameter<edm::InputTag> ("PFMetTag")),
     PzetaCut_(iConfig.getUntrackedParameter<double>("PzetaCut")),
     a_(iConfig.getUntrackedParameter<double>("CoeffPzeta")),
     b_(iConfig.getUntrackedParameter<double>("CoeffPzetaVis"))
{
   //now do what ever initialization is needed
  	produces<reco::CompositeCandidateCollection>("selectedCand1Cand2PairsPzeta").setBranchAlias("selectedCand1Cand2PairsPzeta");
}


PzetaFilter::~PzetaFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
PzetaFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

     Handle<pat::METCollection> pfmet;
     iEvent.getByLabel(PFMetTag_, pfmet);

     double metPx = pfmet->front().px();
     double metPy = pfmet->front().py();

     Handle<reco::CompositeCandidateCollection> diTau;
     iEvent.getByLabel(DiTauTag_, diTau);  

     std::auto_ptr<reco::CompositeCandidateCollection> selectedCand1Cand2PairsPzeta(new reco::CompositeCandidateCollection);

     unsigned int diTauCollectionSize = diTau->size();
     for (unsigned int i=0; i<diTauCollectionSize; ++i) {
	reco::CompositeCandidate pair = diTau->at(i);

    	double leg1x = cos(pair.daughter(0)->phi());
    	double leg1y = sin(pair.daughter(0)->phi());
    	double leg2x = cos(pair.daughter(1)->phi());
    	double leg2y = sin(pair.daughter(1)->phi());
    	double zetaX = leg1x + leg2x;
    	double zetaY = leg1y + leg2y;
    	double zetaR = TMath::Sqrt(zetaX*zetaX + zetaY*zetaY);
    	if ( zetaR > 0. ) {
      		zetaX /= zetaR;
      		zetaY /= zetaR;
    	}

    	double visPx = pair.daughter(0)->px() + pair.daughter(1)->px();
    	double visPy = pair.daughter(0)->py() + pair.daughter(1)->py();
    	double pZetaVis = visPx*zetaX + visPy*zetaY;

    	double px = visPx + metPx;
    	double py = visPy + metPy;
    	double pZeta = px*zetaX + py*zetaY;

	double PzetaDiscr = a_*pZeta + b_*pZetaVis;

	if(PzetaDiscr > PzetaCut_){
		selectedCand1Cand2PairsPzeta->push_back(pair);
		result = true;}
     }

   iEvent.put(selectedCand1Cand2PairsPzeta, "selectedCand1Cand2PairsPzeta");

   return result;
}

// ------------ method called once each job just before starting event loop  ------------
void 
PzetaFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PzetaFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
PzetaFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
PzetaFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
PzetaFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
PzetaFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PzetaFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(PzetaFilter);
