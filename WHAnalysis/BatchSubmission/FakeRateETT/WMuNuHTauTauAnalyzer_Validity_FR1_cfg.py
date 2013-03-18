import FWCore.ParameterSet.Config as cms

process = cms.Process("WMuNuHTauTauAnalyzer")

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string("GR_P_V42_AN3::All")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

		#__inputFile

        ),

)
process.source.skipBadFiles = cms.untracked.bool( True )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#################################################################################################################################

process.load("WHAnalysis.Configuration.ProduceMTAndTriggerMatching_cff")
process.load("WHAnalysis.Configuration.GenFilter_cff")
process.load("WHAnalysis.Configuration.VertexSelector_cff")
process.load("WHAnalysis.Configuration.TriggerSelector_cff")
process.load("WHAnalysis.Configuration.ElectronSelector_ett_cff")
process.load("WHAnalysis.Configuration.MuonSelector_ett_cff")
process.load("WHAnalysis.Configuration.TauSelector_ett_cff")
process.load("WHAnalysis.Configuration.CompositeCandidateCreator_ett_cff")
process.load("WHAnalysis.Configuration.JetSelector_cff")
process.load("WHAnalysis.Configuration.METSelector_cff")
process.load("WHAnalysis.Configuration.TauTauPairSelector_ett_cff")
process.load("WHAnalysis.Configuration.skimming_ett_cff")

process.hltSelection.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.hltSelection.HLTPaths = cms.vstring("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v",
					    "HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v")
process.hltSelection.hltEventRanges = cms.VEventRange("190456:MIN-193680:MAX",
						      "193752:MIN-208357:MAX")
#process.hltSelection.defaultTrigger = cms.string("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v")
process.hltSelection.defaultTrigger = cms.string("")

process.TriggerHistosBeforeSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosBeforeSel.hltPaths = cms.vstring('HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v')

process.TriggerHistosAfterSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosAfterSel.hltPaths = cms.vstring('HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v')

#################################################################################################################################
#PU Correction for MC samples only
isMCBool = cms.bool(False)

process.MuonHistosBeforeMuonPt.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonVeto.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeTauTauPairs.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

process.VertexHistosBeforeMCFilter.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosBeforeMCFilter2.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosBeforeSel.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosAfterSel.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosForPU.isMC = cms.untracked.bool(isMCBool.value())

process.TriggerHistosBeforeSel.isMC = cms.untracked.bool(isMCBool.value())
process.TriggerHistosAfterSel.isMC = cms.untracked.bool(isMCBool.value())

process.TauHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauEta.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauID.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauIso.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeMuonVeto.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeEleVeto.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauPt1.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosAfterTau1Sequence.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosFinal1.isMC = cms.untracked.bool(isMCBool.value())

#process.TauHistosBeforeDeltaR2.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauEta2.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauID2.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauIso2.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeMuonVeto2.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeEleVeto2.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauPt2.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosAfterTau2Sequence.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosFinal2.isMC = cms.untracked.bool(isMCBool.value())

process.JetHistosBeforeJetEt.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosBeforeJetEta.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosBeforeJetBTag.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosAfterJetBTag.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosAfterNumJet.isMC = cms.untracked.bool(isMCBool.value())

process.EleHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeElePt.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleEta.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleCrack.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleID.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosAfterPreEleID.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosAfterEleID.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleTrk.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeOneEle.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeTauTauPairs.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

process.DiTauHistosBeforeMET.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeCharge.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeOnePair.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosFinalForTauTau.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosFinal.isMC = cms.untracked.bool(isMCBool.value())
process.eePairsVeto.isMC = cms.untracked.bool(isMCBool.value())
process.eePairsVetoNoCut.isMC = cms.untracked.bool(isMCBool.value())
process.eePairsVetoAfterSel.isMC = cms.untracked.bool(isMCBool.value())

process.CompCandHistosBeforeSel.isMC = cms.untracked.bool(isMCBool.value())
process.CompCandHistosBeforeZttVeto.isMC = cms.untracked.bool(isMCBool.value())
process.CompCandHistosAfterSel.isMC = cms.untracked.bool(isMCBool.value())
process.CompCandHistosBeforeMet.isMC = cms.untracked.bool(isMCBool.value())
process.CompCandHistosAfterSelLt.isMC = cms.untracked.bool(isMCBool.value())
process.CompCandHistosBeforeZeeStep2.isMC = cms.untracked.bool(isMCBool.value())
process.CompCandHistosAfterZeeStep2.isMC = cms.untracked.bool(isMCBool.value())
process.CompCandHistosBeforeZeeStep4.isMC = cms.untracked.bool(isMCBool.value())

