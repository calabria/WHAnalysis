// -*- C++ -*-
//
// Package:    MtFilter
// Class:      MtFilter
// 
/**\class MtFilter MtFilter.cc MtFilter/MtFilter/src/MtFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Thu May  5 11:32:00 CEST 2011
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

class MtFilter : public edm::EDFilter {
   public:
      explicit MtFilter(const edm::ParameterSet&);
      ~MtFilter();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------

     edm::InputTag DiTauTag_;
     edm::InputTag PFMetTag_;
     double MTCut_;
     int particle_;
     bool invertCut_;
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
MtFilter::MtFilter(const edm::ParameterSet& iConfig):
     DiTauTag_(iConfig.getUntrackedParameter<edm::InputTag> ("DiTauTag")),
     PFMetTag_(iConfig.getUntrackedParameter<edm::InputTag> ("PFMetTag")),
     MTCut_(iConfig.getUntrackedParameter<double>("MTCut")),
     particle_(iConfig.getUntrackedParameter<int>("particle")),
     invertCut_(iConfig.getUntrackedParameter<bool>("invertCut", false))
{
   //now do what ever initialization is needed
  	if(particle_ == 0) produces<reco::CompositeCandidateCollection>("selectedCand1Cand2PairsMT1").setBranchAlias("selectedCand1Cand2PairsMT1");
  	else if (particle_ == 1)produces<reco::CompositeCandidateCollection>("selectedCand1Cand2PairsMT2").setBranchAlias("selectedCand1Cand2PairsMT2");

}


MtFilter::~MtFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
MtFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

     Handle<reco::CompositeCandidateCollection> diTau;
     iEvent.getByLabel(DiTauTag_, diTau);  

     Handle<pat::METCollection> pfmet;
     iEvent.getByLabel(PFMetTag_, pfmet);

     bool result = false;

     double metPx = pfmet->front().px();
     double metPy = pfmet->front().py();
 
     std::auto_ptr<reco::CompositeCandidateCollection> selectedCand1Cand2PairsMT1(new reco::CompositeCandidateCollection);
     std::auto_ptr<reco::CompositeCandidateCollection> selectedCand1Cand2PairsMT2(new reco::CompositeCandidateCollection);

     unsigned int diTauCollectionSize = diTau->size();
     for (unsigned int i=0; i<diTauCollectionSize; ++i) {
	reco::CompositeCandidate pair = diTau->at(i);

	double px = 0;
	double py = 0;
	double et = 0;

	if(particle_ == 0){
		px = pair.daughter(0)->px() + metPx;
	    	py = pair.daughter(0)->py() + metPy;
	    	et = pair.daughter(0)->et() + TMath::Sqrt(metPx*metPx + metPy*metPy);}
	else if (particle_ == 1){
		px = pair.daughter(1)->px() + metPx;
	    	py = pair.daughter(1)->py() + metPy;
	    	et = pair.daughter(1)->et() + TMath::Sqrt(metPx*metPx + metPy*metPy);}
	double mt2 = et*et - (px*px + py*py);
	double mt = 0;
    	if(mt2 > 0) mt = TMath::Sqrt(mt2);

	bool choice;
	if(invertCut_) choice = (mt > MTCut_)? true : false;
	if(!invertCut_) choice = (mt < MTCut_)? true : false;

	if(choice) {
		if(particle_ == 0) selectedCand1Cand2PairsMT1->push_back(pair);
		else if (particle_ == 1) selectedCand1Cand2PairsMT2->push_back(pair);
		result = true;
	}
     }

     if(particle_ == 0) iEvent.put(selectedCand1Cand2PairsMT1, "selectedCand1Cand2PairsMT1");
     else if (particle_ == 1) iEvent.put(selectedCand1Cand2PairsMT2, "selectedCand1Cand2PairsMT2");

   return result;
}

// ------------ method called once each job just before starting event loop  ------------
void 
MtFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MtFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(MtFilter);
