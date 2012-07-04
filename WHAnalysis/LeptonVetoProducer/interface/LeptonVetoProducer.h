// -*- C++ -*-
//
// Package:    LeptonVetoProducer
// Class:      LeptonVetoProducer
// 
/**\class LeptonVetoProducer LeptonVetoProducer.cc WHAnalysis/LeptonVetoProducer/src/LeptonVetoProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Wed Feb  1 16:02:22 CET 2012
// $Id$
//
//

#ifndef WHAnalysis_LeptonVetoProducer_LeptonVetoProducer_h
#define WHAnalysis_LeptonVetoProducer_LeptonVetoProducer_h

// system include files
#include <memory>
#include <map>
#include <string>
#include <cmath>
#include <vector>
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
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/GeometryVector/interface/VectorUtil.h"


//
// class declaration
//
template<typename T>
class LeptonVetoProducer : public edm::EDProducer {
   public:

      explicit LeptonVetoProducer(const edm::ParameterSet&);
      ~LeptonVetoProducer();

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

      edm::InputTag lep1Src_;
      edm::InputTag lep2Src_;
      //double DeltaRCut_;
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
LeptonVetoProducer<T>::LeptonVetoProducer(const edm::ParameterSet& iConfig):
  lep1Src_(iConfig.getUntrackedParameter<edm::InputTag>("lep1Src")),
  lep2Src_(iConfig.getUntrackedParameter<edm::InputTag>("lep2Src"))
  //DeltaRCut_(iConfig.getUntrackedParameter<double>("DeltaRCut"))
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

   produces<TCollection>("");
  
}

template<typename T>
LeptonVetoProducer<T>::~LeptonVetoProducer()
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
LeptonVetoProducer<T>::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  using namespace pat;

  edm::Handle<TView> leptons1;
  iEvent.getByLabel(lep1Src_,leptons1);

  edm::Handle<TView> leptons2;
  iEvent.getByLabel(lep2Src_,leptons2);

  int sizeLep1 = leptons1->size();
  int sizeLep2 = leptons2->size();

  std::auto_ptr<TCollection> SelectedLeptonsForLeptonVeto(new TCollection() );

  //std::cout<<sizeLep1<<" "<<sizeLep2<<std::endl;

  for(int i = 0; i < sizeLep1; i++){

  	bool lepResult = true;

	TPtr lepton1 = leptons1->ptrAt(i);

        T object( *lepton1 );
      
     	double ptLep1 = lepton1->pt();
     	double etaLep1 = lepton1->eta();
      	double phiLep1 = lepton1->phi();

      	if(sizeLep2 != 0){
	  	for(int j = 0; j < sizeLep2; j++){

			TPtr lepton2 = leptons2->ptrAt(j);
	    
	     		double ptLep2 = lepton2->pt();
		    	double etaLep2 = lepton2->eta();
		    	double phiLep2 = lepton2->phi();
		    	//double deltaREle1Ele2 = deltaR(etaLep1, phiLep1, etaLep2, phiLep2 );
		    	//if(deltaREle1Ele2 < DeltaRCut_) lepResult = false;
			if(ptLep1 == ptLep2 && etaLep1 == etaLep2 && phiLep1 == phiLep2) lepResult = false;
		    
		    	//std::cout<<"size ele = "<<sizeEle<<" size mu = "<<sizeMu<<" muEle dR = "<<deltaRmuEle<<" lepResult = "<<lepResult<<std::endl;
	    
	 	}//fine loop
	}

	//std::cout<<" lepResult = "<<lepResult<<std::endl;
      	if(lepResult) SelectedLeptonsForLeptonVeto->push_back(object); 

  }//Fine loop sui leptoni

  iEvent.put(SelectedLeptonsForLeptonVeto);
 
 
}

// ------------ method called once each job just before starting event loop  ------------
template<typename T>
void 
LeptonVetoProducer<T>::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
template<typename T>
void 
LeptonVetoProducer<T>::endJob() {
}

// ------------ method called when starting to processes a run  ------------
template<typename T>
void 
LeptonVetoProducer<T>::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
template<typename T>
void 
LeptonVetoProducer<T>::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
template<typename T>
void 
LeptonVetoProducer<T>::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
template<typename T>
void 
LeptonVetoProducer<T>::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
template<typename T>
void
LeptonVetoProducer<T>::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

#endif

