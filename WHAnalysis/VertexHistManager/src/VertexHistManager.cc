#include <iostream>
#include <cmath>
#include <vector>
#include <string>

#include <TH1.h>
#include <TProfile.h>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

#include <TMath.h>

class VertexHistManager : public edm::EDAnalyzer  {
    public: 
	/// constructor and destructor
	VertexHistManager(const edm::ParameterSet &params);
	~VertexHistManager();

	// virtual methods called from base class EDAnalyzer
	virtual void beginJob();
	virtual void analyze(const edm::Event &event, const edm::EventSetup &es);

    private:
        edm::LumiReWeighting LumiWeights_;
	// configuration parameters
	edm::InputTag vertexSrc_;
	//edm::InputTag genParticles_;
  	typedef std::vector<double> vdouble;
        vdouble MCDist_f_;
        vdouble TrueDist2011_f_;
        bool isMC_;

	TH1 *nVertices_, *nTracks_;
	TH1 *x_, *y_, *z_;
	TH1 *xErr_, *yErr_, *zErr_;
	TH1 *N_eventi;
	TH1 *N_eventi_PU;
	TH1 *hVertexChi2Prob_;
	TH1 *hVertexChi2_;
	TH1 *hVertexNDOF_;
	TH1 *hVertexNormChi2_;
	TH1 *hVertexD0_;
	//TH1 *xDelta_, *yDelta_, *zDelta_;
	//TH1 *xPull_, *yPull_, *zPull_;
};

VertexHistManager::VertexHistManager(const edm::ParameterSet &params) :
	vertexSrc_(params.getParameter<edm::InputTag>("src")),
  	MCDist_f_(params.getUntrackedParameter<vdouble>("MCDist")),
  	TrueDist2011_f_(params.getUntrackedParameter<vdouble>("TrueDist2011")),
  	isMC_(params.getUntrackedParameter<bool>("isMC"))
	//genParticles_(params.getParameter<edm::InputTag>("mc"))
{
}

VertexHistManager::~VertexHistManager()
{
}

