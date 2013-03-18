import FWCore.ParameterSet.Config as cms

process = cms.Process("ETT")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")

process.demo = cms.EDAnalyzer('HistoAdder',

	process = cms.untracked.string("ETT"),

	nostack = cms.untracked.bool(False),

        path = cms.untracked.string("/cmshome/calabria/Code_53X_TauIdDec2012_OnlyAnalysis/CMSSW_5_3_7_patch4/src/WHAnalysis/HistoAdderFirstStep/ETT/"),

        samples = cms.untracked.vstring("DiBosons.root",
                                        "EWK.root",
					"WJets.root",
                                        "DY.root",
                                        #"QCD.root",
					"WH_125.root",
				        "TTH_125.root",
                                        "ZH_125.root",
				       ),

	data = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_53X/ETT/histo_data.root"),
        #data = cms.untracked.string(""),

        labels = cms.untracked.vstring("DiBosons",
                                       "EWK",
				       "WJets",
				       "DY",
				       #"QCD",
				       "WH_125",
                                       "TTH_125",
				       "ZH_125",
				      ),

        logScale = cms.untracked.bool(False),

        setColors = cms.untracked.vdouble(50.,
                                          6.,
					  7,
                                          5.,
					  #38.,
					  2.,
					  8.,
                                          4.,
					 ),

	legendLabels = cms.untracked.vstring("DiBoson",
                                             "t#bar{t}",
					     "WJets",
				             "Drell-Yan",
				             #"QCD",
				  	     #"WH 120 (x5)",
                                             #"t#bar{t}H 120 (x5)",
				             #"ZH 120 (x5)",
				  	     "WH 125",
                                             "t#bar{t}H 125",
				             "ZH 125",
					    ),

        legendDim = cms.untracked.vdouble(0.75, 0.60, 0.9, 0.9),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./Outputs/ETT/outputTOT_ETT.txt"),

        energy = cms.untracked.string("8 TeV"),

        lumi = cms.untracked.string("19.5 fb^{-1}")

)

process.p = cms.Path(process.demo)
