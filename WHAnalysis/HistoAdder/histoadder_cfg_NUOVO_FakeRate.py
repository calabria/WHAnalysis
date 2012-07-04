import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")

process.demo = cms.EDAnalyzer('HistoAdder',

	nostack = cms.untracked.bool(False),

        path = cms.untracked.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/HistoAdderFirstStep/EET/"),

        samples = cms.untracked.vstring("WH_120.root",
                                        "TTH_120.root",
                                        "ZH_120.root",
				        "DiBosons.root",
                                        "histo_data_BackEst_ISO03.root",
                                        #"histo_data_JetToE.root",
                                        "QCD.root",
				       ),

	data = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EET/histo_data.root"),
        #data = cms.untracked.string(""),

        labels = cms.untracked.vstring("WH_115",
                                       "TTH_115",
				       "ZH_115)",
				       "DiBosons",
                                       "BackEst",
				       #"JetToE",
				             "QCD",
				      ),

        logScale = cms.untracked.bool(False),

        setColors = cms.untracked.vdouble(2.,
					  8.,
                                          4.,
					  50.,
                                          6.,
                                          #5.,
					  #38.,
					 ),

	legendLabels = cms.untracked.vstring("WH 120  (x5)",
                                             "t#bar{t}H 120  (x5)",
				             "ZH 120  (x5)",
					     "DiBoson",
                                             "BackEst",
				             #"JetToE",
				             #"JetToMu",
					    ),

        legendDim = cms.untracked.vdouble(0.75, 0.60, 0.9, 0.9),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("outputTOT_BackEstData03.txt")

)

process.p = cms.Path(process.demo)
