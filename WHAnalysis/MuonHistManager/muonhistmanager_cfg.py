import FWCore.ParameterSet.Config as cms

process = cms.Process("MuonHistManager")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(

                #'file:/tmp/calabria/test.root',
		'rfio:/castor/cern.ch/user/c/calabria/TagAndProbe/Skim_DYToTauTau_M-20_CT10_TuneZ2_7TeV-powheg-pythia-tauola_HPS/patTuple_10_1_oxy.root',

  )
)

process.MessageLogger = cms.Service("MessageLogger")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.analyzePatMuons = cms.EDAnalyzer("MuonHistManager",

  muonSrc     = cms.untracked.InputTag("selectedPatMuons"),    
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVertices") 
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('muonHistos.root')
                                   )

process.p = cms.Path(process.analyzePatMuons)


