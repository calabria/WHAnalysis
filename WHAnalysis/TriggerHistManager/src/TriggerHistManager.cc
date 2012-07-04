#include <map>
#include <string>

#include "TH1.h"
#include "TH2.h"

#include <TMath.h>
#include <cmath>

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/Common/interface/RefVector.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMapRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMapFwd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMap.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

#include "DataFormats/Math/interface/LorentzVector.h"


class TriggerHistManager : public edm::EDAnalyzer {

public:
  explicit TriggerHistManager(const edm::ParameterSet&);
  ~TriggerHistManager();
  
private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  typedef std::vector<std::string> vstring;
  
  // simple map to contain all histograms; 
  // histograms are booked in the beginJob() 
  // method

  std::map<std::string,TH1F*> hHLTresults_;
  edm::LumiReWeighting LumiWeights_;

  // input tags  
  edm::InputTag hltResultsSrc_;
  vstring hltPaths_;
  typedef std::vector<double> vdouble;
  vdouble MCDist_f_;
  vdouble TrueDist2011_f_;
  bool isMC_;

};


TriggerHistManager::TriggerHistManager(const edm::ParameterSet& iConfig):

  hHLTresults_(),
  hltResultsSrc_(iConfig.getParameter<edm::InputTag>("hltResultsSource")),
  hltPaths_(iConfig.getParameter<vstring>("hltPaths")),
  MCDist_f_(iConfig.getUntrackedParameter<vdouble>("MCDist")),
  TrueDist2011_f_(iConfig.getUntrackedParameter<vdouble>("TrueDist2011")),
  isMC_(iConfig.getUntrackedParameter<bool>("isMC"))
{
}

TriggerHistManager::~TriggerHistManager()
{
}

void
TriggerHistManager::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

/////////////////////////////////////////////////////////////

  double weight = 1;

  if(isMC_){

	  edm::Handle<std::vector< PileupSummaryInfo > >  PupInfo;
	  iEvent.getByLabel(edm::InputTag("addPileupInfo"), PupInfo);

	  std::vector<PileupSummaryInfo>::const_iterator PVI;

	  int npv = -1;
	  int nti = -1;
	  for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI) {

		  int BX = PVI->getBunchCrossing();

		  if(BX == 0) { 
		     	npv = PVI->getPU_NumInteractions();
		     	continue;
		   	}

	  nti = PVI->getTrueNumInteractions();
	  }

	  weight = LumiWeights_.weight( nti );

  }

/////////////////////////////////////////////////////////////

  double count = 1.;
  hHLTresults_["N_eventi"]->Fill( count );
  hHLTresults_["N_eventi_PU"]->Fill( count, weight );

	if ( hltResultsSrc_.label() != "" ) {
		edm::Handle<edm::TriggerResults> hltResults;
		iEvent.getByLabel(hltResultsSrc_, hltResults);

		const edm::TriggerNames& triggerNames = iEvent.triggerNames(*hltResults);

		//std::cout<<triggerNames.triggerName(1)<<std::endl;

		for ( vstring::const_iterator hltPath = hltPaths_.begin(); hltPath != hltPaths_.end(); ++hltPath ) {

			std::string goodPath;
			for(int i = 0; i < (int)triggerNames.size(); i++){
			
				std::string storedName = triggerNames.triggerName(i);
				size_t found = storedName.find(*hltPath);
				if(found != std::string::npos) goodPath = storedName;
				//std::cout<<storedName<<" "<<*hltPath<<" "<<found<<std::endl;
			}

			unsigned int index = triggerNames.triggerIndex(goodPath);

			//std::cout<<index<<" "<<goodPath<<std::endl;

			if ( index < triggerNames.size() ) {
				bool isTriggered = ( hltResults->accept(index) ) ? true : false;
				hHLTresults_[*hltPath]->Fill(isTriggered, weight);
				//std::cout<<isTriggered<<std::endl;
			} else {
				// HLT path not present in event
				hHLTresults_[*hltPath]->Fill(-1, weight);
				//std::cout<<" Undefined HLT path = " << (*hltPath) << " --> skipping !!";
				//continue;

				//std::cout << "Available trigger Paths:" << std::endl;
				for ( edm::TriggerNames::Strings::const_iterator triggerName = triggerNames.triggerNames().begin(); triggerName != triggerNames.triggerNames().end(); ++triggerName ) {
					unsigned int index = triggerNames.triggerIndex(*triggerName);
					if ( index < triggerNames.size() ) {
						std::string triggerDecision = ( hltResults->accept(index) ) ? "passed" : "failed";
						//std::cout << " triggerName = " << (*triggerName) << " " << triggerDecision << std::endl;
					}
				}


			}
		}
	}

}

void 
TriggerHistManager::beginJob()
{
  // register to the TFileService
  edm::Service<TFileService> fs;
  TH1::SetDefaultSumw2();

  for ( vstring::const_iterator hltPath = hltPaths_.begin();
	hltPath != hltPaths_.end(); ++hltPath ) {
    std::string histoName = std::string("Trigger").append(*hltPath);
    hHLTresults_[*hltPath] = fs->make<TH1F>(histoName.c_str(), histoName.c_str(), 3, -1.5, 1.5);
  }

  hHLTresults_["N_eventi"]=fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
  hHLTresults_["N_eventi_PU"]=fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);

/////////////////////////////////////////////////////////////

  if(isMC_){

	  std::vector< float > MCDist ;
	  std::vector< float > TrueDist2011;

	  int sizeMCDist_f_ = MCDist_f_.size();

	  for( int i=0; i<sizeMCDist_f_; ++i) {
	      TrueDist2011.push_back(TrueDist2011_f_[i]);
	      MCDist.push_back(MCDist_f_[i]);
	    }

	  LumiWeights_ = edm::LumiReWeighting(MCDist, TrueDist2011);

  }

/////////////////////////////////////////////////////////////
    
}

void 
TriggerHistManager::endJob() 
{
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TriggerHistManager);
