import FWCore.ParameterSet.Config as cms
from electronHistos_ett_cff import *

skimmedElectrons = cms.EDFilter("PATElectronSelector",
                         src = cms.InputTag("electronVariables"),
                         cut = cms.string('pt > 24. && abs(eta) < 2.1 && ((isEB && userFloat("PFRelIsoDB04") < 0.15) || (isEE && userFloat("PFRelIsoDB04") < 0.1))'),
                         filter = cms.bool(True)
                         )

skimmedTaus = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("tauVariables"),
                         cut = cms.string('pt > 30.0 && abs(eta) < 2.3 && tauID("decayModeFinding") > 0.5 && tauID("byLooseCombinedIsolationDeltaBetaCorr") > 0.5 && tauID("againstMuonLoose") > 0.5 && tauID("againstElectronLoose") > 0.5'),
                         filter = cms.bool(True)
                         )

skimmingSequence = cms.Sequence(
			skimmedElectrons *
			skimmedTaus
			)
