#include <vector>

#include "TROOT.h"
#include "TFile.h"
#include "TDirectory.h"
#include "TChain.h"
#include "TObject.h"
#include "TCanvas.h"
#include "TMath.h"
#include "TLegend.h"
#include "TGraph.h"
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TTree.h"
#include "TF1.h"
#include "TGraphAsymmErrors.h"
#include "TPaveText.h"
#include "TRandom3.h"
#include "TProfile.h"
#include "TDirectory.h"

namespace reco    { class Vertex; class Track; class GenParticle; class DeDxData; class MuonTimeExtra;}
namespace susybsm { class HSCParticle; class HSCPIsolation;}
namespace fwlite  { class ChainEvent;}
namespace trigger { class TriggerEvent;}
namespace edm     {class TriggerResults; class TriggerResultsByName; class InputTag; class LumiReWeighting;}
namespace reweight{class PoissonMeanShifter;}
namespace fwlite { class ChainEvent;}

#if !defined(__CINT__) && !defined(__MAKECINT__)
#include "DataFormats/FWLite/interface/Handle.h"
#include "DataFormats/FWLite/interface/Event.h"
#include "DataFormats/FWLite/interface/ChainEvent.h"
#include "DataFormats/Common/interface/MergeableCounter.h"
#include "DataFormats/FWLite/interface/LuminosityBlock.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "AnalysisDataFormats/SUSYBSMObjects/interface/HSCParticle.h"
#include "AnalysisDataFormats/SUSYBSMObjects/interface/HSCPIsolation.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtraMap.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METCollection.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

using namespace fwlite;
using namespace reco;
using namespace susybsm;
using namespace std;
using namespace edm;
using namespace trigger;
using namespace reweight;

#endif

void effSkim(std::string nome){

   	char line0[300];
   	std::string fileName;
	std:vector<std::string> vectorFileNames;

	ifstream fileor0(nome.c_str());

   	if (fileor0.is_open()){

		while (fileor0.getline(line0,300)){
         	std::stringstream iss;
         	iss<<line0;
         	iss>>fileName;
         	//std::cout<<fileName<<std::endl;
		vectorFileNames.push_back("/lustre/cms"+fileName);

      		}
   	}

   	fileor0.close();

   	unsigned long Total = 0;
   	fwlite::ChainEvent tree(vectorFileNames);

	for(int i=0; i<vectorFileNames.size(); i++){

        	std::cout<<vectorFileNames[i]<<std::endl;

      		TFile file(vectorFileNames[i].c_str() );
      		fwlite::LuminosityBlock ls( &file );
      		for(ls.toBegin(); !ls.atEnd(); ++ls){

         		fwlite::Handle<edm::MergeableCounter> nEventsTotalCounter;
         		nEventsTotalCounter.getByLabel(ls,"nEventsBefSkim");
         		if(!nEventsTotalCounter.isValid()){printf("Invalid nEventsTotalCounterH\n");continue;}
         		Total+= nEventsTotalCounter->value;

		}



	}



}
