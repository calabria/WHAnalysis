import FWCore.ParameterSet.Config as cms
from electronHistos_ett_cff import *

skimmedElectronsPt = cms.EDFilter("PATElectronSelector",
                         src = cms.InputTag("producesUserDefinedVarsEle"),
                         cut = cms.string('pt > 20. && abs(eta) < 2.5'),
                         filter = cms.bool(True)
                         )

################################ TAU1 ################################ 

skimmedTaus1 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("producesUserDefinedVarsTau"),
                         cut = cms.string('pt > 20.0 && abs(eta) < 2.3 && tauID("decayModeFinding") > 0.5 && tauID("byTightCombinedIsolationDeltaBetaCorr") > 0.5'),
                         filter = cms.bool(True)
                         )

skimmedPairs1 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("skimmedTaus1 producesUserDefinedVarsTau"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

skimmedPairsDeltaR1 = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("skimmedPairs1"),
			DeltaRCut = cms.untracked.double(0.3),
                        filter = cms.bool(True)
			)


################################ TAU2 ################################ 

skimmedTaus2 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("producesUserDefinedVarsTau"),
                         cut = cms.string('pt > 20.0 && abs(eta) < 2.3 && tauID("decayModeFinding") > 0.5'),
                         filter = cms.bool(True)
                         )

skimmedPairs2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("skimmedTaus1 skimmedTaus2"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

skimmedPairsDeltaR2 = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("skimmedPairs2"),
			DeltaRCut = cms.untracked.double(0.3),
                        filter = cms.bool(True)
			)

skimmingSequence = cms.Sequence(
			skimmedElectronsPt
			#skimmedTaus1 
			#skimmedPairs1 *
			#skimmedPairsDeltaR1 *
			#skimmedTaus2 *
			#skimmedPairs2 *
			#skimmedPairsDeltaR2
			)
