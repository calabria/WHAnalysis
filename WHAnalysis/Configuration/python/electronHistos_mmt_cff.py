import FWCore.ParameterSet.Config as cms
from weights_cff import *

EleHistosBeforeDeltaR = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("electronVariables"),
  muonSrc  = cms.untracked.InputTag("muonVariables"),                                     
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosBeforeMu2TauPairs = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsWP95"),
  muonSrc  = cms.untracked.InputTag("muonVariables"),                                       
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosFinal = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsWP95"),
  muonSrc  = cms.untracked.InputTag("muonVariables"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

