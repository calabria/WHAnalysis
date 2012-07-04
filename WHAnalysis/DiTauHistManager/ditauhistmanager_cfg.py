import FWCore.ParameterSet.Config as cms

process = cms.Process("DiTauHistManager")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(

                         'file:/tmp/calabria/test.root',

  )
)

process.MessageLogger = cms.Service("MessageLogger")

process.analyzeDiTau = cms.EDAnalyzer("DiTauHistManager",

  DiTauCand = cms.untracked.InputTag("selectedEleMuPairs"),
  PFMetTag = cms.untracked.InputTag('pfMET'),                                          
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('DiTauHistos.root')
                                   )

process.p = cms.Path(process.analyzeDiTau)


