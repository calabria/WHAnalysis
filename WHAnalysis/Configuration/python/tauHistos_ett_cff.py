import FWCore.ParameterSet.Config as cms
from weights_cff import *

TauHistosBeforeMcMatcher = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("tauVariables"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeDeltaR= cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("tauVariables"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),                                        
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),        
  isMC = cms.untracked.bool(True),           
)

###############################################  TAU1  ###########################################################

TauHistosBeforeTauPt1 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),  
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),        
  isMC = cms.untracked.bool(True),           
)

TauHistosBeforeTauEta = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausPt1"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeTauID = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausEta"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeTauIso = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausID"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),    
  isMC = cms.untracked.bool(True),               
)

TauHistosBeforeMuonVeto = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausIso"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeEleVeto = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausMuonVeto"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),             
  isMC = cms.untracked.bool(True),      
)

TauHistosAfterTau1Sequence = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausEleVeto"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),  
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),        
  isMC = cms.untracked.bool(True),           
)

###############################################  TAU2  ###########################################################

TauHistosBeforeTauPt2 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),  
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),        
  isMC = cms.untracked.bool(True),           
)

TauHistosBeforeTauEta2 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausPt2"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeTauID2 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausEta2"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeTauIso2 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausID2"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),    
  isMC = cms.untracked.bool(True),               
)

TauHistosBeforeMuonVeto2 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausIso2"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),       
  isMC = cms.untracked.bool(True),            
)

TauHistosBeforeEleVeto2 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausMuonVeto2"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),   
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),             
  isMC = cms.untracked.bool(True),      
)

TauHistosAfterTau2Sequence = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausEleVeto2"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),  
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),        
  isMC = cms.untracked.bool(True),           
)

###############################################  Final  ###########################################################

TauHistosFinal1 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausEleVeto"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),         
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

TauHistosFinal2 = cms.EDAnalyzer("TauHistManager",
  tauSrc = cms.untracked.InputTag("selectedTausEleVeto2"),
  lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
  lep2Src = cms.untracked.InputTag("muonVariables"),         
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)
