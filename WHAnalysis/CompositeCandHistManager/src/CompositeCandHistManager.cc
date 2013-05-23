// -*- C++ -*-
//
// Package:    CompositeCandHistManager
// Class:      CompositeCandHistManager
// 
/**\class CompositeCandHistManager CompositeCandHistManager.cc WHAnalysis/CompositeCandHistManager/src/CompositeCandHistManager.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria,161 R-006,+41227670194,
//         Created:  Sun Dec 18 15:51:35 CET 2011
// $Id$
//
//


// system include files
#include <memory>
#include <map>
#include <string>
#include <sstream>
#include <TMath.h>
#include <cmath>
// user include files
#include "TH1.h"
#include "TH2.h"


#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

//
// class declaration
//

class CompositeCandHistManager : public edm::EDAnalyzer {
   public:
      explicit CompositeCandHistManager(const edm::ParameterSet&);
      ~CompositeCandHistManager();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------

      std::map<std::string,TH1F*> histContainer_; 
      std::map<std::string,TH2F*> histContainer2D_;
      edm::LumiReWeighting LumiWeights_;

      // input tags  
      edm::InputTag CompCandSrc_;
      //edm::InputTag muonSrc_;
      //edm::InputTag eleSrc_;
      //edm::InputTag tauSrc_;
      edm::InputTag PFMetTag_;

      typedef std::vector<double> vdouble;
      vdouble MCDist_f_;
      vdouble TrueDist2011_f_;
      bool isMC_;
      int isFR_;
      double wjetsCoeff_;
      double zjetsCoeff_;

};

std::vector<double> candidateType(const reco::Candidate* dau){

  std::vector<double> weights;

  if(dau->isMuon()){

  	const pat::Muon & muon = dynamic_cast<const pat::Muon&>(*dau->masterClone());

	weights.push_back(muon.userFloat("muonWeightTriggerMuLeg"));
	weights.push_back(muon.userFloat("muonWeightID"));
	weights.push_back(muon.userFloat("muonWeightIso"));
	weights.push_back(muon.userFloat("muonWeightFR"));

  }
  if(dau->isElectron()){

  	const pat::Electron & electron = dynamic_cast<const pat::Electron&>(*dau->masterClone());

	weights.push_back(electron.userFloat("eleWeightTriggerEleLeg"));
	weights.push_back(electron.userFloat("eleWeightID"));
	weights.push_back(electron.userFloat("eleWeightIso"));
	weights.push_back(electron.userFloat("eleWeightFR"));

  }
  else{

 	const pat::Tau & tau = dynamic_cast<const pat::Tau&>(*dau->masterClone());

	weights.push_back(tau.userFloat("tauWeightTriggerMuLeg"));
	weights.push_back(tau.userFloat("tauWeightTriggerEleLeg"));
	weights.push_back(tau.userFloat("tauWeightFR"));
	weights.push_back(tau.userFloat("tauWeightFR"));

  }

  return weights;

}

//
// constants, enums and typedefs
//

namespace WJetsMedium{

//////////////FR functions(pt) 1D

	static Double_t fake_rate_tau_pt_20(Double_t pt) {

	    Double_t value = 0;

	    if (pt<0) value = 1.0;
	    if (pt<=100){

		//1D
		Double_t mpv=-4.417;
		Double_t  sigma=3.663;
		Double_t costante=0.002753;

		Double_t f=((TMath::Landau(pt,mpv,sigma))+costante);

		value = f;}

	    else{

		value = fake_rate_tau_pt_20(100);}

	    return value;

	}

//////////////FR functions(pt) 3 regions in eta

	static Double_t fake_rate_tau_pt_eta(Double_t pt, Double_t eta) {

	    Double_t value = 0;

	    if (pt<0) value = 1.0;
	    if (pt<=100){

		//eta1

		if (TMath::Abs(eta) < 0.8){

		    Double_t mpv=-1.488;
		    Double_t sigma=2.607;
		    Double_t costante=0.00271;

		    Double_t f1=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f1;}

		//eta2

		if ((TMath::Abs(eta) > 0.8) && (TMath::Abs(eta) < 1.6)){

		    Double_t mpv=2.408;
		    Double_t  sigma=3;
		    Double_t costante=0.003991;

		    Double_t f2=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f2;}

		//eta3

		if ((TMath::Abs(eta) > 1.6) && (TMath::Abs(eta) < 2.3)){

		    Double_t mpv=3.176;
		    Double_t  sigma=3.105;
		    Double_t costante=0.005468;

		    Double_t f3=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f3;}

	    }

	    else{

		value = fake_rate_tau_pt_eta(100,eta);}

	    return value;

	}

//////////////FR function(pt,eta) 10

	static Double_t fake_rate_tau(Double_t pt, Double_t eta) {

	    Double_t value = 0;

	    //if (pt<0) return 1.0;

	    if (pt<=100 && (TMath::Abs(eta) < 2.3)){

        	Double_t p_par[15] = {2.76927,0.829635,0.845252,-0.170804,0.0795583,1.75812,-0.223468,0.344182,0.0396087,-0.109584,0.00379608,0.00142165,0.00334431,-0.000266454,-0.000104904};

		///parametri!!!!

		Double_t p0 = p_par[0]+p_par[1]*eta+p_par[2]*TMath::Power(eta,2)+p_par[3]*TMath::Power(eta,3)+p_par[4]*TMath::Power(eta,4);
		Double_t p1 = p_par[5]+p_par[6]*eta+p_par[7]*TMath::Power(eta,2)+p_par[8]*TMath::Power(eta,3)+p_par[9]*TMath::Power(eta,4);
		Double_t p2 = p_par[10]+p_par[11]*eta+p_par[12]*TMath::Power(eta,2)+p_par[13]*TMath::Power(eta,3)+p_par[14]*TMath::Power(eta,4);
		Double_t result = TMath::Landau(pt,p0,p1)+p2;

		value = result;

	    }

	    else{

		if (pt>100 && eta < -2.3){

		    value = fake_rate_tau(100,-2.3);}

		if (pt>100 && eta > 2.3){

		    value = fake_rate_tau(100,2.3);}

	    }

	    return value;

	}

}

namespace WJetsTight{

//////////////FR functions(pt) 1D

	static Double_t fake_rate_tau_pt_20(Double_t pt) {

	    Double_t value = 0;

	    if (pt<0) value = 1.0;

	    if (pt<=100){

		//1D

		Double_t mpv=-4.585;
		Double_t  sigma=3.378;
		Double_t costante=0.002719;

		Double_t f=((TMath::Landau(pt,mpv,sigma))+costante);

		value = f;}

	    else{

		value = fake_rate_tau_pt_20(100);}

	    return value;

	}

//////////////FR functions(pt) 3 regions in eta

	static Double_t fake_rate_tau_pt_eta(Double_t pt, Double_t eta) {

	    Double_t value = 0;

	    if (pt<0) value = 1.0;

	    if (pt<=100){

		//eta1

		if (TMath::Abs(eta) < 0.8){

		    Double_t mpv=2.677;
		    Double_t sigma=1.91;
		    Double_t costante=0.003176;

		    Double_t f1=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f1;}

		//eta2

		if ((TMath::Abs(eta) > 0.8) && (TMath::Abs(eta) < 1.6)){

		    Double_t mpv=0.8542;
		    Double_t  sigma=2.905;
		    Double_t costante=0.004203;

		    Double_t f2=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f2;}

		//eta3

		if ((TMath::Abs(eta) > 1.6) && (TMath::Abs(eta) < 2.3)){

		    Double_t mpv=6.706;
		    Double_t  sigma=2.216;
		    Double_t costante=0.007026;

		    Double_t f3=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f3;}

	    }

	    else{

		value = fake_rate_tau_pt_eta(100,eta);}

	    return value;

	}

//////////////FR function(pt,eta) 10

	static Double_t fake_rate_tau(Double_t pt, Double_t eta) {

	    Double_t value = 0;

	    //if (pt<0) return 1.0;

	    if (pt<=100 && (TMath::Abs(eta) < 2.3)){

		Double_t p_par[18] = {2.9794,1.15446,0.256635,-0.304231,0.225319,1.52836,-0.243571,0.453055,0.0622961,-0.131668,0.00430408,-0.000362758,0.000812893,0.000604475,0.000987013,0.000170702,-0.000138295,-6.86732e-05};

		///parametri!!!!

		Double_t p0 = p_par[0]+p_par[1]*eta+p_par[2]*TMath::Power(eta,2)+p_par[3]*TMath::Power(eta,3)+p_par[4]*TMath::Power(eta,4);
		Double_t p1 = p_par[5]+p_par[6]*eta+p_par[7]*TMath::Power(eta,2)+p_par[8]*TMath::Power(eta,3)+p_par[9]*TMath::Power(eta,4);
		Double_t p2 = p_par[10]+p_par[11]*eta+p_par[12]*TMath::Power(eta,2)+p_par[13]*TMath::Power(eta,3)+p_par[14]*TMath::Power(eta,4)+p_par[15]*TMath::Power(eta,5)+p_par[16]*TMath::Power(eta,6)+p_par[17]*TMath::Power(eta,7);

		Double_t result = TMath::Landau(pt,p0,p1)+p2;

		value = result;

	    }

	    else{

		if (pt>100 && eta < -2.3){

		    value = fake_rate_tau(100,-2.3);}

		if (pt>100 && eta > 2.3){

		    value = fake_rate_tau(100,2.3);}

	    }

	    return value;

	}

}

namespace ZJetsMedium{

//////////////FR functions(pt) 1D

	static Double_t fake_rate_tau_pt_20(Double_t pt) {

	    Double_t value = 0;

	    if (pt<0) value = 1.0;

	    if (pt<=100){

		//1D

		Double_t mpv=-12.47;
		Double_t  sigma=7.108;
		Double_t costante=0.003016;

		Double_t f=((TMath::Landau(pt,mpv,sigma))+costante);

		value = f;}

	    else{

		value = fake_rate_tau_pt_20(100);}

	    return value;

	}

//////////////FR functions(pt) 3 regions in eta

	static Double_t fake_rate_tau_pt_eta(Double_t pt, Double_t eta) {

	    Double_t value = 0;

	    if (pt<0) value = 1.0;

	    if (pt<=100){

		//eta1

		if (TMath::Abs(eta) < 0.8){

		    Double_t mpv=-3.077;
		    Double_t sigma=4.431;
		    Double_t costante=0.005742;

		    Double_t f1=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f1;}

		//eta2

		if ((TMath::Abs(eta) > 0.8) && (TMath::Abs(eta) < 1.6)){

		    Double_t mpv=-14.16;
		    Double_t  sigma=8.5;
		    Double_t costante=-0.0006049;

		    Double_t f2=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f2;}

		//eta3

		if ((TMath::Abs(eta) > 1.6) && (TMath::Abs(eta) < 2.3)){

		    Double_t mpv=-8.79;
		    Double_t  sigma=6.853;
		    Double_t costante=0.00795;

		    Double_t f3=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f3;}

	    }

	    else{

		value = fake_rate_tau_pt_eta(100,eta);}

	    return value;

	}

//////////////FR function(pt,eta) 10

	static Double_t fake_rate_tau(Double_t pt, Double_t eta) {

	    Double_t value = 0;

	    //if (pt<0) return 1.0;

	    if (pt<=100 && (TMath::Abs(eta) < 2.3)){

		Double_t p_par[15] = {1.85101,-0.346399,2.41707,0.0679917,-0.168245,3.06144,0.102339,0.0513099,-0.0319107,-0.0789404,0.00762862,-0.000676062,0.00774476,0.000376936,-0.000894677};

		///parametri!!!!

		Double_t p0 = p_par[0]+p_par[1]*eta+p_par[2]*TMath::Power(eta,2)+p_par[3]*TMath::Power(eta,3)+p_par[4]*TMath::Power(eta,4);
		Double_t p1 = p_par[5]+p_par[6]*eta+p_par[7]*TMath::Power(eta,2)+p_par[8]*TMath::Power(eta,3)+p_par[9]*TMath::Power(eta,4);
		Double_t p2 = p_par[10]+p_par[11]*eta+p_par[12]*TMath::Power(eta,2)+p_par[13]*TMath::Power(eta,3)+p_par[14]*TMath::Power(eta,4);
		Double_t result = TMath::Landau(pt,p0,p1)+p2;

		value = result;

	    }

	    else{

		if (pt>100 && eta < -2.3){

		    value = fake_rate_tau(100,-2.3);}

		if (pt>100 && eta > 2.3){

		    value = fake_rate_tau(100,2.3);}

	    }

	    return value;

	}

}

namespace ZJetsTight{

//////////////FR functions(pt) 1D

	static Double_t fake_rate_tau_pt_20(Double_t pt) {

	    Double_t value = 0;

	    if (pt<0) value = 1.0;

	    if (pt<=100){

		//1D

		Double_t mpv=-16.7;
		Double_t  sigma=7.405;
		Double_t costante=0.001794;

		Double_t f=((TMath::Landau(pt,mpv,sigma))+costante);

		value = f;}

	    else{

		value = fake_rate_tau_pt_20(100);}

	    return value;

	}

//////////////FR functions(pt) 3 regions in eta

	static Double_t fake_rate_tau_pt_eta(Double_t pt, Double_t eta) {

	    Double_t value = 0;

	    if (pt<0) value = 1.0;

	    if (pt<=100){

		//eta1

		if (TMath::Abs(eta) < 0.8){

		    Double_t mpv=-5.336;
		    Double_t sigma=4.384;
		    Double_t costante=0.005082;

		    Double_t f1=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f1;}

		//eta2

		if ((TMath::Abs(eta) > 0.8) && (TMath::Abs(eta) < 1.6)){

		    Double_t mpv=-13.71;
		    Double_t  sigma=7.583;
		    Double_t costante=0.0008783;

		    Double_t f2=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f2;}

		//eta3

		if ((TMath::Abs(eta) > 1.6) && (TMath::Abs(eta) < 2.3)){

		    Double_t mpv=-10.54;
		    Double_t  sigma=6.317;
		    Double_t costante=0.009449;

		    Double_t f3=((TMath::Landau(pt,mpv,sigma))+costante);

		    value = f3;}

	    }

	    else{

		value = fake_rate_tau_pt_eta(100,eta);}

	    return value;

	}

//////////////FR function(pt,eta) 10

	static Double_t fake_rate_tau(Double_t pt, Double_t eta) {

	    Double_t value = 0;

	    //if (pt<0) return 1.0;

	    if (pt<=100 && (TMath::Abs(eta) < 2.3)){

		Double_t p_par[14] = {0.411829,-0.330438,3.35952,0.0806,-0.344626,3.1413,0.109505,-0.309343,-0.0359541,0.00541517,-0.000719796,0.00968051,0.000338601,-0.00135203};

		///parametri!!!!

		Double_t p0 = p_par[0]+p_par[1]*eta+p_par[2]*TMath::Power(eta,2)+p_par[3]*TMath::Power(eta,3)+p_par[4]*TMath::Power(eta,4);
		Double_t p1 = p_par[5]+p_par[6]*eta+p_par[7]*TMath::Power(eta,2)+p_par[8]*TMath::Power(eta,3);
		Double_t p2 = p_par[9]+p_par[10]*eta+p_par[11]*TMath::Power(eta,2)+p_par[12]*TMath::Power(eta,3)+p_par[13]*TMath::Power(eta,4);
		Double_t result = TMath::Landau(pt,p0,p1)+p2;

		value = result;

	    }

	    else{

		if (pt>100 && eta < -2.3){

		    value = fake_rate_tau(100,-2.3);}

		if (pt>100 && eta > 2.3){

		    value = fake_rate_tau(100,2.3);}

	    }

	    return value;

	}

}

double corrSSTau(double pt, double eta, int type){

	double value = 1;
	int binPt = (int)pt/20;
	int binEta = (int)(3+eta);

	if(pt >= 100) binPt = 4;

	double matrix_v1[5][6] ={
		{0,0,0,0,0,0},
		{1.55757,1.22742,0.706372,0.764892,1.3528,1.55739},
		{1.92588,1.68548,0.702961,0.679257,1.70985,1.44714},
		{1.96798,2.04543,0.494284,0.690546,1.28928,0.422058},
		{1.28629,4.10797,0.796744,0.610567,0.815997,2.96383}
	};

	double matrix_v2[5][6] ={ 
		{0,0,0,0,0,0},
		{1.16236, 0.999142, 0.919625, 1.00174, 1.10042, 1.16026},
		{1.44367, 1.40675,  0.917275, 0.882521,1.43005, 1.0847},
		{1.28236, 1.55857,  0.585109, 0.812474,0.976749,0.276072},
		{0.743917,2.85922,  0.866117, 0.672947,0.576554,1.74623},
	};

	double matrix_v3[5][6] ={ 
		{0,0,0,0,0,0},
		{1.28604,1.13487,1.05549,1.17374,1.22548,1.40059},
		{0.902857,1.21784,0.893534,0.836269,1.07326,0.74975},
		{0.628427,1.13314,0.504096,0.657499,0.583435,0.147976},
		{0.329319,1.92922,0.698894,0.495738,0.314152,0.843332},
	};

	if(type == 1) value = matrix_v1[binPt][binEta];
	else if(type == 2) value = matrix_v2[binPt][binEta];
	else if(type == 3) value = matrix_v3[binPt][binEta];

	return value;

}

double corrSSTauErr(double pt, double eta, int type){

	double value = 1;
	int binPt = (int)pt/20;
	int binEta = (int)(3+eta);

	if(pt >= 100) binPt = 4;

	double matrix_v1[5][6] ={ 
		{0,0,0,0,0,0},
		{0.194458,0.0836845,0.051853,0.0543301,0.0871463,0.194463},
		{0.485434,0.224845,0.115913,0.111992,0.220512,0.439027},
		{0.989383,0.459975,0.174998,0.20861,0.358866,0.422556},
		{1.28997,1.07033,0.356946,0.305697,0.47197,2.10963},
	};

	double matrix_v2[5][6] ={ 
		{0,0,0,0,0,0},
		{0.145176,0.0681441,0.0675444,0.0711939,0.0709157,0.144936},
		{0.363862,0.187663,0.151269,0.145522,0.184429,0.329052},
		{0.644672,0.350515,0.207162,0.245458,0.271886,0.276395},
		{0.746045,0.745135,0.388044,0.33694,0.333492,1.24295},
	};

	double matrix_v3[5][6] ={ 
		{0,0,0,0,0,0},
		{0.160427,0.0773752,0.077488,0.0833799,0.0789263,0.174772},
		{0.227545,0.162485,0.147336,0.137885,0.138436,0.227457},
		{0.315939,0.254895,0.178474,0.198637,0.162423,0.148152},
		{0.330272,0.502948,0.313116,0.248216,0.181724,0.60034},
	};

	if(type == 1) value = matrix_v1[binPt][binEta];
	else if(type == 2) value = matrix_v2[binPt][binEta];
	else if(type == 3) value = matrix_v3[binPt][binEta];

	return value;

}

std::vector<double> weightCalc(edm::View<reco::CompositeCandidate>::const_iterator CompCand, double a, double b){

	std::vector<double> weightVec;

	const reco::Candidate * WLeptonCand = CompCand->daughter(0); //Candidato leptone dal W
	const reco::Candidate * DiTauCand = CompCand->daughter(1); //Candidato composito DiTau

    	const reco::Candidate * dau1 = DiTauCand->daughter(0); 
    	const reco::Candidate * dau2 = DiTauCand->daughter(1);

	double pt1 = dau1->pt();
	double pt2 = dau2->pt();
	double eta1 = dau1->eta();
	double eta2 = dau2->eta();

  	//const pat::Electron & electron = dynamic_cast<const pat::Electron&>(*WLeptonCand->masterClone());
 	//const pat::Tau & tau1 = dynamic_cast<const pat::Tau&>(*dau1->masterClone());
 	//const pat::Tau & tau2 = dynamic_cast<const pat::Tau&>(*dau2->masterClone());

	bool isEleTau1SS = (((WLeptonCand->charge())*(dau1->charge())) > 0) ? true : false;

	double weightSinglePtParam;
	double weightSinglePt3EtaParam;
	double weightSinglePtEtaParam;

	if(isEleTau1SS){
		
		double value1 = corrSSTau(pt1, eta1, 1);
		double value2 = corrSSTau(pt1, eta1, 2);
		double value3 = corrSSTau(pt1, eta1, 3);

		double value1Up = corrSSTau(pt1, eta1, 1) + corrSSTauErr(pt1, eta1, 1);
		double value2Up = corrSSTau(pt1, eta1, 2) + corrSSTauErr(pt1, eta1, 2);
		double value3Up = corrSSTau(pt1, eta1, 3) + corrSSTauErr(pt1, eta1, 3);

		double value1Down = corrSSTau(pt1, eta1, 1) - corrSSTauErr(pt1, eta1, 1);
		double value2Down = corrSSTau(pt1, eta1, 2) - corrSSTauErr(pt1, eta1, 2);
		double value3Down = corrSSTau(pt1, eta1, 3) - corrSSTauErr(pt1, eta1, 3);

		/*double value1 = 1;
		double value2 = 1;
		double value3 = 1;*/

		weightSinglePtParam     = (a*WJetsTight::fake_rate_tau_pt_20(pt1) + b*ZJetsTight::fake_rate_tau_pt_20(pt1));
		weightSinglePt3EtaParam = (a*WJetsTight::fake_rate_tau_pt_eta(pt1,eta1) + b*ZJetsTight::fake_rate_tau_pt_eta(pt1,eta1));
		weightSinglePtEtaParam  = (a*WJetsTight::fake_rate_tau(pt1,eta1) + b*ZJetsTight::fake_rate_tau(pt1,eta1));

		int binPt = (int)pt1/20;
		int binEta = (int)(3+eta1);
		if(pt1 >= 100) binPt = 4;

		weightVec.push_back(weightSinglePtParam);
		weightVec.push_back(weightSinglePt3EtaParam);
		weightVec.push_back(weightSinglePtEtaParam);
		weightVec.push_back(weightSinglePtParam*value1);
		weightVec.push_back(weightSinglePt3EtaParam*value2);
		weightVec.push_back(weightSinglePtEtaParam*value3);
		weightVec.push_back(weightSinglePtParam*value1Up);
		weightVec.push_back(weightSinglePt3EtaParam*value2Up);
		weightVec.push_back(weightSinglePtEtaParam*value3Up);
		weightVec.push_back(weightSinglePtParam*value1Down);
		weightVec.push_back(weightSinglePt3EtaParam*value2Down);
		weightVec.push_back(weightSinglePtEtaParam*value3Down);

		weightVec.push_back(binPt);
		weightVec.push_back(binEta);

		//if(DiTauCand->mass() > 160 && DiTauCand->mass() < 200) std::cout<<"PT1: "<<pt1<<" Eta1 "<<eta1<<" chargeProd1: "<<isEleTau1SS<<" weight1: "<<weightSinglePtParam<<std::endl;
		//std::cout<<"Normal "<<weightVec[0]<<" NormCorr "<<weightVec[3]<<" Up "<<weightVec[6]<<" Down "<<weightVec[9]<<std::endl;
		//if(DiTauCand->mass() > 160 && DiTauCand->mass() < 200) std::cout<<"Normal "<<weightVec[1]<<" NormCorr "<<weightVec[4]<<" Up "<<weightVec[7]<<" Down "<<weightVec[10]<<std::endl;
		//std::cout<<"Value1 "<<value1<<" Value1Up "<<value1Up<<" Valu1Down "<<value1Down<<std::endl;
		//if(DiTauCand->mass() > 160 && DiTauCand->mass() < 200) std::cout<<"Value2 "<<value2<<" Value2Up "<<value2Up<<" Valu2Down "<<value2Down<<std::endl;
		//std::cout<<corrSSTauErr(pt1, eta1, 1)<<std::endl;

	}
	else{

		double value1 = corrSSTau(pt2, eta2, 1);
		double value2 = corrSSTau(pt2, eta2, 2);
		double value3 = corrSSTau(pt2, eta2, 3);

		double value1Up = corrSSTau(pt2, eta2, 1) + corrSSTauErr(pt2, eta2, 1);
		double value2Up = corrSSTau(pt2, eta2, 2) + corrSSTauErr(pt2, eta2, 2);
		double value3Up = corrSSTau(pt2, eta2, 3) + corrSSTauErr(pt2, eta2, 3);

		double value1Down = corrSSTau(pt2, eta2, 1) - corrSSTauErr(pt2, eta2, 1);
		double value2Down = corrSSTau(pt2, eta2, 2) - corrSSTauErr(pt2, eta2, 2);
		double value3Down = corrSSTau(pt2, eta2, 3) - corrSSTauErr(pt2, eta2, 3);

		/*double value1 = 1;
		double value2 = 1;
		double value3 = 1;*/

		weightSinglePtParam     = (a*WJetsMedium::fake_rate_tau_pt_20(pt2) + b*ZJetsMedium::fake_rate_tau_pt_20(pt2));
		weightSinglePt3EtaParam = (a*WJetsMedium::fake_rate_tau_pt_eta(pt2,eta2) + b*ZJetsMedium::fake_rate_tau_pt_eta(pt2,eta2));
		weightSinglePtEtaParam  = (a*WJetsMedium::fake_rate_tau(pt2,eta2) + b*ZJetsMedium::fake_rate_tau(pt2,eta2));

		int binPt = (int)pt2/20;
		int binEta = (int)(3+eta2);
		if(pt2 >= 100) binPt = 4;

		weightVec.push_back(weightSinglePtParam);
		weightVec.push_back(weightSinglePt3EtaParam);
		weightVec.push_back(weightSinglePtEtaParam);
		weightVec.push_back(weightSinglePtParam*value1);
		weightVec.push_back(weightSinglePt3EtaParam*value2);
		weightVec.push_back(weightSinglePtEtaParam*value3);
		weightVec.push_back(weightSinglePtParam*value1Up);
		weightVec.push_back(weightSinglePt3EtaParam*value2Up);
		weightVec.push_back(weightSinglePtEtaParam*value3Up);
		weightVec.push_back(weightSinglePtParam*value1Down);
		weightVec.push_back(weightSinglePt3EtaParam*value2Down);
		weightVec.push_back(weightSinglePtEtaParam*value3Down);

		weightVec.push_back(binPt);
		weightVec.push_back(binEta);

		//if(DiTauCand->mass() > 160 && DiTauCand->mass() < 200) std::cout<<"PT2: "<<pt2<<" Eta2 "<<eta2<<" chargeProd2: "<<isEleTau1SS<<" weight2: "<<weightSinglePtParam<<std::endl;
		//std::cout<<"Normal "<<weightVec[0]<<" NormCorr "<<weightVec[3]<<" Up "<<weightVec[6]<<" Down "<<weightVec[9]<<std::endl;
		//if(DiTauCand->mass() > 160 && DiTauCand->mass() < 200) std::cout<<"Normal "<<weightVec[1]<<" NormCorr "<<weightVec[4]<<" Up "<<weightVec[7]<<" Down "<<weightVec[10]<<std::endl;
		//std::cout<<"Value1 "<<value1<<" Value1Up "<<value1Up<<" Valu1Down "<<value1Down<<std::endl;
		//if(DiTauCand->mass() > 160 && DiTauCand->mass() < 200) std::cout<<"Value2 "<<value2<<" Value2Up "<<value2Up<<" Valu2Down "<<value2Down<<std::endl;
		//std::cout<<corrSSTauErr(pt1, eta1, 1)<<std::endl;

	}

	return weightVec;	

}

