import FWCore.ParameterSet.Config as cms

process = cms.Process("MMT")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.DYJetsToLL_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DYJetsToLL"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/DYJetsToLL_MMT.txt"),

)

process.QCD_20_MU_mmt  = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("QCD_20_MU"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/QCD_20_MU_MMT.txt"),

)

process.TTH_110_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_110"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_MMT.txt"),

)

process.TTH_115_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_115"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_MMT.txt"),

)

process.TTH_120_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_120"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_MMT.txt"),

)

process.TTH_125_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_125"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_MMT.txt"),

)

process.TTH_130_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_130"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_MMT.txt"),

)

process.TTH_135_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTH_135"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_MMT.txt"),

)

process.WH_110_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_110"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_MMT.txt"),

)

process.WH_115_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_115"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_MMT.txt"),

)

process.WH_120_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_120"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_MMT.txt"),

)

process.WH_125_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_125"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_MMT.txt"),

)

process.WH_130_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_130"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_MMT.txt"),

)

process.WH_135_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WH_135"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_MMT.txt"),

)

process.ZH_110_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_110"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_110_MMT.txt"),

)

process.ZH_115_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_115"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_115_MMT.txt"),

)

process.ZH_120_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_120"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_120_MMT.txt"),

)

process.ZH_125_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_125"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_125_MMT.txt"),

)

process.ZH_130_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_130"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_130_MMT.txt"),

)

process.ZH_135_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZH_135"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WH_135_MMT.txt"),

)

process.TTJets_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTJets"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/TTJets_MMT.txt"),

)

process.WJets_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WJets"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WJets_MMT.txt"),

)

process.WW_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WW"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WW_MMT.txt"),

)

process.WZ_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("WZ"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/WZ_MMT.txt"),

)

process.ZZ_mmt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("ZZ"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/ZZ_MMT.txt"),

)

process.DoubleMuAug5 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleMuAug5"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleMuAug5.txt"),

)

process.DoubleMuMay10 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleMuMay10"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleMuMay10.txt"),

)

process.DoubleMuPromptReco4 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleMuPromptReco4"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleMuPromptReco4.txt"),

)

process.DoubleMuPromptReco6 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleMuPromptReco6"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleMuPromptReco6.txt"),

)

process.DoubleMu_Run2011B_PromptReco1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string("MMT"),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("DoubleMu_Run2011B_PromptReco1"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/MMT/"),
	txtFile = cms.untracked.string("./TXTFiles/DoubleMu_Run2011B_PromptReco1.txt"),

)

process.p = cms.Path(
	process.DYJetsToLL_mmt +
	process.QCD_20_MU_mmt +
	process.TTH_110_mmt + process.TTH_115_mmt + process.TTH_120_mmt + process.TTH_125_mmt + process.TTH_130_mmt + process.TTH_135_mmt +
	process.WH_110_mmt + process.WH_115_mmt + process.WH_120_mmt + process.WH_125_mmt + process.WH_130_mmt + process.WH_135_mmt + 
	process.ZH_110_mmt + process.ZH_115_mmt + process.ZH_120_mmt + process.ZH_125_mmt + process.ZH_130_mmt + process.ZH_135_mmt +
	process.TTJets_mmt +
	process.WJets_mmt +
	process.WW_mmt +
	process.WZ_mmt +
	process.ZZ_mmt +
	process.DoubleMuAug5 + process.DoubleMuMay10 + process.DoubleMuPromptReco4 + process.DoubleMuPromptReco6 + process.DoubleMu_Run2011B_PromptReco1
)
