import FWCore.ParameterSet.Config as cms
from weights_cff import *

EleHistosBeforeMCMatcher = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("electronVariables"),
  muonSrc  = cms.untracked.InputTag("muonVariables"),                                     
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosBeforeDeltaR = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("electronVariables"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),                                     
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosBeforeElePt = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsDeltaR:EleSelByDeltaR"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosBeforeEleEta = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsPt"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),                                       
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosBeforeEleCrack = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsEta"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),                                       
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosBeforeEleID = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsCrack"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),                                       
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosAfterPreEleID = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsPreID"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),                                     
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosAfterEleID = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsID"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),                                     
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosBeforeEleTrk = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsIso"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),                                       
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosBeforeOneEle = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsTrk"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),                                       
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosBeforeEleTauPairs = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsTrk"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),                                       
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

EleHistosFinal = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("selectedElectronsTrk"),
  muonSrc  = cms.untracked.InputTag("selectedMuonsIso"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