#################################################################################################################################

process.out = cms.OutputModule("PoolOutputModule",
                fileName = cms.untracked.string("test.root"),
		outputCommands = cms.untracked.vstring(
		'keep *',
      		#"keep *_*_*_EleTauAnalyzer"
		)
        )

#################################################################################################################################

process.selectedTausPt1.cut = cms.string('pt > 25.0')
process.selectedTausPt2.cut = cms.string('pt > 20.0')

process.selectedTausIso.cut = cms.string('tauID("byTightCombinedIsolationDeltaBetaCorr") < 0.5')
process.selectedTausIso2.cut = cms.string('tauID("byLooseCombinedIsolationDeltaBetaCorr") > 0.5 && (triggerObjectMatchesByPath("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*").size() > 0.5 || triggerObjectMatchesByPath("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*").size() > 0.5)')

process.selectedCompCandCharge = cms.EDFilter("CompCandChargeFilter",
	CompCandSrc = cms.untracked.InputTag("ztautauVeto"),
	applyCharge1 = cms.untracked.bool(True), #is SS with e??
	applyCharge2 = cms.untracked.bool(False),
	filter = cms.bool(True)
	)

process.CompCandHistosAfterSelLt1 = cms.EDAnalyzer('CompositeCandHistManager',
       CompCandSrc = cms.untracked.InputTag("selectedCompCandUW"),
       PFMetTag = cms.untracked.InputTag('patPFMetByMVA'),
       MCDist = cms.untracked.vdouble(1),
       TrueDist2011 = cms.untracked.vdouble(1),
       isMC = cms.untracked.bool(False),
       isFR = cms.untracked.int32(1),
)

process.CompCandHistosAfterSelLt2 = cms.EDAnalyzer('CompositeCandHistManager',
       CompCandSrc = cms.untracked.InputTag("selectedCompCandUW"),
       PFMetTag = cms.untracked.InputTag('patPFMetByMVA'),
       MCDist = cms.untracked.vdouble(1),
       TrueDist2011 = cms.untracked.vdouble(1),
       isMC = cms.untracked.bool(False),
       isFR = cms.untracked.int32(2),
)

process.CompCandHistosAfterSelLt3 = cms.EDAnalyzer('CompositeCandHistManager',
       CompCandSrc = cms.untracked.InputTag("selectedCompCandUW"),
       PFMetTag = cms.untracked.InputTag('patPFMetByMVA'),
       MCDist = cms.untracked.vdouble(1),
       TrueDist2011 = cms.untracked.vdouble(1),
       isMC = cms.untracked.bool(False),
       isFR = cms.untracked.int32(3),
)

process.CompCandHistosAfterSel.CompCandSrc = cms.untracked.InputTag("selectedCompCandCharge")
process.selectedCompCandUW.CompCandSrc = cms.untracked.InputTag("selectedCompCandCharge")

############### Signal veto

process.selectedTau1Sign = cms.EDFilter("PATTauSelector",
	src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
	cut = cms.string('tauID("byTightCombinedIsolationDeltaBetaCorr") > 0.5 && tauID("againstMuonTight") > 0.5 && tauID("againstElectronTight") > 0.5'),
	filter = cms.bool(False)
	)

process.selectedTau2Sign = cms.EDFilter("PATTauSelector",
	src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
	cut = cms.string('tauID("byMediumCombinedIsolationDeltaBetaCorr") > 0.5 && tauID("againstMuonTight") > 0.5 && tauID("againstElectronMedium") > 0.5'),
	filter = cms.bool(False)
	)

process.selectedTau1Tau2Sign = cms.EDProducer("CandViewShallowCloneCombiner",
	decay = cms.string("selectedTau1Sign@+ selectedTau2Sign@-"),
	roles = cms.vstring('tau1', 'tau2'),
	cut =  cms.string("deltaR(daughter('tau1').eta,daughter('tau1').phi,daughter('tau2').eta,daughter('tau2').phi) > 0.5"),
	checkCharge = cms.bool(True)
      	)

