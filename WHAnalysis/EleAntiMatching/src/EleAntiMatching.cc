// -*- C++ -*-
//
// Package:    EleAntiMatching
// Class:      EleAntiMatching
// 
/**\class EleAntiMatching EleAntiMatching.cc WHAnalysis/EleAntiMatching/src/EleAntiMatching.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Thu Oct 27 11:28:30 CEST 2011
// $Id$
//
//


// system include files
#include <memory>
#include <map>
#include <string>
#include <cmath>
#include <vector>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/PatCandidates/interface/Electron.h"


//
// class declaration
//

class EleAntiMatching : public edm::EDProducer {
   public:
      explicit EleAntiMatching(const edm::ParameterSet&);
      ~EleAntiMatching();

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

      std::map<std::string,TH1F*> histContainer_; 
      edm::InputTag genParticleSrc_;
      edm::InputTag eleSrc_;
      int idParticle_;
      double deltaRCut_;

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
EleAntiMatching::EleAntiMatching(const edm::ParameterSet& iConfig):
  histContainer_(),
  genParticleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("genParticles")),
  eleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("eleSrc")),
  idParticle_(iConfig.getUntrackedParameter<int>("idParticle")),
  deltaRCut_(iConfig.getUntrackedParameter<double>("deltaRCut"))
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

  produces<pat::ElectronCollection>( "EleAntiGenMatched" ).setBranchAlias( "EleAntiGenMatched");
  
}


EleAntiMatching::~EleAntiMatching()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
EleAntiMatching::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  using namespace edm;
  using namespace std;
    
  bool matchEle = false;
  
  edm::Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByLabel(genParticleSrc_, genParticles);

  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(eleSrc_,electrons);
  
  std::auto_ptr<pat::ElectronCollection> EleAntiGenMatched(new pat::ElectronCollection);

  for(reco::GenParticleCollection::const_iterator it = genParticles->begin(); it != genParticles->end(); it++ ){
	  
	int id = it->pdgId();
	int status = it->status();

	if (id == 23 && status == 3) {
		histContainer_["numGenParticles"]->Fill(0);
	    	//std::cout<<"sono una Z"<<std::endl; 
	    	int numDaughters = it->numberOfDaughters();
	    	//std::cout<<"idZ = "<<id<<" statusZ = "<<status<<" numFigliZ = "<<numDaughters<<std::endl;
	  
	    	for ( int i = 0; i < numDaughters; i++ ){

	      		int dauId = it->daughter(i)->pdgId();
	      		//int statusZDaughters = it->daughter(i)->status();
	      		//std::cout<<"idFiglioZ = "<<dauId<<" statusFiglioZ = "<<statusZDaughters<<std::endl;
	      
	      		if (TMath::Abs(dauId) == 15) histContainer_["numGenParticles"]->Fill(1);

	    	}

	}

	if (id == 22 && status == 3) {
		histContainer_["numGenParticles"]->Fill(2);
	    	//std::cout<<"sono una Z"<<std::endl; 
	    	int numDaughters = it->numberOfDaughters();
	    	//std::cout<<"idZ = "<<id<<" statusZ = "<<status<<" numFigliZ = "<<numDaughters<<std::endl;
	  
	    	for ( int i = 0; i < numDaughters; i++ ){

	      		int dauId = it->daughter(i)->pdgId();
	      		//int statusZDaughters = it->daughter(i)->status();
	      		//std::cout<<"idFiglioZ = "<<dauId<<" statusFiglioZ = "<<statusZDaughters<<std::endl;
	      
	      		if (TMath::Abs(dauId) == 15) histContainer_["numGenParticles"]->Fill(3);

	    	}

	}

  }

  for(edm::View<pat::Electron>::const_iterator patElectron=electrons->begin(); patElectron!=electrons->end(); ++patElectron){

    	double phiReco = patElectron->phi();
    	double etaReco = patElectron->eta();

	matchEle = false;
 
    	if(genParticles.isValid()){

      		for(reco::GenParticleCollection::const_iterator it = genParticles->begin(); it != genParticles->end(); it++ ){
	  
	  		int id = it->pdgId();
	  		int status = it->status();

	  		if (id == 23 && status == 3) {
	    			//std::cout<<"sono una Z"<<std::endl; 
	    			int numDaughters = it->numberOfDaughters();
	    			//std::cout<<"idZ = "<<id<<" statusZ = "<<status<<" numFigliZ = "<<numDaughters<<std::endl;
	  
	    			for ( int i = 0; i < numDaughters; i++ ){

	      				int dauId = it->daughter(i)->pdgId();
	      				//int statusZDaughters = it->daughter(i)->status();
	      				//std::cout<<"idFiglioZ = "<<dauId<<" statusFiglioZ = "<<statusZDaughters<<std::endl;
	      
	      				if (TMath::Abs(dauId) == 15){
						double phiGen = it->daughter(i)->phi();
						double etaGen = it->daughter(i)->eta();
						double dR = deltaR(etaGen, phiGen, etaReco, phiReco);
						//std::cout<<"deltaR"<<dR<<std::endl;
						histContainer_["dRRecoEleGenTauAll"]->Fill(dR);
						if (dR < deltaRCut_){
							matchEle = true;
							histContainer_["dRRecoEleGenTauMatch"]->Fill(dR);}
						if (dR > deltaRCut_) histContainer_["dRRecoEleGenTauAntiMatch"]->Fill(dR);
						//std::cout<<"deltaR "<<dR<<" match = "<<matchTau<<std::endl;
	      				}

	    			}

	  		}

      		}//fine for genParticle

    	}//fine is.valid   

	//if(matchEle == true) std::cout<<"result = "<<matchEle<<std::endl;
     	if(matchEle == false) EleAntiGenMatched->push_back(*patElectron);

  }//fine for ele

  iEvent.put(EleAntiGenMatched, "EleAntiGenMatched");
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
EleAntiMatching::beginJob()
{

  // register to the TFileService
  edm::Service<TFileService> fs;

  histContainer_["numGenParticles"]=fs->make<TH1F>("numGenParticles", "numGenParticles",    4,   0., 4.);
  histContainer_["numGenParticles"]->GetXaxis()->SetBinLabel(1, "Z (status 3)");
  histContainer_["numGenParticles"]->GetXaxis()->SetBinLabel(2, "#tau (da Z)");
  histContainer_["numGenParticles"]->GetXaxis()->SetBinLabel(3, "#gamma* (status 3)");
  histContainer_["numGenParticles"]->GetXaxis()->SetBinLabel(4, "#tau (da #gamma*)");

  histContainer_["dRRecoEleGenTauAll"]=fs->make<TH1F>("dRRecoEleGenTauAll", "dRRecoEleGenTauAll", 200, 0., 10.);
  histContainer_["dRRecoEleGenTauMatch"]=fs->make<TH1F>("dRRecoEleGenTauMatch", "dRRecoEleGenTauMatch", 200, 0., 10.);
  histContainer_["dRRecoEleGenTauAntiMatch"]=fs->make<TH1F>("dRRecoEleGenTauAntiMatch", "dRRecoEleGenTauAntiMatch", 200, 0., 10.);
  histContainer_["dRRecoEleGenTauAll"]->GetXaxis()->SetTitle("#Delta R^{All}(e^{Reco},#tau^{Gen})");
  histContainer_["dRRecoEleGenTauMatch"]->GetXaxis()->SetTitle("#Delta R^{Match}(e^{Reco},#tau^{Gen})");
  histContainer_["dRRecoEleGenTauAntiMatch"]->GetXaxis()->SetTitle("#Delta R^{AntiMatch}(e^{Reco},#tau^{Gen})");

}

// ------------ method called once each job just after ending the event loop  ------------
void 
EleAntiMatching::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
EleAntiMatching::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
EleAntiMatching::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
EleAntiMatching::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
EleAntiMatching::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
EleAntiMatching::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(EleAntiMatching);
