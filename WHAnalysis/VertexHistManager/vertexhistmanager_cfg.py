import FWCore.ParameterSet.Config as cms

process = cms.Process("VertexHistManager")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(

                         'file:/tmp/calabria/test.root',

  )
)

process.MessageLogger = cms.Service("MessageLogger")

process.analyzePatVertex = cms.EDAnalyzer("VertexHistManager",

  src = cms.InputTag("offlinePrimaryVertices"),
  #mc = cms.InputTag("genParticles")
                                         
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('vertexHistos.root')
                                   )

process.p = cms.Path(process.analyzePatVertex)


