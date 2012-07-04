import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")


process.WH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.5729*0.0637), #WH_125

	skimEff = cms.untracked.vdouble(1.0),

        path = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/"),

        outputFile = cms.untracked.string("./ETT/WH_125_Check_3.root"),

        samples = cms.untracked.vstring("histo_WH125_Check_3.root"),

        labels = cms.untracked.vstring("WH_125"),

        intLumi = cms.untracked.double(5051),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi"),

        txtFile = cms.untracked.string("./ETT/output_WH_125_Check_3.txt")

)

process.p = cms.Path(process.WH_125)
