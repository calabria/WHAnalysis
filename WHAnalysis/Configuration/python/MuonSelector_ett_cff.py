import FWCore.ParameterSet.Config as cms
from muonHistos_ett_cff import *

############################### FOR VETO ############################### 

selectedMuonsPtForVeto = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("muonVariables"),
                         cut = cms.string('pt > 5.'),
                         filter = cms.bool(False)
                         )

############################### FOR VETO ############################### 


selectedMuonsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedMuonsPtForVeto"),
                     	maxNumber = cms.uint32(2000),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
                     	)

muonSequence = cms.Sequence(MuonHistosBeforeMuonPt *
			    selectedMuonsPtForVeto *
			    MuonHistosBeforeMuonVeto *
			    selectedMuonsVeto *
			    MuonHistosBeforeTauTauPairs
)
