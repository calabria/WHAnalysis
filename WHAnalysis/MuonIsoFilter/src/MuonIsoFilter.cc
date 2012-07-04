// -*- C++ -*-
//
// Package:    MuonIsoFilter
// Class:      MuonIsoFilter
// 
/**\class MuonIsoFilter MuonIsoFilter.cc MuonIsoFilter/MuonIsoFilter/src/MuonIsoFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Thu May  5 14:23:53 CEST 2011
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

#include "DataFormats/GeometryVector/interface/Phi.h"

#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"

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

class MuonIsoFilter : public edm::EDFilter {
   public:
      explicit MuonIsoFilter(const edm::ParameterSet&);
      ~MuonIsoFilter();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------

     edm::InputTag muonTag_;
     double isoCut_;
     double vetoCone_;
     double isoCone_;

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
MuonIsoFilter::MuonIsoFilter(const edm::ParameterSet& iConfig):
     muonTag_(iConfig.getUntrackedParameter<edm::InputTag> ("MuonTag")),
     isoCut_(iConfig.getUntrackedParameter<double>("IsoCut")),
     vetoCone_(iConfig.getUntrackedParameter<double>("VetoCone")),
     isoCone_(iConfig.getUntrackedParameter<double>("IsoCone"))
{
   //now do what ever initialization is needed
  produces<pat::MuonCollection>("selectedMuonsIso").setBranchAlias("selectedMuonsIso");
}


MuonIsoFilter::~MuonIsoFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
MuonIsoFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

     Handle<pat::MuonCollection> muonCollection;
     iEvent.getByLabel(muonTag_, muonCollection);  
 
     std::auto_ptr<pat::MuonCollection> selectedMuonsIso(new pat::MuonCollection);

     unsigned int muonCollectionSize = muonCollection->size();
     for (unsigned int i=0; i<muonCollectionSize; ++i) {
    	 pat::Muon mu = muonCollection->at(i);

		if((mu.isolationR03().emEt + mu.isolationR03().hadEt + mu.isolationR03().sumPt)/mu.pt()< isoCut_) {
			selectedMuonsIso->push_back(mu);

			result = true;
	  }
     }

  iEvent.put(selectedMuonsIso, "selectedMuonsIso");

  return result;
}

// ------------ method called once each job just before starting event loop  ------------
void 
MuonIsoFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MuonIsoFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(MuonIsoFilter);
