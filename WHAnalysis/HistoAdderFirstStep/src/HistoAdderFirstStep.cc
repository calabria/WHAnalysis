// -*- C++ -*-
//
// Package:    HistoAdderFirstStep
// Class:      HistoAdderFirstStep
// 
/**\class HistoAdderFirstStep HistoAdderFirstStep.cc WHAnalysis/HistoAdderFirstStep/src/HistoAdderFirstStep.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Thu Oct 20 18:05:48 CEST 2011
// $Id$
//
//

#include "WHAnalysis/HistoAdderFirstStep/interface/HistoAdderFirstStep.h"

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
HistoAdderFirstStep::HistoAdderFirstStep(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

    crossSections_ = iConfig.getUntrackedParameter<vdouble>("crossSections");
    skimEff_ = iConfig.getUntrackedParameter<vdouble>("skimEff");
    path_ = iConfig.getUntrackedParameter<std::string>("path");
    samples_ = iConfig.getUntrackedParameter<vstring>("samples");
    labels_ = iConfig.getUntrackedParameter<vstring>("labels");
    outputFile_ = iConfig.getUntrackedParameter<std::string>("outputFile");
    intLumi_ = iConfig.getUntrackedParameter<double>("intLumi");
    eventsIn_ = iConfig.getUntrackedParameter<std::string>("eventsIn");
    txtFile_ = iConfig.getUntrackedParameter<std::string>("txtFile");

}


HistoAdderFirstStep::~HistoAdderFirstStep()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
HistoAdderFirstStep::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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
  bool flag = true;

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

  //// This is to calculate scale factors

   for(int i = 0; i < sizeFiles; i++){

	std::string nameAndPath;
	nameAndPath = path_ + samples_[i];
	//std::cout<<"sample "<<nameAndPath<<std::endl;
	TFile * fileIn = TFile::Open(nameAndPath.c_str());
	TH1F *histoTMP = (TH1F*)gDirectory->Get(eventsIn_.c_str());
	double events = histoTMP->GetBinContent(2);
	//std::cout<<"events at beginning "<<events<<std::endl;
	eventsAtBeginning.push_back(events);
	fileIn->Close();

   }

   //// Stacked plots ////

   for(int k = 0; k < sizeHistos; k++){//Loop sugli istogrammi

	//std::cout<<histoType[k]<<std::endl;
	if(histoType[k] == 0){

   	   THStack * hs = new THStack(histoStructure[k].c_str(),histoStructure[k].c_str());
	   std::string titleXaxis;

	   for(int i = 0; i < sizeFiles; i++){//Loop sui file

			   std::string nameAndPath;
			   nameAndPath = path_ + samples_[i];
		   	   std::cout<<"sample "<<nameAndPath<<std::endl;
			   TFile * fileIn = TFile::Open(nameAndPath.c_str());
			   fileIn->cd();
			   std::cout<<"histoName "<<histoStructure[k].c_str()<<std::endl;
			   TH1F *histoTMP = (TH1F*)gDirectory->Get(histoStructure[k].c_str());
			   //double nEntries = histoTMP->GetEntries();
			   double Li = 1;
			   if(crossSections_[i]) Li = eventsAtBeginning[i] / ( crossSections_[i] * skimEff_[i] );
			   //std::cout<<"Li "<<Li<<std::endl;
			   double scaleFactor = 1;
			   if(Li) scaleFactor = intLumi_ / Li;
			   if(flag) scaleFactors.push_back(scaleFactor);
			   histoTMP->Scale(scaleFactor);

			   ///////// For Factorization /////////
			   //if(labels_[i] == "DYToTauTau") histoTMP->Scale(scaleFactor*0.02725);
			   //else if(labels_[i] == "DYToTauTau_LOW_MASS") histoTMP->Scale(scaleFactor*0.02455);

			   //if (labels_[i] == "QCD_20-30_EM") histoTMP->Scale(scaleFactor*0.2248);
			   //else if (labels_[i] == "QCD_30-80_EM") histoTMP->Scale(scaleFactor*0.04933);
			   //else if (labels_[i] == "QCD_80-170_EM") histoTMP->Scale(scaleFactor*0.01869);
			   //else if (labels_[i] == "QCD_Mu_20") histoTMP->Scale(scaleFactor*0.02922);

			   //else histoTMP->Scale(scaleFactor);
			   ////////////////////////////////////

			   titleXaxis = histoTMP->GetXaxis()->GetTitle();
			   hs->Add(histoTMP);
			   fileIn->Close();

	   }
	   flag = false;

	   //std::cout<<"label "<<titlexAxis.c_str()<<std::endl;
	   fileOut->cd();
	   //std::cout<<"dir "<<dirStructure[k].c_str()<<std::endl;
	   fileOut->cd(dirStructureRoot[k].c_str());
	   TH1F * histoStack = (TH1F*)(hs->GetStack()->Last())->Clone();
	   if(titleXaxis != "") histoStack->GetXaxis()->SetTitle(titleXaxis.c_str());
	   histoStack->Write(histoNamesForSaving[k].c_str());

	   delete hs;

	}
   }

   fileOut->Close();

   std::ofstream outputTXT;
   outputTXT.open(txtFile_.c_str());

   if(outputTXT.is_open()){

	  //// Final table No Scale Factor ////

	  outputTXT<<"\n"<<setfill('-')<<setw(100)<<"-"<<std::endl;
	  outputTXT<<"Final table (No scale factor)"<<std::endl;
	  outputTXT<<setfill('-')<<setw(100)<<"-"<<std::endl;

	  outputTXT<<"\n ";
	  outputTXT<<"Cut ";
	  for(int i = 0; i < sizeFiles; i++){

		outputTXT<<labels_[i]<<" Err. ";

	  }
  	  outputTXT<<" "<<std::endl;

	  for(int j = 0; j < numFolders; j++){

		std::string name = dirStructure[j] + "/N_eventi_PU";
		//std::cout<<"name "<<name.c_str()<<std::endl;
		outputTXT<<"|"<<dirStructure[j].c_str()<<"|";

	  	for(int i = 0; i < sizeFiles; i++){

			std::string nameAndPath;
			nameAndPath = path_ + samples_[i];
			//std::cout<<"sample "<<nameAndPath<<std::endl;
			TFile * fileIn = TFile::Open(nameAndPath.c_str());
			fileIn->cd();
			TH1F *histoTMP = (TH1F*)gDirectory->Get(name.c_str());
			double numEvents = histoTMP->GetBinContent(2);
			//std::cout<<"dirStructure "<<dirStructure[j].c_str()<<"events "<<numEvents<<std::endl;
			double radqEvt = TMath::Sqrt(numEvents);
			//std::cout<<" "<<fixed<<setprecision(3)<<numEvents*scaleFactor<<" "<<fixed<<setprecision(3)<<scaleFactor*radqEvt;
			outputTXT<<" "<<fixed<<setprecision(3)<<numEvents<<" "<<fixed<<setprecision(3)<<radqEvt;
			fileIn->Close();
		}

		outputTXT<<" "<<std::endl;

	  }

	  //// Final table with Scale Factor ////

	  outputTXT<<"\n"<<setfill('-')<<setw(100)<<"-"<<std::endl;
	  outputTXT<<"Final table (Scale factor)"<<std::endl;
	  outputTXT<<setfill('-')<<setw(100)<<"-"<<std::endl;

	  outputTXT<<"\n ";
	  outputTXT<<"Cut ";
	  for(int i = 0; i < sizeFiles; i++){

		outputTXT<<labels_[i]<<" Err. ";

	  }
  	  outputTXT<<" "<<std::endl;

	  for(int j = 0; j < numFolders; j++){

		std::string name = dirStructure[j] + "/N_eventi_PU";
		//std::cout<<"name "<<name.c_str()<<std::endl;
		outputTXT<<"|"<<dirStructure[j].c_str()<<"|";

	  	for(int i = 0; i < sizeFiles; i++){

			std::string nameAndPath;
			nameAndPath = path_ + samples_[i];
			//std::cout<<"sample "<<nameAndPath<<std::endl;
			TFile * fileIn = TFile::Open(nameAndPath.c_str());
			fileIn->cd();
			//double Li = eventsAtBeginning[i] / (crossSections_[i] * filterEff_[i] * skimEff_[i]);
			double Li = eventsAtBeginning[i] / ( crossSections_[i] * skimEff_[i] );
			double scaleFactor = intLumi_ / Li;
			TH1F *histoTMP = (TH1F*)gDirectory->Get(name.c_str());
			double numEvents = histoTMP->GetBinContent(2);
			//std::cout<<"dirStructure "<<dirStructure[j].c_str()<<"events "<<numEvents<<std::endl;
			double radqEvt = TMath::Sqrt(numEvents);
			outputTXT<<" "<<fixed<<setprecision(6)<<numEvents*scaleFactor<<" "<<fixed<<setprecision(6)<<scaleFactor*radqEvt;
			fileIn->Close();
		}

		outputTXT<<" "<<std::endl;

	  }

	  //// Efficienze assolute ////

	  outputTXT<<"\n"<<setfill('-')<<setw(100)<<"-"<<std::endl;
	  outputTXT<<"Absolute efficiencies"<<std::endl;
	  outputTXT<<setfill('-')<<setw(100)<<"-"<<std::endl;

	  //TH1F * effPlot = new TH1F("","",numFolders,0,numFolders);

	  outputTXT<<"\n ";
	  outputTXT<<"Cut ";
	  for(int i = 0; i < sizeFiles; i++){

		outputTXT<<labels_[i]<<" Err. ";

	  }
  	  outputTXT<<" "<<std::endl;

	  for(int j = 0; j < numFolders; j++){

		//effPlot->GetXaxis()->SetBinLabel(j, dirStructure[j].c_str());

		std::string name = dirStructure[j] + "/N_eventi_PU";
		//std::cout<<"name "<<name.c_str()<<std::endl;
		outputTXT<<"|"<<dirStructure[j].c_str()<<"|";

	  	for(int i = 0; i < sizeFiles; i++){

			std::string nameAndPath;
			nameAndPath = path_ + samples_[i];
			//std::cout<<"sample "<<nameAndPath<<std::endl;
			TFile * fileIn = TFile::Open(nameAndPath.c_str());
			fileIn->cd();
			TH1F *histoTMP = (TH1F*)gDirectory->Get(name.c_str());
			TH1F *histoTMPEvt = (TH1F*)gDirectory->Get("VertexHistosBeforeMCFilter/N_eventi_PU");
			double numEvents = histoTMP->GetBinContent(2);
			double eventsAtBeginning = histoTMPEvt->GetBinContent(2);
			//std::cout<<"dirStructure "<<dirStructure[j].c_str()<<"events "<<numEvents<<std::endl;
			double absEff = 0;
			double errEff = 0;
			if(eventsAtBeginning){
				absEff = numEvents/eventsAtBeginning;
				errEff = TMath::Sqrt(numEvents + absEff*absEff*eventsAtBeginning)/eventsAtBeginning;}
			outputTXT<<" "<<fixed<<setprecision(10)<<absEff<<" "<<fixed<<setprecision(10)<<errEff;
			fileIn->Close();
		}

		outputTXT<<" "<<std::endl;

	  }

	  //// Efficienze relative ////

	  std::vector<double> tmpEvt;

	  outputTXT<<"\n"<<setfill('-')<<setw(100)<<"-"<<std::endl;
	  outputTXT<<"Relative efficiencies"<<std::endl;
	  outputTXT<<setfill('-')<<setw(100)<<"-"<<std::endl;

	  outputTXT<<"\n ";
	  outputTXT<<"Cut ";
	  for(int i = 0; i < sizeFiles; i++){

		outputTXT<<labels_[i]<<" Err. ";

	  }
  	  outputTXT<<" "<<std::endl;

	  for(int j = 0; j < numFolders; j++){

		std::vector<double> actualEvt;
	  	bool firstCycle = true;

		std::string name = dirStructure[j] + "/N_eventi_PU";
		//std::cout<<"name "<<name.c_str()<<std::endl;
		outputTXT<<"|"<<dirStructure[j].c_str()<<"|";

	  	for(int i = 0; i < sizeFiles; i++){

			std::string nameAndPath;
			nameAndPath = path_ + samples_[i];
			//std::cout<<"sample "<<nameAndPath<<std::endl;
			TFile * fileIn = TFile::Open(nameAndPath.c_str());
			fileIn->cd();
			TH1F *histoTMP = (TH1F*)gDirectory->Get(name.c_str());
			double numEvents = histoTMP->GetBinContent(2);
			if(firstCycle) tmpEvt.push_back(numEvents);
			actualEvt.push_back(numEvents);
			//std::cout<<"dirStructure "<<dirStructure[j].c_str()<<"events "<<numEvents<<std::endl;
			fileIn->Close();
		}

		firstCycle = false;

		int sizeEvtVec = actualEvt.size();
		for(int i = 0; i < sizeEvtVec; i++){
			double relEff = 0;
			double errEff = 0;
			if(tmpEvt[i] != 0){
				relEff = actualEvt[i]/tmpEvt[i];
				errEff = TMath::Sqrt(actualEvt[i] + relEff*relEff*tmpEvt[i])/tmpEvt[i];}
			outputTXT<<" "<<fixed<<setprecision(10)<<relEff<<" "<<fixed<<setprecision(10)<<errEff;
		}

		outputTXT<<" "<<std::endl;
		tmpEvt.clear();
		tmpEvt = actualEvt;
		actualEvt.clear();

	  }//Fine loop sulla struttura interna

	  int sizeScaleFactors = scaleFactors.size();
	  outputTXT<<"\n"<<setfill('-')<<setw(100)<<"-"<<endl;
	  outputTXT<<"Sample Events Cross-sections ScaleFactors\n"<<std::endl;
	  outputTXT<<setfill('-')<<setw(100)<<"-"<<endl;
	  for(int i = 0; i < sizeScaleFactors; i++){
		outputTXT<<labels_[i]<<" "<<eventsAtBeginning[i]<<" "<<crossSections_[i]<<" "<<scaleFactors[i]<<"\n";
	  }
	  outputTXT<<"\n"<<setfill('-')<<setw(100)<<"-"<<endl;

   }

}


// ------------ method called once each job just before starting event loop  ------------
void 
HistoAdderFirstStep::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HistoAdderFirstStep::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
HistoAdderFirstStep::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
HistoAdderFirstStep::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
HistoAdderFirstStep::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
HistoAdderFirstStep::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HistoAdderFirstStep::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HistoAdderFirstStep);
