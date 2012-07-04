import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

		'file:/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/Configuration/test/CRAB/patTuple_MCMatch.root',
        
    )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.genFilter = cms.EDFilter("GenFilter",
	genParticles = cms.untracked.InputTag('genParticles'),
	#particles = cms.untracked.vdouble(24, -24),
	process = cms.untracked.int32(1),
    	filter = cms.bool(True)
)

process.myProducerLabel = cms.EDFilter('MCTruthFullyHadronic',
     genParticles = cms.untracked.InputTag("genParticles"),
     filter = cms.bool(True)
)

process.genFilter.process = cms.untracked.int32(1)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)
  
process.p = cms.Path(process.genFilter * process.myProducerLabel)

process.e = cms.EndPath(process.out)
