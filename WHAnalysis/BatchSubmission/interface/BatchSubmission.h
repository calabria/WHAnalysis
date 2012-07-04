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


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <string>
#include <fstream>
#include <iostream>
//
// class declaration
//

class BatchSubmission : public edm::EDAnalyzer {
   public:
      explicit BatchSubmission(const edm::ParameterSet&);
      ~BatchSubmission();

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
      std::ofstream OutputFileCFG;
      std::ofstream OutputFileCSH;
      std::string finalState_;
      std::string fileCFG_;
      std::string fileCSH_;
      std::string sample_;

      std::string pathCFG_;
      //std::string castorPath_;
      std::string savingPath_;
      std::string txtFile_;

      // ----------member data ---------------------------
};
