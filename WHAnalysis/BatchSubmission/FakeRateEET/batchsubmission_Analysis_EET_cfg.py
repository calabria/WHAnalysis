import FWCore.ParameterSet.Config as cms

process = cms.Process("EET")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.DoubleElectronAug5FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronAug5FR1"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronAug5.txt"),

)

process.DoubleElectronMay10FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronMay10FR1"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronMay10.txt"),

)

process.DoubleElectronPromptReco4FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronPromptReco4FR1"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronPromptReco4.txt"),

)

process.DoubleElectronPromptReco6FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronPromptReco6FR1"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronPromptReco6.txt"),

)

process.DoubleElectron_Run2011B_PromptReco1FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectron_Run2011B_PromptReco1FR1"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectron_Run2011B_PromptReco1.txt"),

)

################################################################################################################################################

process.DoubleElectronAug5FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronAug5FR2"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronAug5.txt"),

)

process.DoubleElectronMay10FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronMay10FR2"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronMay10.txt"),

)

process.DoubleElectronPromptReco4FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronPromptReco4FR2"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronPromptReco4.txt"),

)

process.DoubleElectronPromptReco6FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronPromptReco6FR2"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronPromptReco6.txt"),

)

process.DoubleElectron_Run2011B_PromptReco1FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectron_Run2011B_PromptReco1FR2"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectron_Run2011B_PromptReco1.txt"),

)

################################################################################################################################################

process.DoubleElectronAug5QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronAug5QCD"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronAug5.txt"),

)

process.DoubleElectronMay10QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronMay10QCD"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronMay10.txt"),

)

process.DoubleElectronPromptReco4QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronPromptReco4QCD"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronPromptReco4.txt"),

)

process.DoubleElectronPromptReco6QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronPromptReco6QCD"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectronPromptReco6.txt"),

)

process.DoubleElectron_Run2011B_PromptReco1QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectron_Run2011B_PromptReco1QCD"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/DoubleElectron_Run2011B_PromptReco1.txt"),

)


process.p = cms.Path(
	process.DoubleElectronAug5FR1 + 
	process.DoubleElectronMay10FR1 + 
	process.DoubleElectronPromptReco4FR1 + 
	process.DoubleElectronPromptReco6FR1 + 
	process.DoubleElectron_Run2011B_PromptReco1FR1 +
	process.DoubleElectronAug5FR2 + 
	process.DoubleElectronMay10FR2 + 
	process.DoubleElectronPromptReco4FR2 + 
	process.DoubleElectronPromptReco6FR2 + 
	process.DoubleElectron_Run2011B_PromptReco1FR2 +
	process.DoubleElectronAug5QCD + 
	process.DoubleElectronMay10QCD + 
	process.DoubleElectronPromptReco4QCD + 
	process.DoubleElectronPromptReco6QCD + 
	process.DoubleElectron_Run2011B_PromptReco1QCD
)
