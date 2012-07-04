import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.GammaJet_300to470  = cms.EDAnalyzer('BatchSubmission',

	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("G_Pt-300to470"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),
	txtFile = cms.untracked.string("G_Pt-300to470.txt"),

 )

process.p = cms.Path(process.GammaJet_300to470)
