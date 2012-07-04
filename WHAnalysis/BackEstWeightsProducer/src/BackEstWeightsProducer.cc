// -*- C++ -*-
//
// Package:    BackEstWeightsProducer
// Class:      BackEstWeightsProducer
// 
/**\class BackEstWeightsProducer BackEstWeightsProducer.cc WHAnalysis/BackEstWeightsProducer/src/BackEstWeightsProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Sun Nov  6 15:40:05 CET 2011
// $Id$
//
//


// system include files
#include <memory>
#include <TMath.h>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/PatCandidates/interface/PATObject.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/GenericParticle.h"
//
// class declaration
//

class BackEstWeightsProducer : public edm::EDProducer {
   public:
      explicit BackEstWeightsProducer(const edm::ParameterSet&);
      ~BackEstWeightsProducer();

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
      edm::InputTag tauSrc_;
      edm::InputTag jetSrc_;

      bool doMuonWeight_;
      bool doEleWeight_;
      bool doTauWeight_;

};

double fakeRateMu(double pt){
	double p0 = 1.43354e-01;
	double p1 = -2.34616e-01;
	double p2 = 4.57984e+00;
	double p3 = 3.23736e-02;

	double fakeMu = p0*TMath::Exp(p1*pt + p2) + p3;
	return fakeMu;
}

double fakeRateTau(double pt){
   	double p0 = 8.27863e-01;
   	double p1 = -1.07830e-01;
   	double p2 = -1.19827e+00;
   	double p3 = 1.30745e-02;

   	double fakeTau = p0*TMath::Exp(p1*pt + p2) + p3;
	return fakeTau;
}

double fakeRateEle(double pt){
   	double p0 = 1.34898e-01;
   	double p1 = -2.76961e-01;
   	double p2 = 5.05158e+00;
   	double p3 = 6.30212e-02;

   	double fakeEle = p0*TMath::Exp(p1*pt + p2) + p3;
	return fakeEle;
}

double fakeRateEleEvan(double pt){
   	double fakeEle = 7.8269e-01*TMath::Landau(pt,1.9368e+01,1.9240e+00,0)+1.5453e-02;
	return fakeEle;
}

double fakeRateMuEvan(double pt){
   	double fakeMu = 3.1196e+00*TMath::Landau(pt,1.5481e+01,2.7508e+00,0)+6.9223e-03;
	return fakeMu;
}

double fakeRateTauMedium(double pt){
	double mpv = 5.66262;
    	double sigma = 1.34932;
    	double costante = 8.81336e-03;
   
    	double fakeTau = ((TMath::Landau(pt,mpv,sigma))+costante);  
	return fakeTau;
}

double fakeRateTauTight(double pt){
 	double mpv = 7.08367;
    	double sigma = 8.53405e-01;
    	double costante = 9.18288e-03;
   
     	double fakeTau = ((TMath::Landau(pt,mpv,sigma))+costante);
	return fakeTau;
}

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//

BackEstWeightsProducer::BackEstWeightsProducer(const edm::ParameterSet& iConfig):
  muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc")),
  eleSrc_(iConfig.getParameter<edm::InputTag>("eleSrc")),
  tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc")),
  jetSrc_(iConfig.getParameter<edm::InputTag>("jetSrc")),
  doMuonWeight_(iConfig.getParameter<bool>("doMuonWeight")),
  doEleWeight_(iConfig.getParameter<bool>("doEleWeight")),
  doTauWeight_(iConfig.getParameter<bool>("doTauWeight"))
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

  produces< pat::MuonCollection >("patMuonsWithWeights").setBranchAlias("patMuonsWithWeights");
  produces< pat::ElectronCollection >("patElectronsWithWeights").setBranchAlias("patElectronsWithWeights");
  produces< pat::TauCollection >("patTausWithWeightsMedium").setBranchAlias("patTausWithWeightsMedium");
  produces< pat::TauCollection >("patTausWithWeightsTight").setBranchAlias("patTausWithWeightsTight");
  
}


BackEstWeightsProducer::~BackEstWeightsProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------

void
BackEstWeightsProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

//----------------------------------------------------------------------------------------------------------------------------------------

   //std::vector<double> valuesEleFakeRateEvan;

   edm::Handle<edm::View<pat::Electron> > electrons;
   iEvent.getByLabel(eleSrc_,electrons);

   edm::Handle<pat::JetCollection> patJets;
   iEvent.getByLabel(jetSrc_, patJets);

   std::auto_ptr< pat::ElectronCollection > patElectronsWithWeights( new pat::ElectronCollection );

   for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron){

   	pat::Electron * someElectron = electron->clone();

   	double eleEta = electron->eta();
   	double elePhi = electron->phi();
   	double minEleJetDR = 1000000;
   	double ptForWeight = 0;

	 	for(std::vector<pat::Jet>::const_iterator patJet = patJets->begin(); patJet != patJets->end(); ++patJet){

   		double jetEta = patJet->eta();
   		double jetPhi = patJet->phi();
	   	double deltaReleJet = deltaR(eleEta, elePhi, jetEta, jetPhi);
   		if(deltaReleJet < minEleJetDR) minEleJetDR = deltaReleJet;
   	
   		}

   	if(minEleJetDR < 0.5){
   		for(std::vector<pat::Jet>::const_iterator patJet = patJets->begin(); patJet != patJets->end(); ++patJet){

   	   	double jetEta = patJet->eta();
   	   	double jetPhi = patJet->phi();
	      	double deltaReleJet = deltaR(eleEta, elePhi, jetEta, jetPhi);
   	   	if(deltaReleJet == minEleJetDR) ptForWeight = patJet->pt();
   	
   		}
   	}

   	else ptForWeight = electron->pt();

   	double eleWeight = 0;
	if(doEleWeight_) eleWeight = fakeRateEle(ptForWeight);

	//valuesEleFakeRateEvan.push_back(eleWeight);
   	//std::cout<<"eleWeight "<<eleWeight<<std::endl; 

   	someElectron->addUserFloat("eleWeight", eleWeight);
   	patElectronsWithWeights->push_back(*someElectron);
   }

   iEvent.put( patElectronsWithWeights, "patElectronsWithWeights" );

   /*// convert into ValueMap and store
   std::auto_ptr<ValueMap<double> > valMap(new ValueMap<double>());
   ValueMap<double>::Filler filler(*valMap);
   filler.insert(electrons, valuesEleFakeRateEvan.begin(), valuesEleFakeRateEvan.end());
   filler.fill();
   iEvent.put(valMap, "fakeRateEleEvan");*/

