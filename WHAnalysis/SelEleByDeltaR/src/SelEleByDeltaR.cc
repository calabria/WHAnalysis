// -*- C++ -*-
//
// Package:    SelEleByDeltaR   
// Class:      SelEleByDeltaR   
// 
/**\class SelEleByDeltaR    SelEleByDeltaR   .cc WHAnalysis/SelEleByDeltaR   /src/SelEleByDeltaR   .cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Rosamaria Ventitti, reviewed by Cesare Calabria
//         Created:  Mon Sep  5 00:41:24 CEST 2011
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

//
// class declaration
//

class SelEleByDeltaR    : public edm::EDProducer {
   public:
      explicit SelEleByDeltaR   (const edm::ParameterSet&);
      ~SelEleByDeltaR   ();

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
SelEleByDeltaR   ::SelEleByDeltaR   (const edm::ParameterSet& iConfig):
  muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
  eleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("eleSrc")),
  DeltaRCut_(iConfig.getUntrackedParameter<double>("DeltaRCut"))
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

  produces<pat::ElectronCollection>("EleSelByDeltaR").setBranchAlias("EleSelByDeltaR");

}


SelEleByDeltaR   ::~SelEleByDeltaR   ()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
SelEleByDeltaR   ::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
/* This is an event example
   //Read 'ExampleData' from the Event
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   std::auto_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
   iEvent.put(pOut);
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/
  
  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(eleSrc_,electrons);

  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

  int sizeMu = muons->size();
  int sizeEle = electrons->size();

  //std::cout<<"size mu "<<sizeMu<<" size ele "<<sizeEle<<std::endl;

  std::auto_ptr<pat::ElectronCollection> EleSelByDeltaR(new pat::ElectronCollection);

  for(edm::View<pat::Electron>::const_iterator electron = electrons->begin(); electron != electrons->end(); ++electron){

  	bool eleResult = true;
      
     	double etaEle = electron->eta();
      	double phiEle = electron->phi();

      	if(sizeMu != 0){
	  	for(edm::View<pat::Muon>::const_iterator muon = muons->begin(); muon != muons->end(); ++muon){
	    
	    	double etaMu = muon->eta();
	    	double phiMu = muon->phi();
	    	double deltaRmuEle = deltaR(etaEle, phiEle, etaMu, phiMu );
	    	if(deltaRmuEle < DeltaRCut_) eleResult = false;
	    
	    	//std::cout<<"size ele = "<<sizeEle<<" size mu = "<<sizeMu<<" muEle dR = "<<deltaRmuEle<<" eleResult = "<<eleResult<<std::endl;
	    
	 	}//fine loop sui mu
	}

	//std::cout<<" eleResult = "<<eleResult<<std::endl;
      	if(eleResult) EleSelByDeltaR->push_back(*electron); 

  }//Fine loop sugli elettroni

  iEvent.put(EleSelByDeltaR, "EleSelByDeltaR");
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
SelEleByDeltaR   ::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SelEleByDeltaR   ::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
SelEleByDeltaR   ::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SelEleByDeltaR   ::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SelEleByDeltaR   ::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SelEleByDeltaR   ::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SelEleByDeltaR   ::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SelEleByDeltaR);
