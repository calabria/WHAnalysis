import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")

process.WH_110 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.070), #WH_110

	skimEff = cms.untracked.vdouble(0.00405),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/WH_110.root"),

        samples = cms.untracked.vstring("histo_WH_110.root"),

        labels = cms.untracked.vstring("WH_110"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_WH_110.txt")

)

process.TTH_110 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.010), #TTH_110

	skimEff = cms.untracked.vdouble(0.00405),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/TTH_110.root"),

        samples = cms.untracked.vstring("histo_TTH_110.root"),

        labels = cms.untracked.vstring("TTH_110"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_TTH_110.txt")

)

process.ZH_110 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.038), #ZH_110

	skimEff = cms.untracked.vdouble(0.00405),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/ZH_110.root"),

        samples = cms.untracked.vstring("histo_ZH_110.root"),

        labels = cms.untracked.vstring("ZH_110"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_ZH_110.txt")

)

process.WH_115 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.058*5), #WH_115

	skimEff = cms.untracked.vdouble(0.00731),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/WH_115.root"),

        samples = cms.untracked.vstring("histo_WH_115.root"),

        labels = cms.untracked.vstring("WH_115"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_WH_115.txt")

)

process.TTH_115 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.008*5), #TTH_115

	skimEff = cms.untracked.vdouble(0.00731),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/TTH_115.root"),

        samples = cms.untracked.vstring("histo_TTH_115.root"),

        labels = cms.untracked.vstring("TTH_115"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_TTH_115.txt")

)

process.ZH_115 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.031*5), #ZH_115

	skimEff = cms.untracked.vdouble(0.00731),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/ZH_115.root"),

        samples = cms.untracked.vstring("histo_ZH_115.root"),

        labels = cms.untracked.vstring("ZH_115"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_ZH_115.txt")

)

process.WH_120 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.047), #WH_120

	skimEff = cms.untracked.vdouble(0.00164),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/WH_120.root"),

        samples = cms.untracked.vstring("histo_WH_120.root"),

        labels = cms.untracked.vstring("WH_120"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_WH_120.txt")

)

process.TTH_120 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.007), #TTH_120

	skimEff = cms.untracked.vdouble(0.00164),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/TTH_120.root"),

        samples = cms.untracked.vstring("histo_TTH_120.root"),

        labels = cms.untracked.vstring("TTH_120"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_TTH_120.txt")

)

process.ZH_120 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.026), #ZH_120

	skimEff = cms.untracked.vdouble(0.00164),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/ZH_120.root"),

        samples = cms.untracked.vstring("histo_ZH_120.root"),

        labels = cms.untracked.vstring("ZH_120"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_ZH_120.txt")

)

process.WH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.036), #WH_125

	skimEff = cms.untracked.vdouble(0.00453),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/WH_125.root"),

        samples = cms.untracked.vstring("histo_WH_125.root"),

        labels = cms.untracked.vstring("WH_125"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_WH_125.txt")

)

process.TTH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.005), #TTH_125

	skimEff = cms.untracked.vdouble(0.00453),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/TTH_125.root"),

        samples = cms.untracked.vstring("histo_TTH_125.root"),

        labels = cms.untracked.vstring("TTH_125"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_TTH_125.txt")

)

process.ZH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.020), #ZH_125

	skimEff = cms.untracked.vdouble(0.00453),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/ZH_125.root"),

        samples = cms.untracked.vstring("histo_ZH_125.root"),

        labels = cms.untracked.vstring("ZH_125"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_ZH_125.txt")

)

process.WH_130 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.027), #WH_130

	skimEff = cms.untracked.vdouble(0.00245),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/WH_130.root"),

        samples = cms.untracked.vstring("histo_WH_130.root"),

        labels = cms.untracked.vstring("WH_130"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_WH_130.txt")

)

process.TTH_130 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.004), #TTH_130

	skimEff = cms.untracked.vdouble(0.00245),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/TTH_130.root"),

        samples = cms.untracked.vstring("histo_TTH_130.root"),

        labels = cms.untracked.vstring("TTH_130"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_TTH_130.txt")

)

process.ZH_130 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.015), #ZH_130

	skimEff = cms.untracked.vdouble(0.00245),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/ZH_130.root"),

        samples = cms.untracked.vstring("histo_ZH_130.root"),

        labels = cms.untracked.vstring("ZH_130"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_ZH_130.txt")

)

