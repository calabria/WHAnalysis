import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(500) )
process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_100_0_WTr.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_101_0_LLR.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_102_0_79m.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_103_0_vS1.root",

    )
)


#process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.particleListDrawer = cms.EDAnalyzer("ParticleListDrawer",
    	maxEventsToPrint = cms.untracked.int32(1000),
        printVertex = cms.untracked.bool(False),                                            
    	src = cms.InputTag('genParticles')
  )


process.myProducerLabel = cms.EDProducer('FactorizationDY',
     taus = cms.untracked.InputTag("selectedPatTaus"),
     genParticles = cms.untracked.InputTag("genParticles"),                                   
     idParticle = cms.untracked.int32(23),
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(#process.particleListDrawer 
                     process.myProducerLabel 
                     )



process.e = cms.EndPath(process.out)

















