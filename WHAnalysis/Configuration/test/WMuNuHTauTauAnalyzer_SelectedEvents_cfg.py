import FWCore.ParameterSet.Config as cms

process = cms.Process("WMuNuHTauTauAnalyzer")

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
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_1.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_2.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_3.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_4.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_5.root',

        ),

    eventsToProcess = cms.untracked.VEventRange('1:36:26692',
						'1:374:284439',
						'1:500:380162',
						'1:1004:763989',
						'1:1020:775857',
						'1:1049:797556',
						'1:1449:1102515',
						'1:1490:1133783',
						'1:1557:1184382',
						'1:1660:1262504',
						'1:1660:1262663',
						'1:1836:1397106',
						'1:1842:1401314',
						'1:1858:1413524',
						'1:1930:1467989',
						'1:1930:1468434',
						'1:1939:1474959',
						'1:1949:1482886',
						'1:1994:1516954',
						'1:2084:1585364',
						'1:2103:1599679',
						'1:2130:1620719',
						'1:2249:1710741',
						'1:2284:1737509',
						'1:2314:1760757',
						'1:2360:1795673',
						'1:2370:1803558',
						'1:2474:1882532',
						'1:2478:1885024',
						'1:2480:1886817',
						'1:2494:1897865',
						'1:2510:1909756',
						'1:2730:2077454',
						'1:2732:2079008',
						'1:2809:2137025',
						'1:2831:2154157',)

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
#process.hltSelection.HLTPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v*')
#process.hltSelection.HLTPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v*','HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_v*')
process.hltSelection.HLTPaths = cms.vstring('HLT_Mu17_Ele8_CaloIdL_v','HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_v')

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
#process.MuonHistosBeforeMuonIPxy.isMC = cms.untracked.bool(isMCBool.value())
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
process.EleHistosAfterPreEleID.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosAfterEleID.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleTrk.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleIPxy.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleIPz.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeOneEle.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosBeforeEleTauPairs.isMC = cms.untracked.bool(isMCBool.value())
process.EleHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

process.DiTauHistosBeforeMET.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeCharge.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeDeltaR.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforeMT.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosBeforePzeta.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosFinalForEleTau.isMC = cms.untracked.bool(isMCBool.value())
process.DiTauHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

process.CompCandHistosBeforeSel.isMC = cms.untracked.bool(isMCBool.value())
process.CompCandHistosAfterSel.isMC = cms.untracked.bool(isMCBool.value())

process.WHistosFinal.isMC = cms.untracked.bool(isMCBool.value())

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
	path = cms.untracked.string("/cmshome/calabria/Events/"),
        muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
	eleSrc = cms.untracked.InputTag("selectedElectronsIPz"),
	tauSrc = cms.untracked.InputTag("selectedTausHighestPt:TauHighestPt"),
)

process.selectedCompCandUW = cms.EDFilter("CompositeCandFilter",
        CompCandSrc = cms.untracked.InputTag("selectedEleTauMuCand"),
	EtCut = cms.untracked.double(80),
	applyEMuCharge = cms.untracked.bool(True),
        filter = cms.bool(True)
)

process.selectedCompCandVtxChi2 = cms.EDFilter("FinalVertexFilter",
  	muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
  	eleSrc = cms.untracked.InputTag("selectedElectronsIPz"),
  	tauSrc = cms.untracked.InputTag("selectedTausHighestPt:TauHighestPt"),
  	vertexChi2NDOF = cms.untracked.double(10),
        filter = cms.bool(True)
)

process.puDistribution = cms.EDAnalyzer('PuDistribution')

process.genFilter.process = cms.untracked.int32(1)


process.TFileService = cms.Service("TFileService", fileName = cms.string("/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/Configuration/test/histo_WH120_check_evanSelected_36_2.root") )

process.mypath = cms.Path(process.puDistribution * #Enable only for MC samples
			  process.VertexHistosBeforeMCFilter *
			  process.genFilter * #Enable only for Signal
			  process.triggerSequence *
			  process.vertexSequence *
			  process.muonSequence *
			  process.electronSequence *
			  process.tauSequence *
			  process.compositeCandidateSequence *
			  #process.DiTauHistosBeforeMET *
			  #process.selectedMETMax *
			  process.eleTauSequence *
			  process.jetSequence *
			  process.muMetSequence *
			  process.CompCandHistosBeforeSel *
			  process.selectedCompCandUW *
			  process.CompCandHistosAfterSel *
			  process.selectedCompCandVtxChi2 *
			  (process.MuonHistosFinal + process.EleHistosFinal + process.TauHistosFinal + process.DiTauHistosFinal) 
			  #process.selectedEvents
)

#process.outp1 = cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

