import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")

skimWH110      = 0.35944
skimWH115      = 0.36706
skimWH120      = 0.40791
skimWH125      = 0.38837
skimWH130      = 0.39777
skimWH135      = 0.40158
skimDYJetsToLL = 0.23286
skimDYToEE     = 0.28072
skimDYToTauTau = 0.05649
skimWJets      = 0.06624
skimTTJets     = 0.46048
skimWW         = 0.19815
skimWZ         = 0.16757
skimZZ         = 0.15492
skimGVJets     = 0.21369

process.WH_110 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.070), #WH_110

	skimEff = cms.untracked.vdouble(skimWH110),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/WH_110.root"),

        samples = cms.untracked.vstring("histo_WH_110.root"),

        labels = cms.untracked.vstring("WH_110"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_WH_110.txt")

)

process.TTH_110 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.010), #TTH_110

	skimEff = cms.untracked.vdouble(skimWH110),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/TTH_110.root"),

        samples = cms.untracked.vstring("histo_TTH_110.root"),

        labels = cms.untracked.vstring("TTH_110"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_TTH_110.txt")

)

process.ZH_110 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.038), #ZH_110

	skimEff = cms.untracked.vdouble(skimWH110),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/ZH_110.root"),

        samples = cms.untracked.vstring("histo_ZH_110.root"),

        labels = cms.untracked.vstring("ZH_110"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_ZH_110.txt")

)

process.WH_115 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.058*5), #WH_115

	skimEff = cms.untracked.vdouble(skimWH115),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/WH_115.root"),

        samples = cms.untracked.vstring("histo_WH_115.root"),

        labels = cms.untracked.vstring("WH_115"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_WH_115.txt")

)

process.TTH_115 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.008*5), #TTH_115

	skimEff = cms.untracked.vdouble(skimWH115),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/TTH_115.root"),

        samples = cms.untracked.vstring("histo_TTH_115.root"),

        labels = cms.untracked.vstring("TTH_115"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_TTH_115.txt")

)

process.ZH_115 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.031*5), #ZH_115

	skimEff = cms.untracked.vdouble(skimWH115),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/ZH_115.root"),

        samples = cms.untracked.vstring("histo_ZH_115.root"),

        labels = cms.untracked.vstring("ZH_115"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_ZH_115.txt")

)

process.WH_120 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.047), #WH_120

	skimEff = cms.untracked.vdouble(skimWH120),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/WH_120.root"),

        samples = cms.untracked.vstring("histo_WH_120.root"),

        labels = cms.untracked.vstring("WH_120"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_WH_120.txt")

)

process.TTH_120 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.007), #TTH_120

	skimEff = cms.untracked.vdouble(skimWH120),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/TTH_120.root"),

        samples = cms.untracked.vstring("histo_TTH_120.root"),

        labels = cms.untracked.vstring("TTH_120"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_TTH_120.txt")

)

process.ZH_120 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.026), #ZH_120

	skimEff = cms.untracked.vdouble(skimWH120),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/ZH_120.root"),

        samples = cms.untracked.vstring("histo_ZH_120.root"),

        labels = cms.untracked.vstring("ZH_120"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_ZH_120.txt")

)

process.WH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.5729*0.0637), #WH_125

	skimEff = cms.untracked.vdouble(skimWH125),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/WH_125.root"),

        samples = cms.untracked.vstring("histo_WH_125.root"),

        labels = cms.untracked.vstring("WH_125"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_WH_125.txt")

)

process.TTH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.08634*0.0637), #TTH_125

	skimEff = cms.untracked.vdouble(skimWH125),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/TTH_125.root"),

        samples = cms.untracked.vstring("histo_TTH_125.root"),

        labels = cms.untracked.vstring("TTH_125"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_TTH_125.txt")

)

process.ZH_125 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.3158*0.0637), #ZH_125

	skimEff = cms.untracked.vdouble(skimWH125),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/ZH_125.root"),

        samples = cms.untracked.vstring("histo_ZH_125.root"),

        labels = cms.untracked.vstring("ZH_125"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_ZH_125.txt")

)

process.WH_130 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.027), #WH_130

	skimEff = cms.untracked.vdouble(skimWH130),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/WH_130.root"),

        samples = cms.untracked.vstring("histo_WH_130.root"),

        labels = cms.untracked.vstring("WH_130"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_WH_130.txt")

)

process.TTH_130 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.004), #TTH_130

	skimEff = cms.untracked.vdouble(skimWH130),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/TTH_130.root"),

        samples = cms.untracked.vstring("histo_TTH_130.root"),

        labels = cms.untracked.vstring("TTH_130"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_TTH_130.txt")

)

process.ZH_130 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.015), #ZH_130

	skimEff = cms.untracked.vdouble(skimWH130),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/ZH_130.root"),

        samples = cms.untracked.vstring("histo_ZH_130.root"),

        labels = cms.untracked.vstring("ZH_130"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_ZH_130.txt")

)

process.WH_135 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.020), #WH_135

	skimEff = cms.untracked.vdouble(skimWH135),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/WH_135.root"),

        samples = cms.untracked.vstring("histo_WH_135.root"),

        labels = cms.untracked.vstring("WH_135"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_WH_135.txt")

)

