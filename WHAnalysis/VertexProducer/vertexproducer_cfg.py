import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim/DYToTauTau/patTuple_100_1_wgR.root",
    )
)

process.myProducerLabel = cms.EDProducer('VertexProducer',
	vertexSrc = cms.untracked.InputTag('offlinePrimaryVertices'),
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