//
// static data member definitions
//

//
// constructors and destructor
//
CompositeCandHistManager::CompositeCandHistManager(const edm::ParameterSet& iConfig):
  histContainer_(),
  histContainer2D_(),
  CompCandSrc_(iConfig.getUntrackedParameter<edm::InputTag>("CompCandSrc")),
  //muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
  //eleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("eleSrc")),
  //tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc")),
  PFMetTag_(iConfig.getUntrackedParameter<edm::InputTag> ("PFMetTag")),
  MCDist_f_(iConfig.getUntrackedParameter<vdouble>("MCDist")),
  TrueDist2011_f_(iConfig.getUntrackedParameter<vdouble>("TrueDist2011")),
  isMC_(iConfig.getUntrackedParameter<bool>("isMC")),
  isFR_(iConfig.getUntrackedParameter<int>("isFR",0)),
  wjetsCoeff_(iConfig.getUntrackedParameter<double>("wjetsCoeff",0.6666666)),
  zjetsCoeff_(iConfig.getUntrackedParameter<double>("zjetsCoeff",0.3333333))
{
   //now do what ever initialization is needed

}


CompositeCandHistManager::~CompositeCandHistManager()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
CompositeCandHistManager::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;

/////////////////////////////////////////////////////////////

  double weight = 1;

  if(isMC_){

	  edm::Handle<std::vector< PileupSummaryInfo > >  PupInfo;
	  iEvent.getByLabel(edm::InputTag("addPileupInfo"), PupInfo);

	  std::vector<PileupSummaryInfo>::const_iterator PVI;

	  //int npv = -1;
	  int nti = -1;
	  for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI) {

		  /*int BX = PVI->getBunchCrossing();

		  if(BX == 0) { 
		     	npv = PVI->getPU_NumInteractions();
		     	continue;
		   	}*/

	  nti = PVI->getTrueNumInteractions();
	  }

	  weight = LumiWeights_.weight( nti );

  }