process.WH_135 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.020), #WH_135

	skimEff = cms.untracked.vdouble(0.00634),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/WH_135.root"),

        samples = cms.untracked.vstring("histo_WH_135.root"),

        labels = cms.untracked.vstring("WH_135"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_WH_135.txt")

)

process.TTH_135 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.003), #TTH_135

	skimEff = cms.untracked.vdouble(0.00634),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/TTH_135.root"),

        samples = cms.untracked.vstring("histo_TTH_135.root"),

        labels = cms.untracked.vstring("TTH_135"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_TTH_135.txt")

)

process.ZH_135 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.011), #ZH_135

	skimEff = cms.untracked.vdouble(0.00634),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/ZH_135.root"),

        samples = cms.untracked.vstring("histo_ZH_135.root"),

        labels = cms.untracked.vstring("ZH_135"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_ZH_135.txt")

)

process.DiBosons = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(5.9,  #ZZ
                                              18.2, #WZ
                                              43.), #WW

	skimEff = cms.untracked.vdouble(0.01805,
					0.01067,
					0.02521),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/DiBosons.root"),

        samples = cms.untracked.vstring("histo_ZZ.root",
                                        "histo_WZ.root",
                                        "histo_WW.root"),

        labels = cms.untracked.vstring("ZZ",
                                       "WZ",
				       "WW"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_DiBosons.txt")

)

process.DY = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(3048.),

	skimEff = cms.untracked.vdouble(0.02446),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/DY.root"),

        samples = cms.untracked.vstring("histo_DYJetsToLL.root"),

        labels = cms.untracked.vstring("DYJetsToLL"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_DY.txt")

)

process.QCD = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(84679,      #QCD_MU_20
					      139300.,    #QCD20_30_BCToE
                                              2496000.,   #QCD20_30_EM 2496000
                                              143844.,    #QCD30_80_BCToE
                                              3867500.,   #QCD30_80_EM 3867500
					      9431.,      #QCD80_170_BCToE            
                                              139500.),   #QCD80_170_EM  139500

	skimEff = cms.untracked.vdouble(0.12972,
					0.01745,
					0.00354,
					0.03665,
					0.00729,
					0.08963,
					0.02333),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/QCD.root"),

        samples = cms.untracked.vstring("histo_QCD_20_MU.root",
					"histo_QCD20_30_BCtoE.root",
                                        "histo_QCD20_30_EM.root",
                                        "histo_QCD30_80_BCtoE.root",
                                        "histo_QCD30_80_EM.root",
					"histo_QCD80_170_BCtoE.root",
                                        "histo_QCD80_170_EM.root"),

        labels = cms.untracked.vstring("QCD_20_MU",
				       "QCD20_30_BCToE",
                                       "QCD20_30_EM",
                                       "QCD30_80_BCToE",
                                       "QCD30_80_EM",
				       "QCD80_170_BCToE",
				       "QCD80_170_EM"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_QCD.txt")

)

process.EWK = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(56.64,        #GV
                                              165.,         #TT
					      31314.),      #WJets

	skimEff = cms.untracked.vdouble(0.05182,
				        0.00860,
				        0.01516),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/EMT/"),

        outputFile = cms.untracked.string("./EMT/EWK.root"),

        samples = cms.untracked.vstring("histo_GVJets.root",
                                        "histo_TTJets.root",
					"histo_WJets.root"),

        labels = cms.untracked.vstring("gammaV+jets",
                                       "ttbar+jets",
				       "W+jets"),

        intLumi = cms.untracked.double(4664.693),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("./EMT/output_EWK.txt")

)

process.p = cms.Path(process.DiBosons +
		     process.DY +
		     process.QCD + 
		     process.EWK + 
		     process.WH_110 + process.WH_115 + process.WH_120 + process.WH_125 + process.WH_130 + process.WH_135 +
		     process.TTH_110 + process.TTH_115 + process.TTH_120 + process.TTH_125 + process.TTH_130 + process.TTH_135 +
		     process.ZH_110 + process.ZH_115 + process.ZH_120 + process.ZH_125 + process.ZH_130 + process.ZH_135
		     )
