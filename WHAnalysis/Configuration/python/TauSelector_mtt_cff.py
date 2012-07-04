import FWCore.ParameterSet.Config as cms
from tauHistos_mtt_cff import *

selectedTausEta = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("tauVariables"),
                         #cut = cms.string('abs(eta) < 2.5 && !(1.4442 < abs(eta) < 1.566)'),
                         cut = cms.string('abs(eta) < 2.3'),
                         filter = cms.bool(True)
                         )

selectedTausByDeltaR = cms.EDProducer("MuMuSelTauByDeltaR",
     			tauSrc = cms.untracked.InputTag("selectedTausEta"),
     			lep1Src = cms.untracked.InputTag("muonVariables"),
     			lep2Src = cms.untracked.InputTag("muonVariables"),                             
     			DeltaRCut = cms.untracked.double(0.3)
			)

selectedTausID = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
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

selectedTausEleVeto = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausMuonVeto"),
                         cut = cms.string('tauID("againstElectronLoose") > 0.5'),
                         filter = cms.bool(True)
                        )

leadSubLeadTaus = cms.EDProducer('LeadTausProducer',
    			 lepSrc = cms.untracked.InputTag("selectedTausEleVeto"),                                                               
			 )

selectedTausPt1 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("leadSubLeadTaus:leadingLeptons"),
                         cut = cms.string('pt > 15.0'),
                         filter = cms.bool(True)
                         )

selectedTausPt2 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("leadSubLeadTaus:subleadingLeptons"),
                         cut = cms.string('pt > 10.0'),
                         filter = cms.bool(True)
                         )

tauSequence = cms.Sequence(TauHistosBeforeTauEta *
			   selectedTausEta *
                           TauHistosBeforeDeltaR *
			   selectedTausByDeltaR *
			   TauHistosBeforeTauID *
			   selectedTausID *
			   TauHistosBeforeTauIso *
			   selectedTausIso *
			   TauHistosBeforeMuonVeto *
			   selectedTausMuonVeto *
			   TauHistosBeforeEleVeto *
			   selectedTausEleVeto *
			   leadSubLeadTaus *
			   TauHistosBeforeTauPt *
			   selectedTausPt1 *
			   TauHistosAfterTauPt1 *
			   selectedTausPt2 *
			   TauHistosAfterTauPt2
)
