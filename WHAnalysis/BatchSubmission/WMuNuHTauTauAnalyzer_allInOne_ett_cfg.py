import FWCore.ParameterSet.Config as cms

process = cms.Process("WMuNuHTauTauAnalyzer")

#--------------------------------------------------------------------------------

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
options.register ('isMC',
                  True,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "Sample Type: MC or data")

options.register ('target',
                  'MC',
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.string,
                  "Desired channel: WH, TTH, ZH, MC or DATA")    

options.register ('globaltag',
                  'START53_V7F::All',
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.string,
                  "Global Tag to use. Default: START53_V11::All")


import sys
print sys.argv

if hasattr(sys, "argv") == True:
	options.parseArguments()
isMC = options.isMC
target = options.target
globaltag = options.globaltag

print 'Using target: %s' % target

#--------------------------------------------------------------------------------

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string(globaltag)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

		#__inputFile

        ),

#    eventsToProcess = cms.untracked.VEventRange('166512:565:684617144',
#						'176933:53:79915327',
#						'180250:162:285994826')

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
isMCBool = cms.bool(isMC)

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
process.CompCandHistosAfterSelLt.isMC = cms.untracked.bool(isMCBool.value())

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
	path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Events/EventsETT_Signal_MET/"),
        muonSrc = cms.untracked.InputTag("muonVariables"),
	eleSrc = cms.untracked.InputTag("electronVariables"),
	tauSrc = cms.untracked.InputTag("tauVariables"),
	jetSrc = cms.untracked.InputTag("patJets")
)

process.puDistribution = cms.EDAnalyzer('PuDistribution')

if(target == "WH"):
	process.genFilter.process = cms.untracked.int32(1)
if(target == "ZH"):
	process.genFilter.process = cms.untracked.int32(2)
if(target == "TTH"):
	process.genFilter.process = cms.untracked.int32(3)

process.producesUserDefinedVarsEle.isMC = cms.bool(isMC)
process.producesUserDefinedVarsTau.isMC = cms.bool(isMC)

process.eleMatching.filter = cms.bool(False)
process.tau1Matching.filter = cms.bool(False)
process.selectedElectronsPt.src = cms.InputTag("producesUserDefinedVarsEle")
process.selectedTausByDeltaR.tauSrc = cms.untracked.InputTag("producesUserDefinedVarsTau")

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	#__outpuFile

	)
)

process.ettFinalState = cms.EDFilter('MCTruthFullyHadronic',
     genParticles = cms.untracked.InputTag("genParticles"),
     filter = cms.bool(True)
)

if((target == "WH") or (target == "ZH") or (target == "TTH")):
	process.analysisPath = cms.Sequence(
		process.producesUserDefinedVarsEle *
		process.producesUserDefinedVarsTau *
		#process.skimmingSequence *
		process.puDistribution * #Enable only for MC samples
		process.VertexHistosBeforeMCFilter *
		process.genFilter * #Enable only for Signal
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
			### Zee veto della scimmia
				((process.selectedEle1Ele2 + process.selectedEle1Ele2NoCut) *
				(process.eePairsVeto + process.eePairsVetoNoCut) *
				process.selectedEle1Ele2OnePair *
				process.eePairsVetoAfterSel) *
				### Ztt veto della scimmia
				process.CompCandHistosBeforeZttVeto *
				process.ztautauVeto *
		process.CompCandHistosAfterSel *
		process.selectedCompCandUW *
		process.jetSequence *
		process.selectedMETMax *
		process.CompCandHistosAfterSelLt *
		(process.MuonHistosFinal + process.EleHistosFinal + process.TauHistosFinal1 + process.TauHistosFinal2 + process.DiTauHistosFinal) *
		#process.mcMatching *
		#process.compositeCandidateSequenceMcAssignment *
		#process.massPlotsMcAssignment *
		#process.massPlotsLowPtLepton *
		#process.selectedEvents
		process.selectedEvents
	)
if(target == "MC"):
	process.analysisPath = cms.Sequence(
		process.producesUserDefinedVarsEle *
		process.producesUserDefinedVarsTau *
		#process.skimmingSequence *
		process.puDistribution * #Enable only for MC samples
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
			### Zee veto della scimmia
				((process.selectedEle1Ele2 + process.selectedEle1Ele2NoCut) *
				(process.eePairsVeto + process.eePairsVetoNoCut) *
				process.selectedEle1Ele2OnePair *
				process.eePairsVetoAfterSel) *
				### Ztt veto della scimmia
				process.CompCandHistosBeforeZttVeto *
				process.ztautauVeto *
		process.CompCandHistosAfterSel *
		process.selectedCompCandUW *
		process.jetSequence *
		process.selectedMETMax *
		process.CompCandHistosAfterSelLt *
		(process.MuonHistosFinal + process.EleHistosFinal + process.TauHistosFinal1 + process.TauHistosFinal2 + process.DiTauHistosFinal) *
		#process.mcMatching *
		#process.compositeCandidateSequenceMcAssignment *
		#process.massPlotsMcAssignment *
		#process.massPlotsLowPtLepton *
		#process.selectedEvents
		process.selectedEvents
	)
if(target == "DATA"):
	process.analysisPath = cms.Sequence(
		process.producesUserDefinedVarsEle *
		process.producesUserDefinedVarsTau *
		#process.skimmingSequence *
		#process.puDistribution * #Enable only for MC samples
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
			### Zee veto della scimmia
				((process.selectedEle1Ele2 + process.selectedEle1Ele2NoCut) *
				(process.eePairsVeto + process.eePairsVetoNoCut) *
				process.selectedEle1Ele2OnePair *
				process.eePairsVetoAfterSel) *
				### Ztt veto della scimmia
				process.CompCandHistosBeforeZttVeto *
				process.ztautauVeto *
		process.CompCandHistosAfterSel *
		process.selectedCompCandUW *
		process.jetSequence *
		process.selectedMETMax *
		process.CompCandHistosAfterSelLt *
		(process.MuonHistosFinal + process.EleHistosFinal + process.TauHistosFinal1 + process.TauHistosFinal2 + process.DiTauHistosFinal) *
		#process.mcMatching *
		#process.compositeCandidateSequenceMcAssignment *
		#process.massPlotsMcAssignment *
		#process.massPlotsLowPtLepton *
		#process.selectedEvents
		process.selectedEvents
	)

process.mypath = cms.Path(process.analysisPath)

#process.outp1=cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