/////////////////////////////////////////////////////////////

  edm::Handle<edm::View<reco::CompositeCandidate> > CompCandidates;
  iEvent.getByLabel(CompCandSrc_, CompCandidates);

  edm::Handle<pat::METCollection> pfmet;
  iEvent.getByLabel(PFMetTag_, pfmet);

  double met = pfmet->front().et();

  double weightTot = 1;

  if(isFR_){

  	double weightFR1 = 0;
  	double weightFR2 = 0;
  	double weightFR3 = 0;

  	for(edm::View<reco::CompositeCandidate>::const_iterator CompCand=CompCandidates->begin(); CompCand!=CompCandidates->end(); ++CompCand){

		vdouble weightSingleCand = weightCalc(CompCand, wjetsCoeff_, zjetsCoeff_);
		weightFR1 += (weightSingleCand[0]/(1 - weightSingleCand[0]));
		weightFR2 += (weightSingleCand[1]/(1 - weightSingleCand[1]));
		weightFR3 += (weightSingleCand[2]/(1 - weightSingleCand[2]));

  	}

	histContainer_["weightLep_1"]->Fill(weightFR1);
	histContainer_["weightLep_2"]->Fill(weightFR2);
	histContainer_["weightLep_3"]->Fill(weightFR3);

	if(isFR_ == 1) weightTot = weightFR1;
	else if(isFR_ == 2) weightTot = weightFR2;
	else if(isFR_ == 3) weightTot = weightFR3;

  }

  std::vector<double> WLepCandPtVec;
  std::vector<double> DiTauCand1PtVec;
  std::vector<double> DiTauCand2PtVec;

  for(edm::View<reco::CompositeCandidate>::const_iterator CompCand=CompCandidates->begin(); CompCand!=CompCandidates->end(); ++CompCand){

	double weightTotEvt = 1;
	double weightTotEvtCorr = 1;
	double weightTotEvtUp = 1;
	double weightTotEvtDown = 1;

	int binPt = 0;
	int binEta = 0;

  	if(isFR_){

		double weightFR1 = 0;
  		double weightFR2 = 0;
  		double weightFR3 = 0;

		double weightFR1Corr = 0;
  		double weightFR2Corr = 0;
  		double weightFR3Corr = 0;

		double weightFR1Up = 0;
  		double weightFR2Up = 0;
  		double weightFR3Up = 0;

		double weightFR1Down = 0;
  		double weightFR2Down = 0;
  		double weightFR3Down = 0;

		vdouble weightSingleCand = weightCalc(CompCand, wjetsCoeff_, zjetsCoeff_);
		weightFR1 += (weightSingleCand[0]/(1 - weightSingleCand[0]));
		weightFR2 += (weightSingleCand[1]/(1 - weightSingleCand[1]));
		weightFR3 += (weightSingleCand[2]/(1 - weightSingleCand[2]));

		weightFR1Corr += (weightSingleCand[3]/(1 - weightSingleCand[3]));
		weightFR2Corr += (weightSingleCand[4]/(1 - weightSingleCand[4]));
		weightFR3Corr += (weightSingleCand[5]/(1 - weightSingleCand[5]));

		weightFR1Up += (weightSingleCand[6]/(1 - weightSingleCand[6]));
		weightFR2Up += (weightSingleCand[7]/(1 - weightSingleCand[7]));
		weightFR3Up += (weightSingleCand[8]/(1 - weightSingleCand[8]));

		weightFR1Down += (weightSingleCand[9]/(1 - weightSingleCand[9]));
		weightFR2Down += (weightSingleCand[10]/(1 - weightSingleCand[10]));
		weightFR3Down += (weightSingleCand[11]/(1 - weightSingleCand[11]));

		binPt = weightSingleCand[12];
		binEta = weightSingleCand[13];

		if(isFR_ == 1){

		 	weightTotEvt = weightFR1;
		 	weightTotEvtCorr = weightFR1Corr;
		 	weightTotEvtUp = weightFR1Up;
		 	weightTotEvtDown = weightFR1Down;

		}
		else if(isFR_ == 2){
		 
			weightTotEvt = weightFR2;
		 	weightTotEvtCorr = weightFR2Corr;
		 	weightTotEvtUp = weightFR2Up;
		 	weightTotEvtDown = weightFR2Down;

		}
		else if(isFR_ == 3){

			weightTotEvt = weightFR3;
		 	weightTotEvtCorr = weightFR3Corr;
		 	weightTotEvtUp = weightFR3Up;
		 	weightTotEvtDown = weightFR3Down;

		}

  	}

	const reco::Candidate * WLeptonCand = CompCand->daughter(0); //Candidato leptone dal W
	const reco::Candidate * DiTauCand = CompCand->daughter(1); //Candidato composito DiTau

	const reco::Candidate * dau1 = DiTauCand->daughter(0); 
	const reco::Candidate * dau2 = DiTauCand->daughter(1);

 	const pat::Tau & tau1 = dynamic_cast<const pat::Tau&>(*dau1->masterClone());
 	const pat::Tau & tau2 = dynamic_cast<const pat::Tau&>(*dau2->masterClone());

	int trigMatch1 = tau1.triggerObjectMatchByPath("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*") || tau1.triggerObjectMatchByPath("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*");
	int trigMatch2 = tau2.triggerObjectMatchByPath("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*") || tau2.triggerObjectMatchByPath("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*");

	histContainer_["trigMatch1"]->Fill(trigMatch1);
	histContainer_["trigMatch2"]->Fill(trigMatch2);

	double DiTauCand1Et = DiTauCand->daughter(0)->et(); //Et primo membro della coppia DiTau
	double DiTauCand2Et = DiTauCand->daughter(1)->et(); //Et secondo membro della coppia DiTau
	double WLeptonCandEt = WLeptonCand->et();
	double TotEt = WLeptonCandEt + DiTauCand1Et + DiTauCand2Et;
	histContainer_["hLt"]->Fill(TotEt, weight*weightTotEvt);

	int DiTauCand1Charge = DiTauCand->daughter(0)->charge(); //Carica del primo membro della coppia DiTau
	int DiTauCand2Charge = DiTauCand->daughter(1)->charge(); //Carica del secondo membro della coppia DiTau
	int WLeptonCandCharge = WLeptonCand->charge();
	int WLeptonDiTauCand1Charge = WLeptonCandCharge + DiTauCand1Charge;
	int WLeptonDiTauCand2Charge = WLeptonCandCharge + DiTauCand2Charge;

	double DiTauCand1Pt = DiTauCand->daughter(0)->pt(); //Carica del primo membro della coppia DiTau
	double DiTauCand2Pt = DiTauCand->daughter(1)->pt(); //Carica del secondo membro della coppia DiTau
	double WLeptonCandPt = WLeptonCand->pt();
	bool mostEnergetic = DiTauCand1Pt > DiTauCand2Pt ? true : false;
	//std::cout<<"ElePt "<<WLeptonCandPt<<" Tau1Pt "<<DiTauCand1Pt<<" Tau2Pt "<<DiTauCand2Pt<<std::endl;

	bool includeEle = false;
	bool includeTau1 = false;
	bool includeTau2 = false;

	if(WLepCandPtVec.size() > 0 && isFR_ == 0){

		includeEle = std::find(WLepCandPtVec.begin(), WLepCandPtVec.end(), WLeptonCandPt)!=WLepCandPtVec.end();
		includeTau1 = std::find(DiTauCand1PtVec.begin(), DiTauCand1PtVec.end(), DiTauCand1Pt)!=DiTauCand1PtVec.end();
		includeTau2 = std::find(DiTauCand2PtVec.begin(), DiTauCand2PtVec.end(), DiTauCand2Pt)!=DiTauCand2PtVec.end();

	}

	double DiTauCand1Eta = DiTauCand->daughter(0)->eta(); //Carica del primo membro della coppia DiTau
	double DiTauCand2Eta = DiTauCand->daughter(1)->eta(); //Carica del secondo membro della coppia DiTau
	double WLeptonCandEta = WLeptonCand->eta();

	double DiTauCand1Phi = DiTauCand->daughter(0)->phi(); //Carica del primo membro della coppia DiTau
	double DiTauCand2Phi = DiTauCand->daughter(1)->phi(); //Carica del secondo membro della coppia DiTau
	double WLeptonCandPhi = WLeptonCand->phi();

	double massWLeptonDiTauCand1 = (WLeptonCand->p4() + DiTauCand->daughter(0)->p4()).M();
	double massWLeptonDiTauCand2 = (WLeptonCand->p4() + DiTauCand->daughter(1)->p4()).M();
	double massHiggs = (DiTauCand->daughter(0)->p4() + DiTauCand->daughter(1)->p4()).M();

	if(WLeptonDiTauCand1Charge == 0){//Tau1 real (OS), Tau2 fakeable (SS) 

		histContainer_["hMassWLeptonTauOS"]->Fill(massWLeptonDiTauCand1, weight*weightTotEvt);
		histContainer_["hMassWLeptonTauSS"]->Fill(massWLeptonDiTauCand2, weight*weightTotEvt);

		histContainer_["hDiTauCandOSPt"]->Fill(DiTauCand1Pt, weight*weightTotEvt);
   		histContainer_["hDiTauCandOSEta"]->Fill(DiTauCand1Eta, weight*weightTotEvt);
		histContainer_["hDiTauCandSSPt"]->Fill(DiTauCand2Pt, weight*weightTotEvt);
   		histContainer_["hDiTauCandSSEta"]->Fill(DiTauCand2Eta, weight*weightTotEvt);

		histContainer_["hDiTauCandSSPtCorr"]->Fill(DiTauCand2Pt, weight*weightTotEvtCorr);
   		histContainer_["hDiTauCandSSEtaCorr"]->Fill(DiTauCand2Eta, weight*weightTotEvtCorr);

   		histContainer2D_["hDiTauCandOSEtaVsPt"]->Fill(DiTauCand1Pt, DiTauCand1Eta, weight*weightTotEvt);
   		histContainer2D_["hDiTauCandSSEtaVsPt"]->Fill(DiTauCand2Pt, DiTauCand2Eta, weight*weightTotEvt);

		if(isFR_ == 0){

			histContainer_["hDiTauCandOSAntiTightIso"]->Fill(tau1.tauID("byTightCombinedIsolationDeltaBetaCorr"), weight*weightTotEvt);
			histContainer_["hDiTauCandSSMediumIso"]->Fill(tau2.tauID("byMediumCombinedIsolationDeltaBetaCorr"), weight*weightTotEvt);

		}
		else{
		
			histContainer_["hDiTauCandOSAntiTightIso"]->Fill(tau1.tauID("byTightCombinedIsolationDeltaBetaCorr"), weight*weightTotEvt);
			histContainer_["hDiTauCandSSAntiMediumIso"]->Fill(tau2.tauID("byMediumCombinedIsolationDeltaBetaCorr"), weight*weightTotEvt);

		}

	}
	else{//Tau1 fakeable (SS), Tau2 real (OS) 

		histContainer_["hMassWLeptonTauOS"]->Fill(massWLeptonDiTauCand2, weight*weightTotEvt);
		histContainer_["hMassWLeptonTauSS"]->Fill(massWLeptonDiTauCand1, weight*weightTotEvt);

		histContainer_["hDiTauCandOSPt"]->Fill(DiTauCand2Pt, weight*weightTotEvt);
   		histContainer_["hDiTauCandOSEta"]->Fill(DiTauCand2Eta, weight*weightTotEvt);
		histContainer_["hDiTauCandSSPt"]->Fill(DiTauCand1Pt, weight*weightTotEvt);
   		histContainer_["hDiTauCandSSEta"]->Fill(DiTauCand1Eta, weight*weightTotEvt);

		histContainer_["hDiTauCandSSPtCorr"]->Fill(DiTauCand2Pt, weight*weightTotEvtCorr);
   		histContainer_["hDiTauCandSSEtaCorr"]->Fill(DiTauCand2Eta, weight*weightTotEvtCorr);

   		histContainer2D_["hDiTauCandOSEtaVsPt"]->Fill(DiTauCand2Pt, DiTauCand2Eta, weight*weightTotEvt);
   		histContainer2D_["hDiTauCandSSEtaVsPt"]->Fill(DiTauCand1Pt, DiTauCand1Eta, weight*weightTotEvt);

		if(isFR_ == 0){

			histContainer_["hDiTauCandSSTightIso"]->Fill(tau1.tauID("byTightCombinedIsolationDeltaBetaCorr"), weight*weightTotEvt);
			histContainer_["hDiTauCandOSAntiMediumIso"]->Fill(tau2.tauID("byMediumCombinedIsolationDeltaBetaCorr"), weight*weightTotEvt);

		}
		else{
		
			histContainer_["hDiTauCandSSAntiTightIso"]->Fill(tau1.tauID("byTightCombinedIsolationDeltaBetaCorr"), weight*weightTotEvt);
			histContainer_["hDiTauCandOSAntiMediumIso"]->Fill(tau2.tauID("byMediumCombinedIsolationDeltaBetaCorr"), weight*weightTotEvt);

		}

	}

	double higgsPt = DiTauCand->pt(); //Pt of the Higgs candidate

        double scalarSumPt = (WLeptonCand->p4()).Et() + ((*pfmet)[0].p4()).Et();
        double vectorSumPt = (WLeptonCand->p4() + (*pfmet)[0].p4()).Pt() ;
        double Mt = TMath::Sqrt( scalarSumPt*scalarSumPt - vectorSumPt*vectorSumPt );
	//std::cout<<"Mt: "<<Mt<<std::endl; 

	if(!includeEle) histContainer2D_["hMtMet"]->Fill(Mt, met, weight*weightTotEvt);

	double phiTau1 = deltaPhi(DiTauCand1Phi,WLeptonCandPhi);
	double cosTau1 = cos(phiTau1);
	double phiTau2 = deltaPhi(DiTauCand2Phi,WLeptonCandPhi);
	double cosTau2 = cos(phiTau2);

	//double metPt = (*pfmet)[0].pt();
	//double metPhi = (*pfmet)[0].phi();
	//double metEt = (*pfmet)[0].et();
	//double Mt2 = TMath::Sqrt((2*WLeptonCandPt*metEt)*(1-TMath::Cos(deltaPhi(metPhi,WLeptonCandPhi))));
	//std::cout<<"lepPt: "<<WLeptonCandPt<<" lepEt: "<<WLeptonCandEt<<std::endl; 
	//std::cout<<"metPt: "<<metPt<<" metEt: "<<metEt<<std::endl; 
	//std::cout<<"Mt: "<<Mt<<" Mt2: "<<Mt2<<std::endl; 

	histContainer_["hWLeptonTau1Charge"]->Fill(WLeptonDiTauCand1Charge, weight*weightTotEvt);
	histContainer_["hWLeptonTau2Charge"]->Fill(WLeptonDiTauCand2Charge, weight*weightTotEvt);

	histContainer2D_["metVsDiTauMass"]->Fill(massHiggs, met, weight*weightTotEvt);

	if(mostEnergetic){ 
		histContainer_["hWLeptonLeadTauCharge"]->Fill(WLeptonDiTauCand1Charge, weight*weightTotEvt);
		histContainer_["hWLeptonSubLeadTauCharge"]->Fill(WLeptonDiTauCand2Charge, weight*weightTotEvt);

		histContainer_["hMassWLeptonLeadTau"]->Fill(massWLeptonDiTauCand1, weight*weightTotEvt);
		histContainer_["hMassWLeptonSubLeadTau"]->Fill(massWLeptonDiTauCand2, weight*weightTotEvt);

		histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]->Fill(massWLeptonDiTauCand1, higgsPt, weight*weightTotEvt);
		histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]->Fill(massWLeptonDiTauCand2, higgsPt, weight*weightTotEvt);

		histContainer2D_["hMassWLeptonLeadTauVsMET"]->Fill(massWLeptonDiTauCand1, met, weight*weightTotEvt);
		histContainer2D_["hMassWLeptonSubLeadTauVsMET"]->Fill(massWLeptonDiTauCand2, met, weight*weightTotEvt);

		histContainer_["hCosDPhiELeadTau"]->Fill(cosTau1, weight*weightTotEvt);
		histContainer2D_["hCosDPhiELeadTauVsMT"]->Fill(Mt, cosTau1, weight*weightTotEvt);
		histContainer_["hCosDPhiESubLeadTau"]->Fill(cosTau2, weight*weightTotEvt);
		histContainer2D_["hCosDPhiESubLeadTauVsMT"]->Fill(Mt, cosTau2, weight*weightTotEvt);

		histContainer2D_["ptVsDiTauMassLead"]->Fill(massHiggs, DiTauCand1Pt, weight*weightTotEvt);
		histContainer2D_["ptVsDiTauMassSubLead"]->Fill(massHiggs, DiTauCand2Pt, weight*weightTotEvt);
	}
	else{
 		histContainer_["hWLeptonLeadTauCharge"]->Fill(WLeptonDiTauCand2Charge, weight*weightTotEvt);
 		histContainer_["hWLeptonSubLeadTauCharge"]->Fill(WLeptonDiTauCand1Charge, weight*weightTotEvt);

		histContainer_["hMassWLeptonLeadTau"]->Fill(massWLeptonDiTauCand2, weight*weightTotEvt);
		histContainer_["hMassWLeptonSubLeadTau"]->Fill(massWLeptonDiTauCand1, weight*weightTotEvt);

		histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]->Fill(massWLeptonDiTauCand2, higgsPt, weight*weightTotEvt);
		histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]->Fill(massWLeptonDiTauCand1, higgsPt, weight*weightTotEvt);

		histContainer2D_["hMassWLeptonLeadTauVsMET"]->Fill(massWLeptonDiTauCand2, met, weight*weightTotEvt);
		histContainer2D_["hMassWLeptonSubLeadTauVsMET"]->Fill(massWLeptonDiTauCand1, met, weight*weightTotEvt);

		histContainer_["hCosDPhiELeadTau"]->Fill(cosTau2, weight*weightTotEvt);
		histContainer2D_["hCosDPhiELeadTauVsMT"]->Fill(Mt, cosTau2, weight*weightTotEvt);
		histContainer_["hCosDPhiESubLeadTau"]->Fill(cosTau1, weight*weightTotEvt);
		histContainer2D_["hCosDPhiESubLeadTauVsMT"]->Fill(Mt, cosTau1, weight*weightTotEvt);

		histContainer2D_["ptVsDiTauMassLead"]->Fill(massHiggs, DiTauCand2Pt, weight*weightTotEvt);
		histContainer2D_["ptVsDiTauMassSubLead"]->Fill(massHiggs, DiTauCand1Pt, weight*weightTotEvt);
	}

   	if(!includeTau1){

		histContainer_["hDiTauCand1Pt"]->Fill(DiTauCand1Pt, weight*weightTotEvt);
   		histContainer_["hDiTauCand1Eta"]->Fill(DiTauCand1Eta, weight*weightTotEvt);
   		histContainer_["hDiTauCand1Phi"]->Fill(DiTauCand1Phi, weight*weightTotEvt);

	}

   	if(!includeTau2){

   		histContainer_["hDiTauCand2Pt"]->Fill(DiTauCand2Pt, weight*weightTotEvt);
   		histContainer_["hDiTauCand2Eta"]->Fill(DiTauCand2Eta, weight*weightTotEvt);
   		histContainer_["hDiTauCand2Phi"]->Fill(DiTauCand2Phi, weight*weightTotEvt);

	}

   	if(!includeEle){

   		histContainer_["hWLepCandPt"]->Fill(WLeptonCandPt, weight*weightTotEvt);
   		histContainer_["hWLepCandEta"]->Fill(WLeptonCandEta, weight*weightTotEvt);
   		histContainer_["hWLepCandPhi"]->Fill(WLeptonCandPhi, weight*weightTotEvt);
		histContainer_["MTeMET"]->Fill(Mt, weight*weightTotEvt);

	}

   	histContainer_["VisMass"]->Fill(massHiggs, weight*weightTotEvt);
   	histContainer_["VisMassCorr"]->Fill(massHiggs, weight*weightTotEvtCorr);
   	histContainer_["VisMassUp"]->Fill(massHiggs, weight*weightTotEvtUp);
   	histContainer_["VisMassDown"]->Fill(massHiggs, weight*weightTotEvtDown);

	std::stringstream nome1;
	std::stringstream nome2;
	std::stringstream nome3;

	nome1 << "VisMassCorr" << (int)binPt << (int)binEta;
	nome2 << "VisMassUp" << (int)binPt << (int)binEta;
	nome3 << "VisMassDown" << (int)binPt << (int)binEta;

	//std::cout<<nome1.str()<<" "<<nome2.str()<<" "<<nome3.str()<<std::endl;

	histContainer_[nome1.str()]->Fill(massHiggs, weight*weightTotEvtCorr);
   	histContainer_[nome2.str()]->Fill(massHiggs, weight*weightTotEvtUp);
   	histContainer_[nome3.str()]->Fill(massHiggs, weight*weightTotEvtDown);

	histContainer_["hCosDPhiETau1"]->Fill(cosTau1, weight*weightTotEvt);
	histContainer_["hCosDPhiETau2"]->Fill(cosTau2, weight*weightTotEvt);

	WLepCandPtVec.push_back(WLeptonCandPt);
	DiTauCand1PtVec.push_back(DiTauCand1Pt);
	DiTauCand2PtVec.push_back(DiTauCand2Pt);

  }

  histContainer_["MET"]->Fill(met, weight*weightTot);

  double count = 1.;
  histContainer_["N_eventi"]->Fill(count);
  histContainer_["N_eventi_PU"]->Fill(count, weight*weightTot);

  histContainer_["CompCand_mult"]->Fill(CompCandidates->size(), weight*weightTot);

}


