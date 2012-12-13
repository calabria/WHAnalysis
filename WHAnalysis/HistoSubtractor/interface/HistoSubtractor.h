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
#include <iomanip>
//
// class declaration
//

class HistoSubtractor : public edm::EDAnalyzer {
   public:
      explicit HistoSubtractor(const edm::ParameterSet&);
      ~HistoSubtractor();

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

      std::string path_;
      std::string mainSample_;
      vstring samples_;
      vstring labels_;
      std::string outputFile_;


      // ----------member data ---------------------------
};
