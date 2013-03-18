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
pathCFGLocation  = CMSSW_BASE + "/src/WHAnalysis/BatchSubmission/"
fileLocation     = CMSSW_BASE + "/src/WHAnalysis/BatchSubmission/TXTFiles/"
channel          = "ETT"
cshTemp          = "batchJob_cmssusy.csh"

process.DYJetsToLL_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYJetsToLL"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/DYJetsToLL_ETT_ETT.txt"),

)

process.DYToEE_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToEE"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/DYToEE_ETT_ETT.txt"),

)

process.DYToMuMu_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToMuMu"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/DYToMuMu_ETT_ETT.txt"),

)

process.DYToTauTau_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToTauTau"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/DYToTauTau_ETT_ETT.txt"),

)

process.TTH_110_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_110"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_110_ETT_ETT.txt"),

)

process.TTH_115_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_115"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_115_ETT_ETT.txt"),

)

process.TTH_120_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_120"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_120_ETT_ETT.txt"),

)

process.TTH_125_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_125"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_125_ETT_ETT.txt"),

)

process.TTH_130_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_130"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_130_ETT_ETT.txt"),

)

process.TTH_135_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_135"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_135_ETT_ETT.txt"),

)

process.TTH_140_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_140"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_140_ETT_ETT.txt"),

)

process.TTH_145_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_145"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_145_ETT_ETT.txt"),

)

process.TTH_150_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_150"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_150_ETT_ETT.txt"),

)

process.TTH_155_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_155"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_155_ETT_ETT.txt"),

)


process.TTH_160_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_TTH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTH_160"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_160_ETT_ETT.txt"),

)

process.WH_110_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_110"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_110_ETT_ETT.txt"),

)

process.WH_115_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_115"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_115_ETT_ETT.txt"),

)

process.WH_120_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_120"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_120_ETT_ETT.txt"),

)

process.WH_125_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_125"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_125_ETT_ETT.txt"),

)

process.WH_130_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_130"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_130_ETT_ETT.txt"),

)

process.WH_135_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_135"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_135_ETT_ETT.txt"),

)

process.WH_140_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_140"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_140_ETT_ETT.txt"),

)

process.WH_145_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_145"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_145_ETT_ETT.txt"),

)

process.WH_150_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_150"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_150_ETT_ETT.txt"),

)

process.WH_155_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_155"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_155_ETT_ETT.txt"),

)

process.WH_160_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_WH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_160"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_160_ETT_ETT.txt"),

)

process.ZH_110_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_110"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_110_ETT_ETT.txt"),

)

process.ZH_115_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_115"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_115_ETT_ETT.txt"),

)

process.ZH_120_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_120"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_120_ETT_ETT.txt"),

)

process.ZH_125_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_125"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_125_ETT_ETT.txt"),

)

process.ZH_130_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_130"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_130_ETT_ETT.txt"),

)

process.ZH_135_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_135"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_135_ETT_ETT.txt"),

)

process.ZH_140_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_140"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_140_ETT_ETT.txt"),

)

process.ZH_145_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_145"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_145_ETT_ETT.txt"),

)

process.ZH_150_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_150"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_150_ETT_ETT.txt"),

)

process.ZH_155_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_155"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_155_ETT_ETT.txt"),

)

process.ZH_160_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ZH_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZH_160"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WH_160_ETT_ETT.txt"),

)

process.TTJets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTJets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/TTJets_ETT_ETT.txt"),

)

process.WJets_v1_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WJets_v1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WJets_ETT_v1_ETT.txt"),

)

process.WJets_v2_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WJets_v2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WJets_ETT_v2_ETT.txt"),

)

process.W1Jets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("W1Jets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/W1Jets_ETT_ETT.txt"),

)

process.W2Jets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("W2Jets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/W2Jets_ETT_ETT.txt"),

)

process.W3Jets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("W3Jets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/W3Jets_ETT_ETT.txt"),

)

process.W4Jets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("W4Jets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/W4Jets_ETT_ETT.txt"),

)

process.WW_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WW"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WW_ETT_ETT.txt"),

)

process.WZ_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WZ"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/WZ_ETT_ETT.txt"),

)

process.ZZ_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZZ"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/ZZ_ETT_ETT.txt"),

)

process.TauPlusX_RunA_06Aug2012 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_06Aug2012"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/TauPlusX_RunA_06Aug2012_ETT.txt"),

)

process.TauPlusX_RunA_13Jul2012 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_13Jul2012"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/TauPlusX_RunA_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunB_13Jul2012 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunB_13Jul2012"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/TauPlusX_RunB_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunC_24Aug2012 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_24Aug2012"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/TauPlusX_RunC_24Aug2012_ETT.txt"),

)

process.TauPlusX_RunC_PRv2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_PRv2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/TauPlusX_RunC_PRv2_ETT.txt"),

)

process.TauPlusX_RunD_PRv1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_DATA_ett_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunD_PRv1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("./TXTFiles/channelETT_53X/TauPlusX_RunD_PRv1_ETT.txt"),

)


process.p = cms.Path(
	#process.DYJetsToLL_ett +
	#process.DYToEE_ett +
	#process.DYToMuMu_ett +
	#process.DYToTauTau_ett +
	#process.TTH_110_ett + 
	#process.TTH_115_ett + 
	#process.TTH_120_ett + 
	#process.TTH_125_ett + 
	#process.TTH_130_ett + 
	#process.TTH_135_ett +
	#process.TTH_140_ett + 
	#process.TTH_145_ett +
	#process.TTH_150_ett +
	#process.TTH_155_ett +
	#process.TTH_160_ett +
	process.WH_110_ett + 
	process.WH_115_ett + 
	process.WH_120_ett + 
	process.WH_125_ett + 
	process.WH_130_ett + 
	process.WH_135_ett + 
	process.WH_140_ett + 
	process.WH_145_ett + 
	process.WH_150_ett + 
	process.WH_155_ett + 
	process.WH_160_ett + 
	#process.ZH_110_ett + 
	#process.ZH_115_ett + 
	#process.ZH_120_ett + 
	#process.ZH_125_ett + 
	#process.ZH_130_ett + 
	#process.ZH_135_ett +
	#process.ZH_140_ett +
	#process.ZH_145_ett +
	#process.ZH_150_ett +
	#process.ZH_155_ett +
	#process.ZH_160_ett +
	#process.TTJets_ett +
	#process.WJets_v1_ett +
	#process.WJets_v2_ett +
	#process.W1Jets_ett +
	#process.W2Jets_ett +
	#process.W3Jets_ett +
	#process.W4Jets_ett +
	process.WW_ett +
	process.WZ_ett +
	process.ZZ_ett +
	process.TauPlusX_RunA_06Aug2012 + 
	process.TauPlusX_RunA_13Jul2012 + 
	process.TauPlusX_RunB_13Jul2012 + 
	process.TauPlusX_RunC_24Aug2012 + 
	process.TauPlusX_RunC_PRv2 +
	process.TauPlusX_RunD_PRv1
)
