import FWCore.ParameterSet.Config as cms

process = cms.Process("WMuNuHTauTauAnalyzerMMT")

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_85_2_wps.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_86_3_iXN.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_87_2_oXJ.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_88_1_uFP.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_8_1_1UJ.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_90_1_1xk.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_92_1_uqo.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_93_2_br2.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_95_1_Hpt.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_96_1_zns.root',

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
process.hltSelection.HLTPaths = cms.vstring("HLT_IsoMu12_v","HLT_IsoMu17_v","HLT_IsoMu20_v","HLT_IsoMu24_v")
process.hltSelection.hltEventRanges = cms.VEventRange("160403:MIN-163261:MAX","163269:MIN-171178:MAX","171219:MIN-173692:MAX","175832:MIN-180252:MAX")
process.hltSelection.defaultTrigger = cms.string("")

process.TriggerHistosBeforeSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosBeforeSel.hltPaths = cms.vstring('HLT_IsoMu24_v')

process.TriggerHistosAfterSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosAfterSel.hltPaths = cms.vstring('HLT_IsoMu24_v')

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
	path = cms.untracked.string("/cmshome/calabria/Events/EventsETT/"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsIPz"),
	tauSrc = cms.untracked.InputTag("selectedTausHighestPt:TauHighestPt"),
)

process.puDistribution = cms.EDAnalyzer('PuDistribution')

process.genFilter.process = cms.untracked.int32(1)

process.ettFinalState = cms.EDFilter('MCTruthFullyHadronic',
     genParticles = cms.untracked.InputTag("genParticles"),
     #muonSrc = cms.untracked.InputTag("muonVariables"),
     eleSrc = cms.untracked.InputTag("producesUserDefinedVarsEle"),
     tauSrc = cms.untracked.InputTag("tauVariables"),
     deltaR = cms.untracked.double(0.1),
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/Configuration/test/histo_prova.root") )

process.mypath = cms.Path(process.producesUserDefinedVarsEle *
			  process.puDistribution * #Enable only for MC samples
			  process.VertexHistosBeforeMCFilter *
			  process.genFilter * #Enable only for Signal
			  process.VertexHistosBeforeMCFilter2 *
			  process.ettFinalState *
			  process.triggerSequence *
			  process.vertexSequence *
			  process.electronSequence *
			  process.muonSequence *
			  process.tauSequence *
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

