import FWCore.ParameterSet.Config as cms

selectedMETMax = cms.EDFilter("PATMETSelector",
     src = cms.InputTag("patMETsPF"),
     cut = cms.string('10 < et < 80'),
     filter = cms.bool(True)
)
