#include "WHAnalysis/AddUserVariables/interface/AddUserVariables.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

typedef AddUserVariables<pat::Electron> ElectronAddUserVariables;
typedef AddUserVariables<pat::Muon>     MuonAddUserVariables;
typedef AddUserVariables<pat::Tau>      TauAddUserVariables;

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(ElectronAddUserVariables);
DEFINE_FWK_MODULE(MuonAddUserVariables);
DEFINE_FWK_MODULE(TauAddUserVariables);
