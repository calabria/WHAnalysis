import FWCore.ParameterSet.Config as cms
from weights_cff import *

MuonHistosBeforeMuonPt = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("muonVariables"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),                                     
)

MuonHistosBeforeMuonEta = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsPt"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)

MuonHistosBeforeMuonID = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsEta"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)

MuonHistosBeforeMuonIso = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsID"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)

MuonHistosAfterMuonIso = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

MuonHistosBeforeElePt = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)
                                         
MuonHistosFinal = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)
