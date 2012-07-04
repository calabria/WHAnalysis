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


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//Root
#include "TFile.h"
#include "TKey.h"
#include "TStyle.h"
#include "TClass.h"
#include "TAxis.h"
#include "TF1.h"
#include "TH1F.h"
#include "TH1.h"
#include "TH2F.h"
#include "TH2D.h"
#include "TROOT.h"
#include "TMath.h"
#include "TCanvas.h"
#include "TTree.h"
#include "TGaxis.h"
#include <TStyle.h>
#include "TText.h"
#include "TPaveText.h"
#include "TH1D.h"
#include "TGraphErrors.h"
#include "THStack.h"
#include "TLegend.h"
#include <string>
#include <fstream>
#include <iostream>

//
// class declaration
//

using namespace std;
using namespace edm;

class HistoAdder : public edm::EDAnalyzer {
   public:
      explicit HistoAdder(const edm::ParameterSet&);
      ~HistoAdder();
       TFile * fileIn;
       TFile * fileOut;

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      typedef std::vector<std::string> vstring;
      typedef std::vector<double> vdouble;

      std::string process_;
      std::string path_;
      vstring samples_;
      vstring labels_;
      vstring legendLabels_;
      vdouble setColors_;
      vdouble legendDim_;
      bool logScale_;
      std::string data_;
      bool nostack_;
      std::string eventsIn_;
      std::string txtFile_;
      std::string energy_;
      std::string lumi_;


      // ----------member data ---------------------------
};