// ------------ method called once each job just before starting event loop  ------------
void 
CompositeCandHistManager::beginJob()
{
  // register to the TFileService
  edm::Service<TFileService> fs;
  TH1::SetDefaultSumw2();

  histContainer_["hDiTauCandOSAntiTightIso"]=fs->make<TH1F>("DiTauCandOSAntiTightIso", "DiTauCandOSAntiTightIso", 2, -0.5, 1.5);
  histContainer_["hDiTauCandSSMediumIso"]=fs->make<TH1F>("DiTauCandSSMediumIso", "DiTauCandSSMediumIso", 2, -0.5, 1.5);
  histContainer_["hDiTauCandSSAntiMediumIso"]=fs->make<TH1F>("DiTauCandSSAntiMediumIso", "DiTauCandSSAntiMediumIso", 2, -0.5, 1.5);

  histContainer_["hDiTauCandSSTightIso"]=fs->make<TH1F>("DiTauCandSSTightIso", "DiTauCandSSTightIso", 2, -0.5, 1.5);
  histContainer_["hDiTauCandOSAntiMediumIso"]=fs->make<TH1F>("DiTauCandOSAntiMediumIso", "DiTauCandOSAntiMediumIso", 2, -0.5, 1.5);
  histContainer_["hDiTauCandSSAntiTightIso"]=fs->make<TH1F>("DiTauCandSSAntiTightIso", "DiTauCandSSAntiTightIso", 2, -0.5, 1.5);

  histContainer_["N_eventi"]=fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
  histContainer_["N_eventi_PU"]=fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);
  histContainer_["CompCand_mult"]=fs->make<TH1F>("CompCand_mult", "size", 20, 0.5,  20.5);

  histContainer_["weightLep_1"]=fs->make<TH1F>("weightLep_1", "weightLep_1", 50, 0., 0.1);
  histContainer_["weightLep_2"]=fs->make<TH1F>("weightLep_2", "weightLep_2", 50, 0., 0.1);
  histContainer_["weightLep_3"]=fs->make<TH1F>("weightLep_3", "weightLep_3", 50, 0., 0.1);

  histContainer_["trigMatch1"]=fs->make<TH1F>("trigMatch1", "trigMatch1", 2, 0, 2);
  histContainer_["trigMatch2"]=fs->make<TH1F>("trigMatch2", "trigMatch2", 2, 0, 2);

  histContainer_["hDiTauCand1Pt"]=fs->make<TH1F>("DiTauCand1Pt", "DiTauCand1Pt", 25, 0, 100);
  histContainer_["hDiTauCand1Eta"]=fs->make<TH1F>("DiTauCand1Eta", "DiTauCand1Eta",  24, -3,  3);
  histContainer_["hDiTauCand1Phi"]=fs->make<TH1F>("DiTauCand1Phi", "DiTauCand1Phi",  36,   -TMath::Pi(), +TMath::Pi());

  histContainer_["hDiTauCand2Pt"]=fs->make<TH1F>("DiTauCand2Pt", "DiTauCand2Pt", 25, 0, 100);
  histContainer_["hDiTauCand2Eta"]=fs->make<TH1F>("DiTauCand2Eta", "DiTauCand2Eta",  24, -3,  3);
  histContainer_["hDiTauCand2Phi"]=fs->make<TH1F>("DiTauCand2Phi", "DiTauCand2Phi",  36,   -TMath::Pi(), +TMath::Pi());

  histContainer_["hDiTauCandOSPt"]=fs->make<TH1F>("DiTauCandOSPt", "DiTauCandOSPt", 25, 0, 100);
  histContainer_["hDiTauCandOSEta"]=fs->make<TH1F>("DiTauCandOSEta", "DiTauCandOSEta",  24, -3,  3);

  histContainer_["hDiTauCandSSPt"]=fs->make<TH1F>("DiTauCandSSPt", "DiTauCandSSPt", 25, 0, 100);
  histContainer_["hDiTauCandSSEta"]=fs->make<TH1F>("DiTauCandSSEta", "DiTauCandSSEta",  24, -3,  3);

  histContainer_["hDiTauCandSSPtCorr"]=fs->make<TH1F>("DiTauCandSSPtCorr", "DiTauCandSSPt", 25, 0, 100);
  histContainer_["hDiTauCandSSEtaCorr"]=fs->make<TH1F>("DiTauCandSSEtaCorr", "DiTauCandSSEta",  24, -3,  3);

  histContainer2D_["hDiTauCandOSEtaVsPt"]=fs->make<TH2F>("hDiTauCandOSEtaVsPt", "hDiTauCandOSEtaVsPt", 25, 0, 100, 24, -3,  3);
  histContainer2D_["hDiTauCandSSEtaVsPt"]=fs->make<TH2F>("hDiTauCandSSEtaVsPt", "hDiTauCandSSEtaVsPt", 25, 0, 100, 24, -3,  3);

  histContainer_["hWLepCandPt"]=fs->make<TH1F>("WLepCandPt", "WLepCandPt", 25, 0, 100);
  histContainer_["hWLepCandEta"]=fs->make<TH1F>("WLepCandEta", "WLepCandEta",  24, -3,  3);
  histContainer_["hWLepCandPhi"]=fs->make<TH1F>("WLepCandPhi", "WLepCandPhi",  36,   -TMath::Pi(), +TMath::Pi());

  histContainer_["VisMass"]=fs->make<TH1F>("VisMass", "mass", 10, 0., 400.);
  histContainer_["VisMassCorr"]=fs->make<TH1F>("VisMassCorr", "mass", 10, 0., 400.);
  histContainer_["VisMassUp"]=fs->make<TH1F>("VisMassUp", "mass", 10, 0., 400.);
  histContainer_["VisMassDown"]=fs->make<TH1F>("VisMassDown", "mass", 10, 0., 400.);

  for(int i = 0; i < 5; i++){

	for(int j = 0; j < 6 ; j++){

		std::stringstream name1;
		std::stringstream name2;
		std::stringstream name3;

		name1 << "VisMassCorr" << i << j;
		name2 << "VisMassUp" << i << j;
		name3 << "VisMassDown" << i << j;

		std::string s1 = name1.str();
		std::string s2 = name2.str();
		std::string s3 = name3.str();

		//std::cout<<name1.str()<<" "<<name2.str()<<" "<<name3.str()<<std::endl;

  		histContainer_[name1.str()]=fs->make<TH1F>(s1.c_str(), "mass", 10, 0., 400.);
  		histContainer_[name2.str()]=fs->make<TH1F>(s2.c_str(), "mass", 10, 0., 400.);
  		histContainer_[name3.str()]=fs->make<TH1F>(s3.c_str(), "mass", 10, 0., 400.);

	}

  } 

  histContainer_["MTeMET"]=fs->make<TH1F>("MTeMET", "MTeMET", 25, 0., 200.);

  histContainer_["hCosDPhiETau1"]=fs->make<TH1F>("cosTau1", "cosTau1", 50, -1, 1);
  histContainer_["hCosDPhiETau2"]=fs->make<TH1F>("cosTau2", "cosTau2", 50, -1, 1);
  histContainer_["hCosDPhiELeadTau"]=fs->make<TH1F>("cosLeadTau", "cosLeadTau", 50, -1, 1);
  histContainer_["hCosDPhiESubLeadTau"]=fs->make<TH1F>("cosSubLeadTau", "cosSubLeadTau2", 50, -1, 1);
  histContainer2D_["hCosDPhiELeadTauVsMT"]=fs->make<TH2F>("CosDPhiELeadTauVsMT", "CosDPhiELeadTauVsMT", 25, 0., 200., 50, -1, 1);
  histContainer2D_["hCosDPhiESubLeadTauVsMT"]=fs->make<TH2F>("CosDPhiESubLeadTauVsMT", "CosDPhiESubLeadTauVsMT", 25, 0., 200., 50, -1, 1);

  histContainer2D_["hMtMet"]=fs->make<TH2F>("MtMet", "MtMet", 25, 0., 200., 40, 0., 200.);

  histContainer_["MET"]=fs->make<TH1F>("MET", "met", 50, 0, 200);
  histContainer_["hLt"]=fs->make<TH1F>("Lt", "Lt", 50, 0,200);

  histContainer_["hWLeptonLeadTauCharge"]=fs->make<TH1F>("WLeptonLeadTauCharge", "WLeptonLeadTauCharge", 7, -3.5, +3.5);
  histContainer_["hWLeptonSubLeadTauCharge"]=fs->make<TH1F>("WLeptonSubLeadTauCharge", "WLeptonSubLeadTauCharge", 7, -3.5, +3.5);
  histContainer_["hWLeptonTau1Charge"]=fs->make<TH1F>("WLeptonTau1Charge", "WLeptonTau1Charge", 7, -3.5, +3.5);
  histContainer_["hWLeptonTau2Charge"]=fs->make<TH1F>("WLeptonTau2Charge", "WLeptonTau2Charge", 7, -3.5, +3.5);
  //histContainer_["hVertexChi2NDOF"]=fs->make<TH1F>("VertexChi2NDOF", "VertexChi2NDOF",20, 0, 30);
  histContainer_["hMassWLeptonLeadTau"]=fs->make<TH1F>("MassWLeptonLeadTau", "MassWLeptonLeadTau", 30, 0., 300.);
  histContainer_["hMassWLeptonSubLeadTau"]=fs->make<TH1F>("MassWLeptonSubLeadTau", "MassWLeptonSubLeadTau", 30, 0., 300.);
  histContainer_["hMassWLeptonTauSS"]=fs->make<TH1F>("hMassWLeptonTauSS", "hMassWLeptonTauSS", 60, 0., 300.);
  histContainer_["hMassWLeptonTauOS"]=fs->make<TH1F>("hMassWLeptonTauOS", "hMassWLeptonTauOS", 60, 0., 300.);

  histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]=fs->make<TH2F>("MassWLeptonLeadTauVsPtHiggs", "MassWLeptonLeadTauVsPtHiggs", 30, 0., 300., 50, 0., 200.);
  histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]=fs->make<TH2F>("MassWLeptonSubLeadTauPtVsHiggs", "MassWLeptonSubLeadTauVsPtHiggs", 30, 0., 300., 50, 0., 200.);

  histContainer2D_["hMassWLeptonLeadTauVsMET"]=fs->make<TH2F>("MassWLeptonLeadTauVsMET", "MassWLeptonLeadTauVsMET", 30, 0., 300., 40, 0., 200.);
  histContainer2D_["hMassWLeptonSubLeadTauVsMET"]=fs->make<TH2F>("MassWLeptonSubLeadTauVsMET", "MassWLeptonSubLeadTauVsMET", 30, 0., 300., 40, 0., 200.);

  histContainer2D_["ptVsDiTauMassLead"]=fs->make<TH2F>("ptVsDiTauMassLead", "ptVsDiTauMassLead", 300, 0., 300., 200, 0., 200.);
  histContainer2D_["ptVsDiTauMassSubLead"]=fs->make<TH2F>("ptVsDiTauMassSubLead", "ptVsDiTauMassSubLead", 300, 0., 300., 200, 0., 200.);
  histContainer2D_["metVsDiTauMass"]=fs->make<TH2F>("metVsDiTauMass", "metVsDiTauMass", 300, 0., 300., 200, 0., 200.);

