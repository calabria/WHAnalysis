import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_100_0_WTr.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_101_0_LLR.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_102_0_79m.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_103_0_vS1.root',
        
    )
)

process.myProducerLabel = cms.EDProducer('LeptonHighestPt',
     tauSrc = cms.untracked.InputTag("selectedPatTaus")
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)
  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
