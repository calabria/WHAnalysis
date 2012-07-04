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
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_10_1_uwv.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_11_1_xXm.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_12_1_Hel.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_13_1_oI7.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_14_1_01N.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_15_1_Dsc.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_16_1_wiU.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_1_1_Duy.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_2_1_qep.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_3_1_g9G.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_4_1_3x4.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_5_1_QTz.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_6_1_lP8.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_7_1_flc.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_8_1_0Q1.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT_2/WH_125_ETT_NoSkim/patTuple_9_1_dUE.root',

        )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#################################################################################################################################

process.load("WHAnalysis.Configuration.ProduceMTAndTriggerMatching_cff")
process.load("WHAnalysis.Configuration.skimming_ett_cff")
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
process.hltSelection.defaultTrigger = cms.string("HLT_Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v")

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
process.VertexHistosBeforeMCFilter3.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosBeforeMCFilter4.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosBeforeMCFilter5.isMC = cms.untracked.bool(isMCBool.value())
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

#################################################################################################################################

process.out = cms.OutputModule("PoolOutputModule",
                fileName = cms.untracked.string("/tmp/calabria/test.root"),
		outputCommands = cms.untracked.vstring(
		#'keep *',
      		"keep *_*_*_EleTauAnalyzer"
		)
        )

#################################################################################################################################

process.selectedEvents = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events/EventsETT/"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsIPz"),
	tauSrc = cms.untracked.InputTag("selectedTausHighestPt:TauHighestPt"),
)

process.puDistribution = cms.EDAnalyzer('PuDistribution')

process.genFilter.process = cms.untracked.int32(1)


process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'histo_WH125_Check_3.root'

	)
)

process.ettFinalState = cms.EDFilter('MCTruthFullyHadronic',
     genParticles = cms.untracked.InputTag("genParticles"),
     filter = cms.bool(True)
)

############################################################    Ele   ###########################################################

process.eleMatching = cms.EDFilter("PATElectronSelector",
                         src = cms.InputTag("producesUserDefinedVarsEle"),
                         cut = cms.string("userInt('mcMatch') > 0.5"),
                         filter = cms.bool(True)
                         )

process.producesUserDefinedVarsEle.isMC = cms.bool(True)

process.selectedElectronsPt.cut = cms.string("pt > 24. && userInt('mcMatch') > 0.5")
process.selectedElectronsEta.cut = cms.string("abs(eta) < 2.1")
process.selectedElectronsCrack.cut = cms.string("(isEB && userFloat('HoE') <0.15) || (isEE && userFloat('HoE') <0.10)")
process.selectedElectronsPreID.cut = cms.string("(isEB && userFloat('sihih') < 0.014) || (isEE && userFloat('sihih') < 0.35)")
process.selectedElectronsID.cut = cms.string("(isEB && userFloat('dEta') < 0.01) || (isEE && userFloat('dEta') < 0.01)")
process.selectedElectronsIso.cut = cms.string("(isEB && userFloat('dPhi') < 0.15) || (isEE && userFloat('dPhi') < 0.10)")
process.selectedElectronsTrk.cut = cms.string("dr03EcalRecHitSumEt < 4.5")
process.selectedElectronsAdditional.cut = cms.string("dr03TkSumPt < 3.5")

############################################################    Tau1   ##########################################################

process.tau1Matching = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("producesUserDefinedVarsTau"),
                         cut = cms.string("userInt('mcMatch') > 0.5"),
                         filter = cms.bool(True)
                         )

process.producesUserDefinedVarsTau.isMC = cms.bool(True)

process.selectedTausPt1.cut = cms.string("pt > 25.0 && userInt('mcMatch') > 0.5")
process.selectedTausEta.cut = cms.string("abs(eta) < 2.1")
process.selectedTausEleVeto.cut = cms.string('tauID("againstElectronLoose") > 0.5')

############################################################    Tau2   ##########################################################

process.selectedTausPt2.cut = cms.string("pt > 20.0 && userInt('mcMatch') > 0.5")
process.selectedTausEta2.cut = cms.string("abs(eta) < 2.3")
process.selectedTausEleVeto2.cut = cms.string('tauID("againstElectronMedium") > 0.5')

############################################################    Pairs   #########################################################

process.selectedEleTau1Tau2Cand.decay = cms.string("selectedElectronsAdditional selectedTauTauPairsByCharge:selectedCand1Cand2PairsByCharge")

#################################################################################################################################

process.mypath = cms.Path(
			  process.producesUserDefinedVarsEle *
			  process.producesUserDefinedVarsTau *
			  #process.puDistribution * #Enable only for MC samples
			  process.VertexHistosBeforeMCFilter *
			  process.genFilter * #Enable only for Signal
			  process.VertexHistosBeforeMCFilter2 *
			  process.ettFinalState *
			  process.VertexHistosBeforeMCFilter3 *
			  process.eleMatching *
			  process.VertexHistosBeforeMCFilter4 *
			  process.tau1Matching *
			  process.VertexHistosBeforeMCFilter5 *
			  #process.skimmingSequence *
			  #process.triggerSequence *
			  process.vertexSequence *
			  process.electronSequence *
			  #process.muonSequence *
			  process.tauSequence *
			  #process.VertexHistosForPU *
			  process.selectedTau1Tau2 *
			  process.TauTauSequence *
			  process.jetSequence *
			  process.selectedEleTau1Tau2Cand *
			  process.CompCandHistosBeforeSel *
				  ### Zee veto della scimmia
				  ((process.selectedEle1Ele2 + process.selectedEle1Ele2NoCut) *
				   (process.eePairsVeto + process.eePairsVetoNoCut) *
				   process.selectedEle1Ele2OnePair *
				   process.eePairsVetoAfterSel) *
				  ### Ztt veto della scimmia
			 	  process.CompCandHistosBeforeZttVeto *
			  	  process.ztautauVeto *
			  process.CompCandHistosAfterSel
			  #(process.MuonHistosFinal + process.EleHistosFinal + process.TauHistosFinal1 + process.TauHistosFinal2 + process.DiTauHistosFinal)
			  #process.selectedEvents
)

#process.outp1=cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

