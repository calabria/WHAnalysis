import FWCore.ParameterSet.Config as cms
from WHAnalysis.Configuration.weights_cff import *

process = cms.Process("ElectronHistManager")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(

                #'file:/tmp/calabria/test.root',
		#'file:/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/Configuration/test/CRAB/patTuple.root',
		'file:/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/AddUserVariables/myOutputFile.root'

  )
)

process.MessageLogger = cms.Service("MessageLogger")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.analyzePatElectrons = cms.EDAnalyzer("ElectronHistManager",
  #electronSrc = cms.untracked.InputTag("electronVariables"),
  electronSrc = cms.untracked.InputTag("myProducerLabel"),
  muonSrc  = cms.untracked.InputTag("patMuons"),                                     
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVertices"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(False),
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('electronsHistos.root')
                                   )

process.p = cms.Path(process.analyzePatElectrons)


