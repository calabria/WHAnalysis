import FWCore.ParameterSet.Config as cms

process = cms.Process("ETT")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

pathForSaving    = "/lustre/cms/store/user/calabria/Data/Analisi/ETT/"
pathCFGLocation  = "/cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/"
fileLocation     = "/cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TXTFiles/"
channel          = "ETT"
cshTemp          = "batchJob_cmssusy.csh"

process.TauPlusXAug5FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXAug5FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXAug5_Trigger_TauID.txt"),

)

process.TauPlusXMay10FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXMay10FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXMay10_Trigger_TauID.txt"),

)

process.TauPlusXPromptReco4FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco4FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXPromptReco4_Trigger_TauID.txt"),

)

process.TauPlusXPromptReco6FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco6FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXPromptReco6_Trigger_TauID.txt"),

)

process.TauPlusX_Run2011B_PromptReco1FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_Run2011B_PromptReco1FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusX_Run2011B_PromptReco1_Trigger_TauID.txt"),

)

################################################################################################################################################

process.TauPlusXAug5FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXAug5FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXAug5_Trigger_TauID.txt"),

)

process.TauPlusXMay10FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXMay10FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXMay10_Trigger_TauID.txt"),

)

process.TauPlusXPromptReco4FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco4FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXPromptReco4_Trigger_TauID.txt"),

)

process.TauPlusXPromptReco6FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco6FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXPromptReco6_Trigger_TauID.txt"),

)

process.TauPlusX_Run2011B_PromptReco1FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateLep2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_Run2011B_PromptReco1FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusX_Run2011B_PromptReco1_Trigger_TauID.txt"),

)

################################################################################################################################################

process.TauPlusXAug5QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXAug5QCD"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXAug5.txt"),

)

process.TauPlusXMay10QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXMay10QCD"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXMay10.txt"),

)

process.TauPlusXPromptReco4QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco4QCD"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXPromptReco4.txt"),

)

process.TauPlusXPromptReco6QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco6QCD"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXPromptReco6.txt"),

)

process.TauPlusX_Run2011B_PromptReco1QCD = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_FakeRateQCD_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_Run2011B_PromptReco1QCD"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusX_Run2011B_PromptReco1.txt"),

)

################################################################################################################################################

process.TauPlusXAug5DC = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DoubleCounting_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXAug5DC"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXAug5.txt"),

)

process.TauPlusXMay10DC = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DoubleCounting_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXMay10DC"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXMay10.txt"),

)

process.TauPlusXPromptReco4DC = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DoubleCounting_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco4DC"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXPromptReco4.txt"),

)

process.TauPlusXPromptReco6DC = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DoubleCounting_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusXPromptReco6DC"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusXPromptReco6.txt"),

)

process.TauPlusX_Run2011B_PromptReco1DC = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DoubleCounting_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_Run2011B_PromptReco1DC"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"/TauPlusX_Run2011B_PromptReco1.txt"),

)


process.p = cms.Path(
	process.TauPlusXAug5FR1 + 
	process.TauPlusXMay10FR1 + 
	process.TauPlusXPromptReco4FR1 + 
	process.TauPlusXPromptReco6FR1 + 
	process.TauPlusX_Run2011B_PromptReco1FR1 +
	process.TauPlusXAug5FR2 + 
	process.TauPlusXMay10FR2 + 
	process.TauPlusXPromptReco4FR2 + 
	process.TauPlusXPromptReco6FR2 + 
	process.TauPlusX_Run2011B_PromptReco1FR2 
	#process.TauPlusXAug5QCD + 
	#process.TauPlusXMay10QCD + 
	#process.TauPlusXPromptReco4QCD + 
	#process.TauPlusXPromptReco6QCD + 
	#process.TauPlusX_Run2011B_PromptReco1QCD
	#process.TauPlusXAug5DC + 
	#process.TauPlusXMay10DC + 
	#process.TauPlusXPromptReco4DC + 
	#process.TauPlusXPromptReco6DC + 
	#process.TauPlusX_Run2011B_PromptReco1DC
)
