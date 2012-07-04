import FWCore.ParameterSet.Config as cms

genFilter = cms.EDFilter("GenFilter",
	genParticles = cms.untracked.InputTag('genParticles'),
	#particles = cms.untracked.vdouble(24, -24),
	process = cms.untracked.int32(1),
    	filter = cms.bool(True)
)
