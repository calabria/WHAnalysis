import FWCore.ParameterSet.Config as cms


process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet(
     input = cms.untracked.int32(1)
     )
process.source = cms.Source("EmptySource")


process.QCD20_30_EM_FATT  = cms.EDAnalyzer('BatchSubmission',
                                   fileCFG = cms.untracked.string("WMuNuHTauTauAnalyzer_cfg.py"),
                                   fileCSH = cms.untracked.string("batchJob_cmssusy.csh"),
                                   sample = cms.untracked.string("QCD20_30_EM_FATT"),
                                   pathCFG = cms.untracked.string("/cmshome/venditti/PU_analisiWH/CMSSW_4_2_4_patch2/src/"),
                                   castorPath = cms.untracked.string("/lustre/cms/store/user/rvenditti/Analisi/QCD20_30_EM/"),
                                   tmpPath = cms.untracked.string("/lustre/cms/store/user/rvenditti/"),
                                   txtFile = cms.untracked.string("QCD20_30_EM_2.txt"),
 )

process.p = cms.Path(process.QCD20_30_EM_FATT)
