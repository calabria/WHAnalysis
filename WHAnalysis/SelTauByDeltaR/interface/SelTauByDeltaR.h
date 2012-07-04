// -*- C++ -*-
//
// Package:    SelTauByDeltaR
// Class:      SelTauByDeltaR
// 
/**\class SelTauByDeltaR SelTauByDeltaR.cc WHAnalysis/SelTauByDeltaR/src/SelTauByDeltaR.cc

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

#ifndef WHAnalysis_SelTauByDeltaR_SelTauByDeltaR_h
#define WHAnalysis_SelTauByDeltaR_SelTauByDeltaR_h

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

template<typename T1, typename T2>
class SelTauByDeltaR : public edm::EDProducer {
   public:
      explicit SelTauByDeltaR(const edm::ParameterSet&);
      ~SelTauByDeltaR();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

      typedef edm::Ptr<T1> TPtr1;
      typedef edm::View<T1> TView1;
      typedef std::vector<T1> TCollection1;

      typedef edm::Ptr<T2> TPtr2;
      typedef edm::View<T2> TView2;
      typedef std::vector<T2> TCollection2;

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
                       
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag tauSrc_;
      edm::InputTag lep1Src_;
      edm::InputTag lep2Src_;
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
template<typename T1, typename T2>
SelTauByDeltaR<T1,T2>::SelTauByDeltaR(const edm::ParameterSet& iConfig):
  tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc")),
  lep1Src_(iConfig.getUntrackedParameter<edm::InputTag>("lep1Src")),
  lep2Src_(iConfig.getUntrackedParameter<edm::InputTag>("lep2Src")),
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

  produces<pat::TauCollection>("TauSelByDeltaR").setBranchAlias("TauSelByDeltaR");
}

template<typename T1, typename T2>
SelTauByDeltaR<T1,T2>::~SelTauByDeltaR()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
template<typename T1, typename T2>
void
SelTauByDeltaR<T1,T2>::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);

  edm::Handle<TView1> leptons1;
  iEvent.getByLabel(lep1Src_,leptons1);

  edm::Handle<TView2> leptons2;
  iEvent.getByLabel(lep2Src_,leptons2);

  int sizeLep1 = leptons1->size();
  int sizeLep2 = leptons2->size();
  int sizeTau = taus->size();

  //std::cout<<"size mu "<<sizeMu<<" size ele "<<sizeEle<<" size tau "<<sizeTau<<std::endl;

  std::auto_ptr<pat::TauCollection> TauSelByDeltaR(new pat::TauCollection);

  for(edm::View<pat::Tau>::const_iterator tau = taus->begin(); tau != taus->end(); ++tau){

  	bool lep2Result = true;
  	bool lep1Result = true;

	double etaTau=tau->eta();   
	double phiTau=tau->phi();

	if(sizeLep2 != 0){
	 	for(int i = 0; i < sizeLep2; i++){

			TPtr2 lepton2 = leptons2->ptrAt(i);

	   		double etaLep2 = lepton2->eta();
	   		double phiLep2 = lepton2->phi();
	   		double deltaRLep2Tau = deltaR(etaTau, phiTau, etaLep2, phiLep2);
	   		if (deltaRLep2Tau < DeltaRCut_) lep2Result = false;

	   		//std::cout<<"lep2 dR = "<<deltaRLep2Tau<<" bool lep2 = "<< lep2Result<<std::endl;

	  	}//fine loop lep2
	}

	if(sizeLep1 != 0){
	 	for(int i = 0; i < sizeLep1; i++){

			TPtr1 lepton1 = leptons1->ptrAt(i);

	   		double etaLep1 = lepton1->eta();
	   		double phiLep1 = lepton1->phi();
	   		double deltaRLep1Tau = deltaR(etaTau, phiTau, etaLep1, phiLep1 );
	   		if (deltaRLep1Tau < DeltaRCut_) lep1Result = false;

	   		//std::cout<<"lep1 dR = "<<deltaRLep1Tau<<" bool lep1 = "<<lep1Result<<std::endl;

	 	}//fine loop sui lep1
	}
   
	bool tauResult = lep2Result && lep1Result;
	//std::cout<<"bool lep2 = "<<lep2Result<<" bool lep1 = "<<lep1Result<<" bool tau = "<<tauResult<<" tau pt = "<<tau->pt()<<std::endl;
	if(lep2Result && lep1Result) TauSelByDeltaR->push_back(*tau);
 
 
  }//fine loop tau

  iEvent.put(TauSelByDeltaR, "TauSelByDeltaR");
 
}

// ------------ method called once each job just before starting event loop  ------------
template<typename T1, typename T2>
void 
SelTauByDeltaR<T1,T2>::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
template<typename T1, typename T2>
void 
SelTauByDeltaR<T1,T2>::endJob() {
}

// ------------ method called when starting to processes a run  ------------
template<typename T1, typename T2>
void 
SelTauByDeltaR<T1,T2>::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
template<typename T1, typename T2>
void 
SelTauByDeltaR<T1,T2>::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
template<typename T1, typename T2>
void 
SelTauByDeltaR<T1,T2>::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
template<typename T1, typename T2>
void 
SelTauByDeltaR<T1,T2>::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
template<typename T1, typename T2>
void
SelTauByDeltaR<T1,T2>::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

#endif

