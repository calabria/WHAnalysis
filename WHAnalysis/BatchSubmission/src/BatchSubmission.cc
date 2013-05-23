// -*- C++ -*-
//
// Package:    BatchSubmission
// Class:      BatchSubmission
// 
/**\class BatchSubmission BatchSubmission.cc BatchSubmission/BatchSubmission/src/BatchSubmission.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Thu Jun 23 09:54:48 CEST 2011
// $Id$
//
//


#include "WHAnalysis/BatchSubmission/interface/BatchSubmission.h"

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
BatchSubmission::BatchSubmission(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

   finalState_ = iConfig.getUntrackedParameter<std::string>("finalState");
   fileCFG_ = iConfig.getUntrackedParameter<std::string>("fileCFG");
   fileCSH_ = iConfig.getUntrackedParameter<std::string>("fileCSH");
   sample_ = iConfig.getUntrackedParameter<std::string>("sample");

   pathCFG_ = iConfig.getUntrackedParameter<std::string>("pathCFG");
   savingPath_ = iConfig.getUntrackedParameter<std::string>("savingPath");
   txtFile_ = iConfig.getUntrackedParameter<std::string>("txtFile");

}


BatchSubmission::~BatchSubmission()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
BatchSubmission::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   using namespace std;

   std::ifstream ifin(txtFile_.c_str());
   std::vector<std::string> fileInput;

   if(ifin.is_open()){
    	std::string line;
   	while (ifin.good()){
      		ifin>>line;
      		std::cout<<" line = "<<line<<std::endl;
      		fileInput.push_back(line);
    	}
   }

   int sizeInput = fileInput.size();
   std::cout<<"size "<<sizeInput-1<<std::endl;
   int cont = 1;

   int upperLimit = (int)((sizeInput-1)/20)+1;

   for(int i = 1; i <= upperLimit; i++){ //Loop sui file di input

        //std::cout<<fileCFG_.c_str()<<std::endl;
   	std::ifstream fCFG(fileCFG_.c_str());
    	char line[500];
    	std::string lineContent;
       	std::stringstream ss;
       	ss<<cont;
       	std::string contS = ss.str();

	std::ofstream outputCFG;
	int choice = 0;
	std::string name = "./CFGFiles/" + finalState_ + "/" + sample_ + "/WMuNuHTauTauAnalyzer_" + sample_ + "_" + contS + "_cfg.py";
        //std::cout<<name<<std::endl;
	outputCFG.open(name.c_str());

	if(fCFG.is_open()){
    		while (fCFG.getline(line,500)){
	       		lineContent = std::string(line);
			//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;

	       		size_t foundInput, foundOutput;
	       		foundInput = lineContent.find("#__inputFile");
	       		foundOutput = lineContent.find("#__outpuFile");
			if(foundInput!=string::npos) choice = 1;
			else if(foundOutput!=string::npos) choice = 2;
			else choice = 3;

			int maxFor = i*20 - 1;
			int minFor = i*20 - 20;

	    		if(outputCFG.is_open()){
				switch(choice){
					case 1:
						for(int j = minFor; j <= maxFor; j++){
							if(j < sizeInput-1) {
								lineContent = "	'file:" + fileInput[j] + "',";
								//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;
								outputCFG<<lineContent<<"\n";
							}
						}
						break;
					case 2:
						lineContent = "	'" + savingPath_ + sample_ +"/histo_" + sample_ + "_" + contS + ".root'";
						//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;
						outputCFG<<lineContent<<"\n";
						break;
					case 3:
						//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;
						outputCFG<<lineContent<<"\n";
						break;
				}
		}


    	}

    }

    fCFG.close();
    outputCFG.close();
    cont++;
    
   }


   cont = 1;

    for(int i = 1; i <= upperLimit; i++){ //Loop sui file di input

	char line[500];
    	std::string lineContent;
   	std::ifstream fCSH(fileCSH_.c_str());
       	std::stringstream ss;
       	ss<<cont;
       	std::string contS = ss.str();

	std::ofstream outputCSH;
	int choice = 0;
	std::string name = "./CFGFiles/" + finalState_ + "/" + sample_ + "/batchJob_" + sample_ + "_" + contS + ".csh";
	outputCSH.open(name.c_str());

   	if(fCSH.is_open()){
    		while (fCSH.getline(line,500)){
	       		lineContent = std::string(line);
			//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;

	       		size_t foundPath, foundCFG, foundTmpPath, foundMK, foundRM;
	       		foundPath = lineContent.find("#__pathCFG");
	       		foundCFG = lineContent.find("#__nameCFG");
			foundTmpPath = lineContent.find("#__savingPath");
			foundMK = lineContent.find("mkdir");
			foundRM = lineContent.find("rm -r");
		
			if(foundPath!=string::npos) choice = 1;
			else if(foundCFG!=string::npos) choice = 2;
			else if(foundTmpPath!=string::npos && foundMK==string::npos && foundRM==string::npos) choice = 3;
			else if(foundTmpPath!=string::npos && foundMK!=string::npos) choice = 4;
			else if(foundTmpPath!=string::npos && foundRM!=string::npos) choice = 5;
			else choice = 6;

	    		if(outputCSH.is_open()){
				switch(choice){
					case 1:
						lineContent = "cd " + pathCFG_;
						//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;
						outputCSH<<lineContent<<"\n";
						break;
					case 2:
						lineContent = "cmsRun " + pathCFG_ + "CFGFiles/" + finalState_ + "/" + sample_ + "/" + "WMuNuHTauTauAnalyzer_" + sample_ + "_" + contS + "_cfg.py";
						//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;
						outputCSH<<lineContent<<"\n";
						break;
					case 3:
						lineContent = "cd " + savingPath_ + sample_;
						//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;
						outputCSH<<lineContent<<"\n";
						break;
					case 4:
						lineContent = "mkdir " + savingPath_ + sample_;
						//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;
						outputCSH<<lineContent<<"\n";
						break;
					case 5:
						lineContent = "rm -r " + savingPath_ + sample_;
						//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;
						outputCSH<<lineContent<<"\n";
						break;
					case 6:
						//std::cout<<"lineContent "<<lineContent.c_str()<<std::endl;
						outputCSH<<lineContent<<"\n";
						break;
				}
			}

    		}

    }

    fCSH.close();
    outputCSH.close();
    cont++;

   }


}


// ------------ method called once each job just before starting event loop  ------------
void 
BatchSubmission::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
BatchSubmission::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
BatchSubmission::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
BatchSubmission::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
BatchSubmission::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
BatchSubmission::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
BatchSubmission::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(BatchSubmission);
