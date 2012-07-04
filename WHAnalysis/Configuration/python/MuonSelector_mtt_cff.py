import FWCore.ParameterSet.Config as cms
from muonHistos_mtt_cff import *

selectedMuonsPt = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("muonVariables"),
                         cut = cms.string('pt > 25.'),
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
                         cut = cms.string("userInt('muonID') > 0.5"),
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


muonSequence = cms.Sequence(MuonHistosBeforeMuonPt *
			    selectedMuonsPt * 
			    selectedMuonsPtForVeto *
			    MuonHistosBeforeMuonEta *
			    selectedMuonsEta *
			    MuonHistosBeforeMuonID *
			    selectedMuonsID *
			    MuonHistosBeforeMuonIso *
		      	    selectedMuonsIso *
			    MuonHistosAfterMuonIso *
			    selectedMuonsVeto *
			    MuonHistosBeforeEleSequence
)
