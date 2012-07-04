// -*- C++ -*-
//
// Package:    AddEleMVA
// Class:      AddEleMVA
// 
/**\class AddEleMVA AddEleMVA.cc WHAnalysis/AddEleMVA/src/AddEleMVA.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Wed Jan 18 14:08:25 CET 2012
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"

#include "HiggsAnalysis/HiggsToWW2Leptons/interface/ElectronIDMVA.h"

#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/Scalers/interface/DcsStatus.h"
#include "RecoEgamma/EgammaTools/interface/ConversionFinder.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHit.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"

using namespace edm;
using namespace std;
using namespace reco;

//
// class declaration
//

class AddEleMVA : public edm::EDProducer {
   public:
      explicit AddEleMVA(const edm::ParameterSet&);
      ~AddEleMVA();

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

      edm::InputTag electronTag_;
      bool doMVA_;
      ElectronIDMVA* fMVA_;
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
AddEleMVA::AddEleMVA(const edm::ParameterSet& iConfig)
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

  electronTag_ = iConfig.getParameter<edm::InputTag>("electronTag");
  doMVA_       = iConfig.getParameter<bool>("doMVA");

  edm::FileInPath inputFileName0 = iConfig.getParameter<edm::FileInPath>("inputFileName0");
  edm::FileInPath inputFileName1 = iConfig.getParameter<edm::FileInPath>("inputFileName1");
  edm::FileInPath inputFileName2 = iConfig.getParameter<edm::FileInPath>("inputFileName2");
  edm::FileInPath inputFileName3 = iConfig.getParameter<edm::FileInPath>("inputFileName3");
  edm::FileInPath inputFileName4 = iConfig.getParameter<edm::FileInPath>("inputFileName4");
  edm::FileInPath inputFileName5 = iConfig.getParameter<edm::FileInPath>("inputFileName5");

  if(doMVA_){
    fMVA_ = new ElectronIDMVA();
    fMVA_->Initialize("BDTG method",
		      inputFileName0.fullPath().data(),
		      inputFileName1.fullPath().data(),
		      inputFileName2.fullPath().data(),
		      inputFileName3.fullPath().data(),
		      inputFileName4.fullPath().data(),
		      inputFileName5.fullPath().data(),                
		      ElectronIDMVA::kNoIPInfo);
  }

  produces<pat::ElectronCollection>("");
  
}


AddEleMVA::~AddEleMVA()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

  if(doMVA_) delete fMVA_;

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
AddEleMVA::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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

  edm::Handle<pat::ElectronCollection> electronsHandle;
  iEvent.getByLabel(electronTag_,electronsHandle);
  const pat::ElectronCollection* electrons = electronsHandle.product();

  std::auto_ptr< pat::ElectronCollection > electronsUserEmbeddedColl( new pat::ElectronCollection() ) ;

  for(unsigned int i = 0; i < electrons->size(); i++){

    pat::Electron aElectron( (*electrons)[i] );
    const reco::GsfElectron* aGsf = static_cast<reco::GsfElectron*>(&aElectron); 

    EcalClusterLazyTools lazyTools(iEvent,iSetup,
				   edm::InputTag("reducedEcalRecHitsEB"),
				   edm::InputTag("reducedEcalRecHitsEE"));
    float mva = -99;
    if(doMVA_)
      mva = fMVA_->MVAValue(aGsf, lazyTools);
    aElectron.addUserFloat("mvaCorr",mva);

    electronsUserEmbeddedColl->push_back(aElectron);

  }

  iEvent.put( electronsUserEmbeddedColl );
  return;
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
AddEleMVA::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
AddEleMVA::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
AddEleMVA::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
AddEleMVA::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
AddEleMVA::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
AddEleMVA::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
AddEleMVA::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(AddEleMVA);
