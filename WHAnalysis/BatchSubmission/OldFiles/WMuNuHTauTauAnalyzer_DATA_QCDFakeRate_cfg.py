import FWCore.ParameterSet.Config as cms

process = cms.Process("WMuNuHTauTauAnalyzer")

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
process.load("WHAnalysis.Configuration.CompositeCandidateCreator_cff")

process.hltSelection.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.hltSelection.HLTPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v*')

process.TriggerHistosBeforeSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosBeforeSel.hltPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v')

process.TriggerHistosAfterSel.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistosAfterSel.hltPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v')

#################################################################################################################################
#PU Correction for MC samples only
isMCBool = cms.bool(False)

process.MuonHistosBeforeMuonPt.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonEta.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonID.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonIPxy.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeMuonIso.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosAfterMuonIso.isMC = cms.untracked.bool(isMCBool.value())
process.MuonHistosBeforeElePt.isMC = cms.untracked.bool(isMCBool.value())                        
process.MuonHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

process.VertexHistosBeforeMCFilter.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosBeforeSel.isMC = cms.untracked.bool(isMCBool.value())
process.VertexHistosAfterSel.isMC = cms.untracked.bool(isMCBool.value())

process.TriggerHistosBeforeSel.isMC = cms.untracked.bool(isMCBool.value())
process.TriggerHistosAfterSel.isMC = cms.untracked.bool(isMCBool.value())

process.TauHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauPt.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauEta.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauID.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeTauIso.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeMuonVeto.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeEleVeto.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeHighestPt.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosBeforeDiTau.isMC = cms.untracked.bool(isMCBool.value())
process.TauHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

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
process.EleHistosAfterWWId1.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosAfterWWId2.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleTrk.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleIPxy.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosAfterEleIPxy.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleTauPairs.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosFinal.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosAfterEleID55.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosAfterEleID65.isMC = cms.untracked.bool(isMCBool.value())

process.DiTauHistosBeforeMET.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeCharge.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeMT.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforePzeta.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosFinalForEleTau.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

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

process.produceEleMT = cms.EDProducer('AddUserVariables',
    objects = cms.InputTag("patElectrons"),
    met = cms.InputTag("patMETsPF")
)

process.selectedEvents = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/Events/")
)

process.puDistribution = cms.EDAnalyzer('PuDistribution')

process.genFilter.process = cms.untracked.int32(1)

process.selectedMuonsIso2 = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("selectedMuonsIPxy:selectedMuonsByIP"),
                         cut = cms.string('(isolationR03.hadEt+isolationR03.emEt+isolationR03.sumPt)/pt > 0.3'),
                         filter = cms.bool(True)
                         )

process.selectedTausIso.cut = cms.string('tauID("byLooseIsolation") < 0.5')

process.selectedElectronsPt.cut = cms.string('')

process.selectedEleMT = cms.EDFilter('PATElectronSelector',
                        src = cms.InputTag("selectedElectronsCrack"),
    			cut = cms.string("userFloat('Mt') < 40"),
    			filter = cms.bool(True)
			)

process.selectedElectronsID55 = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedEleMT"),
    			cut = cms.string('(electronID("simpleEleId80cIso") > 4.5 && electronID("simpleEleId80cIso") < 5.5) || electronID("simpleEleId80cIso") > 6.5'),
    			#cut = cms.string(''),
    			filter = cms.bool(False)
)

process.selectedElectronsID65 = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedEleMT"),
    			cut = cms.string('electronID("simpleEleId80cIso") > 6.5'),
    			filter = cms.bool(False)
)

process.selectedElectronsDeltaR.eleSrc = cms.untracked.InputTag("produceEleMT")
process.EleHistosBeforeDeltaR.electronSrc = cms.untracked.InputTag("produceEleMT")
process.selectedMuonsOneMuon.src = cms.InputTag("selectedMuonsIso2")
process.MuonHistosBeforeElePt.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.MuonHistosFinal.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.MuonHistosAfterMuonIso.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.selectedElectronsDeltaR.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosBeforeDeltaR.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosBeforeElePt.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosBeforeEleEta.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosBeforeEleCrack.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosBeforeEleID.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosAfterWWId1.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosAfterWWId2.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosBeforeEleTrk.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosBeforeEleIPxy.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosAfterEleIPxy.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosBeforeEleTauPairs.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosFinal.muonSrc  = cms.untracked.InputTag("selectedMuonsIso2")
process.selectedTausByDeltaR.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.selectedTausByDeltaR.eleSrc = cms.untracked.InputTag("patElectrons")
process.TauHistosBeforeTauEta.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.TauHistosBeforeDeltaR.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")                                   
process.TauHistosBeforeTauPt.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.TauHistosBeforeTauID.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.TauHistosBeforeTauIso.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.TauHistosBeforeMuonVeto.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.TauHistosBeforeEleVeto.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.TauHistosBeforeHighestPt.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.TauHistosBeforeDiTau.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.TauHistosBeforeTauEta.eleSrc = cms.untracked.InputTag("produceEleMT")
process.TauHistosBeforeDeltaR.eleSrc = cms.untracked.InputTag("produceEleMT")                                   
process.TauHistosBeforeTauPt.eleSrc = cms.untracked.InputTag("produceEleMT")
process.TauHistosBeforeTauID.eleSrc = cms.untracked.InputTag("produceEleMT")
process.TauHistosBeforeTauIso.eleSrc = cms.untracked.InputTag("produceEleMT")
process.TauHistosBeforeMuonVeto.eleSrc = cms.untracked.InputTag("produceEleMT")
process.TauHistosBeforeEleVeto.eleSrc = cms.untracked.InputTag("produceEleMT")
process.TauHistosBeforeHighestPt.eleSrc = cms.untracked.InputTag("produceEleMT")
process.TauHistosBeforeDiTau.eleSrc = cms.untracked.InputTag("produceEleMT")
process.EleHistosAfterEleID55.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")
process.EleHistosAfterEleID65.muonSrc = cms.untracked.InputTag("selectedMuonsIso2")

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	#__outpuFile

	)
)

process.mypath = cms.Path(#process.puDistribution * #Enable only for MC samples
			  #process.VertexHistosBeforeMCFilter *
			  #process.genFilter *
			  #process.triggerSequence *
			  process.produceEleMT *
			  process.vertexSequence *
			  #################################
			  process.MuonHistosBeforeMuonPt *
			  process.selectedMuonsPt * 
			  process.MuonHistosBeforeMuonEta *
			  process.selectedMuonsEta *
			  process.MuonHistosBeforeMuonID *
			  process.selectedMuonsID *
			  process.MuonHistosBeforeMuonIPxy *
			  process.selectedMuonsIPxy *
			  process.MuonHistosBeforeMuonIso *
			  process.selectedMuonsIso2 *
			  process.MuonHistosAfterMuonIso *
			  process.selectedMuonsOneMuon *
			  process.MuonHistosBeforeElePt *
			  #################################
			  process.tauSequence *
			  #################################
			  process.EleHistosBeforeDeltaR *
			  process.selectedElectronsDeltaR *
			  process.EleHistosBeforeElePt *
			  process.selectedElectronsPt *
			  process.EleHistosBeforeEleEta *
			  process.selectedElectronsEta *
			  process.EleHistosBeforeEleCrack *
			  process.selectedElectronsCrack *
			  process.EleHistosBeforeEleID *
			  process.selectedEleMT *
			  ((process.selectedElectronsID55*process.EleHistosAfterEleID55) + (process.selectedElectronsID65*process.EleHistosAfterEleID65))
)

#process.outp1=cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

