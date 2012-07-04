import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_1.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_2.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_3.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_4.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_5.root',
    )
)

process.myProducerLabel = cms.EDProducer('MuonsUserEmbedded',
	muonTag = cms.InputTag("patMuons"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS")
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)
  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
