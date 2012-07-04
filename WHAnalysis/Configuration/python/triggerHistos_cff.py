import FWCore.ParameterSet.Config as cms
from weights_cff import *

TriggerHistosBeforeSel= cms.EDAnalyzer("TriggerHistManager",
       hltResultsSource = cms.InputTag('TriggerResults::REDIGI38XPU'),
       hltPaths = cms.vstring('HLT_Mu9', 'HLT_Mu11'),    
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),  
       isMC = cms.untracked.bool(True),
)

TriggerHistosAfterSel= cms.EDAnalyzer("TriggerHistManager",
       hltResultsSource = cms.InputTag('TriggerResults::REDIGI38XPU'),
       hltPaths = cms.vstring('HLT_Mu9', 'HLT_Mu11'),    
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),  
       isMC = cms.untracked.bool(True),
)
