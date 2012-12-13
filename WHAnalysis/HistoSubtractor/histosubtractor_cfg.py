import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")


process.WH_125 = cms.EDAnalyzer('HistoSubtractor',

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/"),

        outputFile = cms.untracked.string("cazziemazzi.root"),

        mainSample = cms.untracked.string("histo_WH_125_53X.root"),

        samples = cms.untracked.vstring("histo_WH_125_53X.root","histo_WH_125_53X.root"),

        labels = cms.untracked.vstring("WH_125"),

)


process.p = cms.Path(process.WH_125)