void VertexHistManager::beginJob()
{
	// retrieve handle to auxiliary service
	//  used for storing histograms into ROOT file
	edm::Service<TFileService> fs;
  	TH1::SetDefaultSumw2();

	nVertices_ = fs->make<TH1F>("nVertices", "number of reconstructed primary vertices", 50, 0, 50);
	nTracks_ = fs->make<TH1F>("nTracks", "number of tracks at primary vertex", 100, 0, 300);
	x_ = fs->make<TH1F>("pvX", "primary vertex x", 200, -1., 1.);
	y_ = fs->make<TH1F>("pvY", "primary vertex y", 200, -1., 1.);
	z_ = fs->make<TH1F>("pvZ", "primary vertex z", 100, -30, 30);
	xErr_ = fs->make<TH1F>("pvErrorX", "primary vertex x error", 100, 0, 0.005);
	yErr_ = fs->make<TH1F>("pvErrorY", "primary vertex y error", 100, 0, 0.005);
	zErr_ = fs->make<TH1F>("pvErrorZ", "primary vertex z error", 100, 0, 0.01);
	N_eventi = fs->make<TH1F>("N_eventi", "count",    2,   0., 2.);
	N_eventi_PU = fs->make<TH1F>("N_eventi_PU", "count",    2,   0., 2.);
  	hVertexChi2_ = fs->make<TH1F>("VertexChi2", "VertexChi2", 100, 0., 200.);
  	hVertexNDOF_ = fs->make<TH1F>("VertexNODF", "VertexChi2NDOF", 15, -0.5, 14.5);
  	hVertexNormChi2_ = fs->make<TH1F>("VertexNormChi2", "VertexNormChi2", 202, -0.01, 2.01);
  	hVertexD0_ = fs->make<TH1F>("VertexD0", "VertexD0", 100, 0., 3.);
  	hVertexChi2Prob_ = fs->make<TH1F>("VertexChi2Prob", "VertexChi2Prob", 102, -0.01, 1.01);
	//xDelta_ = fs->make<TH1F>("pvDeltaX", "x shift wrt simulated vertex", 100, -0.01, 0.01);
	//yDelta_ = fs->make<TH1F>("pvDeltaY", "y shift wrt simulated vertex", 100, -0.01, 0.01);
	//zDelta_ = fs->make<TH1F>("pvDeltaZ", "z shift wrt simulated vertex", 100, -0.02, 0.02);
	//xPull_ = fs->make<TH1F>("pvPullX", "primary vertex x pull", 100, -5, 5);
	//yPull_ = fs->make<TH1F>("pvPullY", "primary vertex y pull", 100, -5, 5);
	//zPull_ = fs->make<TH1F>("pvPullZ", "primary vertex z pull", 100, -5, 5);

	nVertices_->GetXaxis()->SetTitle("# Vertices");
	nTracks_->GetXaxis()->SetTitle("# Tracks");
	x_->GetXaxis()->SetTitle("pv_{X} [cm]");
	y_->GetXaxis()->SetTitle("pv_{Y} [cm]");
	z_->GetXaxis()->SetTitle("pv_{Z} [cm]");
	xErr_->GetXaxis()->SetTitle("pvError X [cm]");
	yErr_->GetXaxis()->SetTitle("pvError Y [cm]");
	zErr_->GetXaxis()->SetTitle("pvError Z [cm]");
	N_eventi->GetXaxis()->SetTitle("Events");

  	hVertexChi2_ ->GetXaxis()->SetTitle("Vertex #chi^{2}");
  	hVertexNDOF_ ->GetXaxis()->SetTitle("Vertex ndof");
  	hVertexNormChi2_ ->GetXaxis()->SetTitle("Vertex #chi^{2}/ndof");
  	hVertexD0_ ->GetXaxis()->SetTitle("d_{0} [cm]");
  	hVertexChi2Prob_ ->GetXaxis()->SetTitle("Vertex P(#chi^{2})");

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

void VertexHistManager::analyze(const edm::Event &event, const edm::EventSetup &es)
{  

/////////////////////////////////////////////////////////////

  	double weight = 1;

  	if(isMC_){

		edm::Handle<std::vector< PileupSummaryInfo > >  PupInfo;
		event.getByLabel(edm::InputTag("addPileupInfo"), PupInfo);

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

	// handle to the primary vertex collection
	edm::Handle<reco::VertexCollection> pvHandle;
	event.getByLabel(vertexSrc_, pvHandle);

	// handle to the generator particles (i.e. the MC truth)
	//edm::Handle<reco::GenParticleCollection> genParticlesHandle;
	//event.getByLabel(genParticles_, genParticlesHandle);

	// extract the position of the simulated vertex
	//math::XYZPoint simPV = (*genParticlesHandle)[2].vertex();

	// the number of reconstructed primary vertices

	double numVertices = pvHandle->size();
	nVertices_->Fill(numVertices, weight);

	double count = 1.;
  	N_eventi->Fill(count);
  	N_eventi_PU->Fill(count, weight);

	// if we have at least one, use the first (highest pt^2 sum)
	if (!pvHandle->empty()) {
		const reco::Vertex &pv = (*pvHandle)[0];

		nTracks_->Fill(pv.tracksSize(), weight);

		x_->Fill(pv.x(), weight);
		y_->Fill(pv.y(), weight);
		z_->Fill(pv.z(), weight);

		xErr_->Fill(pv.xError(), weight);
		yErr_->Fill(pv.yError(), weight);
		zErr_->Fill(pv.zError(), weight);

		hVertexChi2_->Fill(pv.chi2(), weight);
		hVertexNDOF_->Fill(pv.ndof(), weight);
		hVertexNormChi2_->Fill(pv.normalizedChi2(), weight);
		hVertexD0_->Fill(pv.position().rho(), weight);
		hVertexChi2Prob_->Fill(TMath::Prob(pv.chi2(), TMath::Nint(pv.ndof())), weight);

		//xDelta_->Fill(pv.x() - simPV.X());
		//yDelta_->Fill(pv.y() - simPV.Y());
		//zDelta_->Fill(pv.z() - simPV.Z());

		//xPull_->Fill((pv.x() - simPV.X()) / pv.xError());
		//yPull_->Fill((pv.y() - simPV.Y()) / pv.yError());
		//zPull_->Fill((pv.z() - simPV.Z()) / pv.zError());

		// we could access the tracks using the
		// pv.tracks_begin() ... pv.tracks_end() iterators
	}
}
	
#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(VertexHistManager);

