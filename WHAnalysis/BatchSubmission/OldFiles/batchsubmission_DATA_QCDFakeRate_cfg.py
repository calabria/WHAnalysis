import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.SingleMuAug05  = cms.EDAnalyzer('BatchSubmission',

	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_QCDFakeRate_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("SingleMuAug05_QCDFakeRate"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/"),
	txtFile = cms.untracked.string("SingleMuAug5_GRID.txt"),

 )

process.SingleMuMay10  = cms.EDAnalyzer('BatchSubmission',

	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_QCDFakeRate_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("SingleMuMay10_QCDFakeRate"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/"),
	txtFile = cms.untracked.string("SingleMuMay10_GRID.txt"),

 )

process.SingleMuPromptReco4  = cms.EDAnalyzer('BatchSubmission',

	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_QCDFakeRate_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("SingleMuPromptReco4_QCDFakeRate"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/"),
	txtFile = cms.untracked.string("SingleMuPromptReco4_GRID.txt"),

 )

process.SingleMuPromptReco6  = cms.EDAnalyzer('BatchSubmission',

	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_QCDFakeRate_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("SingleMuPromptReco6_QCDFakeRate"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/"),
	txtFile = cms.untracked.string("SingleMuPromptReco6_GRID.txt"),

 )

process.p = cms.Path(process.SingleMuAug05 + process.SingleMuMay10 + process.SingleMuPromptReco4 + process.SingleMuPromptReco6)
