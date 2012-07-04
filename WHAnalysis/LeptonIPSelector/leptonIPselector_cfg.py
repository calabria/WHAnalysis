import FWCore.ParameterSet.Config as cms

process = cms.Process("LeptonIPSelector")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
	'file:/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/Configuration/test/CRAB/patTuple.root'
    )
)

process.myProducerLabel = cms.EDFilter('LeptonIPSelector',
    vertexSrc = cms.untracked.InputTag("offlinePrimaryVertices"),                                                               
    leptonSrc = cms.untracked.InputTag("patMuons"),                                                               
    IPmin = cms.untracked.double(-0.02), 
    IPmax = cms.untracked.double(+0.02), 
    filter = cms.bool(True)
)
  
process.p = cms.Path(process.myProducerLabel)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
    #SelectEvents = cms.untracked.PSet(
    #	SelectEvents = cms.vstring('p')
    #)
)

process.e = cms.EndPath(process.out)
