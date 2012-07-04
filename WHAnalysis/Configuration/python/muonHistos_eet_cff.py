import FWCore.ParameterSet.Config as cms
from weights_cff import *

MuonHistosBeforeMuonPt = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("muonVariables"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),                                     
)

MuonHistosBeforeMuonVeto = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("muonVariables"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)

MuonHistosBeforeEle2TauPairs = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsPtForVeto"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)

MuonHistosFinal = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsPtForVeto"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)
