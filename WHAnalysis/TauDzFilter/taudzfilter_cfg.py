import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
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

process.myProducerLabel = cms.EDFilter('TauDzFilter',
    vertexSrc = cms.untracked.InputTag("offlinePrimaryVertices"),                                                               
    tauSrc = cms.untracked.InputTag("patTaus"),     
    dzCutMax = cms.untracked.double(+0.2),                                                          
    dzCutMin = cms.untracked.double(-0.2),
    filter = cms.bool(True)
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