selLongDist = "(abs(daughter('ele').vz - daughter('tau1tau2').daughter(0).vz) < 0.14 && abs(daughter('ele').vz - daughter('tau1tau2').daughter(1).vz) < 0.14)"

process.selectedEleTau1Tau2CandSign = cms.EDProducer("CandViewShallowCloneCombiner",
	decay = cms.string("selectedElectronsTrk selectedTau1Tau2Sign"),
	roles = cms.vstring('ele', 'tau1tau2'),
	cut = cms.string(selLongDist),
	checkCharge = cms.bool(False)
  	)

process.selectedCompCandNearZSgn = cms.EDFilter("ZEleTauVeto",
	CompCandSrc = cms.untracked.InputTag("selectedEleTau1Tau2CandSign"),
	cut = cms.untracked.double(6),
	filter = cms.bool(False)
	)

process.ztautauVetoSgn = cms.EDFilter('ZTauTauVeto',
	CompCandSrc = cms.untracked.InputTag("selectedCompCandNearZSgn"),
	PFMetTag = cms.untracked.InputTag('patPFMetByMVA'),
	cosCut1 = cms.untracked.double(-0.5),
	mtCut1 = cms.untracked.double(50),
	cosCut2 = cms.untracked.double(-0.5),
	mtCut2 = cms.untracked.double(50),
	filter = cms.bool(False)
	)

process.rejectSgnEvent = cms.EDFilter("PATCandViewCountFilter",
	src = cms.InputTag("ztautauVetoSgn"),
	minNumber = cms.uint32(0),
	maxNumber = cms.uint32(0),
	filter = cms.bool(True)
	)

process.sequenceSgn = cms.Sequence(
	process.selectedTau1Sign *
	process.selectedTau2Sign *
	process.selectedTau1Tau2Sign *
	process.selectedEleTau1Tau2CandSign *
	process.selectedCompCandNearZSgn *
	process.ztautauVetoSgn *
	process.rejectSgnEvent
	)

############### Signal veto

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	#__outpuFile

	)
)

process.mypath = cms.Path(#process.skimmingSequence *
			  #process.producesUserDefinedVarsEle *
			  #process.producesUserDefinedVarsTau *
			  process.VertexHistosBeforeMCFilter *
			  #process.genFilter * #Enable only for Signal
			  process.VertexHistosBeforeMCFilter2 *
			  #process.ettFinalState *
			  process.triggerSequence *
			  process.vertexSequence *
			  process.electronSequence *
			  process.muonSequence *
			  process.tauSequence *
			  process.VertexHistosForPU *
			  process.selectedTau1Tau2 *
			  process.TauTauSequence *
			  process.selectedEleTau1Tau2Cand *
			  process.CompCandHistosBeforeSel *
				  ### Zee 1
				  ((process.selectedEle1Ele2 + process.selectedEle1Ele2NoCut) *
				   (process.eePairsVeto + process.eePairsVetoNoCut) *
				   process.selectedEle1Ele2OnePair *
				   process.eePairsVetoAfterSel) *
				  ### Zee 2
				  process.CompCandHistosBeforeZeeStep2 *
				  process.selectedCompCandNearZ *
				  #process.selectedNoEleTauPair *
				  process.CompCandHistosAfterZeeStep2 *
				  ### Zee 4
				  process.selectedEleTau1Tau2CandZeeStep4 *
				  process.CompCandHistosBeforeZeeStep4 *
				  process.selectedNoEleTauMatch *
				  ### Ztt veto
			 	  process.CompCandHistosBeforeZttVeto *
			  	  process.ztautauVeto *
			  process.selectedCompCandCharge *
			  process.CompCandHistosAfterSel *
			  process.selectedCompCandUW *
			  process.jetSequence *
			  process.CompCandHistosBeforeMet *
			  process.selectedMETMax *
			  process.sequenceSgn *
			  process.CompCandHistosAfterSelLt *
			  process.CompCandHistosAfterSelLt1 *
			  process.CompCandHistosAfterSelLt2 *
			  process.CompCandHistosAfterSelLt3
)

#process.outp1 = cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

