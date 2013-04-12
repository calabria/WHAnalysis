// -*- C++ -*-
//
// Package:    HistoAdder
// Class:      HistoAdder
// 
/**\class HistoAdder HistoAdder.cc HistoAdder/HistoAdder/src/HistoAdder.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Fri Jun 17 16:32:41 CEST 2011
// $Id$
//
//

#include "WHAnalysis/HistoAdder/interface/HistoAdder.h"

void setTDRStyle() {
  TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

// For the canvas:
  tdrStyle->SetCanvasBorderMode(0);
  tdrStyle->SetCanvasColor(kWhite);
  tdrStyle->SetCanvasDefH(600); //Height of canvas
  tdrStyle->SetCanvasDefW(700); //Width of canvas
  tdrStyle->SetCanvasDefX(0);   //POsition on screen
  tdrStyle->SetCanvasDefY(0);

// For the Pad:
  tdrStyle->SetPadBorderMode(0);
  // tdrStyle->SetPadBorderSize(Width_t size = 1);
  tdrStyle->SetPadColor(kWhite);
  tdrStyle->SetPadGridX(false);
  tdrStyle->SetPadGridY(false);
  tdrStyle->SetGridColor(0);
  tdrStyle->SetGridStyle(3);
  tdrStyle->SetGridWidth(1);

// For the frame:
  tdrStyle->SetFrameBorderMode(0);
  tdrStyle->SetFrameBorderSize(1);
  tdrStyle->SetFrameFillColor(0);
  tdrStyle->SetFrameFillStyle(0);
  tdrStyle->SetFrameLineColor(1);
  tdrStyle->SetFrameLineStyle(1);
  tdrStyle->SetFrameLineWidth(1);

// For the histo:
  // tdrStyle->SetHistFillColor(1);
  // tdrStyle->SetHistFillStyle(0);
  tdrStyle->SetHistLineColor(1);
  tdrStyle->SetHistLineStyle(0);
  tdrStyle->SetHistLineWidth(1);
  // tdrStyle->SetLegoInnerR(Float_t rad = 0.5);
  // tdrStyle->SetNumberContours(Int_t number = 20);

  tdrStyle->SetEndErrorSize(2);
//  tdrStyle->SetErrorMarker(20);
  tdrStyle->SetErrorX(0.);
  
  tdrStyle->SetMarkerStyle(20);

//For the fit/function:
  tdrStyle->SetOptFit(1);
  tdrStyle->SetFitFormat("5.4g");
  tdrStyle->SetFuncColor(2);
  tdrStyle->SetFuncStyle(1);
  tdrStyle->SetFuncWidth(1);

//For the date:
  tdrStyle->SetOptDate(0);
  // tdrStyle->SetDateX(Float_t x = 0.01);
  // tdrStyle->SetDateY(Float_t y = 0.01);

// For the statistics box:
  tdrStyle->SetOptFile(0);
  tdrStyle->SetOptStat(0); // To display the mean and RMS:   SetOptStat("mr");
  tdrStyle->SetStatColor(kWhite);
  tdrStyle->SetStatFont(42);
  tdrStyle->SetStatFontSize(0.025);
  tdrStyle->SetStatTextColor(1);
  tdrStyle->SetStatFormat("6.4g");
  tdrStyle->SetStatBorderSize(1);
  tdrStyle->SetStatH(0.1);
  tdrStyle->SetStatW(0.15);
  // tdrStyle->SetStatStyle(Style_t style = 1001);
  // tdrStyle->SetStatX(Float_t x = 0);
  // tdrStyle->SetStatY(Float_t y = 0);

// Margins:
  tdrStyle->SetPadTopMargin(0.05);
  tdrStyle->SetPadBottomMargin(0.13);
  tdrStyle->SetPadLeftMargin(0.16);
  tdrStyle->SetPadRightMargin(0.02);

// For the Global title:

  tdrStyle->SetOptTitle(1);
  tdrStyle->SetTitleFont(42);
  tdrStyle->SetTitleColor(1);
  tdrStyle->SetTitleTextColor(1);
  tdrStyle->SetTitleFillColor(10);
  tdrStyle->SetTitleStyle(4000);
  tdrStyle->SetTitleFontSize(0.0212);
  // tdrStyle->SetTitleH(0); // Set the height of the title box
  // tdrStyle->SetTitleW(0); // Set the width of the title box
  tdrStyle->SetTitleX(0.2); // Set the position of the title box
  tdrStyle->SetTitleY(0.982); // Set the position of the title box
  //tdrStyle->SetTitleStyle(Style_t style = 1001);
  tdrStyle->SetTitleBorderSize(0);

// For the axis titles:

  tdrStyle->SetTitleColor(1, "XYZ");
  tdrStyle->SetTitleFont(42, "XYZ");
  tdrStyle->SetTitleSize(0.03, "XYZ");
  // tdrStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // tdrStyle->SetTitleYSize(Float_t size = 0.02);
  tdrStyle->SetTitleXOffset(0.9);
  tdrStyle->SetTitleYOffset(1.25);
  // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

// For the axis labels:

  tdrStyle->SetLabelColor(1, "XYZ");
  tdrStyle->SetLabelFont(42, "XYZ");
  tdrStyle->SetLabelOffset(0.007, "XYZ");
  tdrStyle->SetLabelSize(0.03, "XYZ");

// For the axis:

  tdrStyle->SetAxisColor(1, "XYZ");
  tdrStyle->SetStripDecimals(kTRUE);
  tdrStyle->SetTickLength(0.03, "XYZ");
  tdrStyle->SetNdivisions(510, "XYZ");
  tdrStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  tdrStyle->SetPadTickY(1);

// Change for log plots:
  tdrStyle->SetOptLogx(0);
  tdrStyle->SetOptLogy(0);
  tdrStyle->SetOptLogz(0);

// Postscript options:
  tdrStyle->SetPaperSize(20.,20.);
  // tdrStyle->SetLineScalePS(Float_t scale = 3);
  // tdrStyle->SetLineStyleString(Int_t i, const char* text);
  // tdrStyle->SetHeaderPS(const char* header);
  // tdrStyle->SetTitlePS(const char* pstitle);

  // tdrStyle->SetBarOffset(Float_t baroff = 0.5);
  // tdrStyle->SetBarWidth(Float_t barwidth = 0.5);
  // tdrStyle->SetPaintTextFormat(const char* format = "g");
  // tdrStyle->SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
  // tdrStyle->SetTimeOffset(Double_t toffset);
  // tdrStyle->SetHistMinimumZero(kTRUE);

  tdrStyle->cd();

}

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
HistoAdder::HistoAdder(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

    process_ = iConfig.getUntrackedParameter<std::string>("process");
    path_ = iConfig.getUntrackedParameter<std::string>("path");
    samples_ = iConfig.getUntrackedParameter<vstring>("samples");
    labels_ = iConfig.getUntrackedParameter<vstring>("labels");
    legendLabels_ = iConfig.getUntrackedParameter<vstring>("legendLabels");
    logScale_ = iConfig.getUntrackedParameter<bool>("logScale");
    setColors_ = iConfig.getUntrackedParameter<vdouble>("setColors");
    legendDim_ = iConfig.getUntrackedParameter<vdouble>("legendDim");
    data_ = iConfig.getUntrackedParameter<std::string>("data");
    nostack_ = iConfig.getUntrackedParameter<bool>("nostack");
    eventsIn_ = iConfig.getUntrackedParameter<std::string>("eventsIn");
    txtFile_ = iConfig.getUntrackedParameter<std::string>("txtFile");
    energy_ = iConfig.getUntrackedParameter<std::string>("energy");
    lumi_ = iConfig.getUntrackedParameter<std::string>("lumi");

}


HistoAdder::~HistoAdder()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
HistoAdder::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  std::vector<std::string> dirStructure;
  std::vector<std::string> onlyHistos;
  std::vector<std::string> histoStructure;
  std::vector<std::string> histoNamesForSaving;
  std::vector<double> eventsAtBeginning;
  std::vector<int> histoType;
  std::vector<double> scaleFactors;
  dirStructure.clear();
  histoStructure.clear();
  bool flag = true;

  std::string nameAndPath = path_ + samples_[0];
  TFile * fileIn = TFile::Open(nameAndPath.c_str());
  TIter next(fileIn->GetListOfKeys());
  TKey *key;
  while ((key=(TKey*)next())) {
	//std::cout<<"key: "<<key->GetName()<<" points to an object of class:"<<key->GetClassName()<<std::endl;
	std::string folder = key->GetName();
	//Include here all the folders to be skipped
	//if(folder == "TriggerHistosBeforeSel") continue;
	//if(folder == "TriggerHistosAfterSel") continue;
	if(folder == "puDistribution") continue;
	if(folder != "CompCandHistosAfterSelLt" && folder != "CompCandHistosAfterSelLt1" && folder != "CompCandHistosAfterSelLt2" && folder != "CompCandHistosAfterSelLt3") continue;
	dirStructure.push_back(folder);
	//gDirectory->pwd();
        fileIn->cd();
        gDirectory->cd(folder.c_str());
	TIter next2(gDirectory->GetListOfKeys());
  	TKey *key2;
	while ((key2=(TKey*)next2())) {
		//std::cout<<"key: "<<key2->GetName()<<" points to an object of class:"<<key2->GetClassName()<<std::endl;
		TObject * obj = key2->ReadObj();
		std::string histoName = key2->GetName();
		onlyHistos.push_back(histoName);
		//if(histoName == "TriggerHLT_Mu17_Ele8_CaloIdL_v") continue;
		std::string folderHisto = folder + "/" + histoName;
		std::string namesForSaving = folder + "_" + histoName;
		//std::cout<<"folderHisto "<<folderHisto.c_str()<<std::endl;
		if(obj->IsA()->InheritsFrom("TH2")) histoType.push_back(1);
		else if(obj->IsA()->InheritsFrom("TH1")) histoType.push_back(0);
		histoStructure.push_back(folderHisto);
		histoNamesForSaving.push_back(namesForSaving);
	}
  }

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

   	   TCanvas * cvStack = new TCanvas("","",700,700);
	   TPad *pad1 = new TPad("pad1", "The pad 70% of the height",0.0,0.3,1.0,1.0,10);
	   TPad *pad2 = new TPad("pad2", "The pad 30% of the height",0.0,0.0,1.0,0.3,10);
	   pad1->Draw();
	   pad2->Draw();
	   pad1->cd();

   	   THStack * hs = new THStack(histoStructure[k].c_str(),histoStructure[k].c_str());
      	   TLegend * legend = new TLegend(legendDim_[0],legendDim_[1],legendDim_[2],legendDim_[3]);
	   std::string titleXaxis;
	   cvStack->SetFillColor(10);
	   Double_t binWidth = 1;

	   if(logScale_) gPad->SetLogy();

	   for(int i = 0; i < sizeFiles; i++){//Loop sui file

			   std::string nameAndPath;
			   nameAndPath = path_ + samples_[i];
		   	   std::cout<<"sample "<<nameAndPath<<std::endl;
			   TFile * fileIn = TFile::Open(nameAndPath.c_str());
			   fileIn->cd();
			   std::cout<<"histoName "<<histoStructure[k].c_str()<<std::endl;
			   TH1F * histoTMP;
			   //if(i == 0) histoTMP = (TH1F*)gDirectory->Get(("CompCandHistosAfterSelLt/" + onlyHistos[k]).c_str());    
			   //else histoTMP = (TH1F*)gDirectory->Get(histoStructure[k].c_str());	  
			   histoTMP = (TH1F*)gDirectory->Get(histoStructure[k].c_str());	   	 	
			   //double scaledEvents = nEntries * scaleFactor;
			   //if(histoTMP->GetSize()%2 == 0 && histoStructure[k].find("TauRecDecayMode") == string::npos) histoTMP->Rebin();
			   //if(histoStructure[k].find("/VisMass") != string::npos) histoTMP->Rebin(3);
			   //if(histoStructure[k].find("DiTauHistosFinal/Pt_Ditau") != string::npos) histoTMP->Rebin(4);
			   //if(histoStructure[k].find("EleHistosFinal/elePt") != string::npos) histoTMP->Rebin(4);
			   //if(histoStructure[k].find("CompCandHistosBeforeSel/Lt") != string::npos) histoTMP->Rebin();
			   if(histoStructure[k].find("DiTauCandSSEta") != string::npos) {

				histoTMP->Rebin(3);
				//histoTMP->GetXaxis()->SetTitle("#eta");
	
			   }
			   /*if(histoStructure[k].find("DiTauCandSSPt") != string::npos){

				histoTMP->Rebin(5);
			 	histoTMP->GetXaxis()->SetTitle("p_{T} [GeV/c]");

			   }*/
			   histoTMP->SetLineColor(1);
			   histoTMP->SetFillColor(setColors_[i]);
		 	   histoTMP->SetFillStyle(1000);
			   titleXaxis = histoTMP->GetXaxis()->GetTitle();
			   //std::cout<<"label "<<titleXaxis.c_str()<<std::endl;
	   		   binWidth = histoTMP->GetBinWidth(1);
			   hs->Add(histoTMP);
			   legend->AddEntry(histoTMP, legendLabels_[i].c_str(), "f");
			   fileIn->Close();

	   }
	   flag = false;

	   //// Cosmetics ////	

	   if(logScale_) hs->SetMinimum(0.0001);
	   else hs->SetMinimum(0);
	   //std::cout<<"label "<<titlexAxis.c_str()<<std::endl;
	   hs->Draw("HIST");
	   if(titleXaxis != "") hs->GetXaxis()->SetTitle(titleXaxis.c_str());
	   std::stringstream ss;
	   ss<<binWidth;
	   std::string width = ss.str();
	   std::string titleY = "Events/" + width;
	   hs->GetYaxis()->SetTitle(titleY.c_str());
	   double maxMC = hs->GetMaximum();
	   double maxData = 0;

	   TH1F * stack = (TH1F*)hs->GetStack()->Last()->Clone();
	   TH1F * histoData2;
	   TH1F * histoData3;

	   if(data_ != ""){
	   	TFile * fileData = TFile::Open(data_.c_str());
	   	//TH1F *histoData = (TH1F*)gDirectory->Get(("CompCandHistosAfterSelLt/" + onlyHistos[k]).c_str());
		TH1F *histoData = (TH1F*)gDirectory->Get(histoStructure[k].c_str());
	   	histoData2 = (TH1F*)histoData->Clone();
	   	histoData3 = (TH1F*)histoData->Clone();
	   	legend->AddEntry(histoData, "Data", "p");
		//if(histoStructure[k].find("/VisMass") != string::npos) histoData->Rebin(3);
		//if(histoStructure[k].find("DiTauHistosFinal/Pt_Ditau") != string::npos) histoData->Rebin(4);
		//if(histoStructure[k].find("EleHistosFinal/elePt") != string::npos) histoData->Rebin(4);
		//if(histoStructure[k].find("CompCandHistosBeforeSel/Lt") != string::npos) histoData->Rebin();
		if(histoStructure[k].find("DiTauCandSSEta") != string::npos) {
			histoData->Rebin(3);
			histoData2->Rebin(3);
			histoData3->Rebin(3);
			//histoData2->GetXaxis()->SetTitle("#eta");
		}
		/*if(histoStructure[k].find("DiTauCandSSPt") != string::npos){
			histoData->Rebin(5);
			histoData2->Rebin(5);
			histoData3->Rebin(5);
		 	histoData2->GetXaxis()->SetTitle("p_{T} [GeV/c]");
		}*/
		histoData->SetMarkerColor(1);
		histoData->SetMarkerStyle(20);
		histoData->SetMarkerSize(0.5);
		histoData->Draw("SAME, ep");
		maxData = histoData->GetMaximum();
	   	fileData->Close();
		}
	   double max = std::max(maxData, maxMC);
	   if(max != 0) hs->SetMaximum(max*120/100);
	   legend->SetFillColor(10);
	   legend->Draw();

	   std::string title = " CMS Preliminary 2012      #sqrt{s} = " + energy_ + "   #int L = " + lumi_;
	   hs->SetTitle(title.c_str());
	   setTDRStyle();

	   pad2->cd();
  	   pad2->SetGridx();
   	   pad2->SetGridy();
   	   //pad2->SetLogy();
	   histoData2->Add(stack, -1);
	   histoData2->Divide(histoData3);
	   for(int i=1; i<histoData2->GetSize(); i++){

		float diff = histoData2->GetBinContent(i);
		if(diff < 0){

			diff *= -1;
			//histoData2->SetBinContent(i,diff);

		}

	   }

	   float sysUn = 0;

	   for(int i=1; i<histoData2->GetSize(); i++){

		float diff = histoData2->GetBinContent(i);
		if(diff != 0){

			sysUn += diff*diff;


		}

	   }
	   std::cout<<"Tot. Sys. Uncertainty: "<<100*sqrt(sysUn)<<std::endl;

	   histoData2->Fit("pol0");      
	   //if(histoStructure[k].find("DiTauCandSSPt") != string::npos || histoStructure[k].find("DiTauCandSSEta") != string::npos) histoData2->Fit("pol7","","SAMES");              
	   histoData2->SetTitle("");
	   histoData2->GetYaxis()->SetTitle("(obs-exp)/obs");
	   histoData2->GetYaxis()->SetTitleSize(0.06);
  	   histoData2->GetYaxis()->SetLabelSize(0.06);
	   histoData2->GetXaxis()->SetTitleSize(0.06);
  	   histoData2->GetXaxis()->SetLabelSize(0.06);
  	   histoData2->SetMaximum(+1);
  	   histoData2->SetMinimum(-1);
  	   histoData2->SetMarkerColor(1);
  	   histoData2->SetMarkerStyle(20);
  	   histoData2->SetMarkerSize(0.5);
	   histoData2->Draw("1ep");
	   pad2->Update();
	   TPaveText * box = new TPaveText(0.20,0.7,0.5,0.87, "NDC");
	   box->AddText("i murt tu");
	   box->SetFillColor(0);
	   //box->Draw();
	   pad2->Update();
	   TPaveStats* st = (TPaveStats*) histoData2->FindObject("stats");
	   if(st){

		st->SetX1NDC(0.6);
	   	st->SetX2NDC(0.9);
	  	st->SetY1NDC(0.6);
	   	st->SetY2NDC(0.9);
	   	st->SetOptFit(0111);
	   	st->Draw();

	   }
	   pad2->Update();

	   std::string saveName;
           if(logScale_) saveName = "./Plots/" + process_ + "/plots_stack_log/" + histoNamesForSaving[k] + ".png";
           else saveName = "./Plots/" + process_ + "/plots_stack/" + histoNamesForSaving[k] + ".png";
	   cvStack->Print(saveName.c_str());

	   delete hs;
	   delete cvStack;
	   delete legend;

	}
   }

  //// Non stacked plots ////

  if(nostack_){
   for(int k = 0; k < sizeHistos; k++){//Loop sugli istogrammi

	if(histoType[k] == 0){

   	   TCanvas * cvStack = new TCanvas("","",700,700);
      	   TLegend * legend = new TLegend(legendDim_[0],legendDim_[1],legendDim_[2],legendDim_[3]);
   	   THStack * hs = new THStack(histoStructure[k].c_str(),histoStructure[k].c_str());
	   std::string titleXaxis;
	   cvStack->SetFillColor(10);
	   Double_t binWidth = 1;

	   if(logScale_) gPad->SetLogy();

	   for(int i = 0; i < sizeFiles; i++){//Loop sui file
		   std::string nameAndPath;
		   nameAndPath = path_ + samples_[i];
	   	   std::cout<<"sample "<<nameAndPath<<std::endl;
		   TFile * fileIn = TFile::Open(nameAndPath.c_str());
		   fileIn->cd();
		   std::cout<<"histoName "<<histoStructure[k].c_str()<<std::endl;
		   TH1F *histoTMP = (TH1F*)gDirectory->Get(histoStructure[k].c_str());
		   //double nEntries = histoTMP->GetEntries();
		   histoTMP->SetLineColor(setColors_[i]);
		   histoTMP->SetLineWidth(2);
		   histoTMP->SetFillColor(setColors_[i]);
	 	   histoTMP->SetFillStyle(0);
		   titleXaxis = histoTMP->GetXaxis()->GetTitle();
	   	   binWidth = histoTMP->GetBinWidth(1);
		   hs->Add(histoTMP);
		   legend->AddEntry(histoTMP, labels_[i].c_str(), "l");
		   fileIn->Close();

	   }


	   if(logScale_) hs->SetMinimum(0.001);
	   else hs->SetMinimum(0);
	   hs->Draw("HISTnostack");
	   if(titleXaxis != "") hs->GetXaxis()->SetTitle(titleXaxis.c_str());
	   std::stringstream ss;
	   ss<<binWidth;
	   std::string width = ss.str();
	   std::string titleY = "Events/" + width;
	   hs->GetYaxis()->SetTitle(titleY.c_str());
	   legend->SetFillColor(10);
	   legend->Draw();

	   std::string title = " CMS Preliminary 2012      #sqrt{s} = " + energy_ + "   L = " + lumi_;
	   hs->SetTitle(title.c_str());
	   setTDRStyle();

           std::string saveName = "./Plots/" + process_ + "/plots_nostack/" + histoNamesForSaving[k] + ".png";
	   cvStack->Print(saveName.c_str());

	   delete hs;
	   delete cvStack;
	   delete legend;

	}

   }

  }

  std::ofstream outputTXT;
  outputTXT.open(txtFile_.c_str());

  if(outputTXT.is_open()){

	  //// Final table ////

	  outputTXT<<"\n"<<setfill('-')<<setw(100)<<"-"<<endl;
	  outputTXT<<"Final table"<<std::endl;
	  outputTXT<<setfill('-')<<setw(100)<<"-"<<endl;

	  outputTXT<<"\n ";
	  outputTXT<<"Cut ";
	  for(int i = 0; i < sizeFiles; i++){

		outputTXT<<labels_[i]<<" Err. ";

	  }
	  outputTXT<<"Data Err."<<std::endl;

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
			double radqEvt = histoTMP->GetBinError(2);
			//std::cout<<" "<<fixed<<setprecision(3)<<numEvents*scaleFactor<<" "<<fixed<<setprecision(3)<<scaleFactor*radqEvt;
			outputTXT<<" "<<fixed<<setprecision(3)<<numEvents<<" "<<fixed<<setprecision(3)<<radqEvt;
			fileIn->Close();
		}

		if(data_ != ""){
			TFile * fileData = TFile::Open(data_.c_str());
			fileData->cd();
		   	TH1F *histoData = (TH1F*)gDirectory->Get(name.c_str());
			double numEvents = histoData->GetBinContent(2);
			double radqEvt = TMath::Sqrt(numEvents);
			outputTXT<<" "<<fixed<<setprecision(3)<<numEvents<<" "<<fixed<<setprecision(3)<<radqEvt;
			fileData->Close();
		}

		outputTXT<<" "<<std::endl;

	  }

	  //// Efficienze assolute ////

	  outputTXT<<"\n"<<setfill('-')<<setw(100)<<"-"<<endl;
	  outputTXT<<"Absolute efficiencies"<<std::endl;
	  outputTXT<<setfill('-')<<setw(100)<<"-"<<endl;

	  //TH1F * effPlot = new TH1F("","",numFolders,0,numFolders);

	  outputTXT<<"\n ";
	  outputTXT<<"Cut ";
	  for(int i = 0; i < sizeFiles; i++){

		outputTXT<<labels_[i]<<" Err. ";

	  }
	  outputTXT<<"Data Err."<<std::endl;

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
			TH1F *histoTMPEvt = (TH1F*)gDirectory->Get("VertexHistosBeforeMCFilter2/N_eventi_PU");
			double numEvents = histoTMP->GetBinContent(2);
			double eventsAtBeginning = histoTMPEvt->GetBinContent(2);
			double numEventsErr = histoTMP->GetBinError(2);
			double eventsAtBeginningErr = histoTMPEvt->GetBinError(2);
			//std::cout<<"dirStructure "<<dirStructure[j].c_str()<<"events "<<numEvents<<std::endl;
			double absEff = 0;
			double errEff = 0;
			if(eventsAtBeginning){
				absEff = numEvents/eventsAtBeginning;
				errEff = TMath::Sqrt(numEventsErr*numEventsErr + absEff*absEff*eventsAtBeginningErr*eventsAtBeginningErr)/eventsAtBeginning;}
			outputTXT<<" "<<fixed<<setprecision(10)<<absEff<<" "<<fixed<<setprecision(10)<<errEff;
			fileIn->Close();
		}

		if(data_ != ""){
			TFile * fileData = TFile::Open(data_.c_str());
			fileData->cd();
		   	TH1F *histoData = (TH1F*)gDirectory->Get(name.c_str());
			TH1F *histoTMPEvt = (TH1F*)gDirectory->Get("VertexHistosBeforeMCFilter2/N_eventi_PU");
			double numEvents = histoData->GetBinContent(2);
			double eventsAtBeginning = histoTMPEvt->GetBinContent(2);
			double absEff = 0;
			double errEff = 0;
			if(eventsAtBeginning){
				absEff = numEvents/eventsAtBeginning;
				errEff = TMath::Sqrt(numEvents + absEff*absEff*eventsAtBeginning)/eventsAtBeginning;}
			outputTXT<<" "<<fixed<<setprecision(10)<<absEff<<" "<<fixed<<setprecision(10)<<errEff;
			fileData->Close();
		}

		outputTXT<<" "<<std::endl;

	  }

	  //// Efficienze relative ////

	  std::vector<double> tmpEvt;
	  std::vector<double> tmpEvtErr;

	  outputTXT<<"\n"<<setfill('-')<<setw(100)<<"-"<<endl;
	  outputTXT<<"Relative efficiencies"<<std::endl;
	  outputTXT<<setfill('-')<<setw(100)<<"-"<<endl;

	  outputTXT<<"\n ";
	  outputTXT<<"Cut ";
	  for(int i = 0; i < sizeFiles; i++){

		outputTXT<<labels_[i]<<" Err. ";

	  }
	  outputTXT<<"Data Err."<<std::endl;

	  for(int j = 0; j < numFolders; j++){

		std::vector<double> actualEvt;
		std::vector<double> actualEvtErr;
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
			double numErr = histoTMP->GetBinError(2);
			if(firstCycle){
				tmpEvt.push_back(numEvents);
				tmpEvtErr.push_back(numErr);}
			actualEvt.push_back(numEvents);
			actualEvtErr.push_back(numErr);
			//std::cout<<"dirStructure "<<dirStructure[j].c_str()<<"events "<<numEvents<<std::endl;
			fileIn->Close();

		}

		if(data_ != ""){
			TFile * fileData = TFile::Open(data_.c_str());
			fileData->cd();
		   	TH1F *histoData = (TH1F*)gDirectory->Get(name.c_str());
			double numEvents = histoData->GetBinContent(2);
			if(firstCycle) tmpEvt.push_back(numEvents);
			actualEvt.push_back(numEvents);
			fileData->Close();
		}

		firstCycle = false;

		int sizeEvtVec = actualEvt.size();
		for(int i = 0; i < sizeEvtVec; i++){
			double relEff = 0;
			double errEff = 0;
			if(tmpEvt[i] != 0){
				relEff = actualEvt[i]/tmpEvt[i];
				errEff = TMath::Sqrt(actualEvtErr[i]*actualEvtErr[i] + relEff*relEff*tmpEvtErr[i]*tmpEvtErr[i])/tmpEvt[i];}
			outputTXT<<" "<<fixed<<setprecision(10)<<relEff<<" "<<fixed<<setprecision(10)<<errEff;
		}

		outputTXT<<" "<<std::endl;
		tmpEvt.clear();
		tmpEvtErr.clear();
		tmpEvt = actualEvt;
		tmpEvtErr = actualEvtErr;
		actualEvt.clear();
		actualEvtErr.clear();

	  }//Fine loop sulla struttura interna

  }

}


// ------------ method called once each job just before starting event loop  ------------
void 
HistoAdder::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HistoAdder::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
HistoAdder::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
HistoAdder::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
HistoAdder::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
HistoAdder::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HistoAdder::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HistoAdder);
