// -*- C++ -*-
//
// Package:    AddUserTauLifeTimeVariables
// Class:      AddUserTauLifeTimeVariables
// 
/**\class AddUserTauLifeTimeVariables AddUserTauLifeTimeVariables.cc WHAnalysis/AddUserTauLifeTimeVariables/src/AddUserTauLifeTimeVariables.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Thu Dec 20 15:31:53 CET 2012
// $Id$
//
//


// system include files
#include <memory>
#include <TMath.h>
#include <stdlib.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/TauReco/interface/PFTauDecayMode.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "RecoVertex/AdaptiveVertexFit/interface/AdaptiveVertexFitter.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"


//
// class declaration
//

class AddUserTauLifeTimeVariables : public edm::EDProducer {
   public:
      explicit AddUserTauLifeTimeVariables(const edm::ParameterSet&);
      ~AddUserTauLifeTimeVariables();

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

      edm::InputTag tauSrc_;
      edm::InputTag muonSrc_;
      edm::InputTag vertexSrc_;
      edm::InputTag srcBeamSpot_;

      typedef std::vector<double> vdouble;
      VertexState beamSpotState_;
      bool beamSpotIsValid_;

      const TransientTrackBuilder* trackBuilder_;

};

template<typename T>
bool isValidRef(const edm::Ref<T>& ref)
{
  return ( (ref.isAvailable() || ref.isTransient()) && ref.isNonnull() );  
}

//-------------------------------------------------------------------------------
 // auxiliary functions to compare two Tracks 


bool tracksMatchByDeltaR(const reco::Track* trk1, const reco::Track* trk2)
{
  if ( reco::deltaR(*trk1, *trk2) < 1.e-2 && trk1->charge() == trk2->charge() ) return true;
  else return false;
}

// auxiliary function to exclude tracks associated to tau lepton decay "leg"
// from primary event vertex refit
typedef std::map<const reco::Track*, reco::TransientTrack> TransientTrackMap;
void removeTracks(TransientTrackMap& pvTracks_toRefit, const std::vector<reco::Track*> svTracks)
{
  for ( std::vector<reco::Track*>::const_iterator svTrack = svTracks.begin(); svTrack != svTracks.end(); ++svTrack ) {
    
    //--- remove track from list of tracks included in primary event vertex refit
    //    if track matches by reference or in eta-phi
    //    any of the tracks associated to tau lepton decay "leg"
    for ( TransientTrackMap::iterator pvTrack = pvTracks_toRefit.begin(); pvTrack != pvTracks_toRefit.end(); ++pvTrack ) {
      if ( tracksMatchByDeltaR(pvTrack->first, *svTrack) ) {
	pvTracks_toRefit.erase(pvTrack);
	break;
      }
    }
  }
}
//-------------------------------------------------------------------------------


//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
AddUserTauLifeTimeVariables::AddUserTauLifeTimeVariables(const edm::ParameterSet& iConfig):
  tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc")),
  muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
  vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc")),
  srcBeamSpot_(iConfig.getUntrackedParameter<edm::InputTag>("srcBeamSpot"))
{

  produces<pat::TauCollection>("");  

}


AddUserTauLifeTimeVariables::~AddUserTauLifeTimeVariables()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
AddUserTauLifeTimeVariables::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   edm::Handle<edm::View<pat::Tau> > taus;
   iEvent.getByLabel(tauSrc_,taus);

   std::auto_ptr< pat::TauCollection > tausUserEmbeddedColl( new pat::TauCollection() ) ;

   edm::Handle<edm::View<pat::Muon> > muons;
   iEvent.getByLabel(muonSrc_,muons);

   edm::Handle<reco::VertexCollection> pvHandle;
   iEvent.getByLabel(vertexSrc_, pvHandle);

   edm::Handle<reco::BeamSpot> beamSpotHandle;
   iEvent.getByLabel(srcBeamSpot_, beamSpotHandle);
   const reco::BeamSpot*  beamSpot_ = beamSpotHandle.product();
   
   if ( beamSpot_ ) {
     beamSpotState_ = VertexState(*beamSpot_);    
     beamSpotIsValid_ = (beamSpotState_.error().cxx() > 0. &&
			 beamSpotState_.error().cyy() > 0. &&
			 beamSpotState_.error().czz() > 0.);
   } else {
     edm::LogError ("NSVfitEventVertexRefitter::beginEvent")
       << " Failed to access BeamSpot !!";
     beamSpotIsValid_ = false;
   }
   
   const TransientTrackBuilder* trackBuilder_;
   edm::ESHandle<TransientTrackBuilder> trackBuilderHandle;
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", trackBuilderHandle);
   trackBuilder_ = trackBuilderHandle.product();

   std::vector<reco::TransientTrack> tracks;


////////////////////////////////////////////////////////////////////////////////////////////////////////////// Loop Tau

  for(unsigned int i = 0; i < taus->size(); i++){

   pat::Tau patTau( (*taus)[i] );

   //if (patTau.pfJetRef().isAvailable() && patTau.pfJetRef().isNonnull()) std::cout<<"pfJet: "<<patTau.pfJetRef()->pt()<<std::endl;
   //if (patTau.pfJetRef().isAvailable() && patTau.pfJetRef().isNonnull()) std::cout<<"pfJet: "<<patTau.pfJetRef()->phi()<<std::endl;
   //if (patTau.pfJetRef().isAvailable() && patTau.pfJetRef().isNonnull()) std::cout<<"pfJet: "<<patTau.pfJetRef()->eta()<<std::endl;

   const reco::PFCandidateRefVector& signalPFChargedHadrCandidates = patTau.signalPFChargedHadrCands();

   float SecVtx_x = 0, SecVtx_y = 0, SecVtx_z = 0;
   float PV_x = 0, PV_y = 0, PV_z = 0;
   bool isSV = false;

   int isOneProng = 9999;
   int isThreeProng = 9999;
   float IPxyLead = 9999;
   float sigma_IPxyLead = 9999;
   float IPxySigLead = 9999;
   float IPzLead = 9999;

////////////////////////////////////////////////////////////////////////////////////////////////////////////// Zona IP

   if((patTau.signalPFGammaCands().size() > 0 || patTau.signalPFGammaCands().size() == 0) && patTau.signalPFChargedHadrCands().size() == 1){

 	isOneProng = 1;
	isThreeProng = 0;

   }
   else if(signalPFChargedHadrCandidates.size() == 3){

 	isOneProng = 0;
	isThreeProng = 1;

   }

   patTau.addUserInt("isOneProng", isOneProng);
   patTau.addUserInt("isThreeProng", isThreeProng);

   if( isValidRef(patTau.leadPFChargedHadrCand()) && isValidRef(patTau.leadPFChargedHadrCand()->trackRef()) ) {

	if ( vertexSrc_.label() != "" ) {

	  	edm::Handle<std::vector<reco::Vertex> > recoVertices;
	  	iEvent.getByLabel(vertexSrc_, recoVertices);

	  	if ( recoVertices->size() >= 1 ) {

	    		const reco::Vertex& thePrimaryEventVertex = (*recoVertices->begin());
	    		//std::cout<<"impact parameter "<<patTau.leadPFChargedHadrCand()->trackRef()->dxy(thePrimaryEventVertex.position())<<"  err    "<<patTau.leadPFChargedHadrCand()->trackRef()->d0Error()<<std::endl;
	     		IPxyLead = patTau.leadPFChargedHadrCand()->trackRef()->dxy(thePrimaryEventVertex.position());
	    		sigma_IPxyLead = patTau.leadPFChargedHadrCand()->trackRef()->d0Error();
	    		IPxySigLead = IPxyLead/sigma_IPxyLead;

	    		//std::cout<<"  **db/sigmadB********    "<<patTau.leadPFChargedHadrCand()->trackRef()->dxy(thePrimaryEventVertex.position())/(patTau.leadPFChargedHadrCand()->trackRef()->d0Error())<<std::endl;
	    		IPzLead = patTau.leadPFChargedHadrCand()->trackRef()->dz(thePrimaryEventVertex.position());

	  	}
	}
   }

   patTau.addUserFloat("IPxyLead", IPxyLead);
   patTau.addUserFloat("sigma_IPxyLead", sigma_IPxyLead);
   patTau.addUserFloat("IPxySigLead", IPxySigLead);
   patTau.addUserFloat("IPzLead", IPzLead);
   
////////////////////////////////////////////////////////////////////////////////////////////////////////////// Zona SV

   reco::TransientTrack transtrack0; 
   reco::TransientTrack transtrack1; 
   reco::TransientTrack transtrack2; 

   float distSV_PVRef = -999;
    
   if(signalPFChargedHadrCandidates.size() == 3){

	  if(patTau.signalPFChargedHadrCands()[0]->trackRef().isNonnull()) transtrack0 = trackBuilderHandle->build(patTau.signalPFChargedHadrCands()[0]->trackRef());
	  if(patTau.signalPFChargedHadrCands()[1]->trackRef().isNonnull()) transtrack1 = trackBuilderHandle->build(patTau.signalPFChargedHadrCands()[1]->trackRef());
	  if(patTau.signalPFChargedHadrCands()[2]->trackRef().isNonnull()) transtrack2 = trackBuilderHandle->build(patTau.signalPFChargedHadrCands()[2]->trackRef());
	  if (transtrack0.isValid()) tracks.push_back(transtrack0);
	  if (transtrack1.isValid()) tracks.push_back(transtrack1);
	  if (transtrack2.isValid()) tracks.push_back(transtrack2);
	  
	  float vtxChi2 = -1;
	  float vtxNDOF = -1;

	  if (tracks.size() > 1) {

	    	KalmanVertexFitter kvf(true);
	    	TransientVertex vtx = kvf.vertex(tracks);
	    	vtxChi2 = vtx.totalChiSquared();
	    	vtxNDOF = vtx.degreesOfFreedom();
	    
	    	//std::cout<<" vtx chi2="<<vtxChi2<<std::endl;
	    	//std::cout<<" vtx NDOF="<<vtxNDOF<<std::endl;
	    	//std::cout<<" vtx pos="<<vtx.position()<<std::endl;

	    	GlobalPoint SecVtx = vtx.position();
	    	SecVtx_x =  SecVtx.x();
	    	SecVtx_y =  SecVtx.y();
	    	SecVtx_z =  SecVtx.z();
	 
	    ///////////////////////////metto le tracce del 3 prong + la traccia del mu in un vettore//////////////////////////////////////////////////

	    std::vector<reco::Track*> svTracks;
	    bool isValidTauTrack = false;
	    if((patTau.signalPFChargedHadrCands()[0]->trackRef().isNonnull()) && (patTau.signalPFChargedHadrCands()[1]->trackRef().isNonnull()) && (patTau.signalPFChargedHadrCands()[2]->trackRef().isNonnull()) ) isValidTauTrack=true;

	    if(isValidTauTrack){

	    	reco::Track trk_tmp0 = *(patTau.signalPFChargedHadrCands()[0]->trackRef());
	    	reco::Track trk_tmp1 = *(patTau.signalPFChargedHadrCands()[1]->trackRef());
	    	reco::Track trk_tmp2 = *(patTau.signalPFChargedHadrCands()[2]->trackRef());
	    	reco::Track* ftrk_tmp0 = &trk_tmp0; 
	    	reco::Track* ftrk_tmp1 = &trk_tmp1; 
	    	reco::Track* ftrk_tmp2 = &trk_tmp2; 
	    	svTracks.push_back(ftrk_tmp0);
	    	svTracks.push_back(ftrk_tmp1);
	    	svTracks.push_back(ftrk_tmp2);
	    
	    	for(edm::View<pat::Muon>::const_iterator patMu=muons->begin(); patMu!=muons->end(); ++patMu){

	      		bool isValidMuTrack=false;
	      		if(patMu->track().isNonnull()){isValidMuTrack=true;}
			if(isValidMuTrack){

		   		reco::Track trk_tmp_mu = *(patMu->track());
		   		reco::Track* ftrk_tmp_mu = &trk_tmp_mu; 
		   		svTracks.push_back(ftrk_tmp_mu);

			}
		 
           	}
	    
	    //std::cout<<" puntatore  traccia "<<ftrk_tmp0<<"  =  "<<&trk_tmp0<<"  pt   "<<(*svTracks[0]).pt()<<std::endl;

	    int idx=0;
	     for ( std::vector<reco::Track*>::const_iterator svTrack = svTracks.begin();  svTrack != svTracks.end(); ++svTrack ) {
	      std::cout << "Track #" << idx << ": Pt = " << (*svTrack)->pt() << "," 
			<< " eta = " << (*svTrack)->eta() << ", phi = " << (*svTrack)->phi() 
			<< " (charge = " << (*svTrack)->charge() << ", chi2 = " << (*svTrack)->normalizedChi2() << ")" << std::endl;
	      	      ++idx;

	    }
	    
	    ///////////////////////////////////////////metto le tracce del PV in una mappa/////////////////////////////////////////////////////////////

	    std::vector<reco::TransientTrack> pvTracks_original;
	    TransientTrackMap pvTrackMap_refit;
	    const reco::Vertex* eventVertex;

	    for ( reco::Vertex::trackRef_iterator pvTrack = (*pvHandle)[0].tracks_begin(); pvTrack != (*pvHandle)[0].tracks_end(); ++pvTrack ) {

	      	reco::TransientTrack pvTrack_transient = trackBuilder_->build(pvTrack->get());
	      	pvTracks_original.push_back(pvTrack_transient);
	      	pvTrackMap_refit.insert(std::make_pair(pvTrack->get(), pvTrack_transient)); //a questo punto nella mappa entrambi gli elementi sono le tracce associate al PV

	    }

	    isSV = true;
	    removeTracks(pvTrackMap_refit, svTracks); //rimuovo dalla mappa gli elementi in cui le tracce associate al PV coincidono con quelle associate al SV

	    ////////////////definisco un vettore con le tracce del PV da cui ho tolto le tracce del SV///////////////////////////////////////////

	    std::vector<reco::TransientTrack> pvTracks_refit;
	    for ( TransientTrackMap::iterator pvTrack = pvTrackMap_refit.begin();  pvTrack != pvTrackMap_refit.end(); ++pvTrack ) {

	      	pvTracks_refit.push_back(pvTrack->second);

	    }

	    //////////////////////////////////////////Refit del PV//////////////////////////////////////////////////////////////////////////////

	    AdaptiveVertexFitter adf;
	    TransientVertex pvVtx;

	    if ( pvTracks_refit.size() >= 2) {
	      
	      if (  beamSpotIsValid_ )  pvVtx = adf.vertex(pvTracks_refit, *beamSpot_);
	      else pvVtx = adf.vertex(pvTracks_refit);

	    }
	    else{

	      if ( beamSpotIsValid_ ) pvVtx = adf.vertex(pvTracks_original, *beamSpot_);
	      else pvVtx = adf.vertex(pvTracks_original);

	    }

	    GlobalPoint PV =  pvVtx.position();
	    PV_x = PV.x();
	    PV_y = PV.y();
	    PV_z = PV.z();
	    std::cout<<" PV_X="<< PV_x<<std::endl; 
	    std::cout<<" PV_Y="<< PV_y<<std::endl; 
	    std::cout<<" PV_Z="<< PV_z<<std::endl; 

	    distSV_PVRef = TMath::Sqrt((PV_x-SecVtx_x)*(PV_x-SecVtx_x) + (PV_y-SecVtx_y)*(PV_y-SecVtx_y) + (PV_z-SecVtx_z)*(PV_z-SecVtx_z)); 
	    std::cout<<"  ***dist pvRefit-sv***  "<<distSV_PVRef<<std::endl;

	    }//is valid tau track 
	  }
	}//is 3 prong

	patTau.addUserFloat("distSV_PVRef", distSV_PVRef);
	
	
	if(isSV){

	  	//std::cout<<" sec vtx posX="<<SecVtx_x<<std::endl;
	  	if (!pvHandle->empty()) {

	    		const reco::Vertex &pv = (*pvHandle)[0];
	    		float pvx = pv.x();
	    		float pvy = pv.y();
	    		float pvz = pv.z();
	    		//std::cout<<" PV_X="<<pv.x()<<std::endl; 
	    		// std::cout<<" PV_Y="<<pv.y()<<std::endl; 
	    		//std::cout<<" PV_Z="<<pv.z()<<std::endl; 
	    		float distPS = TMath::Sqrt((pvx-SecVtx_x)*(pvx-SecVtx_x) + (pvy-SecVtx_y)*(pvy-SecVtx_y) + (pvz-SecVtx_z)*(pvz-SecVtx_z));
	    		//std::cout<<"  ***dist pv-sv***  "<< distPS<<std::endl;

	  	}
	}

    tausUserEmbeddedColl->push_back(patTau);

  }//Qui finisce il loop sui tau

  iEvent.put( tausUserEmbeddedColl );
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
AddUserTauLifeTimeVariables::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
AddUserTauLifeTimeVariables::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
AddUserTauLifeTimeVariables::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
AddUserTauLifeTimeVariables::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
AddUserTauLifeTimeVariables::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
AddUserTauLifeTimeVariables::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
AddUserTauLifeTimeVariables::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(AddUserTauLifeTimeVariables);
