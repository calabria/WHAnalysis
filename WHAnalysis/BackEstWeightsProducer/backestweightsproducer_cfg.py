import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

		'file:/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/Configuration/test/CRAB/patTuple.root',

    )
)

process.myProducerLabel = cms.EDProducer('BackEstWeightsProducer',
  	muonSrc = cms.InputTag("muonVariables"),
  	eleSrc = cms.InputTag("electronVariables"),
  	tauSrc = cms.InputTag("tauVariables"),
  	jetSrc = cms.InputTag("patJetsAK5PF"),
        doEleWeight = cms.bool(True),
        doMuonWeight = cms.bool(True),
        doTauWeight = cms.bool(True)
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
