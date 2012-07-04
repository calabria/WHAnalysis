import FWCore.ParameterSet.Config as cms
from triggerHistos_cff import *

#hltSelection = cms.EDFilter("HLTHighLevel",
#                             TriggerResultsTag = cms.InputTag("TriggerResults","","REDIGI38XPU"),
#                             HLTPaths = cms.vstring('HLT_Mu9','HLT_Mu11'),
#                             eventSetupPathsKey = cms.string(''),                 
#                             andOr = cms.bool(True), #True (OR) accept if ANY is true, False (AND) accept if ALL are true
#                             throw = cms.bool(True)                               
#                             )

hltSelection = cms.EDFilter("TriggerFilter",
                             TriggerResultsTag = cms.InputTag("TriggerResults","","REDIGI38XPU"),
                             HLTPaths = cms.vstring("HLT_Mu17_Ele8_CaloIdL_v","HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_v"),
			     defaultTrigger = cms.string("HLT_Mu17_Ele8_CaloIdL_v"),
                             hltEventRanges = cms.VEventRange("160431:MIN-176469:MAX","176545:MIN-180252:MAX"),
                             )

triggerSequence = cms.Sequence(TriggerHistosBeforeSel *
			       hltSelection *
			       TriggerHistosAfterSel
)
