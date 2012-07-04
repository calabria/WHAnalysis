// -*- C++ -*-
//
// Package:    MCTruthFullyHadronic
// Class:      MCTruthFullyHadronic
// 
/**\class MCTruthFullyHadronic MCTruthFullyHadronic.cc WHAnalysis/MCTruthFullyHadronic/src/MCTruthFullyHadronic.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  
//         Created:  Wed May  9 23:55:12 CEST 2012
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
#include "FWCore/Framework/interface/EDFilter.h"

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

class MCTruthFullyHadronic : public edm::EDFilter {
   public:
      explicit MCTruthFullyHadronic(const edm::ParameterSet&);
      ~MCTruthFullyHadronic();

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

      edm::InputTag genParticleSrc_;

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
MCTruthFullyHadronic::MCTruthFullyHadronic(const edm::ParameterSet& iConfig):
  genParticleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("genParticles"))
{
   //now do what ever initialization is needed

}


MCTruthFullyHadronic::~MCTruthFullyHadronic()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
MCTruthFullyHadronic::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;

  bool debug = true;
  
  edm::Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByLabel(genParticleSrc_, genParticles);

  bool isEleFromWtaunu = false;
  bool isEleFromWenu = false;
  bool isTauHadronicFromHiggs = false;
  int numHadronicTaus = 0;

  if(genParticles.isValid()){

  for(reco::GenParticleCollection::const_iterator it = genParticles->begin(); it != genParticles->end(); ++it ){

	//Variabili della prima particella madre di tutte le altre
	int id = it->pdgId();
	int status = it->status();
	//Numero di figli della particella iniziale

	if(fabs(id) == 24 && status == 3){ //Controllo che sia un W stato 3

		int nDaughters = it->numberOfDaughters();

		for ( int i = 0; i < nDaughters; i++ ){ //Loop sui suoi figli

	      		const  Candidate *  Daughters = it->daughter(i); //Reference al figlio i-esimo
	      		int idDaughter = Daughters->pdgId();
	      		if(debug) std::cout<<"id = "<<id<<" idDaughterW = "<<idDaughter<<std::endl;

			if(fabs(idDaughter) == 11){
 					
				isEleFromWenu = true;
				if(debug) std::cout<<"Particle is an electron coming from Wenu"<<std::endl;

			}
			else if(fabs(idDaughter) == 15){

				int numDaughtersTau1 = Daughters->numberOfDaughters();

				for ( int j = 0; j < numDaughtersTau1; j++ ){ //Loop sui figli del primo tau

					const  Candidate *  DaughtersTau1 = Daughters->daughter(j); //Figlio i-esimo del tau1
		      			int idDaughterTau1 = DaughtersTau1->pdgId(); //Id del figlio i-esimo del tau1
		      			if(debug) std::cout<<"idDaughterTau1 = "<<idDaughterTau1<<std::endl;

					if(fabs(idDaughterTau1) == 15){//Se il figlio del tau1 è ancora un tau...

						int numDaughtersTau2 = DaughtersTau1->numberOfDaughters();//Numero di figli del figlio j-esimo del tau1

						for ( int k = 0; k < numDaughtersTau2; k++ ){ //Loop sui figli del tau2

							const  Candidate *  DaughtersTau2 = DaughtersTau1->daughter(k);
							int idDaughterTau2 = DaughtersTau2->pdgId();
		      					if(debug) std::cout<<"idDaughterTau2 = "<<idDaughterTau2<<std::endl;

							if(fabs(idDaughterTau2) == 11){

								isEleFromWtaunu = true;
								if(debug) std::cout<<"Particle is an electron coming from Wtaunu"<<std::endl;

							}

						}
	
					}

				}

			} //Fine tragedia

		}

	}
	else if(fabs(id) == 25 && status == 3){

		int nDaughters = it->numberOfDaughters();

		for ( int i = 0; i < nDaughters; i++ ){

	      		const  Candidate *  Daughters = it->daughter(i);
	      		int idDaughter = Daughters->pdgId();
	      		if(debug) std::cout<<"id = "<<id<<" idDaughterH = "<<idDaughter<<std::endl;

			if(fabs(idDaughter) == 15){

				int numDaughtersTau1 = Daughters->numberOfDaughters();

				for ( int j = 0; j < numDaughtersTau1; j++ ){ //Loop sui figli del primo tau

					const  Candidate *  DaughtersTau1 = Daughters->daughter(j); //Figlio i-esimo del tau1
		      			int idDaughterTau1 = DaughtersTau1->pdgId(); //Id del figlio i-esimo del tau1
		      			if(debug) std::cout<<"idDaughterTau1 = "<<idDaughterTau1<<std::endl;

					if(fabs(idDaughterTau1) == 15){//Se il figlio del tau1 è ancora un tau...

						int numDaughtersTau2 = DaughtersTau1->numberOfDaughters();//Numero di figli del figlio i-esimo del tau1
						int numLeptons = 0;

						for ( int k = 0; k < numDaughtersTau2; k++ ){ //Loop sui figli del tau2

							const  Candidate *  DaughtersTau2 = DaughtersTau1->daughter(k);
							int idDaughterTau2 = DaughtersTau2->pdgId();
		      					if(debug) std::cout<<"idDaughterTau2 = "<<idDaughterTau2<<std::endl;

							if(fabs(idDaughterTau2) == 11 || fabs(idDaughterTau2) == 13) ++numLeptons;

						}

						if(!numLeptons){

							isTauHadronicFromHiggs = true;
							if(debug) std::cout<<"Particle is a hadronic tau coming from Higgs"<<std::endl;
							++numHadronicTaus;

						}
	
					}

				}

			}

		}

	}

    }//fine loop gen particle  

  }//fine isValid

  std::cout<<"Number of hadronic taus: "<<numHadronicTaus<<std::endl;
  std::cout<<"isTauHadronicFromHiggs "<<isTauHadronicFromHiggs<<std::endl;
  std::cout<<"isEleFromWtaunu: "<<isEleFromWtaunu<<std::endl;
  std::cout<<"isEleFromWenu: "<<isEleFromWenu<<std::endl;
  bool result = isTauHadronicFromHiggs && (isEleFromWtaunu | isEleFromWenu) && numHadronicTaus == 2;

  if(result) std::cout<<"Is an ett final state? "<<result<<std::endl;

  return result;
}

// ------------ method called once each job just before starting event loop  ------------
void 
MCTruthFullyHadronic::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MCTruthFullyHadronic::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
MCTruthFullyHadronic::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
MCTruthFullyHadronic::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
MCTruthFullyHadronic::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
MCTruthFullyHadronic::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MCTruthFullyHadronic::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(MCTruthFullyHadronic);
