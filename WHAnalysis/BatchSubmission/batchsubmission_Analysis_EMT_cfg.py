import FWCore.ParameterSet.Config as cms

process = cms.Process("EET")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.DYJetsToLL_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DYJetsToLL"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/DYJetsToLL_EMT.txt"),

)

process.GVJets_emt  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("GVJets"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/GVJets_EMT.txt"),

)

process.QCD20_30_BCtoE_emt  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD20_30_BCtoE"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD20_30_BCtoE_EMT.txt"),

)

process.QCD20_30_EM_emt  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD20_30_EM"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD20_30_EM_EMT.txt"),

)

process.QCD30_80_BCtoE_emt  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD30_80_BCtoE"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD30_80_BCtoE_EMT.txt"),

)

process.QCD30_80_EM_emt  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD30_80_EM"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD30_80_EM_EMT.txt"),

)

process.QCD80_170_BCtoE_emt  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD80_170_BCtoE"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD80_170_BCtoE_EMT.txt"),

)

process.QCD80_170_EM_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD80_170_EM"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD80_170_EM_EMT.txt"),

)

process.QCD_20_MU_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD_20_MU"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD_20_MU_EMT.txt"),

)

process.TTH_110_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_110"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_EMT.txt"),

)

process.TTH_115_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_115"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_EMT.txt"),

)

process.TTH_120_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_120"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_EMT.txt"),

)

process.TTH_125_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_125"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_EMT.txt"),

)

process.TTH_130_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_130"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_EMT.txt"),

)

process.TTH_135_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_135"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_EMT.txt"),

)

process.WH_110_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_110"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_EMT.txt"),

)

process.WH_115_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_115"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_EMT.txt"),

)

process.WH_120_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_120"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_EMT.txt"),

)

process.WH_125_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_125"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_EMT.txt"),

)

process.WH_130_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_130"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_EMT.txt"),

)

process.WH_135_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_135"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_EMT.txt"),

)

process.ZH_110_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_110"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_EMT.txt"),

)

process.ZH_115_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_115"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_EMT.txt"),

)

process.ZH_120_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_120"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_EMT.txt"),

)

process.ZH_125_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_125"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_EMT.txt"),

)

process.ZH_130_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_130"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_EMT.txt"),

)

process.ZH_135_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_135"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_EMT.txt"),

)

process.TTJets_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTJets"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/TTJets_EMT.txt"),

)

process.WJets_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WJets"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WJets_EMT.txt"),

)

process.WW_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WW"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WW_EMT.txt"),

)

process.WZ_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WZ"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WZ_EMT.txt"),

)

process.ZZ_emt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZZ"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/ZZ_EMT.txt"),

)

process.MuEGAug5 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("MuEGAug5"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/MuEGAug5.txt"),

)

process.MuEGMay10 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("MuEGMay10"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/MuEGMay10.txt"),

)

process.MuEGPromptReco4 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("MuEGPromptReco4"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/MuEGPromptReco4.txt"),

)

process.MuEGPromptReco6 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("MuEGPromptReco6"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/MuEGPromptReco6.txt"),

)

process.MuEG_Run2011B_PromptReco1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("EMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_emt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("MuEG_Run2011B_PromptReco1"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),
	txtFile = cms.untracked.string("./TXTFiles/MuEG_Run2011B_PromptReco1.txt"),

)

process.p = cms.Path(
	process.DYJetsToLL_emt +
	process.GVJets_emt +
	process.QCD20_30_BCtoE_emt +
	process.QCD20_30_EM_emt +
	process.QCD30_80_BCtoE_emt +
	process.QCD30_80_EM_emt +
	process.QCD80_170_BCtoE_emt +
	process.QCD80_170_EM_emt +
	process.QCD_20_MU_emt +
	process.TTH_110_emt + process.TTH_115_emt + process.TTH_120_emt + process.TTH_125_emt + process.TTH_130_emt + process.TTH_135_emt +
	process.WH_110_emt + process.WH_115_emt + process.WH_120_emt + process.WH_125_emt + process.WH_130_emt + process.WH_135_emt + 
	process.ZH_110_emt + process.ZH_115_emt + process.ZH_120_emt + process.ZH_125_emt + process.ZH_130_emt + process.ZH_135_emt +
	process.TTJets_emt +
	process.WJets_emt +
	process.WW_emt +
	process.WZ_emt +
	process.ZZ_emt +
	process.MuEGAug5 + process.MuEGMay10 + process.MuEGPromptReco4 + process.MuEGPromptReco6 + process.MuEG_Run2011B_PromptReco1
)
