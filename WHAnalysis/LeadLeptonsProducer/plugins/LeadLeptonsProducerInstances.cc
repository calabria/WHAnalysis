#include "WHAnalysis/LeadLeptonsProducer/interface/LeadLeptonsProducer.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

typedef LeadLeptonsProducer<pat::Electron> LeadElectronsProducer;
typedef LeadLeptonsProducer<pat::Muon>     LeadMuonsProducer;
typedef LeadLeptonsProducer<pat::Tau>      LeadTausProducer;

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(LeadElectronsProducer);
DEFINE_FWK_MODULE(LeadMuonsProducer);
DEFINE_FWK_MODULE(LeadTausProducer);
