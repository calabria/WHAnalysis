import FWCore.ParameterSet.Config as cms
from WHAnalysis.Configuration.weights_cff import *

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_100_0_WTr.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_101_0_LLR.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_102_0_79m.root",
		"file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_103_0_vS1.root",
    )
)

process.eleIdWW = cms.EDFilter('EleIdWWFilter',
    electronSrc = cms.untracked.InputTag("patElectrons"),                                                               
    separationPt = cms.untracked.double(20),
    eleIdWP1 = cms.untracked.string("simpleEleId70cIso"),
    eleIdWP2 = cms.untracked.string("simpleEleId80cIso"),
    output1 = cms.untracked.double(6.5), 
    output2 = cms.untracked.double(6.5), 
    filter = cms.bool(True)
)

process.EleHistos1 = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("eleIdWW:selectedElectronsByEleIdWW1"),
  muonSrc  = cms.untracked.InputTag("patMuons"),                                     
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVertices"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

process.EleHistos2 = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("eleIdWW:selectedElectronsByEleIdWW2"),
  muonSrc  = cms.untracked.InputTag("patMuons"),                                     
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVertices"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

process.EleHistos = cms.EDAnalyzer("ElectronHistManager",
  electronSrc = cms.untracked.InputTag("eleIdWW:selectedElectronsByEleIdWW"),
  muonSrc  = cms.untracked.InputTag("patMuons"),                                     
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVertices"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo.root") )

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.eleIdWW *
		     (process.EleHistos1 + process.EleHistos2 + process.EleHistos)
)

process.e = cms.EndPath(process.out)