///////////////////////////////////////////////////////////// X axis

  histContainer_["N_eventi"]->GetXaxis()->SetTitle("Events");
  histContainer_["N_eventi_PU"]->GetXaxis()->SetTitle("Events");

  histContainer_["hDiTauCand1Pt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hDiTauCand1Eta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hDiTauCand1Phi"]->GetXaxis()->SetTitle("#phi");

  histContainer_["hDiTauCand2Pt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hDiTauCand2Eta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hDiTauCand2Phi"]->GetXaxis()->SetTitle("#phi");

  histContainer_["hDiTauCandOSPt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hDiTauCandOSEta"]->GetXaxis()->SetTitle("#eta");

  histContainer_["hDiTauCandSSPt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hDiTauCandSSEta"]->GetXaxis()->SetTitle("#eta");

  histContainer_["hDiTauCandSSPtCorr"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hDiTauCandSSEtaCorr"]->GetXaxis()->SetTitle("#eta");

  histContainer2D_["hDiTauCandOSEtaVsPt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer2D_["hDiTauCandSSEtaVsPt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");

  histContainer_["hWLepCandPt"]->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histContainer_["hWLepCandEta"]->GetXaxis()->SetTitle("#eta");
  histContainer_["hWLepCandPhi"]->GetXaxis()->SetTitle("#phi");

  histContainer_["VisMass"]->GetXaxis()->SetTitle("Vis.Mass [GeV/c^{2}]");
  histContainer_["VisMassCorr"]->GetXaxis()->SetTitle("Vis.Mass Corr. [GeV/c^{2}]");
  histContainer_["VisMassUp"]->GetXaxis()->SetTitle("Vis.Mass Up [GeV/c^{2}]");
  histContainer_["VisMassDown"]->GetXaxis()->SetTitle("Vis.Mass Down [GeV/c^{2}]");
  histContainer_["MTeMET"]->GetXaxis()->SetTitle("M_{T} (l_{W}, MET) [GeV/c^{2}]");

  histContainer_["MET"]->GetXaxis()->SetTitle("MET [GeV]");
  histContainer_["hLt"]->GetXaxis()->SetTitle("#sum_{All leptons} E_{T} [GeV]");

  histContainer_["hCosDPhiETau1"]->GetXaxis()->SetTitle("cos#Delta#phi(#tau_{1},e)");
  histContainer_["hCosDPhiETau2"]->GetXaxis()->SetTitle("cos#Delta#phi(#tau_{2},e)");
  histContainer_["hCosDPhiELeadTau"]->GetXaxis()->SetTitle("cos#Delta#phi(#tau_{lead},e)");
  histContainer_["hCosDPhiESubLeadTau"]->GetXaxis()->SetTitle("cos#Delta#phi(#tau_{sublead},e)");
  histContainer2D_["hCosDPhiELeadTauVsMT"]->GetXaxis()->SetTitle("M_{T} (l_{W}, MET) [GeV/c^{2}]");
  histContainer2D_["hCosDPhiESubLeadTauVsMT"]->GetXaxis()->SetTitle("M_{T} (l_{W}, MET) [GeV/c^{2}]");

  histContainer2D_["hMtMet"]->GetXaxis()->SetTitle("M_{T} (l_{W}, MET) [GeV/c^{2}]");

  histContainer_["hWLeptonLeadTauCharge"]->GetXaxis()->SetTitle("Charge (l_{W},#tau_{lead})");
  histContainer_["hWLeptonSubLeadTauCharge"]->GetXaxis()->SetTitle("Charge (l_{W},#tau_{sublead})");
  histContainer_["hWLeptonTau1Charge"]->GetXaxis()->SetTitle("Charge (l_{W},#tau_{1})");
  histContainer_["hWLeptonTau2Charge"]->GetXaxis()->SetTitle("Charge (l_{W},#tau_{2})");
  //histContainer_["hVertexChi2NDOF"]->GetXaxis()->SetTitle("Vertex #chi^{2}/NDOF");

  histContainer_["hMassWLeptonLeadTau"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{lead}) [GeV/c^{2}]");
  histContainer_["hMassWLeptonSubLeadTau"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{sublead}) [GeV/c^{2}]");

  histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{lead}) [GeV/c^{2}]");
  histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{sublead}) [GeV/c^{2}]");
  histContainer2D_["hMassWLeptonLeadTauVsMET"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{lead}) [GeV/c^{2}]");
  histContainer2D_["hMassWLeptonSubLeadTauVsMET"]->GetXaxis()->SetTitle("Vis.Mass (l_{W},#tau_{sublead}) [GeV/c^{2}]");

