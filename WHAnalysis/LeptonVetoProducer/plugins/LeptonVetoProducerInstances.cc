#include "WHAnalysis/LeptonVetoProducer/interface/LeptonVetoProducer.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

typedef LeptonVetoProducer<pat::Electron> ElectronVetoProducer;
typedef LeptonVetoProducer<pat::Muon>     MuonVetoProducer;
typedef LeptonVetoProducer<pat::Tau>      TauVetoProducer;

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(MuonVetoProducer);
DEFINE_FWK_MODULE(ElectronVetoProducer);
DEFINE_FWK_MODULE(TauVetoProducer);