//----------------------------------------------------------------------------------------------------------------------------------------

   edm::Handle<edm::View<pat::Muon> > muons;
   iEvent.getByLabel(muonSrc_,muons);

   //std::vector<double> valuesMuFakeRateEvan;

   std::auto_ptr< pat::MuonCollection > patMuonsWithWeights( new pat::MuonCollection );

   for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon){

	pat::Muon * someMuon = muon->clone();

	double muonEta = muon->eta();
	double muonPhi = muon->phi();
	double minMuJetDR = 1000000;
	double ptForWeight = 0;

 	for(std::vector<pat::Jet>::const_iterator patJet = patJets->begin(); patJet != patJets->end(); ++patJet){

	   	double jetEta = patJet->eta();
	   	double jetPhi = patJet->phi();
	   	double deltaRmuonJet = deltaR(muonEta, muonPhi, jetEta, jetPhi);
	   	if(deltaRmuonJet < minMuJetDR) minMuJetDR = deltaRmuonJet;
   	
	}

	if(minMuJetDR < 0.5){
   	 	for(std::vector<pat::Jet>::const_iterator patJet = patJets->begin(); patJet != patJets->end(); ++patJet){

	   		double jetEta = patJet->eta();
	   		double jetPhi = patJet->phi();
	      		double deltaRmuonJet = deltaR(muonEta, muonPhi, jetEta, jetPhi);
	   		if(deltaRmuonJet == minMuJetDR) ptForWeight = patJet->pt();
   	
   		}
	}

	else ptForWeight = muon->pt();

	double muonWeight = 0;
	if(doMuonWeight_) muonWeight = fakeRateMu(ptForWeight);

	//valuesMuFakeRateEvan.push_back(muonWeight);
   	//std::cout<<"muonWeight "<<muonWeight<<std::endl; 

	someMuon->addUserFloat("muonWeight", muonWeight);
	patMuonsWithWeights->push_back(*someMuon);

   }

   iEvent.put( patMuonsWithWeights, "patMuonsWithWeights" );

   /*// convert into ValueMap and store
   std::auto_ptr<ValueMap<double> > valMap2(new ValueMap<double>());
   ValueMap<double>::Filler filler2(*valMap2);
   filler2.insert(muons, valuesMuFakeRateEvan.begin(), valuesMuFakeRateEvan.end());
   filler2.fill();
   iEvent.put(valMap2, "fakeRateMuonEvan");*/