///////////////////////////////////////////////////////////// Y axis

  histContainer2D_["hDiTauCandOSEtaVsPt"]->GetYaxis()->SetTitle("#eta");
  histContainer2D_["hDiTauCandSSEtaVsPt"]->GetYaxis()->SetTitle("#eta");

  histContainer2D_["hMassWLeptonLeadTauVsPtHiggs"]->GetYaxis()->SetTitle("HiggsCand p_{T} [GeV/c]");
  histContainer2D_["hMassWLeptonSubLeadTauVsPtHiggs"]->GetYaxis()->SetTitle("HiggsCand p_{T} [GeV/c]");
  histContainer2D_["hMassWLeptonLeadTauVsMET"]->GetYaxis()->SetTitle("MET [GeV]");
  histContainer2D_["hMassWLeptonSubLeadTauVsMET"]->GetYaxis()->SetTitle("MET [GeV]");

  histContainer2D_["hMtMet"]->GetYaxis()->SetTitle("MET [GeV]");

  histContainer2D_["hCosDPhiELeadTauVsMT"]->GetYaxis()->SetTitle("cos#Delta#phi(#tau_{lead},e)");
  histContainer2D_["hCosDPhiESubLeadTauVsMT"]->GetYaxis()->SetTitle("cos#Delta#phi(#tau_{sublead},e)");

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

// ------------ method called once each job just after ending the event loop  ------------
void 
CompositeCandHistManager::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
CompositeCandHistManager::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
CompositeCandHistManager::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
CompositeCandHistManager::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
CompositeCandHistManager::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CompositeCandHistManager::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CompositeCandHistManager);
