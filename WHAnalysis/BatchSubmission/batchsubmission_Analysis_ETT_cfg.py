import FWCore.ParameterSet.Config as cms

process = cms.Process("ETT")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

pathForSaving    = "/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"
pathCFGLocation  = "/cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/"
fileLocation     = "/cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/"
channel          = "ETT"
cshTemp          = "batchJob_cmssusy.csh"

process.DYJetsToLL_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYJetsToLL"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/DYJetsToLL_ETT_TauID.txt"),

)

process.DYToEE_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToEE"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/DYToEE_ETT_TauID.txt"),

)

process.DYToTauTau_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToTauTau"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/DYToTauTau_ETT_TauID.txt"),

)

process.GVJets_ett  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("GVJets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/GVJets_ETT_TauID.txt"),

)

process.QCD20_30_BCtoE_ett  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("QCD20_30_BCtoE"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/QCD20_30_BCtoE_ETT_TauID.txt"),

)

process.QCD20_30_EM_ett  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("QCD20_30_EM"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/QCD20_30_EM_ETT_TauID.txt"),

)

process.QCD30_80_BCtoE_ett  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("QCD30_80_BCtoE"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/QCD30_80_BCtoE_ETT_TauID.txt"),

)

process.QCD30_80_EM_ett  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("QCD30_80_EM"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/QCD30_80_EM_ETT_TauID.txt"),

)

process.QCD80_170_BCtoE_ett  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("QCD80_170_BCtoE"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/QCD80_170_BCtoE_ETT_TauID.txt"),

)

process.QCD80_170_EM_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("QCD80_170_EM"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/QCD80_170_EM_ETT_TauID.txt"),

)

process.TTH_110_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_110"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_ETT_TauID.txt"),

)

process.TTH_115_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_115"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_ETT_TauID.txt"),

)

process.TTH_120_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_120"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_ETT_TauID.txt"),

)

process.TTH_125_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_125"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_ETT_TauID.txt"),

)

process.TTH_130_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_130"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_ETT_TauID.txt"),

)

process.TTH_135_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_135"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_ETT_TauID.txt"),

)

process.WH_110_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_110"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_ETT_TauID.txt"),

)

process.WH_115_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_115"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_ETT_TauID.txt"),

)

process.WH_120_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_120"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_ETT_TauID.txt"),

)

process.WH_125_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_125"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_ETT_TauID.txt"),

)

process.WH_130_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_130"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_ETT_TauID.txt"),

)

process.WH_135_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_135"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_ETT_TauID.txt"),

)

process.ZH_110_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_110"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_ETT_TauID.txt"),

)

process.ZH_115_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_115"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_ETT_TauID.txt"),

)

process.ZH_120_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_120"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_ETT_TauID.txt"),

)

process.ZH_125_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_125"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_ETT_TauID.txt"),

)

process.ZH_130_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_130"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_ETT_TauID.txt"),

)

process.ZH_135_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_135"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_ETT_TauID.txt"),

)

process.TTJets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTJets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/TTJets_ETT_TauID.txt"),

)

process.WJets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WJets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WJets_ETT_TauID.txt"),

)

process.WW_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WW"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WW_ETT_TauID.txt"),

)

process.WZ_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WZ"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/WZ_ETT_TauID.txt"),

)

process.ZZ_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZZ"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/ZZ_ETT_TauID.txt"),

)

process.TauPlusXAug5 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXAug5"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/TauPlusXAug5_Trigger_TauID.txt"),

)

process.TauPlusXMay10 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXMay10"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/TauPlusXMay10_Trigger_TauID.txt"),

)

process.TauPlusXPromptReco4 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco4"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/TauPlusXPromptReco4_Trigger_TauID.txt"),

)

process.TauPlusXPromptReco6 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco6"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/TauPlusXPromptReco6_Trigger_TauID.txt"),

)

process.TauPlusX_Run2011B_PromptReco1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_Run2011B_PromptReco1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/TauPlusX_Run2011B_PromptReco1_Trigger_TauID.txt"),

)

process.p = cms.Path(
	process.DYJetsToLL_ett +
	process.DYToEE_ett +
	process.DYToTauTau_ett +
	process.GVJets_ett +
	process.QCD20_30_BCtoE_ett +
	process.QCD20_30_EM_ett +
	process.QCD30_80_BCtoE_ett +
	process.QCD30_80_EM_ett +
	process.QCD80_170_BCtoE_ett +
	process.QCD80_170_EM_ett +
	process.TTH_110_ett + process.TTH_115_ett + process.TTH_120_ett + process.TTH_125_ett + process.TTH_130_ett + process.TTH_135_ett +
	process.WH_110_ett + process.WH_115_ett + process.WH_120_ett + process.WH_125_ett + process.WH_130_ett + process.WH_135_ett + 
	process.ZH_110_ett + process.ZH_115_ett + process.ZH_120_ett + process.ZH_125_ett + process.ZH_130_ett + process.ZH_135_ett +
	process.TTJets_ett +
	process.WJets_ett +
	process.WW_ett +
	process.WZ_ett +
	process.ZZ_ett +
	process.TauPlusXAug5 + process.TauPlusXMay10 + process.TauPlusXPromptReco4 + process.TauPlusXPromptReco6 + process.TauPlusX_Run2011B_PromptReco1
)