//----------------------------------------------------------------------------------------------------------------------------------------

   edm::Handle<edm::View<pat::Tau> > taus;
   iEvent.getByLabel(tauSrc_,taus);

   //std::vector<double> valuesTauFakeRateEvan;

   std::auto_ptr< pat::TauCollection > patTausWithWeightsMedium( new pat::TauCollection );
   std::auto_ptr< pat::TauCollection > patTausWithWeightsTight( new pat::TauCollection );

   for(edm::View<pat::Tau>::const_iterator patTau=taus->begin(); patTau!=taus->end(); ++patTau){

	pat::Tau * someTau = patTau->clone();	

   	double tauPt = patTau->pt();
	double tauWeight = 0;
	//double tauWeightMedium = 0;
	//double tauWeightTight = 0;

	if(doTauWeight_){
		tauWeight = fakeRateTauMedium(tauPt);
		//tauWeightMedium = fakeRateTauMedium(tauPt);
		//tauWeightTight = fakeRateTauTight(tauPt);
	}

   	//std::cout<<"tauWeight "<<tauWeight<<std::endl;
	//valuesTauFakeRateEvan.push_back(tauWeight);

	someTau->addUserFloat("tauWeight", tauWeight);
	patTausWithWeightsMedium->push_back(*someTau);

   }

   for(edm::View<pat::Tau>::const_iterator patTau=taus->begin(); patTau!=taus->end(); ++patTau){

	pat::Tau * someTau = patTau->clone();	

   	double tauPt = patTau->pt();
	double tauWeight = 0;
	//double tauWeightMedium = 0;
	//double tauWeightTight = 0;

	if(doTauWeight_){
		tauWeight = fakeRateTauTight(tauPt);
		//tauWeightMedium = fakeRateTauMedium(tauPt);
		//tauWeightTight = fakeRateTauTight(tauPt);
	}

   	//std::cout<<"tauWeight "<<tauWeight<<std::endl; 
	//valuesTauFakeRateEvan.push_back(tauWeight);

	someTau->addUserFloat("tauWeight", tauWeight);
	patTausWithWeightsTight->push_back(*someTau);

   }

   iEvent.put( patTausWithWeightsMedium, "patTausWithWeightsMedium" );
   iEvent.put( patTausWithWeightsTight, "patTausWithWeightsTight" );

   /*// convert into ValueMap and store
   std::auto_ptr<ValueMap<double> > valMap2(new ValueMap<double>());
   ValueMap<double>::Filler filler2(*valMap2);
   filler2.insert(muons, valuesMuFakeRateEvan.begin(), valuesMuFakeRateEvan.end());
   filler2.fill();
   iEvent.put(valMap2, "fakeRateMuonEvan");*/

}

// ------------ method called once each job just before starting event loop  ------------

void 
BackEstWeightsProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------

void 
BackEstWeightsProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------

void 
BackEstWeightsProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------

void 
BackEstWeightsProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------

void 
BackEstWeightsProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------

void 
BackEstWeightsProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------

void
BackEstWeightsProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(BackEstWeightsProducer);
