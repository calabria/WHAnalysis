// -*- C++ -*-
//
// Package:    HistoSubtractor
// Class:      HistoSubtractor
// 
/**\class HistoSubtractor HistoSubtractor.cc WHAnalysis/HistoSubtractor/src/HistoSubtractor.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Wed Dec 12 21:36:05 CET 2012
// $Id$
//
//

#include "WHAnalysis/HistoSubtractor/interface/HistoSubtractor.h"

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
HistoSubtractor::HistoSubtractor(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

    path_ = iConfig.getUntrackedParameter<std::string>("path");
    mainSample_ = iConfig.getUntrackedParameter<std::string>("mainSample");
    samples_ = iConfig.getUntrackedParameter<vstring>("samples");
    labels_ = iConfig.getUntrackedParameter<vstring>("labels");
    outputFile_ = iConfig.getUntrackedParameter<std::string>("outputFile");

}


HistoSubtractor::~HistoSubtractor()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
HistoSubtractor::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace std;

  std::vector<std::string> dirStructure;
  std::vector<std::string> dirStructureRoot;
  std::vector<std::string> histoStructure;
  std::vector<std::string> histoNamesForSaving;
  std::vector<double> eventsAtBeginning;
  std::vector<int> histoType;
  std::vector<double> scaleFactors;

  dirStructure.clear();
  dirStructureRoot.clear();
  histoStructure.clear();

  std::string nameAndPath = path_ + samples_[0];
  TFile * fileIn = TFile::Open(nameAndPath.c_str());

  TFile * fileOut = new TFile(outputFile_.c_str(), "RECREATE");
  TIter next(fileIn->GetListOfKeys());
  TKey *key;
  while ((key=(TKey*)next())) {
	//std::cout<<"key: "<<key->GetName()<<" points to an object of class:"<<key->GetClassName()<<std::endl;
	std::string folder = key->GetName();
	//Include here all the folders to be skipped
	if (folder == "puDistribution") continue;
	dirStructure.push_back(folder);
        fileOut->cd();
	fileOut->mkdir(folder.c_str());
	//gDirectory->pwd();
        fileIn->cd();
        gDirectory->cd(folder.c_str());
	TIter next2(gDirectory->GetListOfKeys());
  	TKey *key2;
	while ((key2=(TKey*)next2())) {
		//std::cout<<"key: "<<key2->GetName()<<" points to an object of class:"<<key2->GetClassName()<<std::endl;
		TObject * obj = key2->ReadObj();
		std::string histoName = key2->GetName();
		std::string folderHisto = folder + "/" + histoName;
		std::string namesForSaving = histoName;
		//std::cout<<"folderHisto "<<folderHisto.c_str()<<std::endl;
		if(obj->IsA()->InheritsFrom("TH2")) histoType.push_back(1);
		else if(obj->IsA()->InheritsFrom("TH1")) histoType.push_back(0);
		histoStructure.push_back(folderHisto);
		histoNamesForSaving.push_back(namesForSaving);
	      	dirStructureRoot.push_back(folder);
	}
  }

  fileOut->Write();

  //std::cout<<"folder "<<dirStructure.size()<<std::endl;

  int sizeHistos = histoStructure.size();
  int sizeFiles = samples_.size();
  int numFolders = dirStructure.size();
  //std::cout<<"sizeHistos "<<sizeHistos<<std::endl;
  //std::cout<<"sizeFiles "<<sizeFiles<<std::endl;


   //// Stacked plots ////

   for(int k = 0; k < sizeHistos; k++){//Loop sugli istogrammi

	//std::cout<<histoType[k]<<std::endl;
	if(histoType[k] == 0){

  	   std::string nameAndPathMain = path_ + mainSample_;
	   TFile * fileInMain = TFile::Open(nameAndPathMain.c_str());
	   fileInMain->cd();

	   TH1F *histoMain = (TH1F*)gDirectory->Get(histoStructure[k].c_str());
	   std::string titleXaxis;

	   for(int i = 0; i < sizeFiles; i++){//Loop sui file

			   std::string nameAndPath;
			   nameAndPath = path_ + samples_[i];
		   	   std::cout<<"sample "<<nameAndPath<<std::endl;
			   TFile * fileIn = TFile::Open(nameAndPath.c_str());

			   fileIn->cd();
			   std::cout<<"histoName "<<histoStructure[k].c_str()<<std::endl;
			   TH1F *histoTMP = (TH1F*)gDirectory->Get(histoStructure[k].c_str());

			   titleXaxis = histoTMP->GetXaxis()->GetTitle();
			   histoMain->Add(histoTMP,-1);
			   fileIn->Close();

	   }

	   //std::cout<<"label "<<titlexAxis.c_str()<<std::endl;
	   fileOut->cd();
	   //std::cout<<"dir "<<dirStructure[k].c_str()<<std::endl;
	   fileOut->cd(dirStructureRoot[k].c_str());
	   TH1F * histoStack = (TH1F*) histoMain->Clone();
	   if(titleXaxis != "") histoStack->GetXaxis()->SetTitle(titleXaxis.c_str());

	   double nEntries = histoStack->GetEntries();
	   for(int i = 0; i < nEntries; i++){

		double binContent = histoStack->GetBinContent(i);
		if(binContent < 0) histoStack->SetBinContent(i,0);

	   }

	   histoStack->Write(histoNamesForSaving[k].c_str());

	   fileInMain->Close();


	}
   }

   fileOut->Close();

}


// ------------ method called once each job just before starting event loop  ------------
void 
HistoSubtractor::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HistoSubtractor::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
HistoSubtractor::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
HistoSubtractor::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
HistoSubtractor::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
HistoSubtractor::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HistoSubtractor::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HistoSubtractor);
