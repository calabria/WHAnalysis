import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(500) )
process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToEE/patTuple_95_1_lMA.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToEE/patTuple_96_1_RpA.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToEE/patTuple_97_1_hG4.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToEE/patTuple_98_1_OYc.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToEE/patTuple_99_1_4Az.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToEE/patTuple_9_1_vPK.root",

    )
)


#process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.particleListDrawer = cms.EDAnalyzer("ParticleListDrawer",
    	maxEventsToPrint = cms.untracked.int32(1000),
        printVertex = cms.untracked.bool(False),                                            
    	src = cms.InputTag('genParticles')
  )


process.myProducerLabel = cms.EDProducer('EleAntiMatching',
     eleSrc = cms.untracked.InputTag("selectedPatElectrons"),
     genParticles = cms.untracked.InputTag("genParticles"),                                   
     idParticle = cms.untracked.int32(23),
     deltaRCut = cms.untracked.double(0.8)
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(#process.particleListDrawer 
                     process.myProducerLabel 
                     )

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'histo.root'

	)
)

process.e = cms.EndPath(process.out)
