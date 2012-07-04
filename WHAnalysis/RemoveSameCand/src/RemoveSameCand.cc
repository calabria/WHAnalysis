// -*- C++ -*-
//
// Package:    RemoveSameCand
// Class:      RemoveSameCand
// 
/**\class RemoveSameCand RemoveSameCand.cc WHAnalysis/RemoveSameCand/src/RemoveSameCand.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Tue May 22 15:31:30 CEST 2012
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/Math/interface/deltaR.h"

#include <iostream>
#include <iomanip>

using namespace edm;
using namespace pat;
using namespace std;
using namespace reco;

//
// class declaration
//

class RemoveSameCand : public edm::EDProducer {
   public:
      explicit RemoveSameCand(const edm::ParameterSet&);
      ~RemoveSameCand();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag DiTauTag_;

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
RemoveSameCand::RemoveSameCand(const edm::ParameterSet& iConfig):
     DiTauTag_(iConfig.getUntrackedParameter<edm::InputTag> ("DiTauTag"))
{
   //now do what ever initialization is needed
    produces<reco::CompositeCandidateCollection>("");

}


RemoveSameCand::~RemoveSameCand()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
RemoveSameCand::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

     Handle<reco::CompositeCandidateCollection> diTau;
     iEvent.getByLabel(DiTauTag_, diTau);  

     std::auto_ptr<reco::CompositeCandidateCollection> selectedTauPairs(new reco::CompositeCandidateCollection);

     unsigned int diTauCollectionSize = diTau->size();
     for (unsigned int i=0; i<diTauCollectionSize; ++i) {

	bool isDoubleCounted = false;

	reco::CompositeCandidate pair1 = diTau->at(i);

	Candidate * DiTauCand11 = pair1.daughter(0);
	Candidate * DiTauCand12 = pair1.daughter(1);

	double pt11 = DiTauCand11->pt();
	double pt12 = DiTauCand12->pt();

	std::cout<<"FistLoop pt: "<<pt11<<" "<<pt12<<std::endl;

	for (unsigned int j=0; j<diTauCollectionSize; ++j) {

		reco::CompositeCandidate pair2 = diTau->at(j);

		Candidate * DiTauCand21 = pair2.daughter(0);
		Candidate * DiTauCand22 = pair2.daughter(1);

		double pt21 = DiTauCand21->pt();
		double pt22 = DiTauCand22->pt();

		std::cout<<"SecondLoop pt: "<<pt21<<" "<<pt22<<std::endl;

		if(pt11 == pt22 && pt12 == pt21) isDoubleCounted = true;

	}

	if(!isDoubleCounted) selectedTauPairs->push_back(pair1);
	if(isDoubleCounted && pt11 > pt12) selectedTauPairs->push_back(pair1);

     }

     iEvent.put(selectedTauPairs);

}

// ------------ method called once each job just before starting event loop  ------------
void 
RemoveSameCand::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RemoveSameCand::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
RemoveSameCand::beginRun(edm::Run&, edm::EventSetup const&)
{ 
}

// ------------ method called when ending the processing of a run  ------------
void 
RemoveSameCand::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
RemoveSameCand::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
RemoveSameCand::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
RemoveSameCand::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(RemoveSameCand);
