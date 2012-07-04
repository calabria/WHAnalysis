import FWCore.ParameterSet.Config as cms
from muonHistos_cff import *

selectedMuonsPt = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("muonVariables"),
                         cut = cms.string('pt > 20.'),
                         filter = cms.bool(True)
                         )

############################### FOR VETO ############################### 

selectedMuonsPtForVeto = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("muonVariables"),
                         cut = cms.string('pt > 5.'),
                         filter = cms.bool(False)
                         )

############################### FOR VETO ############################### 

selectedMuonsEta = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("selectedMuonsPt"),
                         cut = cms.string('abs(eta) < 2.1'),
                         filter = cms.bool(True)
                         )

selectedMuonsID = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("selectedMuonsEta"),
                         cut = cms.string("userInt('muonID') > 0.5 && abs(userFloat('dxyWrtPV')) < 0.02 && abs(userFloat('dzWrtPV')) < 0.2"),
                         filter = cms.bool(True)
                         )

selectedMuonsIso = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("selectedMuonsID"),
                         cut = cms.string("userFloat('PFRelIsoDB04v2') < 0.3"),
                         #cut = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt < 0.1"),
                         filter = cms.bool(True)
                         )

selectedMuonsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedMuonsPtForVeto"),
                     	maxNumber = cms.uint32(1),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
                     	)

selectedEventsMu1 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("muonVariables"),
	eleSrc = cms.untracked.InputTag("electronVariables"),
	tauSrc = cms.untracked.InputTag("tauVariables"),
)

selectedEventsMu2 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsPt"),
	eleSrc = cms.untracked.InputTag("electronVariables"),
	tauSrc = cms.untracked.InputTag("tauVariables"),
)

selectedEventsMu3 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsEta"),
	eleSrc = cms.untracked.InputTag("electronVariables"),
	tauSrc = cms.untracked.InputTag("tauVariables"),
)

selectedEventsMu4 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsID:selectedMuonsByID"),
	eleSrc = cms.untracked.InputTag("electronVariables"),
	tauSrc = cms.untracked.InputTag("tauVariables"),
)

selectedEventsMu5 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("electronVariables"),
	tauSrc = cms.untracked.InputTag("tauVariables"),
)

selectedEventsMu6 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("electronVariables"),
	tauSrc = cms.untracked.InputTag("tauVariables"),
)


muonSequence = cms.Sequence(MuonHistosBeforeMuonPt *
			    #selectedEventsMu1 *
			    selectedMuonsPt * 
			    selectedMuonsPtForVeto *
			    #selectedEventsMu2 *
			    MuonHistosBeforeMuonEta *
			    selectedMuonsEta *
			    #selectedEventsMu3 *
			    MuonHistosBeforeMuonID *
			    selectedMuonsID *
			    #selectedEventsMu4 *
			    MuonHistosBeforeMuonIso *
		      	    selectedMuonsIso *
			    #selectedEventsMu5 *
			    MuonHistosAfterMuonIso *
			    selectedMuonsVeto *
			    #selectedEventsMu6 *
			    MuonHistosBeforeElePt
)
