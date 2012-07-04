import FWCore.ParameterSet.Config as cms
from weights_cff import *

TauHistosBeforeMcMatcher = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("tauVariables"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeTauEta = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("tauVariables"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeDeltaR= cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausEta"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),                                        
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),        
  isMC = cms.untracked.bool(True),           
)

TauHistosBeforeTauID = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeTauIso = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausID"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),    
  isMC = cms.untracked.bool(True),               
)

TauHistosBeforeMuonVeto = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausIso"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeEleVeto = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausMuonVeto"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),             
  isMC = cms.untracked.bool(True),      
)

TauHistosBeforeTauPt = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausEleVeto"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),  
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),        
  isMC = cms.untracked.bool(True),           
)

TauHistosAfterTauPt1 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausPt1"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),  
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),        
  isMC = cms.untracked.bool(True),           
)

TauHistosAfterTauPt2 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausPt1"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),  
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),        
  isMC = cms.untracked.bool(True),           
)

TauHistosFinal = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausPt1"),
  lep1Src = cms.untracked.InputTag("electronVariables"),
  lep2Src = cms.untracked.InputTag("selectedMuonsIso"),         
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)
