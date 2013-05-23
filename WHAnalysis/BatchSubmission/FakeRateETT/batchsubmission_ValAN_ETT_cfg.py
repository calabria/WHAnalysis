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
channel          = "ETT_ValAN"
cshTemp          = "batchJob_cmssusy.csh"

process.TauPlusX_RunA_06Aug2012_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_06Aug2012_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunA_06Aug2012_ETT.txt"),

)

process.TauPlusX_RunA_13Jul2012_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_13Jul2012_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunA_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunB_13Jul2012_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunB_13Jul2012_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunB_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunC_24Aug2012_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_24Aug2012_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunC_24Aug2012_ETT.txt"),

)

process.TauPlusX_RunC_PRv2_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_PRv2_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunC_PRv2_ETT.txt"),

)

process.TauPlusX_RunD_PRv1_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunD_PRv1_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TauPlusX_RunD_PRv1_ETT.txt"),

)

process.WZ_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_MC_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WZ_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/WZ_ETT_ETT.txt"),

)

process.ZZ_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_MC_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZZ_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/ZZ_ETT_ETT.txt"),

)

process.DYJetsToLL_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_MC_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYJetsToLL_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/DYJetsToLL_ETT_ETT.txt"),

)

process.TTJets_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_MC_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTJets_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/TTJets_ETT_ETT.txt"),

)

process.WJets_v1_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_MC_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WJets_v1_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/WJets_ETT_v1_ETT.txt"),

)

process.WJets_v2_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_MC_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WJets_v2_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/WJets_ETT_v2_ETT.txt"),

)

process.WW_AN1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_Validity_AN1_MC_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WW_AN1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation+"channelETT_53X/WW_ETT_ETT.txt"),

)

process.p = cms.Path(
	process.TauPlusX_RunA_06Aug2012_AN1 + 
	process.TauPlusX_RunA_13Jul2012_AN1 + 
	process.TauPlusX_RunB_13Jul2012_AN1 + 
	process.TauPlusX_RunC_24Aug2012_AN1 + 
	process.TauPlusX_RunC_PRv2_AN1 +
	process.TauPlusX_RunD_PRv1_AN1 +
	process.WZ_AN1 +
	process.ZZ_AN1 +
	process.DYJetsToLL_AN1 +
	process.TTJets_AN1 +
	process.WJets_v1_AN1 +
	process.WJets_v2_AN1 +
	process.WW_AN1
)
