// -*- C++ -*-
//
// Package:    ZTauTauVeto
// Class:      ZTauTauVeto
// 
/**\class ZTauTauVeto ZTauTauVeto.cc WHAnalysis/ZTauTauVeto/src/ZTauTauVeto.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Fri May 25 10:07:29 CEST 2012
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

class ZTauTauVeto : public edm::EDFilter {
   public:
      explicit ZTauTauVeto(const edm::ParameterSet&);
      ~ZTauTauVeto();

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

      edm::InputTag CompCandSrc_;
      edm::InputTag PFMetTag_;
      double mtCut1_;
      double cosCut1_;
      double mtCut2_;
      double cosCut2_;
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
ZTauTauVeto::ZTauTauVeto(const edm::ParameterSet& iConfig):
  CompCandSrc_(iConfig.getUntrackedParameter<edm::InputTag>("CompCandSrc")),
  PFMetTag_(iConfig.getUntrackedParameter<edm::InputTag> ("PFMetTag")),
  mtCut1_(iConfig.getUntrackedParameter<double>("mtCut1")),
  cosCut1_(iConfig.getUntrackedParameter<double>("cosCut1")),
  mtCut2_(iConfig.getUntrackedParameter<double>("mtCut2")),
  cosCut2_(iConfig.getUntrackedParameter<double>("cosCut2")),
  filter_(iConfig.getParameter<bool>("filter"))
{
   //now do what ever initialization is needed
   produces<reco::CompositeCandidateCollection>("");

}


ZTauTauVeto::~ZTauTauVeto()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
ZTauTauVeto::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;

   bool result = false;

   edm::Handle<edm::View<reco::CompositeCandidate> > CompCandidates;
   iEvent.getByLabel(CompCandSrc_, CompCandidates);

   //std::cout<<"size: "<<CompCandidates->size()<<std::endl;

   edm::Handle<pat::METCollection> pfmet;
   iEvent.getByLabel(PFMetTag_, pfmet);

   double met = pfmet->front().et();

   std::auto_ptr<reco::CompositeCandidateCollection> selectedFinalCand(new reco::CompositeCandidateCollection);

   for(edm::View<reco::CompositeCandidate>::const_iterator CompCand=CompCandidates->begin(); CompCand!=CompCandidates->end(); ++CompCand){

   	//bool result1 = false;
   	//bool result2 = false;

	const Candidate * WLepCand = CompCand->daughter(0);
	const Candidate * DiTauCand = CompCand->daughter(1);

	double WLepPt = WLepCand->pt();
	double DiTauCand1Pt = DiTauCand->daughter(0)->pt();
	double DiTauCand2Pt = DiTauCand->daughter(1)->pt();
	bool mostEnergetic = DiTauCand1Pt > DiTauCand2Pt ? true : false;

	double massWLeptonLeadTau = 0;
	if(mostEnergetic) massWLeptonLeadTau = (WLepCand->p4() + DiTauCand->daughter(0)->p4()).M();
	else massWLeptonLeadTau = (WLepCand->p4() + DiTauCand->daughter(1)->p4()).M();

	//std::cout<<"WLepPt: "<<WLepPt<<" DiTauCand1Pt: "<<DiTauCand1Pt<<" DiTauCand2Pt: "<<DiTauCand2Pt<<std::endl;

	double WLepPhi = WLepCand->phi();
	double DiTauCand1Phi = DiTauCand->daughter(0)->phi();
	double DiTauCand2Phi = DiTauCand->daughter(1)->phi();

	double phiTau1 = deltaPhi(DiTauCand1Phi,WLepPhi);
	double cosTau1 = cos(phiTau1);
	double phiTau2 = deltaPhi(DiTauCand2Phi,WLepPhi);
	double cosTau2 = cos(phiTau2);

        double scalarSumPt = (WLepCand->p4()).Et() + ((*pfmet)[0].p4()).Et();
        double vectorSumPt = (WLepCand->p4() + (*pfmet)[0].p4()).Pt() ;
        double Mt = TMath::Sqrt( scalarSumPt*scalarSumPt - vectorSumPt*vectorSumPt );

	//std::cout<<"cos1: "<<cosTau1<<" cos2: "<<cosTau2<<" Mt: "<<Mt<<std::endl;
	//std::cout<<"MET: "<<met<<std::endl;

	//if(!(cosTau1 < cosCut1_ && Mt < mtCut1_)) result1 = true;
	//if(!(cosTau2 < cosCut2_ && Mt < mtCut2_)) result2 = true;

	//if(!(Mt < mtCut1_)) result1 = true;
	//if(!(Mt < mtCut2_)) result2 = true;

	//if(!(fabs(massWLeptonLeadTau-91.1876) < 12.476 && met < 30)){ 
	//	result1 = true;
	//	result2 = true;
	//}

	if(Mt > mtCut1_){
		//std::cout<<"cos1: "<<cosTau1<<" cos2: "<<cosTau2<<" Mt: "<<Mt<<std::endl;
		//std::cout<<"cos1: "<<cosTau1<<" cos2: "<<cosTau2<<" Mt: "<<Mt<<std::endl;
		selectedFinalCand->push_back(*CompCand);
		result = true;
	}

   }

   iEvent.put(selectedFinalCand);
   //std::cout<<"result "<<result<<std::endl;
   if(!filter_) result = true;
   return result;

}

// ------------ method called once each job just before starting event loop  ------------
void 
ZTauTauVeto::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ZTauTauVeto::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
ZTauTauVeto::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
ZTauTauVeto::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
ZTauTauVeto::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
ZTauTauVeto::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ZTauTauVeto::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(ZTauTauVeto);
