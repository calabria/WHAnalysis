import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.TTJets = cms.EDAnalyzer('BatchSubmission',

	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTJets"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),
	txtFile = cms.untracked.string("./TXTFiles/TTJets.txt"),

)

process.TTJets_eet = cms.EDAnalyzer('BatchSubmission',

	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_eet_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTJets_eet"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),
	txtFile = cms.untracked.string("./TXTFiles/TTJets_eet.txt"),

)

process.TTJets_mmt = cms.EDAnalyzer('BatchSubmission',

	fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_mmt_cfg.py"),
	fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),

	sample = cms.untracked.string("TTJets_mmt"),
	pathCFG = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/"),
	savingPath = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),
	txtFile = cms.untracked.string("./TXTFiles/TTJets_mmt.txt"),

)

process.p = cms.Path(process.TTJets + process.TTJets_eet + process.TTJets_mmt)
