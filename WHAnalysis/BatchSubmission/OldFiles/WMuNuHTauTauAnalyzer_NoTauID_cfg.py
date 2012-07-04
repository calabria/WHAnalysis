import FWCore.ParameterSet.Config as cms

process = cms.Process("WMuNuHTauTauAnalyzer")

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

        )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#################################################################################################################################

process.load("WHAnalysis.Configuration.VertexSelector_cff")
process.load("WHAnalysis.Configuration.TriggerSelector_cff")
process.load("WHAnalysis.Configuration.TauSelector_cff")
process.load("WHAnalysis.Configuration.ElectronSelector_cff")
process.load("WHAnalysis.Configuration.MuonSelector_cff")
process.load("WHAnalysis.Configuration.JetSelector_cff")
process.load("WHAnalysis.Configuration.METSelector_cff")
process.load("WHAnalysis.Configuration.MuMETPairSelector_cff")
process.load("WHAnalysis.Configuration.EleTauPairSelector_cff")
process.load("WHAnalysis.Configuration.GenFilter_cff")
process.load("WHAnalysis.Configuration.MuEleSelector_cff")
process.load("WHAnalysis.Configuration.weights_cff")
process.load("WHAnalysis.Configuration.MCSelector_cff")
process.load("WHAnalysis.Configuration.TauMCSelector_cff")



process.hltSelection.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.hltSelection.HLTPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v*')

process.TriggerHistosBeforeSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosBeforeSel.hltPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v')

process.TriggerHistosAfterSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosAfterSel.hltPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v')

#################################################################################################################################
#PU Correction for MC samples only
isMCBool = cms.bool(True)

process.MuonHistosBeforeMuonPt.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonEta.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonID.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonIso.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeElePt.isMC = cms.untracked.bool(isMCBool.value())                        
process.MuonHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

process.VertexHistosBeforeMCFilter.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosBeforeSel.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosAfterSel.isMC = cms.untracked.bool(isMCBool.value())

process.TriggerHistosBeforeSel.isMC = cms.untracked.bool(isMCBool.value())
process.TriggerHistosAfterSel.isMC = cms.untracked.bool(isMCBool.value())

process.TauHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforePt.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauEta.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauID.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauIso.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeMuonVeto.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeEleVeto.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeDiTau.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeHighestPt.isMC = cms.untracked.bool(isMCBool.value())

process.JetHistosBeforeJetEt.isMC = cms.untracked.bool(isMCBool.value())
#process.JetHistosBeforeJetEta.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosBeforeJetBTag.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosAfterJetBTag.isMC = cms.untracked.bool(isMCBool.value())
process.JetHistosAfterNumJet.isMC = cms.untracked.bool(isMCBool.value())

process.EleHistosBeforeElePt.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleEta.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleCrack.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleID.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleTrk.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleIPxy.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleTauPairs.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())

process.DiTauHistosBeforeCharge.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeMT.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforePzeta.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosFinalForEleTau.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeMET.isMC = cms.untracked.bool(isMCBool.value())
process.WHistosFinal.isMC = cms.untracked.bool(isMCBool.value())
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
	path = cms.untracked.string("/cmshome/calabria/")
)

process.puDistribution = cms.EDAnalyzer('PuDistribution')

process.genFilter.process = cms.untracked.int32(1)

process.selectedTausID.cut = cms.string('')
process.selectedTausIso.cut = cms.string('')
process.selectedTausMuonVeto.cut = cms.string('')
process.selectedTausEleVeto.cut = cms.string('')

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	#__outpuFile

	)
)

process.mypath = cms.Path(process.puDistribution * #Enable only for MC samples
			  process.VertexHistosBeforeMCFilter *
			  #process.genFilter *
			  process.triggerSequence *
			  process.vertexSequence *
			  process.muonSequence *
			  process.electronSequence *
			  process.tauSequence *
			  (process.selectedEleTauPairs + process.selectedMuMETPairs + process.selectedEleMuPairs) *
			  #process.DiTauHistosBeforeMET *
			  #process.selectedMETMax *
			  process.eleTauSequence *
			  process.jetSequence *
			  process.muMetSequence 
			  #process.MuonHistosFinal *
			  #(process.EleHistosFinal + process.TauHistosFinal + process.DiTauHistosFinal)
			  #process.selectedEvents
)

#process.outp1=cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

