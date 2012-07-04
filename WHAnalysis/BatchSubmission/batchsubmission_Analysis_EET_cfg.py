import FWCore.ParameterSet.Config as cms

process = cms.Process("EET")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.DYJetsToLL_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DYJetsToLL"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/DYJetsToLL_EET.txt"),

)

process.GVJets_eet  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("GVJets"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/GVJets_EET.txt"),

)

process.QCD20_30_BCtoE_eet  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD20_30_BCtoE"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD20_30_BCtoE_EET.txt"),

)

process.QCD20_30_EM_eet  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD20_30_EM"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD20_30_EM_EET.txt"),

)

process.QCD30_80_BCtoE_eet  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD30_80_BCtoE"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD30_80_BCtoE_EET.txt"),

)

process.QCD30_80_EM_eet  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD30_80_EM"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD30_80_EM_EET.txt"),

)

process.QCD80_170_BCtoE_eet  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD80_170_BCtoE"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD80_170_BCtoE_EET.txt"),

)

process.QCD80_170_EM_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD80_170_EM"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD80_170_EM_EET.txt"),

)

process.TTH_110_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_110"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_EET.txt"),

)

process.TTH_115_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_115"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_EET.txt"),

)

process.TTH_120_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_120"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_EET.txt"),

)

process.TTH_125_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_125"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_EET.txt"),

)

process.TTH_130_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_130"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_EET.txt"),

)

process.TTH_135_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_135"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_EET.txt"),

)

process.WH_110_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_110"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_EET.txt"),

)

process.WH_115_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_115"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_EET.txt"),

)

process.WH_120_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_120"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_EET.txt"),

)

process.WH_125_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_125"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_EET.txt"),

)

process.WH_130_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_130"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_EET.txt"),

)

process.WH_135_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_135"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_EET.txt"),

)

process.ZH_110_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_110"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_EET.txt"),

)

process.ZH_115_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_115"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_EET.txt"),

)

process.ZH_120_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_120"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_EET.txt"),

)

process.ZH_125_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_125"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_EET.txt"),

)

process.ZH_130_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_130"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_EET.txt"),

)

process.ZH_135_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_135"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_EET.txt"),

)

process.TTJets_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTJets"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/TTJets_EET.txt"),

)

process.WJets_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WJets"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WJets_EET.txt"),

)

process.WW_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WW"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WW_EET.txt"),

)

process.WZ_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WZ"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/WZ_EET.txt"),

)

process.ZZ_eet = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZZ"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/ZZ_EET.txt"),

)

process.DoubleElectronAug5 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronAug5"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleElectronAug5.txt"),

)

process.DoubleElectronMay10 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronMay10"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleElectronMay10.txt"),

)

process.DoubleElectronPromptReco4 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronPromptReco4"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleElectronPromptReco4.txt"),

)

process.DoubleElectronPromptReco6 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectronPromptReco6"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleElectronPromptReco6.txt"),

)

process.DoubleElectron_Run2011B_PromptReco1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EET"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleElectron_Run2011B_PromptReco1"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleElectron_Run2011B_PromptReco1.txt"),

)

process.p = cms.Path(
	process.DYJetsToLL_eet +
	process.GVJets_eet +
	process.QCD20_30_BCtoE_eet +
	process.QCD20_30_EM_eet +
	process.QCD30_80_BCtoE_eet +
	process.QCD30_80_EM_eet +
	process.QCD80_170_BCtoE_eet +
	process.QCD80_170_EM_eet +
	process.TTH_110_eet + process.TTH_115_eet + process.TTH_120_eet + process.TTH_125_eet + process.TTH_130_eet + process.TTH_135_eet +
	process.WH_110_eet + process.WH_115_eet + process.WH_120_eet + process.WH_125_eet + process.WH_130_eet + process.WH_135_eet + 
	process.ZH_110_eet + process.ZH_115_eet + process.ZH_120_eet + process.ZH_125_eet + process.ZH_130_eet + process.ZH_135_eet +
	process.TTJets_eet +
	process.WJets_eet +
	process.WW_eet +
	process.WZ_eet +
	process.ZZ_eet +
	process.DoubleElectronAug5 + process.DoubleElectronMay10 + process.DoubleElectronPromptReco4 + process.DoubleElectronPromptReco6 + process.DoubleElectron_Run2011B_PromptReco1
)
