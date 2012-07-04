import FWCore.ParameterSet.Config as cms

process = cms.Process("ETT")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")

process.demo = cms.EDAnalyzer('HistoAdder',

	process = cms.untracked.string("ETT"),

	nostack = cms.untracked.bool(False),

        path = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/"),

        samples = cms.untracked.vstring("histo_WH125_Check.root"),

	#data = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/histo_data.root"),
        data = cms.untracked.string(""),

        labels = cms.untracked.vstring("WH_125"),

        logScale = cms.untracked.bool(False),

        setColors = cms.untracked.vdouble(50.),

	legendLabels = cms.untracked.vstring("WH 120"),

        legendDim = cms.untracked.vdouble(0.75, 0.60, 0.9, 0.9),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./Outputs/ETT/outputTOT_ETT_Check.txt"),

        energy = cms.untracked.string("7 TeV"),

        lumi = cms.untracked.string("5 fb^{-1}")

)

process.p = cms.Path(process.demo)
