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

		#'file:./CRAB/patTuple_evan.root'
		#'file:./CRAB/patTuple_WH120_evan.root'
		#'file:./CRAB/patTuple_cesare.root'
		#'file:./CRAB/patTuple.root'
		#'file:./CRAB/patTuple_moreEvents.root'
		#'file:./CRAB/patTuple_evan_jan11_correctMVA.root'
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_1.root',
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_2.root',
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_3.root',
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_4.root',
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_5.root',

		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_90_1_Hjk.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_91_1_QkT.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_92_1_emM.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_93_1_j1J.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_94_1_312.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_95_1_YEp.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_96_1_uQ6.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_97_1_S9n.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_98_1_6VE.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ReReco/WH_120/patTuple_99_1_CRb.root',

        ),


)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#################################################################################################################################

process.load("WHAnalysis.Configuration.GenFilter_cff")
process.load("WHAnalysis.Configuration.VertexSelector_cff")
process.load("WHAnalysis.Configuration.TriggerSelector_cff")
process.load("WHAnalysis.Configuration.ElectronSelector_mtt_cff")
process.load("WHAnalysis.Configuration.MuonSelector_mtt_cff")
process.load("WHAnalysis.Configuration.TauSelector_mtt_cff")
process.load("WHAnalysis.Configuration.CompositeCandidateCreator_mtt_cff")
process.load("WHAnalysis.Configuration.JetSelector_cff")
process.load("WHAnalysis.Configuration.METSelector_cff")
process.load("WHAnalysis.Configuration.TauTauPairSelector_cff")

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
process.MuonHistosBeforeMuonEta.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonID.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonIso.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosAfterMuonIso.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeEleSequence.isMC = cms.untracked.bool(isMCBool.value())                        
process.MuonHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

process.VertexHistosBeforeMCFilter.isMC = cms.untracked.bool(isMCBool.value())
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
process.TauHistosBeforeTauPt.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosAfterTauPt1.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosAfterTauPt2.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

process.JetHistosBeforeJetEt.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosBeforeJetEta.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosBeforeJetBTag.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosAfterJetBTag.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosAfterNumJet.isMC = cms.untracked.bool(isMCBool.value())

process.EleHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeTauSquence.isMC = cms.untracked.bool(isMCBool.value())
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
	path = cms.untracked.string("/cmshome/calabria/Events/EventsMTT/"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsIPz"),
	tauSrc = cms.untracked.InputTag("selectedTausHighestPt:TauHighestPt"),
)

process.puDistribution = cms.EDAnalyzer('PuDistribution')

process.genFilter.process = cms.untracked.int32(1)


process.TFileService = cms.Service("TFileService", fileName = cms.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/Configuration/test/histo_prova.root") )

process.mypath = cms.Path(process.puDistribution * #Enable only for MC samples
			  process.VertexHistosBeforeMCFilter *
			  #process.genFilter * #Enable only for Signal
			  process.triggerSequence *
			  process.vertexSequence *
			  process.muonSequence *
			  process.tauSequence *
			  process.electronSequence *
			  process.compositeCandidateSequenceForMTT *
			  process.TauTauSequence *
			  process.jetSequence *
			  process.CompCandHistosBeforeSel *
			  process.selectedCompCandUW *
			  process.CompCandHistosAfterSel *
			  (process.MuonHistosFinal + process.EleHistosFinal + process.TauHistosFinal + process.DiTauHistosFinal)
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

