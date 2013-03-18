import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("ETT")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

CMSSW_BASE       = os.environ['CMSSW_BASE']
pathForSaving    = "/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/"
pathCFGLocation  = CMSSW_BASE + "/src/WHAnalysis/SimpleCounter/"
fileLocation     = CMSSW_BASE + "/src/WHAnalysis/SimpleCounter/TXTFiles/"
channel          = "ETT"
cshTemp          = "batchJob_cmssusy.csh"

process.DYJetsToLL_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYJetsToLL"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYJetsToLL_ETT_ETT.txt"),

)

process.DYToEE_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToEE"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYToEE_ETT_ETT.txt"),

)

process.DYToMuMu_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToMuMu"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYToMuMu_ETT_ETT.txt"),

)

process.DYToTauTau_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToTauTau"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYToTauTau_ETT_ETT.txt"),

)

process.DYToEE_ett_HS = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToEE_ett_HS"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYToEE_ETT_HS_ETT.txt"),

)

process.DYToMuMu_ett_HS = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToMuMu_ett_HS"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYToMuMu_ETT_HS_ETT.txt"),

)

process.DYToTauTau_ett_HS = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToTauTau_ett_HS"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYToTauTau_ETT_HS_ETT.txt"),

)

process.DYToEE_mtt_HS = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToEE_mtt_HS"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYToEE_MTT_HS_MTT.txt"),

)

process.DYToMuMu_mtt_HS = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToMuMu_mtt_HS"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYToMuMu_MTT_HS_MTT.txt"),

)

process.DYToTauTau_mtt_HS = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("DYToTauTau_mtt_HS"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/DYToTauTau_MTT_HS_MTT.txt"),

)

process.WH_110_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_110"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_110_ETT_ETT.txt"),

)

process.WH_115_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_115"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_115_ETT_ETT.txt"),

)

process.WH_120_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_120"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_120_ETT_ETT.txt"),

)

process.WH_125_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_125"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_125_ETT_ETT.txt"),

)

process.WH_130_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_130"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_130_ETT_ETT.txt"),

)

process.WH_135_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_135"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_135_ETT_ETT.txt"),

)

process.WH_140_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_140"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_140_ETT_ETT.txt"),

)

process.WH_145_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_145"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_145_ETT_ETT.txt"),

)

process.WH_150_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_150"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_150_ETT_ETT.txt"),

)

process.WH_155_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_155"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_155_ETT_ETT.txt"),

)

process.WH_160_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_160"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_160_ETT_ETT.txt"),

)

process.WH_110_ett_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_110_ett_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_110_ETT_LepDecay_ETT.txt"),

)

process.WH_115_ett_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_115_ett_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_115_ETT_LepDecay_ETT.txt"),

)

process.WH_120_ett_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_120_ett_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_120_ETT_LepDecay_ETT.txt"),

)

process.WH_125_ett_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_125_ett_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_125_ETT_LepDecay_ETT.txt"),

)

process.WH_130_ett_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_130_ett_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_130_ETT_LepDecay_ETT.txt"),

)

process.WH_135_ett_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_135_ett_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_135_ETT_LepDecay_ETT.txt"),

)

process.WH_140_ett_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_140_ett_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_140_ETT_LepDecay_ETT.txt"),

)

process.WH_145_ett_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_145_ett_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_145_ETT_LepDecay_ETT.txt"),

)

process.WH_110_mtt_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_110_mtt_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_110_MTT_LepDecay_MTT.txt"),

)

process.WH_115_mtt_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_115_mtt_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_115_MTT_LepDecay_MTT.txt"),

)

process.WH_120_mtt_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_120_mtt_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_120_MTT_LepDecay_MTT.txt"),

)

process.WH_125_mtt_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_125_mtt_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_125_MTT_LepDecay_MTT.txt"),

)

process.WH_130_mtt_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_130_mtt_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_130_MTT_LepDecay_MTT.txt"),

)

process.WH_135_mtt_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_135_mtt_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_135_MTT_LepDecay_MTT.txt"),

)

process.WH_140_mtt_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_140_mtt_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_140_MTT_LepDecay_MTT.txt"),

)

process.WH_145_mtt_LepDecay = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_145_mtt_LepDecay"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WH_145_MTT_LepDecay_MTT.txt"),

)

