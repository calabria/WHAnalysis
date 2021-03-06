import FWCore.ParameterSet.Config as cms

process = cms.Process("WMuNuHTauTauAnalyzer")

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 5000
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

		#__inputFile

        ),

)

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

process.hltSelection.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
#process.hltSelection.HLTPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v*')
#process.hltSelection.HLTPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v*','HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_v*')
process.hltSelection.HLTPaths = cms.vstring("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v",
					    "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v",
					    "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v",
					    "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v",
					    "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v",
					    "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v",
					    "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TightIsoPFTau20_v",
					    "HLT_Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v",
					    "HLT_Ele20_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v",
					    "HLT_Ele20_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v")
process.hltSelection.hltEventRanges = cms.VEventRange("160404:MIN-161176:MAX",
						      "161216:MIN-163261:MAX",
						      "163269:MIN-163869:MAX",
						      "165088:MIN-165633:MAX",
						      "165970:MIN-166967:MAX",
						      "167039:MIN-167913:MAX",
						      "170249:MIN-173198:MAX",
						      "173236:MIN-178380:MAX",
						      "178420:MIN-179889:MAX",
						      "179959:MIN-180252:MAX")
process.hltSelection.defaultTrigger = cms.string("HLT_Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v1")

process.TriggerHistosBeforeSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosBeforeSel.hltPaths = cms.vstring('HLT_Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v')

process.TriggerHistosAfterSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosAfterSel.hltPaths = cms.vstring('HLT_Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v')

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

process.TauHistosBeforeDeltaR2.isMC = cms.untracked.bool(isMCBool.value())
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

process.CompCandHistosBeforeSel.isMC = cms.untracked.bool(isMCBool.value())
process.CompCandHistosAfterSel.isMC = cms.untracked.bool(isMCBool.value())

#################################################################################################################################

process.out = cms.OutputModule("PoolOutputModule",
                fileName = cms.untracked.string("test.root"),
		outputCommands = cms.untracked.vstring(
		'keep *',
      		#"keep *_*_*_EleTauAnalyzer"
		)
        )

#################################################################################################################################

process.selectedEvents = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events/EventsEMT/"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
	tauSrc = cms.untracked.InputTag("selectedTausHighestPt:TauHighestPt"),
)

process.produceWeightsLep1 = cms.EDProducer('BackEstWeightsProducer',
  	muonSrc = cms.InputTag("muonVariables"),
  	eleSrc = cms.InputTag("producesUserDefinedVarsEle"),
  	tauSrc = cms.InputTag("leadSubLeadTaus:leadingLeptons"),
  	jetSrc = cms.InputTag("patJetsAK5PF"),
        doEleWeight = cms.bool(False),
        doMuonWeight = cms.bool(False),
        doTauWeight = cms.bool(True)
)

process.selectedTausByDeltaR.tauSrc = cms.untracked.InputTag("produceWeightsLep1:patTausWithWeightsTight")
process.TauHistosBeforeDeltaR.tauSrc = cms.untracked.InputTag("produceWeightsLep1:patTausWithWeightsTight")
process.selectedTausIso.cut = cms.string('tauID("byTightCombinedIsolationDeltaBetaCorr") < 0.5')

process.produceWeightsLep2 = cms.EDProducer('BackEstWeightsProducer',
  	muonSrc = cms.InputTag("muonVariables"),
  	eleSrc = cms.InputTag("producesUserDefinedVarsEle"),
  	tauSrc = cms.InputTag("leadSubLeadTaus:subleadingLeptons"),
  	jetSrc = cms.InputTag("patJetsAK5PF"),
        doEleWeight = cms.bool(False),
        doMuonWeight = cms.bool(False),
        doTauWeight = cms.bool(True)
)

process.selectedTausByDeltaR2.tauSrc = cms.untracked.InputTag("produceWeightsLep2:patTausWithWeightsMedium")
process.TauHistosBeforeDeltaR2.tauSrc = cms.untracked.InputTag("produceWeightsLep2:patTausWithWeightsMedium")
process.selectedTausIso2.cut = cms.string('tauID("byMediumCombinedIsolationDeltaBetaCorr") < 0.5')

process.puDistribution = cms.EDAnalyzer('PuDistribution')

process.genFilter.process = cms.untracked.int32(1)


process.TFileService = cms.Service("TFileService", fileName = cms.string(

	#__outpuFile

	)
)

process.mypath = cms.Path(process.producesUserDefinedVarsEle *
			  #process.puDistribution * #Enable only for MC samples
			  process.VertexHistosBeforeMCFilter *
			  #process.genFilter * #Enable only for Signal
			  process.VertexHistosBeforeMCFilter2 *
			  process.triggerSequence *
			  process.vertexSequence *
			  process.electronSequence *
			  process.muonSequence *
			  #TauSequence
			  process.leadSubLeadTaus *
			  #TAU1
			  process.produceWeightsLep1 * #####
			  process.TauHistosBeforeDeltaR *
			  process.selectedTausByDeltaR *
			  process.TauHistosBeforeTauPt1 *
			  process.selectedTausPt1 *
			  process.TauHistosBeforeTauEta *
			  process.selectedTausEta *
			  process.TauHistosBeforeTauID *
			  process.selectedTausID *
			  process.TauHistosBeforeTauIso *
			  process.selectedTausIso *
			  process.TauHistosBeforeMuonVeto *
			  process.selectedTausMuonVeto *
			  process.TauHistosBeforeEleVeto *
			  process.selectedTausEleVeto *
			  process.TauHistosAfterTau1Sequence *
			  #TAU2
			  process.produceWeightsLep2 * #####
			  process.TauHistosBeforeDeltaR2 *
			  process.selectedTausByDeltaR2 *
			  process.TauHistosBeforeTauPt2 *
			  process.selectedTausPt2 *
			  process.TauHistosBeforeTauEta2 *
			  process.selectedTausEta2 *
			  process.TauHistosBeforeTauID2 *
			  process.selectedTausID2 *
			  process.TauHistosBeforeTauIso2 *
			  process.selectedTausIso2 *
			  process.TauHistosBeforeMuonVeto2 *
			  process.selectedTausMuonVeto2 *
			  process.TauHistosBeforeEleVeto2 *
			  process.selectedTausEleVeto2 *
			  process.TauHistosAfterTau2Sequence *
			  #EndTauSequence
			  process.compositeCandidateSequenceForETT *
			  process.TauTauSequence *
			  process.jetSequence *
			  process.CompCandHistosBeforeSel *
			  process.selectedCompCandUW *
			  process.CompCandHistosAfterSel *
			  (process.MuonHistosFinal + process.EleHistosFinal + process.TauHistosFinal1 + process.TauHistosFinal2 + process.DiTauHistosFinal)
			  #process.mcMatching *
			  #process.compositeCandidateSequenceMcAssignment *
			  #process.massPlotsMcAssignment *
			  #process.massPlotsLowPtLepton *
			  #process.selectedEvents
)

#process.outp1 = cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

