// -*- C++ -*-
//
// Package:    ZEleTauVeto
// Class:      ZEleTauVeto
// 
/**\class ZEleTauVeto ZEleTauVeto.cc WHAnalysis/ZEleTauVeto/src/ZEleTauVeto.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  
//         Created:  Thu Feb 21 16:14:42 CET 2013
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
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

//
// class declaration
//

class ZEleTauVeto : public edm::EDFilter {
   public:
      explicit ZEleTauVeto(const edm::ParameterSet&);
      ~ZEleTauVeto();

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
  
      edm::InputTag CompCandTag_;
      double Cut_;
      bool filter_;

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
ZEleTauVeto::ZEleTauVeto(const edm::ParameterSet& iConfig):
   CompCandTag_(iConfig.getUntrackedParameter<edm::InputTag>("CompCandSrc")),
   Cut_(iConfig.getUntrackedParameter<double>("cut")),
   filter_(iConfig.getParameter<bool>("filter"))
{
   //now do what ever initialization is needed
  produces<reco::CompositeCandidateCollection>("");
}


ZEleTauVeto::~ZEleTauVeto()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
ZEleTauVeto::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   bool result=false;

   edm::Handle<edm::View<reco::CompositeCandidate> > CompCandidates;
   iEvent.getByLabel(CompCandTag_, CompCandidates);
     
   std::auto_ptr<reco::CompositeCandidateCollection> selectedFinalCand(new reco::CompositeCandidateCollection);
   
   for(edm::View<reco::CompositeCandidate>::const_iterator CompCand=CompCandidates->begin(); CompCand!=CompCandidates->end(); ++CompCand){
       
       const reco::Candidate * WLepCand = CompCand->daughter(0);
       const reco::Candidate * DiTauCand = CompCand->daughter(1);
       
       const double Zmass = 91.1876;
       
       int WLepCharge = WLepCand->charge();
       int Tau1Charge = DiTauCand->daughter(0)->charge();
       int Tau2Charge = DiTauCand->daughter(1)->charge();
       
       //std::cout<<WLepCharge<<"    "<<Tau1Charge<<"   "<<Tau2Charge<<"   "<<std::endl;
       int ctrlCharge = WLepCharge*Tau1Charge;
       
       double massWLepTauOS = 0;
       if(ctrlCharge==-1) massWLepTauOS = (WLepCand->p4() + DiTauCand->daughter(0)->p4()).M();
       else massWLepTauOS = (WLepCand->p4() + DiTauCand->daughter(1)->p4()).M();
	 
       double ctrlMass = TMath::Abs(massWLepTauOS - Zmass);
       //std::cout<<ctrlMass<<std::endl;
       
       if(ctrlMass > Cut_){

	 selectedFinalCand->push_back(*CompCand);
	 result=true;

       }

   }
   
   iEvent.put(selectedFinalCand);
   if(!filter_) result = true;
   return result;

}

// ------------ method called once each job just before starting event loop  ------------
void 
ZEleTauVeto::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ZEleTauVeto::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
ZEleTauVeto::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
ZEleTauVeto::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
ZEleTauVeto::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
ZEleTauVeto::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ZEleTauVeto::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(ZEleTauVeto);
