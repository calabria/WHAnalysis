import FWCore.ParameterSet.Config as cms
from weights_cff import *

WHistosFinal = cms.EDAnalyzer("WHistManager",
   	WCand = cms.untracked.InputTag("selectedMuMETPairs"),
  	PFMetTag = cms.untracked.InputTag('patMETsPF'),  
	electronSrc = cms.untracked.InputTag("selectedElectronsTrk"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)
