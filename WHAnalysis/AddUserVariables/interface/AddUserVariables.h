// -*- C++ -*-
//
// Package:    AddUserVariables
// Class:      AddUserVariables
// 
/**\class AddUserVariables AddUserVariables.cc WHAnalysis/AddUserVariables/src/AddUserVariables.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Sat Nov 26 12:12:11 CET 2011
// $Id$
//
//

#ifndef WHAnalysis_AddUserVariables_AddUserVariables_h
#define WHAnalysis_AddUserVariables_AddUserVariables_h


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/PatCandidates/interface/MET.h"

#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "TLorentzVector.h"

#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include <DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h>
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h"
#include "DataFormats/GeometryVector/interface/VectorUtil.h"

using namespace edm;
using namespace std;


//
// class declaration
//
template<typename T>
class AddUserVariables : public edm::EDProducer {
   public:
      explicit AddUserVariables(const edm::ParameterSet&);
      ~AddUserVariables();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

      typedef edm::Ptr<T> TPtr;
      typedef edm::View<T> TView;
      typedef std::vector<T> TCollection;

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      typedef std::vector<std::string> vstring;
      typedef std::vector<edm::EventRange> VEventRange;

      edm::InputTag objects_;
      edm::InputTag met_;       
      //edm::InputTag triggerResultsTag_;
      vstring triggerPaths_;
      vstring triggerObjNamesLeg1_;
      vstring triggerObjNamesLeg2_;
      //vstring triggerPathsMC_;
      //vstring triggerObjNamesLeg1MC_;
      //vstring triggerObjNamesLeg2MC_;
      VEventRange hltEventRanges_;
      edm::InputTag genParticleSrc_;
      int particleId_;
      bool isMC_;

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
template<typename T>
AddUserVariables<T>::AddUserVariables(const edm::ParameterSet& iConfig):
  objects_(iConfig.getParameter<edm::InputTag>("objects")),
  met_(iConfig.getParameter<edm::InputTag>("met")),
  //triggerResultsTag_(iConfig.getParameter<edm::InputTag>("triggerResults")), 
  triggerPaths_(iConfig.getParameter<vstring>("triggerPaths")), 
  triggerObjNamesLeg1_(iConfig.getParameter<vstring>("triggerObjNamesLeg1")), 
  triggerObjNamesLeg2_(iConfig.getParameter<vstring>("triggerObjNamesLeg2")),
  //triggerPathsMC_(iConfig.getParameter<vstring>("triggerPathsMC")), 
  //triggerObjNamesLeg1MC_(iConfig.getParameter<vstring>("triggerObjNamesLeg1MC")), 
  //triggerObjNamesLeg2MC_(iConfig.getParameter<vstring>("triggerObjNamesLeg2MC")), 
  hltEventRanges_(iConfig.getParameter<VEventRange>("hltEventRanges")),
  genParticleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("genParticles")),
  particleId_(iConfig.getParameter<int>("particleId")),
  isMC_(iConfig.getParameter<bool>("isMC"))
{

   produces<TCollection>("");
  
}

template<typename T>
AddUserVariables<T>::~AddUserVariables()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
template<typename T>
void
AddUserVariables<T>::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;
  using namespace reco;
  using namespace pat;

  edm::Handle<TView> leptons;
  iEvent.getByLabel(objects_,leptons);

  edm::Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByLabel(genParticleSrc_, genParticles);

  edm::Handle<pat::METCollection> metHandle;
  iEvent.getByLabel(met_,metHandle);
  const pat::METCollection* met = metHandle.product();

  std::auto_ptr<TCollection> leptonsWithMt(new TCollection() );

  string triggerPath;
  string HLTfilterLeg1;
  string HLTfilterLeg2;

  int runNumber = iEvent.id().run();
  int triggerPathsSize = triggerPaths_.size();

  for(int i = 0; i < triggerPathsSize; i++){

	edm::EventRange range;
	range = hltEventRanges_[i];
	int startRun = range.startRun();
	int endRun = range.endRun();
	if(runNumber >= startRun && runNumber <= endRun && runNumber != 1){

		triggerPath = triggerPaths_[i];
		HLTfilterLeg1 = triggerObjNamesLeg1_[i];
		HLTfilterLeg2 = triggerObjNamesLeg2_[i];

		//std::cout<<"InRun: "<<startRun<<" EndRun: "<<endRun<<" Trigger: "<<triggerPath<<std::endl;
		//std::cout<<"ActualRun: "<<runNumber<<std::endl;

	}
	//else if(runNumber == 1){

	//	triggerPath = triggerPathsMC_[i];
	//	HLTfilterLeg1 = triggerObjNamesLeg1MC_[i];
	//	HLTfilterLeg2 = triggerObjNamesLeg2MC_[i];

	//}

  }

  //edm::Handle<pat::TriggerEvent> triggerHandle;
  //iEvent.getByLabel(triggerResultsTag_, triggerHandle);
  //const pat::TriggerEvent* trigger = triggerHandle.product();

  for(unsigned int i = 0; i < leptons->size(); i++){ //Loop sugli oggetti

	TPtr lepton = leptons->ptrAt(i);
        T object( *lepton );

        float scalarSumPt = (object.p4()).Et() + ((*met)[0].p4()).Et();
        float vectorSumPt = (object.p4() + (*met)[0].p4()).Pt() ;
        float Mt = TMath::Sqrt( scalarSumPt*scalarSumPt - vectorSumPt*vectorSumPt );

        object.addUserFloat("Mt",Mt);

	if(iEvent.id().run() != 1){

		bool matchedLeg1 = false;
		bool matchedLeg2 = false;

	  	edm::Handle<pat::TriggerObjectStandAloneCollection > triggerObjsHandle;
	  	iEvent.getByLabel(edm::InputTag("patTrigger"),triggerObjsHandle);
	  	const pat::TriggerObjectStandAloneCollection* triggerObjs = triggerObjsHandle.product();

		for(pat::TriggerObjectStandAloneCollection::const_iterator it = triggerObjs->begin() ; it !=triggerObjs->end() ; it++){

			pat::TriggerObjectStandAlone *aObj = const_cast<pat::TriggerObjectStandAlone*>(&(*it));

		      	if( Geom::deltaR( aObj->triggerObject().p4(), object.p4() ) < 0.3 && aObj->hasFilterLabel(HLTfilterLeg1) ){
				matchedLeg1 = true;
		      	}
		      	if( Geom::deltaR( aObj->triggerObject().p4(), object.p4() ) < 0.3 && aObj->hasFilterLabel(HLTfilterLeg2) ){
				matchedLeg2 = true;
		      	}

		}

		int triggerMatchingLeg1 = 0;
		int triggerMatchingLeg2 = 0;
		if(matchedLeg1) triggerMatchingLeg1 = 1;
		else triggerMatchingLeg1 = 0;
		if(matchedLeg2) triggerMatchingLeg2 = 1;
		else triggerMatchingLeg2 = 0;

		//std::cout<<"leg1 "<<triggerMatchingLeg1<<" leg2 "<<triggerMatchingLeg2<<std::endl;

		object.addUserInt("triggerMatchingLeg1",triggerMatchingLeg1);
		object.addUserInt("triggerMatchingLeg2",triggerMatchingLeg2);

	}

	int mcMatch = 0;
	double phiReco = object.phi();
	double etaReco = object.eta();

	if(isMC_ && genParticles.isValid()){

	  	for(reco::GenParticleCollection::const_iterator it = genParticles->begin(); it != genParticles->end(); ++it ){

			int id = it->pdgId();
			//int status = it->status();
			int nDaughters = it->numberOfDaughters();
			double phiGen =it->phi();
			double etaGen=it->eta();

			int numNeutrinoTau = 0;
			int numNeutrinos = 0;

			if(abs(id) == 15){

				for ( int k = 0; k < nDaughters; k++ ){

					const  Candidate *  DaughterTau = it->daughter(k);
					int idDaughterTau = DaughterTau->pdgId();
			      		//std::cout<<"idDaughterTau = "<<idDaughterTau<<std::endl;
					if(fabs(idDaughterTau) == 16) ++numNeutrinoTau;
					if(fabs(idDaughterTau) == 12 || fabs(idDaughterTau) == 14) ++numNeutrinos;

				}

			}
			else{ 

				numNeutrinoTau = 1;
				numNeutrinos = 0;

			}

			if(abs(id) == particleId_){

				double dR = deltaR(etaGen, phiGen, etaReco, phiReco);
				if(dR <= 0.5 && numNeutrinoTau == 1 && numNeutrinos == 0){

					mcMatch = 1;
					std::cout<<"Id = "<<id<<" pId = "<<particleId_<<" dR = "<<dR<<" numNeutrinoTau = "<<numNeutrinoTau<<std::endl;
					std::cout<<" numNeutrinos = "<<numNeutrinos<<std::endl;

				}

			}

		}

	}

        object.addUserInt("mcMatch",mcMatch);

        leptonsWithMt->push_back(object);

  }

  iEvent.put( leptonsWithMt );
  return;

}

// ------------ method called once each job just before starting event loop  ------------
template<typename T>
void 
AddUserVariables<T>::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
template<typename T>
void 
AddUserVariables<T>::endJob() {
}

// ------------ method called when starting to processes a run  ------------
template<typename T>
void 
AddUserVariables<T>::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
template<typename T>
void 
AddUserVariables<T>::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
template<typename T>
void 
AddUserVariables<T>::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
template<typename T>
void 
AddUserVariables<T>::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
template<typename T>
void
AddUserVariables<T>::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

#endif
