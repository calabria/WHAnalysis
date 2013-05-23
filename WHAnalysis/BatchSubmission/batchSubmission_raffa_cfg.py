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
channel          = "MTT"
cshTemp          = "batchJob_cmssusy.csh"

process.WH_125_mtt = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("test_template.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("WH_125"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation + "prog/ETT/WH125_MTT_NoSkim_MTT2.txt"),
	PatNumber = cms.untracked.int32(10),

)

process.p = cms.Path(
	process.WH_125_mtt
)
