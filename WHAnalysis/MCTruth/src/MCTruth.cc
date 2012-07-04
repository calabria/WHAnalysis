
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
//Check the provenance of electrons, muons and taus


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
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"

using namespace reco;

//
// class declaration
//

class MCTruth : public edm::EDProducer {
   public:
      explicit MCTruth(const edm::ParameterSet&);
      ~MCTruth();

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

      edm::InputTag genParticleSrc_;
      edm::InputTag muonSrc_;
      edm::InputTag eleSrc_;
      edm::InputTag tauSrc_;
      double deltaR_;

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
MCTruth::MCTruth(const edm::ParameterSet& iConfig):
  genParticleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("genParticles")),
  muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
  eleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("eleSrc")),
  tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc")),
  deltaR_(iConfig.getUntrackedParameter<double>("deltaR"))
{
   //register your products

  produces<pat::ElectronCollection>( "EleWGenMatch" ).setBranchAlias( "EleWGenMatch");
  produces<pat::ElectronCollection>( "EleHGenMatch" ).setBranchAlias( "EleHGenMatch");

  produces<pat::MuonCollection>( "MuWGenMatch" ).setBranchAlias( "MuWGenMatch");
  produces<pat::MuonCollection>( "MuHGenMatch" ).setBranchAlias( "MuHGenMatch");

  produces<pat::TauCollection>( "TauWGenMatch" ).setBranchAlias( "TauWGenMatch");
  produces<pat::TauCollection>( "TauHGenMatch" ).setBranchAlias( "TauHGenMatch");

}


