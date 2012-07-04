import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")

process.WH_110 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.070), #WH_110

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("WH_110.root"),

        samples = cms.untracked.vstring("histo_WH_110.root"),

        labels = cms.untracked.vstring("WH_110"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_WH_110.txt")

)

process.TTH_110 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.010), #TTH_110

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("TTH_110.root"),

        samples = cms.untracked.vstring("histo_TTH_110.root"),

        labels = cms.untracked.vstring("TTH_110"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_TTH_110.txt")

)

process.ZH_110 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.038), #ZH_110

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("ZH_110.root"),

        samples = cms.untracked.vstring("histo_ZH_110.root"),

        labels = cms.untracked.vstring("ZH_110"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_ZH_110.txt")

)

process.WH_115 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.058*5), #WH_115

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("WH_115.root"),

        samples = cms.untracked.vstring("histo_WH_115.root"),

        labels = cms.untracked.vstring("WH_115"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_WH_115.txt")

)

process.TTH_115 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.008*5), #TTH_115

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("TTH_115.root"),

        samples = cms.untracked.vstring("histo_TTH_115.root"),

        labels = cms.untracked.vstring("TTH_115"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_TTH_115.txt")

)

process.ZH_115 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.031*5), #ZH_115

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("ZH_115.root"),

        samples = cms.untracked.vstring("histo_ZH_115.root"),

        labels = cms.untracked.vstring("ZH_115"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_ZH_115.txt")

)

process.WH_120 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.047), #WH_120

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("WH_120.root"),

        samples = cms.untracked.vstring("histo_WH_120.root"),

        labels = cms.untracked.vstring("WH_120"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_WH_120.txt")

)

process.TTH_120 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.007), #TTH_120

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("TTH_120.root"),

        samples = cms.untracked.vstring("histo_TTH_120.root"),

        labels = cms.untracked.vstring("TTH_120"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_TTH_120.txt")

)

process.ZH_120 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.026), #ZH_120

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("ZH_120.root"),

        samples = cms.untracked.vstring("histo_ZH_120.root"),

        labels = cms.untracked.vstring("ZH_120"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_ZH_120.txt")

)

process.WH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.036), #WH_125

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("WH_125.root"),

        samples = cms.untracked.vstring("histo_WH_125.root"),

        labels = cms.untracked.vstring("WH_125"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_WH_125.txt")

)

process.TTH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.005), #TTH_125

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("TTH_125.root"),

        samples = cms.untracked.vstring("histo_TTH_125.root"),

        labels = cms.untracked.vstring("TTH_125"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_TTH_125.txt")

)

process.ZH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.020), #ZH_125

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("ZH_125.root"),

        samples = cms.untracked.vstring("histo_ZH_125.root"),

        labels = cms.untracked.vstring("ZH_125"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_ZH_125.txt")

)

process.WH_130 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.027), #WH_130

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("WH_130.root"),

        samples = cms.untracked.vstring("histo_WH_130.root"),

        labels = cms.untracked.vstring("WH_130"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_WH_130.txt")

)

process.TTH_130 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.004), #TTH_130

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("TTH_130.root"),

        samples = cms.untracked.vstring("histo_TTH_130.root"),

        labels = cms.untracked.vstring("TTH_130"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_TTH_130.txt")

)

process.ZH_130 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.015), #ZH_130

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("ZH_130.root"),

        samples = cms.untracked.vstring("histo_ZH_130.root"),

        labels = cms.untracked.vstring("ZH_130"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_ZH_130.txt")

)

process.WH_135 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.020), #WH_135

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("WH_135.root"),

        samples = cms.untracked.vstring("histo_WH_135.root"),

        labels = cms.untracked.vstring("WH_135"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_WH_135.txt")

)

process.TTH_135 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.003), #TTH_135

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("TTH_135.root"),

        samples = cms.untracked.vstring("histo_TTH_135.root"),

        labels = cms.untracked.vstring("TTH_135"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_TTH_135.txt")

)

process.ZH_135 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.011), #ZH_135

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("ZH_135.root"),

        samples = cms.untracked.vstring("histo_ZH_135.root"),

        labels = cms.untracked.vstring("ZH_135"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_ZH_135.txt")

)

process.DiBosons = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(5.9,  #ZZ
                                              18.2, #WZ
                                              43.), #WW

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("DiBosons.root"),

        samples = cms.untracked.vstring("histo_ZZ.root",
                                        "histo_WZ.root",
                                        "histo_WW.root"),

        labels = cms.untracked.vstring("ZZ",
                                       "WZ",
				       "WW"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_DiBosons.txt")

)

