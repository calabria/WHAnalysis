import FWCore.ParameterSet.Config as cms
from weights_cff import *

MuonHistosBeforeMuonEta = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("muonVariables"),
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

MuonHistosBeforeMuonPt1 = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("leadSubLeadMuons:leadingLeptons"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),                                     
)

MuonHistosBeforeMuonPt2 = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("leadSubLeadMuons:subleadingLeptons"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),                                     
)

MuonHistosAfterMuonPt1 = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsPt1"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

MuonHistosAfterMuonPt2 = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsPt2"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

MuonHistosBeforeEleSequence = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsPt1"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)
                                         
MuonHistosFinal = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuonsPt1"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),   
  isMC = cms.untracked.bool(True),
)
