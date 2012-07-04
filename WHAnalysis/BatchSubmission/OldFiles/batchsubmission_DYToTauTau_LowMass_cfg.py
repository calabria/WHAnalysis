import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.LowMassDYToTauTau = cms.EDAnalyzer('BatchSubmission',

	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DYToTauTau_LowMass"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),
	txtFile = cms.untracked.string("DYToTauTau_LowMass.txt"),

 )

process.p = cms.Path(process.LowMassDYToTauTau)