process.TTJets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TTJets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/TTJets_ETT_ETT.txt"),

)

process.WJets_ett_v1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WJets_v1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WJets_ETT_v1_ETT.txt"),

)

process.WJets_ett_v2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WJets_v2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WJets_ETT_v2_ETT.txt"),

)

process.W1Jets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("W1Jets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/W1Jets_ETT_ETT.txt"),

)

process.W2Jets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("W2Jets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/W2Jets_ETT_ETT.txt"),

)

process.W3Jets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("W3Jets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/W3Jets_ETT_ETT.txt"),

)

process.W4Jets_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("W4Jets"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/W4Jets_ETT_ETT.txt"),

)

process.WW_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WW"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WW_ETT_ETT.txt"),

)

process.WZ_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WZ"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/WZ_ETT_ETT.txt"),

)

process.ZZ_ett = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("ZZ"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/ZZ_ETT_ETT.txt"),

)

process.TauPlusX_RunA_06Aug2012 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_06Aug2012"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/TauPlusX_RunA_06Aug2012_ETT.txt"),

)

process.TauPlusX_RunA_13Jul2012 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunA_13Jul2012"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/TauPlusX_RunA_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunB_13Jul2012 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunB_13Jul2012"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/TauPlusX_RunB_13Jul2012_ETT.txt"),

)

process.TauPlusX_RunC_24Aug2012 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_24Aug2012"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/TauPlusX_RunC_24Aug2012_ETT.txt"),

)

process.TauPlusX_RunC_PRv2 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunC_PRv2"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/TauPlusX_RunC_PRv2_ETT.txt"),

)

process.TauPlusX_RunD_PRv1 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("simplecounter_cfg.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("TauPlusX_RunD_PRv1"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string("/cmshome/calabria/prog/channelETT_53X/TauPlusX_RunD_PRv1_ETT.txt"),

)

process.p = cms.Path(
	#process.DYJetsToLL_ett +
	#process.DYToEE_ett +
	#process.DYToMuMu_ett +
	#process.DYToTauTau_ett +
	process.DYToEE_ett_HS +
	#process.DYToMuMu_ett_HS +
	process.DYToTauTau_ett_HS +
	process.DYToEE_mtt_HS +
	process.DYToMuMu_mtt_HS +
	process.DYToTauTau_mtt_HS +
	#process.WH_110_ett + 
	#process.WH_115_ett + 
	#process.WH_120_ett + 
	#process.WH_125_ett + 
	#process.WH_130_ett + 
	#process.WH_135_ett + 
	#process.WH_140_ett + 
	#process.WH_145_ett + 
	#process.WH_150_ett + 
	#process.WH_155_ett + 
	#process.WH_160_ett + 
	process.WH_110_ett_LepDecay + 
	process.WH_115_ett_LepDecay + 
	process.WH_120_ett_LepDecay + 
	process.WH_125_ett_LepDecay + 
	process.WH_130_ett_LepDecay + 
	process.WH_135_ett_LepDecay + 
	process.WH_140_ett_LepDecay + 
	process.WH_145_ett_LepDecay + 
	process.WH_110_mtt_LepDecay + 
	process.WH_115_mtt_LepDecay + 
	process.WH_120_mtt_LepDecay + 
	process.WH_125_mtt_LepDecay + 
	process.WH_130_mtt_LepDecay + 
	process.WH_135_mtt_LepDecay + 
	process.WH_140_mtt_LepDecay + 
	process.WH_145_mtt_LepDecay 
	#process.TTJets_ett +
	#process.WJets_ett_v1 +
	#process.WJets_ett_v2 +
	#process.W1Jets_ett +
	#process.W2Jets_ett +
	#process.W3Jets_ett +
	#process.W4Jets_ett +
	#process.WW_ett +
	#process.WZ_ett +
	#process.ZZ_ett +
	#process.TauPlusX_RunA_06Aug2012 + 
	#process.TauPlusX_RunA_13Jul2012 + 
	#process.TauPlusX_RunB_13Jul2012 + 
	#process.TauPlusX_RunC_24Aug2012 + 
	#process.TauPlusX_RunC_PRv2 +
	#process.TauPlusX_RunD_PRv1
)
