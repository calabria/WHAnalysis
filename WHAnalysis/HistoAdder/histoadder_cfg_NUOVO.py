import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")

process.demo = cms.EDAnalyzer('HistoAdder',

	nostack = cms.untracked.bool(False),

        path = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/HistoAdderFirstStep/"),

        samples = cms.untracked.vstring("WH_115.root",
                                        "TTH_115.root",
                                        "ZH_115.root",
				        "DiBosons.root",
                                        "EWK.root",
                                        "DY.root",
                                        "QCD.root",
				       ),

	data = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/histo_data.root"),
        #data = cms.untracked.string(""),

        labels = cms.untracked.vstring("WH_115",
                                       "TTH_115",
				       "ZH_115",
				       "DiBosons",
                                       "EWK",
				       "DY",
				       "QCD",
				      ),

        logScale = cms.untracked.bool(False),

        setColors = cms.untracked.vdouble(2.,
					  8.,
                                          4.,
					  50.,
                                          6.,
                                          5.,
					  38.,
					 ),

	legendLabels = cms.untracked.vstring("WH 115 (x5)",
                                             "t#bar{t}H 115 (x5)",
				             "ZH 115 (x5)",
					     "DiBoson",
                                             "EWK",
				             "Drell Yan",
				             "QCD",
					    ),

        legendDim = cms.untracked.vdouble(0.75, 0.60, 0.9, 0.9),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("outputTOT_WholeStat.txt")

)

process.p = cms.Path(process.demo)
