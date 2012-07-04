#include "WHAnalysis/SelTauByDeltaR/interface/SelTauByDeltaR.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

typedef SelTauByDeltaR<pat::Electron, pat::Electron> EleEleSelTauByDeltaR;
typedef SelTauByDeltaR<pat::Electron, pat::Muon>     EleMuSelTauByDeltaR;
typedef SelTauByDeltaR<pat::Muon, pat::Muon>         MuMuSelTauByDeltaR;

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(EleEleSelTauByDeltaR);
DEFINE_FWK_MODULE(EleMuSelTauByDeltaR);
DEFINE_FWK_MODULE(MuMuSelTauByDeltaR);
