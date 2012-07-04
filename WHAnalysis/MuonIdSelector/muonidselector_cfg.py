import FWCore.ParameterSet.Config as cms
from WHAnalysis.Configuration.weights_cff import *

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
		'file:/lustre/cms/store/user/rosma/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_998_1_EBO.root',
		'file:/lustre/cms/store/user/rosma/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_999_2_SBh.root',
		'file:/lustre/cms/store/user/rosma/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_99_1_TRs.root',
		'file:/lustre/cms/store/user/rosma/Data/PAT2011_NoSkim_MC/DYToTauTau/patTuple_9_1_MKO.root',
    )
)

process.selectedMuons = cms.EDProducer('MuonIdSelector',
   beamSpotSource = cms.InputTag("offlineBeamSpot"),
   vertexSource = cms.InputTag("offlinePrimaryVertices"),
   muonSrc = cms.InputTag("patMuons"),

   applyGlobalMuonPromptTight = cms.bool(True),
   applyAllArbitrated = cms.bool(True),
   maxIPxy = cms.double(0.02),
   maxIPz = cms.double(1.e+3),
   maxChi2red = cms.double(10),
   maxDptOverPt = cms.double(0.1),
   minTrackerHits = cms.uint32(10),
   minPixelHits = cms.uint32(1),
   minMuonStations = cms.uint32(2),
   minMatchedSegments = cms.uint32(1)
)

process.MuonHistosBeforeCut = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("patMuons"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVertices"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),                                     
)

process.MuonHistosAfterCut = cms.EDAnalyzer("MuonHistManager",
  muonSrc = cms.untracked.InputTag("selectedMuons:selectedMuonsByID"),
  vertexSrc = cms.untracked.InputTag("offlinePrimaryVertices"),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),                                     
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo.root") )
  
process.p = cms.Path(process.MuonHistosBeforeCut * process.selectedMuons * process.MuonHistosAfterCut)

process.e = cms.EndPath(process.out)
