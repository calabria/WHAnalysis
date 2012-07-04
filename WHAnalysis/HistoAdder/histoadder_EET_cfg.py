import FWCore.ParameterSet.Config as cms

process = cms.Process("EET")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")

process.demo = cms.EDAnalyzer('HistoAdder',

	process = cms.untracked.string("EET"),

	nostack = cms.untracked.bool(False),

        path = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/HistoAdderFirstStep/EET/"),

        samples = cms.untracked.vstring("WH_120.root",
                                        "TTH_120.root",
                                        "ZH_120.root",
				        "DiBosons.root",
                                        "EWK.root",
                                        "DY.root",
                                        "QCD.root",
				       ),

	data = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/histo_data.root"),
        #data = cms.untracked.string(""),

        labels = cms.untracked.vstring("WH_120",
                                       "TTH_120",
				       "ZH_120",
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

	legendLabels = cms.untracked.vstring("WH 120 Gev/c^{2} (x5)",
                                             "t#bar{t}H 120 Gev/c^{2} (x5)",
				             "ZH 120 Gev/c^{2} (x5)",
					     "DiBoson",
                                             "EWK",
				             "Drell-Yan",
				             "QCD",
					    ),

        legendDim = cms.untracked.vdouble(0.75, 0.60, 0.9, 0.9),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./Outputs/EET/outputTOT_EET.txt")

)

process.p = cms.Path(process.demo)
