// -*- C++ -*-
//
// Package:    GenFilter
// Class:      GenFilter
// 
/**\class GenFilter GenFilter.cc WHAnalysis/GenFilter/src/GenFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  
//         Created:  Tue Jul 12 11:05:25 CEST 2011
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"

#include <string>
#include <vector>

//
// class declaration
//

class GenFilter : public edm::EDFilter {
   public:
      explicit GenFilter(const edm::ParameterSet&);
      ~GenFilter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual bool beginRun(edm::Run&, edm::EventSetup const&);
      virtual bool endRun(edm::Run&, edm::EventSetup const&);
      virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      edm::InputTag inputTag_;
      //typedef std::vector<double> vdouble;
      //vdouble particles_;

      int process_;


      // ----------member data ---------------------------
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
GenFilter::GenFilter(const edm::ParameterSet& iConfig):
   inputTag_(iConfig.getUntrackedParameter<edm::InputTag>("genParticles")),
   //particles_(iConfig.getUntrackedParameter<vdouble>("particles"))
   process_(iConfig.getUntrackedParameter<int>("process"))
{
   //now do what ever initialization is needed

}


GenFilter::~GenFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//
//int cont = 0;
// ------------ method called on each new Event  ------------
bool
GenFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif

#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif

  //int sizeParticles = particles_.size();

  edm::Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByLabel(inputTag_, genParticles);

  /*int nMothers = 0;
  int mother1Higgs = 0;
  int mother2Higgs = 0;
  bool flagHiggs = false;
  int mother1 = 0;
  int mother2 = 0;
  std::vector<bool> idRes;*/
  bool result = false;
  int event_type = 0;

  if(genParticles.isValid()){

	for(reco::GenParticleCollection::const_iterator it = genParticles->begin(); it != genParticles->end(); ++it ){

		/*int id = it->pdgId();
		int status = it->status();
		nMothers = it->numberOfMothers();
		//if(id == 25 && status == 3 && nMothers != 2) std::cout<<"id "<<id<<" status "<<status<<" nMothers "<<nMothers<<std::endl;

		if(id == 25 && status == 3 && nMothers == 2){

			mother2Higgs = it->mother(nMothers-1)->pdgId();
			mother1Higgs = it->mother(0)->pdgId();
			flagHiggs = true;
			//std::cout<<"id "<<id<<" status "<<status<<" nMothers "<<nMothers<<" mother1 "<<mother1Higgs<<" mother2 "<<mother2Higgs<<" flag "<<flagHiggs<<std::endl;

		}

	}


	if(flagHiggs){

		for(int i = 0; i < sizeParticles; i++){

			for(reco::GenParticleCollection::const_iterator it2 = genParticles->begin(); it2 != genParticles->end(); ++it2 ){

				int id2 = it2->pdgId();
				int status2 = it2->status();
				int nMothers2 = it2->numberOfMothers();
				bool tmp1 = (id2 == particles_[i]) && (id2 != 25);
				bool tmp2 = (status2 == 3) && (nMothers2 == 2);
				//if(tmp2) std::cout<<"id "<<id2<<" status "<<status2<<" nMothers2 "<<nMothers2<<" particle "<<particles_[i]<<" choice "<<tmp1<<" "<<tmp2<<std::endl;

				if(tmp1 & tmp2){

					mother1 = it2->mother(0)->pdgId();
					mother2 = it2->mother(nMothers2-1)->pdgId();
					bool discr1 = (mother1Higgs == mother1);
					bool discr2 = (mother2Higgs == mother2);
					if(discr1 & discr2) idRes.push_back(true); 
					else idRes.push_back(false);
					//std::cout<<"id "<<id2<<" status "<<status2<<" nMothers "<<nMothers2<<" mother1 "<<mother1<<" mother2 "<<mother2<<" discr1 "<<discr1<<" discr2 "<<discr2<<std::endl;
					
				}

			}

		}*/


	int id = it->pdgId();
	int status = it->status();

	if(TMath::Abs(id) == 24 && status == 3 ){
		event_type = 1;
		break;
	}  // fine if GenParticle = W
	else if(id == 23 && status == 3 ){
		event_type = 2;
		break;
	}  // fine if GenParticle = Z
	else if(TMath::Abs(id) == 6 && status == 3 ){
		event_type = 3;
		break;
	}  // fine if GenParticle = t



	}

  }

  /*int sizeRes = idRes.size();
  bool res = true;
  if(sizeRes >= 1){
	  for(int j = 0; j < sizeRes; j++){

		//std::cout<<"Size "<<sizeRes<<" idRes "<<idRes[j]<<std::endl;
		res &= idRes[j];

	  }
  }else res = false;
  
  //std::cout<<"Res "<<res<<std::endl;
  if(res == 1) result = true;
  else result = false;
  return result;*/

  if(process_ == event_type) result = true;
  return result;


}

// ------------ method called once each job just before starting event loop  ------------
void 
GenFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
GenFilter::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
GenFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
GenFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
GenFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(GenFilter);
