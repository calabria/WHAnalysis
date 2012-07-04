import FWCore.ParameterSet.Config as cms
from tauHistos_cff import *

selectedTausEta = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("tauVariables"),
                         #cut = cms.string('abs(eta) < 2.5 && !(1.4442 < abs(eta) < 1.566)'),
                         cut = cms.string('abs(eta) < 2.3'),
                         filter = cms.bool(True)
                         )

selectedTausByDeltaR = cms.EDProducer("EleMuSelTauByDeltaR",
     			tauSrc = cms.untracked.InputTag("selectedTausEta"),
     			lep1Src = cms.untracked.InputTag("selectedElectronsPt"),
     			lep2Src = cms.untracked.InputTag("muonVariables"),                             
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

selectedEventsTau1 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("tauVariables"),
)

selectedEventsTau2 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("selectedTausEta"),
)

selectedEventsTau3 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
)

selectedEventsTau4 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("selectedTausPt"),
)

selectedEventsTau5 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("selectedTausID"),
)

selectedEventsTau6 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("selectedTausIso"),
)

selectedEventsTau7 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("selectedTausMuonVeto"),
)

selectedEventsTau8 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("selectedTausEleVeto"),
)

selectedEventsTau9 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("selectedTausHighestPt:TauHighestPt"),
)

tauSequence = cms.Sequence(TauHistosBeforeTauEta *
			   #selectedEventsTau1 *
			   selectedTausEta *
			   #selectedEventsTau2 *
                           TauHistosBeforeDeltaR *
			   selectedTausByDeltaR *
			   #selectedEventsTau3 *
			   TauHistosBeforeTauPt *
			   selectedTausPt *
			   #selectedEventsTau4 *
			   TauHistosBeforeTauID *
			   selectedTausID *
			   #selectedEventsTau5 *
			   TauHistosBeforeTauIso *
			   selectedTausIso *
			   #selectedEventsTau6 *
			   TauHistosBeforeMuonVeto *
			   selectedTausMuonVeto *
			   #selectedEventsTau7 *
			   TauHistosBeforeEleVeto *
			   selectedTausEleVetoPre *
			   selectedTausEleVeto *
			   #selectedEventsTau8 *
                           TauHistosBeforeHighestPt *
			   selectedTausHighestPt *
			   #selectedEventsTau9 *
			   TauHistosBeforeDiTau 
)
