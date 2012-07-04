import FWCore.ParameterSet.Config as cms
from wHistos_cff import *
from muonHistos_cff import *

selectedMuMETPairsMT = cms.EDFilter('MtFilter',
			DiTauTag = cms.untracked.InputTag('selectedMuMETPairs'),
			PFMetTag = cms.untracked.InputTag('patMETsPF'),
			MTCut = cms.untracked.double(500000000.),
			particle = cms.untracked.int32(0), #muon
			invertCut = cms.untracked.bool(False),
                        filter = cms.bool(True)
			)

muMetSequence = cms.Sequence(
			     WHistosFinal
			     #selectedMuMETPairsMT *
			     #MuonHistosFinal
)
