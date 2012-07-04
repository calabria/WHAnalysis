import FWCore.ParameterSet.Config as cms

process = cms.Process("TriggerHistManager")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(

                         'file:/tmp/calabria/test.root',

  )
)

process.MessageLogger = cms.Service("MessageLogger")

process.analyzeTrigger = cms.EDAnalyzer("TriggerHistManager",

    hltResultsSource = cms.InputTag('TriggerResults::REDIGI38XPU'),
    hltPaths = cms.vstring('HLT_Mu9', 'HLT_Mu11'),                                           
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('triggerHistos.root')
                                   )

process.p = cms.Path(process.analyzeTrigger)