process.TTH_135 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.003), #TTH_135

	skimEff = cms.untracked.vdouble(skimWH135),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/TTH_135.root"),

        samples = cms.untracked.vstring("histo_TTH_135.root"),

        labels = cms.untracked.vstring("TTH_135"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_TTH_135.txt")

)

process.ZH_135 = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(0.011), #ZH_135

	skimEff = cms.untracked.vdouble(skimWH135),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/ZH_135.root"),

        samples = cms.untracked.vstring("histo_ZH_135.root"),

        labels = cms.untracked.vstring("ZH_135"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_ZH_135.txt")

)

process.DiBosons = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(5.9,  #ZZ
                                              18.2, #WZ
                                              43.), #WW

	skimEff = cms.untracked.vdouble(skimZZ,
					skimWZ,
					skimWW),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/DiBosons.root"),

        samples = cms.untracked.vstring("histo_ZZ.root",
                                        "histo_WZ.root",
                                        "histo_WW.root"),

        labels = cms.untracked.vstring("ZZ",
                                       "WZ",
				       "WW"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_DiBosons.txt")

)

process.DiBosonsNoWW = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(5.9,  #ZZ
                                              18.2), #WZ

	skimEff = cms.untracked.vdouble(skimZZ,
					skimWZ),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/DiBosonsNoWW.root"),

        samples = cms.untracked.vstring("histo_ZZ.root",
                                        "histo_WZ.root"),

        labels = cms.untracked.vstring("ZZ",
                                       "WZ"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_DiBosonsNoWW.txt")

)

process.DY = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(3048.),

	skimEff = cms.untracked.vdouble(skimDYJetsToLL),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/DY.root"),

        samples = cms.untracked.vstring("histo_DYJetsToLL.root"),

        labels = cms.untracked.vstring("DYJetsToLL"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_DY.txt")

)

process.DYToEE = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(1666.),

	skimEff = cms.untracked.vdouble(skimDYToEE),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/DYToEE.root"),

        samples = cms.untracked.vstring("histo_DYToEE.root"),

        labels = cms.untracked.vstring("DYToEE"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_DYToEE.txt")

)

process.DYToTauTau = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(1666.),

	skimEff = cms.untracked.vdouble(skimDYToTauTau),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/DYToTauTau.root"),

        samples = cms.untracked.vstring("histo_DYToTauTau.root"),

        labels = cms.untracked.vstring("DYToTauTau"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_DYToTauTau.txt")

)

process.QCD = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(139300.,    #QCD20_30_BCToE
                                              2496000.,   #QCD20_30_EM 2496000
                                              143844.,    #QCD30_80_BCToE
                                              3867500.,   #QCD30_80_EM 3867500
					      9431.,      #QCD80_170_BCToE            
                                              139500.),   #QCD80_170_EM  139500

	skimEff = cms.untracked.vdouble(0.67069,
					0.18178,
					0.73384,
					0.23997,
					0.70311,
					0.29857),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/QCD.root"),

        samples = cms.untracked.vstring("histo_QCD20_30_BCtoE.root",
                                        "histo_QCD20_30_EM.root",
                                        "histo_QCD30_80_BCtoE.root",
                                        "histo_QCD30_80_EM.root",
					"histo_QCD80_170_BCtoE.root",
                                        "histo_QCD80_170_EM.root"),

        labels = cms.untracked.vstring("QCD20_30_BCToE",
                                       "QCD20_30_EM",
                                       "QCD30_80_BCToE",
                                       "QCD30_80_EM",
				       "QCD80_170_BCToE",
				       "QCD80_170_EM"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_QCD.txt")

)

process.EWK = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(56.64,        #GV
                                              165.,         #TT
					      #31314.
					     ),      #WJets

	skimEff = cms.untracked.vdouble(skimGVJets,
				        skimTTJets
				        #0.22428
				       ),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/EWK.root"),

        samples = cms.untracked.vstring("histo_GVJets.root",
                                        "histo_TTJets.root",
					#"histo_WJets.root"
				       ),

        labels = cms.untracked.vstring("gammaV+jets",
                                       "ttbar+jets",
				       #"W+jets"
				      ),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_EWK.txt")

)

process.WJets = cms.EDAnalyzer('HistoAdderFirstStep',

        crossSections = cms.untracked.vdouble(31314.),      #WJets

	skimEff = cms.untracked.vdouble(skimWJets),

        path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/"),

        outputFile = cms.untracked.string("./ETT/WJets.root"),

        samples = cms.untracked.vstring("histo_WJets.root"),

        labels = cms.untracked.vstring("W+jets"),

        intLumi = cms.untracked.double(5000.),

        eventsIn = cms.untracked.string("VertexHistosBeforeMCFilter2/N_eventi_PU"),

        txtFile = cms.untracked.string("./ETT/output_WJets.txt")

)

process.p = cms.Path(process.DiBosons + 
		     process.DiBosonsNoWW +
		     process.DY + process.DYToEE + process.DYToTauTau +
		     process.QCD + 
		     process.EWK + 
		     process.WJets +
		     process.WH_110 + process.WH_115 + process.WH_120 + process.WH_125 + process.WH_130 + process.WH_135 +
		     process.TTH_110 + process.TTH_115 + process.TTH_120 + process.TTH_125 + process.TTH_130 + process.TTH_135 +
		     process.ZH_110 + process.ZH_115 + process.ZH_120 + process.ZH_125 + process.ZH_130 + process.ZH_135
		     )