MCTruth::~MCTruth()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
MCTruth::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;
  using namespace std;
  
  edm::Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByLabel(genParticleSrc_, genParticles);
  
  std::auto_ptr<pat::ElectronCollection> EleWGenMatch(new pat::ElectronCollection);
  std::auto_ptr<pat::ElectronCollection> EleHGenMatch(new pat::ElectronCollection);

  std::auto_ptr<pat::MuonCollection> MuWGenMatch(new pat::MuonCollection);
  std::auto_ptr<pat::MuonCollection> MuHGenMatch(new pat::MuonCollection);

  std::auto_ptr<pat::TauCollection> TauWGenMatch(new pat::TauCollection);
  std::auto_ptr<pat::TauCollection> TauHGenMatch(new pat::TauCollection);
  
  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(eleSrc_,electrons);

  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);

  if(genParticles.isValid()){

  for(reco::GenParticleCollection::const_iterator it = genParticles->begin(); it != genParticles->end(); ++it ){

	int id = it->pdgId();
	//int status = it->status();
	int nMothers = it->numberOfMothers();
	double phiGen =it->phi();
	double etaGen=it->eta();

	const  Candidate * mom = it->mother();

	if(mom && nMothers == 1){

		int motherPdgId = mom->pdgId();
		int motherStatus = mom->status();
		int mothernMothers = mom->numberOfMothers();

		//// Electrons ////

		if(abs(id) == 11 && abs(motherPdgId) == 15){

			const  Candidate * grandMother = mom->mother();

			if(grandMother && mothernMothers == 1){

				int grandMotherPdgId  = grandMother->pdgId();
				//int grandMotherStatus  = grandMother->status();
				int grandMotherNMothers  = grandMother->numberOfMothers();

				const  Candidate * grandgrandMother = grandMother->mother();

				if(grandgrandMother && grandMotherNMothers == 1 && abs(grandMotherPdgId) == 15){

					int grandgrandMotherPdgId = grandgrandMother->pdgId();
					int grandgrandMotherStatus = grandgrandMother->status();

			  		for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron){

			    			double phiReco = electron->phi();
			    			double etaReco = electron->eta();

						double dR = deltaR(etaGen, phiGen, etaReco, phiReco);
						std::cout<<"id = "<<id<<" momID = "<<motherPdgId<<" grandMotherID = "<<grandgrandMotherPdgId<<" dR = "<<dR<<std::endl;

						if(dR <= deltaR_ && grandgrandMotherPdgId == 25 && grandgrandMotherStatus == 3){
 
							EleHGenMatch->push_back(*electron);

						}
						else if(dR <= deltaR_ && abs(grandgrandMotherPdgId) == 24 && grandgrandMotherStatus == 3){

							EleWGenMatch->push_back(*electron);

						}

					}//fine loop ele reco

				}

			}
		}
		else if(abs(id) == 11 && abs(motherPdgId) == 24 && motherStatus == 3){

			for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron){

			    	double phiReco = electron->phi();
			    	double etaReco = electron->eta();

				double dR = deltaR(etaGen, phiGen, etaReco, phiReco);
				std::cout<<"id = "<<id<<" momID = "<<motherPdgId<<" dR = "<<dR<<std::endl;

				if(dR <= deltaR_ && abs(motherPdgId) == 24 && motherStatus == 3){

					EleWGenMatch->push_back(*electron);

				}

			}//fine loop ele reco

		}

		//// Muons ////

		else if(abs(id) == 13 && abs(motherPdgId) == 15){

			const  Candidate * grandMother = mom->mother();

			if(grandMother && mothernMothers == 1){

				int grandMotherPdgId  = grandMother->pdgId();
				//int grandMotherStatus  = grandMother->status();
				int grandMotherNMothers  = grandMother->numberOfMothers();

				const  Candidate * grandgrandMother = grandMother->mother();

				if(grandgrandMother && grandMotherNMothers == 1 && abs(grandMotherPdgId) == 15){

					int grandgrandMotherPdgId = grandgrandMother->pdgId();
					int grandgrandMotherStatus = grandgrandMother->status();

			  		for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon){

			    			double phiReco = muon->phi();
			    			double etaReco = muon->eta();

						double dR = deltaR(etaGen, phiGen, etaReco, phiReco);
						std::cout<<"id = "<<id<<" momID = "<<motherPdgId<<" grandMotherID = "<<grandgrandMotherPdgId<<" dR = "<<dR<<std::endl;

						if(dR <= deltaR_ && grandgrandMotherPdgId == 25 && grandgrandMotherStatus == 3){

							MuHGenMatch->push_back(*muon);

						}
						else if(dR <= deltaR_ && abs(grandgrandMotherPdgId) == 24 && grandgrandMotherStatus == 3){

							MuWGenMatch->push_back(*muon);

						}

					}

				}//fine loop muon reco

			}

		}
		else if(abs(id) == 13 && abs(motherPdgId) == 24 && motherStatus == 3){

			for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon){

			    	double phiReco = muon->phi();
			    	double etaReco = muon->eta();

				double dR = deltaR(etaGen, phiGen, etaReco, phiReco);
				std::cout<<"id = "<<id<<" momID = "<<motherPdgId<<" dR = "<<dR<<std::endl;

				if(dR <= deltaR_ && abs(motherPdgId) == 24 && motherStatus == 3){

					MuWGenMatch->push_back(*muon);

				}

			}//fine loop muon reco

		}

		//// Taus //// Check hadronic tau to be implemented

		else if(abs(id) == 15){

	  		for(edm::View<pat::Tau>::const_iterator tau=taus->begin(); tau!=taus->end(); ++tau){

	    			double phiReco = tau->phi();
	    			double etaReco = tau->eta();

				double dR = deltaR(etaGen, phiGen, etaReco, phiReco);
				if(dR <= deltaR_ && abs(motherPdgId) == 24 && motherStatus == 3){

				    		std::cout<<"id = "<<id<<" momID = "<<motherPdgId<<" dR = "<<dR<<std::endl;
						TauWGenMatch->push_back(*tau);

				}
				else if(dR <= deltaR_ && motherPdgId == 25 && motherStatus == 3){

				    		std::cout<<"id = "<<id<<" momID = "<<motherPdgId<<" dR = "<<dR<<std::endl;
						TauHGenMatch->push_back(*tau);

				}

			}//fine loop muon reco

		}

	}//fine if

    }//fine loop gen particle  

  }//fine isValid

  iEvent.put(EleWGenMatch, "EleWGenMatch");
  iEvent.put(EleHGenMatch, "EleHGenMatch");

  iEvent.put(MuWGenMatch, "MuWGenMatch");
  iEvent.put(MuHGenMatch, "MuHGenMatch");

  iEvent.put(TauWGenMatch, "TauWGenMatch");
  iEvent.put(TauHGenMatch, "TauHGenMatch");

}
 


// ------------ method called once each job just before starting event loop  ------------
void 
MCTruth::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MCTruth::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
MCTruth::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
MCTruth::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
MCTruth::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
MCTruth::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MCTruth::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MCTruth);