process.DY = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(1666.,
                                              1666.,
                                              1666.,),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("DY.root"),

        samples = cms.untracked.vstring("histo_DYToEE.root",
                                        "histo_DYToMuMu.root",
                                        "histo_DYToTauTau.root",),

        labels = cms.untracked.vstring("DYToEE",
                                       "DYToMuMu",
                                       "DYToTauTau",),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_DY.txt")

)

process.QCD = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(9431.,      #QCD_80_170_BC
                                              84679.3,    #QCD_pt20
                                              139300.,    #QCD_20_BC
                                              139500.,    #QCD_Pt-80to170  139500
                                              143844.,    #QCD_30_80_BC
                                              2496000.,   #qcd20_30 2496000
                                              3867500.,), #qcd30_80 3867500

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("QCD.root"),

        samples = cms.untracked.vstring("histo_QCD80_170_BCtoE.root",
                                        "histo_QCD_20_MU.root",
                                        "histo_QCD20_30_BCtoE.root",
                                        "histo_QCD80_170_EM.root",
                                        "histo_QCD30_80_BCtoE.root",
                                        "histo_QCD20_30_EM.root",
                                        "histo_QCD30_80_EM.root"),

        labels = cms.untracked.vstring("QCD_80-170_BCToE",
                                       "QCD_Mu_20",
                                       "QCD_20-30_BCToE",
				       "QCD_80-170_EM",
                                       "QCD_30-80_BCToE",
                                       "QCD_20-30_EM",
                                       "QCD_30-80_EM"),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_QCD.txt")

)

process.EWK = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(56.64,       #GV
                                              165.,        #TT
					      31314.,      #WJets
                                              #84200000.,   #G_Pt-0to15
                                              #172000.,     #G_Pt-15to30
                                              #16700.,      #G_Pt-30to50
                                              #2720.,       #G_Pt-50to80
                                              #447.,        #G_Pt-80to120
                                              #84.2,	   #G_Pt-120to170
                                              #22.6,	   #G_Pt-170to300
                                              #1.49,	   #G_Pt-300to470
					      #0.132,	   #G_Pt-470to800
                                              #0.00348,	   #G_Pt-800to1400
                                              #0.0000127,   #G_Pt-1400to1800
                                              #0.000000294  #G_Pt-1800
					     ),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi/"),

        outputFile = cms.untracked.string("EWK.root"),

        samples = cms.untracked.vstring("histo_GVJets.root",
                                        "histo_TTJets.root",
					"histo_WJets.root",
                                        #"histo_G_Pt-0to15.root",
                                        #"histo_G_Pt-15to30.root",
                                        #"histo_G_Pt-30to50.root",
                                        #"histo_G_Pt-50to80.root",
                                        #"histo_G_Pt-80to120.root",
                                        #"histo_G_Pt-120to170.root",
                                        #"histo_G_Pt-170to300.root",
                                        #"histo_G_Pt-300to470.root",
                                        #"histo_G_Pt-470to800.root",
                                        #"histo_G_Pt-800to1400.root",
					#"histo_G_Pt-1400to1800.root",
                                        #"histo_G_Pt-1800.root"
					),

        labels = cms.untracked.vstring("gammaV+jets",
                                       "ttbar+jets",
				       "W+jets",
                                       #"G_Pt-0to15",
                                       #"G_Pt-15to30",
                                       #"G_Pt-30to50",
                                       #"G_Pt-50to80",
                                       #"G_Pt-80to120",
                                       #"G_Pt-120to170",
                                       #"G_Pt-170to300",
                                       #"G_Pt-300to470",
                                       #"G_Pt-470to800",
                                       #"G_Pt-800to1400",
				       #"G_Pt-1400to1800",
                                       #"G_Pt-1800"
				       ),

        intLumi = cms.untracked.double(4636.33),

        eventsIn = cms.untracked.string("TriggerHistosBeforeSel/N_eventi_PU"),

        txtFile = cms.untracked.string("output_EWK.txt")

)

process.p = cms.Path(process.DiBosons +
		     process.DY +
		     process.QCD + 
		     process.EWK + 
		     process.WH_110 + process.WH_115 + process.WH_120 + process.WH_125 + process.WH_130 + process.WH_135 +
		     process.TTH_110 + process.TTH_115 + process.TTH_120 + process.TTH_125 + process.TTH_130 + process.TTH_135 +
		     process.ZH_110 + process.ZH_115 + process.ZH_120 + process.ZH_125 + process.ZH_130 + process.ZH_135
		     )
