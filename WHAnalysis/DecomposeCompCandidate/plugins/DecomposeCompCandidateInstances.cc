#include "WHAnalysis/DecomposeCompCandidate/interface/DecomposeCompCandidate.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

typedef DecomposeCompCandidate<pat::Muon>     MuObjSSProducer;
typedef DecomposeCompCandidate<pat::Electron> EleObjSSProducer;
typedef DecomposeCompCandidate<pat::Tau>      TauObjSSProducer;

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(MuObjSSProducer);
DEFINE_FWK_MODULE(EleObjSSProducer);
DEFINE_FWK_MODULE(TauObjSSProducer);
