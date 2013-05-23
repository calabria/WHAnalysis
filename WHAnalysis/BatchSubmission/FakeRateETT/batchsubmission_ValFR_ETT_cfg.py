import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("ETT")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

CMSSW_BASE       = os.environ['CMSSW_BASE']
pathForSaving    = "/lustre/cms/store/user/calabria/Data/Analisi_53X/ETT/"
pathCFGLocation  = CMSSW_BASE + "/src/WHAnalysis/BatchSubmission/FakeRateETT/"
fileLocation     = CMSSW_BASE + "/src/WHAnalysis/BatchSubmission/TXTFiles/"
channel          = "ETT_ValFR"
cshTemp          = "batchJob_cmssusy.csh"

process.TauPlusX_RunA_06Aug2012_FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_06Aug2012_FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunA_06Aug2012_ETT.txt"),

)

process.TauPlusX_RunA_13Jul2012_FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_13Jul2012_FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunA_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunB_13Jul2012_FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunB_13Jul2012_FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunB_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunC_24Aug2012_FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_24Aug2012_FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunC_24Aug2012_ETT.txt"),

)

process.TauPlusX_RunC_PRv2_FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_PRv2_FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunC_PRv2_ETT.txt"),

)

process.TauPlusX_RunD_PRv1_FR1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunD_PRv1_FR1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunD_PRv1_ETT.txt"),

)

process.TauPlusX_RunA_06Aug2012_FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_06Aug2012_FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunA_06Aug2012_ETT.txt"),

)

process.TauPlusX_RunA_13Jul2012_FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_13Jul2012_FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunA_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunB_13Jul2012_FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunB_13Jul2012_FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunB_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunC_24Aug2012_FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_24Aug2012_FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunC_24Aug2012_ETT.txt"),

)

process.TauPlusX_RunC_PRv2_FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_PRv2_FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunC_PRv2_ETT.txt"),

)

process.TauPlusX_RunD_PRv1_FR2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_FR2_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunD_PRv1_FR2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunD_PRv1_ETT.txt"),

)


process.p = cms.Path(
	process.TauPlusX_RunA_06Aug2012_FR1 + 
	process.TauPlusX_RunA_13Jul2012_FR1 + 
	process.TauPlusX_RunB_13Jul2012_FR1 + 
	process.TauPlusX_RunC_24Aug2012_FR1 + 
	process.TauPlusX_RunC_PRv2_FR1 +
	process.TauPlusX_RunD_PRv1_FR1
	#process.TauPlusX_RunA_06Aug2012_FR2 + 
	#process.TauPlusX_RunA_13Jul2012_FR2 + 
	#process.TauPlusX_RunB_13Jul2012_FR2 + 
	#process.TauPlusX_RunC_24Aug2012_FR2 + 
	#process.TauPlusX_RunC_PRv2_FR2 +
	#process.TauPlusX_RunD_PRv1_FR2
)
