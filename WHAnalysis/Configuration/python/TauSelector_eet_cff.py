import FWCore.ParameterSet.Config as cms
from tauHistos_eet_cff import *

selectedTausEta = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("tauVariables"),
                         #cut = cms.string('abs(eta) < 2.5 && !(1.4442 < abs(eta) < 1.566)'),
                         cut = cms.string('abs(eta) < 2.3'),
                         filter = cms.bool(True)
                         )

selectedTausByDeltaR = cms.EDProducer("EleEleSelTauByDeltaR",
     			tauSrc = cms.untracked.InputTag("selectedTausEta"),
     			lep1Src = cms.untracked.InputTag("selectedElectronsPt1"),
     			lep2Src = cms.untracked.InputTag("selectedElectronsPt2"),                             
     			DeltaRCut = cms.untracked.double(0.3)
			)

selectedTausPt = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
                         cut = cms.string('pt > 20.0'),
                         filter = cms.bool(True)
                         )

selectedTausID = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausPt"),
                         cut = cms.string('tauID("decayModeFinding") > 0.5'),
                         filter = cms.bool(True)
                        )

selectedTausIso = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausID"),
                         cut = cms.string('tauID("byLooseCombinedIsolationDeltaBetaCorr") > 0.5'),
                         filter = cms.bool(True)
                        )

selectedTausMuonVeto = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausIso"),
                         cut = cms.string('tauID("againstMuonTight") > 0.5'),
                         filter = cms.bool(True)
                        )

selectedTausEleVetoPre = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausMuonVeto"),
                         #cut = cms.string('tauID("againstElectronMVA") > 0.5'),
                         cut = cms.string('tauID("againstElectronMedium") > 0.5'),
                         filter = cms.bool(True)
                        )

selectedTausEleVeto = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausEleVetoPre"),
                         cut = cms.string('tauID("againstElectronMVA") > 0.5'),
                         #cut = cms.string('tauID("againstElectronTight") > 0.5'),
                         filter = cms.bool(True)
                        )

selectedTausHighestPt = cms.EDProducer("LeptonHighestPt",
    			tauSrc = cms.untracked.InputTag("selectedTausEleVeto")
  			)

tauSequence = cms.Sequence(TauHistosBeforeTauEta *
			   selectedTausEta *
                           TauHistosBeforeDeltaR *
			   selectedTausByDeltaR *
			   TauHistosBeforeTauPt *
			   selectedTausPt *
			   TauHistosBeforeTauID *
			   selectedTausID *
			   TauHistosBeforeTauIso *
			   selectedTausIso *
			   TauHistosBeforeMuonVeto *
			   selectedTausMuonVeto *
			   TauHistosBeforeEleVeto *
			   selectedTausEleVetoPre *
			   selectedTausEleVeto *
                           TauHistosBeforeHighestPt *
			   selectedTausHighestPt *
			   TauHistosBeforeDiTau 
)
