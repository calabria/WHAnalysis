// -*- C++ -*-
//
// Package:    EleMuPtAssignment
// Class:      EleMuPtAssignment
// 
/**\class EleMuPtAssignment EleMuPtAssignment.cc WHAnalysis/EleMuPtAssignment/src/EleMuPtAssignment.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Wed Feb 15 10:29:29 CET 2012
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
//
// class declaration
//

class EleMuPtAssignment : public edm::EDProducer {
   public:
      explicit EleMuPtAssignment(const edm::ParameterSet&);
      ~EleMuPtAssignment();

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

      edm::InputTag muonSrc_;
      edm::InputTag eleSrc_;
      //edm::InputTag tauSrc_;
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
EleMuPtAssignment::EleMuPtAssignment(const edm::ParameterSet& iConfig):
  muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
  eleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("eleSrc"))
  //tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc"))
{
   //register your products
/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
 
   //if you want to put into the Run
   produces<ExampleData2,InRun>();
*/
   //now do what ever other initialization is needed

   produces< pat::ElectronCollection >("eleLowPt").setBranchAlias("eleLowPt");
   produces< pat::ElectronCollection >("eleHighPt").setBranchAlias("eleHighPt");
   produces< pat::MuonCollection >("muonLowPt").setBranchAlias("muonLowPt");
   produces< pat::MuonCollection >("muonHighPt").setBranchAlias("muonHighPt");

}


EleMuPtAssignment::~EleMuPtAssignment()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
EleMuPtAssignment::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

  //edm::Handle<edm::View<pat::Tau> > taus;
  //iEvent.getByLabel(tauSrc_,taus);

  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(eleSrc_,electrons);

  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

  std::auto_ptr< pat::ElectronCollection > eleLowPt( new pat::ElectronCollection );
  std::auto_ptr< pat::ElectronCollection > eleHighPt( new pat::ElectronCollection );
  std::auto_ptr< pat::MuonCollection > muonLowPt( new pat::MuonCollection );
  std::auto_ptr< pat::MuonCollection > muonHighPt( new pat::MuonCollection );

  for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon){

	double muPt = muon->pt();

	for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron){

		double elePt = electron->pt();

		//std::cout<<"elePt: "<<elePt<<" muPt: "<<muPt<<std::endl;

		if(elePt > muPt){
			eleHighPt->push_back(*electron);
			muonLowPt->push_back(*muon);
		}
		else{
		 	eleLowPt->push_back(*electron);
		 	muonHighPt->push_back(*muon);
		}

	}
  }

  //std::cout<<"eleHighPtSize: "<<eleHighPt->size()<<" eleLowPtSize: "<<eleLowPt->size()<<std::endl;
  //std::cout<<"muonHighPtSize: "<<muonHighPt->size()<<" muonLowPtSize: "<<muonLowPt->size()<<std::endl;

  iEvent.put( eleLowPt, "eleLowPt" );
  iEvent.put( eleHighPt, "eleHighPt" );
  iEvent.put( muonLowPt, "muonLowPt" );
  iEvent.put( muonHighPt, "muonHighPt" );
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
EleMuPtAssignment::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
EleMuPtAssignment::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
EleMuPtAssignment::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
EleMuPtAssignment::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
EleMuPtAssignment::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
EleMuPtAssignment::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
EleMuPtAssignment::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(EleMuPtAssignment);
