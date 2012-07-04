#include "WHAnalysis/PatCompositeCandidateProducer/interface/PatCompositeCandidateProducer.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

typedef PatCompositeCandidateProducer<pat::Electron, pat::Electron, pat::Tau> EleEleTauPatCompositeCandidateProducer;
typedef PatCompositeCandidateProducer<pat::Electron, pat::Muon, pat::Tau>     EleMuTauPatCompositeCandidateProducer;
typedef PatCompositeCandidateProducer<pat::Muon, pat::Muon, pat::Tau>         MuMuTauPatCompositeCandidateProducer;
typedef PatCompositeCandidateProducer<pat::Electron, pat::Tau, pat::Tau>      EleTauTauPatCompositeCandidateProducer;
typedef PatCompositeCandidateProducer<pat::Muon, pat::Tau, pat::Tau>          MuTauTauPatCompositeCandidateProducer;

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(EleEleTauPatCompositeCandidateProducer);
DEFINE_FWK_MODULE(EleMuTauPatCompositeCandidateProducer);
DEFINE_FWK_MODULE(MuMuTauPatCompositeCandidateProducer);
DEFINE_FWK_MODULE(EleTauTauPatCompositeCandidateProducer);
DEFINE_FWK_MODULE(MuTauTauPatCompositeCandidateProducer);
