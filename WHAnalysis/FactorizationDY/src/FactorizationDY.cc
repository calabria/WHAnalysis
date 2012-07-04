
// -*- C++ -*-
//
// Package:    
// Class:      
// 
/**\class 

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Mon Sep  5 00:41:24 CEST 2011
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
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/TauReco/interface/PFTauDecayMode.h"

using namespace reco;

//
// class declaration
//

class FactorizationDY : public edm::EDProducer {
   public:
      explicit FactorizationDY(const edm::ParameterSet&);
      ~FactorizationDY();

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
      edm::InputTag tauSrc_;
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
FactorizationDY::FactorizationDY(const edm::ParameterSet& iConfig):
  histContainer_(),
  genParticleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("genParticles")),
  tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("taus")),
  idParticle_(iConfig.getUntrackedParameter<int>("idParticle")),
  deltaRCut_(iConfig.getUntrackedParameter<double>("deltaRCut"))
{
   //register your products

  produces<pat::TauCollection>( "TausAntiGenMatched" ).setBranchAlias( "TausAntiGenMatched");

}


FactorizationDY::~FactorizationDY()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
FactorizationDY::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;
  using namespace std;
    
  bool matchTau = false;
  
  edm::Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByLabel(genParticleSrc_, genParticles);

  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);
  
  std::auto_ptr<pat::TauCollection> TausAntiGenMatched(new pat::TauCollection);

  for(reco::GenParticleCollection::const_iterator it = genParticles->begin(); it != genParticles->end(); it++ ){
	  
	int id = it->pdgId();
	int status = it->status();

	if (id == 23 && status == 3) {
		histContainer_["numGenParticles"]->Fill(0);
	    	//std::cout<<"sono una Z"<<std::endl; 
	    	int numDaughters = it->numberOfDaughters();
	    	//std::cout<<"idZ = "<<id<<" statusZ = "<<status<<" numFigliZ = "<<numDaughters<<std::endl;
	  
	    	for ( int i = 0; i < numDaughters; i++ ){
	      		const  Candidate *  ZDaughters = it->daughter(i);
	      		int dauId = ZDaughters->pdgId();
	      		//int statusZDaughters = ZDaughters->status();
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
	      		const  Candidate *  ZDaughters = it->daughter(i);
	      		int dauId = ZDaughters->pdgId();
	      		//int statusZDaughters = ZDaughters->status();
	      		//std::cout<<"idFiglioZ = "<<dauId<<" statusFiglioZ = "<<statusZDaughters<<std::endl;
	      
	      		if (TMath::Abs(dauId) == 15) histContainer_["numGenParticles"]->Fill(3);

	    	}

	}

  }

  for(edm::View<pat::Tau>::const_iterator tau=taus->begin(); tau!=taus->end(); ++tau){

    	double phiReco = tau->phi();
    	double etaReco = tau->eta();

	matchTau = false;
 
    	if(genParticles.isValid()){

      		for(reco::GenParticleCollection::const_iterator it = genParticles->begin(); it != genParticles->end(); it++ ){
	  
	  		int id = it->pdgId();
	  		int status = it->status();

	  		if (id == 23 && status == 3) {
	    			//std::cout<<"sono una Z"<<std::endl; 
	    			int numDaughters = it->numberOfDaughters();
	    			//std::cout<<"idZ = "<<id<<" statusZ = "<<status<<" numFigliZ = "<<numDaughters<<std::endl;
	  
	    			for ( int i = 0; i < numDaughters; i++ ){
	      				const  Candidate *  ZDaughters = it->daughter(i);
	      				int dauId = ZDaughters->pdgId();
	      				//int statusZDaughters = ZDaughters->status();
	      				//std::cout<<"idFiglioZ = "<<dauId<<" statusFiglioZ = "<<statusZDaughters<<std::endl;
	      
	      				if (TMath::Abs(dauId) == 15){
						double phiGen = ZDaughters->phi();
						double etaGen = ZDaughters->eta();
						double dR = deltaR(etaGen, phiGen, etaReco, phiReco);
						//std::cout<<"deltaR"<<dR<<std::endl;
						histContainer_["dRRecoTauGenTauAll"]->Fill(dR);
						if (dR < deltaRCut_){
							matchTau = true;
							histContainer_["dRRecoTauGenTauMatch"]->Fill(dR);}
						if (dR > deltaRCut_) histContainer_["dRRecoTauGenTauAntiMatch"]->Fill(dR);
						//std::cout<<"deltaR "<<dR<<" match = "<<matchTau<<std::endl;
	      				}

	    			}

	  		}

      		}//fine for genParticle

    	}//fine is.valid   

	//if(matchTau == true) std::cout<<"result = "<<matchTau<<std::endl;
     	if(matchTau == false) TausAntiGenMatched->push_back(*tau);

  }//fine for tau

  iEvent.put(TausAntiGenMatched, "TausAntiGenMatched");

}
 


// ------------ method called once each job just before starting event loop  ------------
void 
FactorizationDY::beginJob()
{
  // register to the TFileService
  edm::Service<TFileService> fs;

  histContainer_["numGenParticles"]=fs->make<TH1F>("numGenParticles", "numGenParticles",    4,   0., 4.);
  histContainer_["numGenParticles"]->GetXaxis()->SetBinLabel(1, "Z (status 3)");
  histContainer_["numGenParticles"]->GetXaxis()->SetBinLabel(2, "#tau (da Z)");
  histContainer_["numGenParticles"]->GetXaxis()->SetBinLabel(3, "#gamma* (status 3)");
  histContainer_["numGenParticles"]->GetXaxis()->SetBinLabel(4, "#tau (da #gamma*)");
  histContainer_["dRRecoTauGenTauAll"]=fs->make<TH1F>("dRRecoTauGenTauAll", "dRRecoTauGenTauAll", 200, 0., 10.);
  histContainer_["dRRecoTauGenTauMatch"]=fs->make<TH1F>("dRRecoTauGenTauMatch", "dRRecoTauGenTauMatch", 200, 0., 10.);
  histContainer_["dRRecoTauGenTauAntiMatch"]=fs->make<TH1F>("dRRecoTauGenTauAntiMatch", "dRRecoTauGenTauAntiMatch", 200, 0., 10.);
  histContainer_["dRRecoTauGenTauAll"]->GetXaxis()->SetTitle("#Delta R^{All}(#tau^{Reco},#tau^{Gen})");
  histContainer_["dRRecoTauGenTauMatch"]->GetXaxis()->SetTitle("#Delta R^{Match}(#tau^{Reco},#tau^{Gen})");
  histContainer_["dRRecoTauGenTauAntiMatch"]->GetXaxis()->SetTitle("#Delta R^{AntiMatch}(#tau^{Reco},#tau^{Gen})");

}

// ------------ method called once each job just after ending the event loop  ------------
void 
FactorizationDY::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
FactorizationDY::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
FactorizationDY::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
FactorizationDY::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
FactorizationDY::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
FactorizationDY::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(FactorizationDY);
