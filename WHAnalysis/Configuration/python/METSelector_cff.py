import FWCore.ParameterSet.Config as cms

selectedMETMax = cms.EDFilter("PATMETSelector",
     #src = cms.InputTag("patMETsPF"),
     #src = cms.InputTag("patPFMETsTypeIcorrected"),
     src = cms.InputTag("patPFMetByMVA"),
     cut = cms.string('et > 20'),
     filter = cms.bool(True)
)
