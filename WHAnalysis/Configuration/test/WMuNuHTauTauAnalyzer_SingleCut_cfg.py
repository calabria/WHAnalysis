import FWCore.ParameterSet.Config as cms

process = cms.Process("WMuNuHTauTauAnalyzer")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

		'file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_1_2_PUm.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_97_2_Qip.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_99_4_5Lh.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_89_2_k8E.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_94_1_6b8.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_80_1_xUD.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_81_1_lIw.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_82_1_R09.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_83_4_A81.root',
        )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5000) )

#################################################################################################################################

process.load("WHAnalysis.Configuration.VertexSelector_cff")
process.load("WHAnalysis.Configuration.TauSelector_cff")
process.load("WHAnalysis.Configuration.ElectronSelector_cff")
process.load("WHAnalysis.Configuration.MuonSelector_cff")
process.load("WHAnalysis.Configuration.JetSelector_cff")
process.load("WHAnalysis.Configuration.METSelector_cff")
process.load("WHAnalysis.Configuration.MuMETPairSelector_cff")
process.load("WHAnalysis.Configuration.EleTauPairSelector_cff")
process.load("WHAnalysis.Configuration.GenFilter_cff")

process.hltHighLevelMuons.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.hltHighLevelMuons.HLTPaths = cms.vstring('HLT_Mu3_v*')

process.TriggerHistos.hltResultsSource = cms.InputTag('TriggerResults::HLT')
process.TriggerHistos.hltPaths = cms.vstring('HLT_Mu3_v3')

#################################################################################################################################

process.out = cms.OutputModule("PoolOutputModule",
                fileName = cms.untracked.string("/tmp/calabria/test.root"),
		outputCommands = cms.untracked.vstring(
		#'keep *',
      		"keep *_*_*_EleTauAnalyzer"
		)
        )

#################################################################################################################################

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo.root") )

process.mypath1 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedMuonsPt 
			  + process.VertexHistosAfterSel1
)

process.mypath2 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedMuonsEta 
			  + process.VertexHistosAfterSel2
)

process.mypath3 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedMuonsID
			  + process.VertexHistosAfterSel3
)

process.mypath4 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
		      	  process.selectedMuonsIso
			  + process.VertexHistosAfterSel4
)

process.mypath5 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedElectronsPt
			  + process.VertexHistosAfterSel5
)

process.mypath6 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedElectronsEta
			  + process.VertexHistosAfterSel6
)

process.mypath7 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedElectronsCrack
			  + process.VertexHistosAfterSel7
)

process.mypath8 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedElectronsID
			  + process.VertexHistosAfterSel8
)

process.mypath9 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedElectronsID
			  + process.VertexHistosAfterSel9
)

process.mypath10 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedElectronsTrk
			  + process.VertexHistosAfterSel10
)

process.mypath11 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedElectronsIPxy
			  + process.VertexHistosAfterSel11
)

process.mypath12 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedTausPt
			  + process.VertexHistosAfterSel12
)

process.mypath13 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedTausEta
			  + process.VertexHistosAfterSel13
)

process.mypath14 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedTausID
			  + process.VertexHistosAfterSel14
)

process.mypath15 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedTausIso
			  + process.VertexHistosAfterSel15
)

process.mypath16 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedTausMuonVeto
			  + process.VertexHistosAfterSel16
)

process.mypath17 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  process.selectedTausEleVeto
			  + process.VertexHistosAfterSel17
)

process.mypath18 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  (process.selectedEleTauPairs + process.selectedMuMETPairs) *
			  process.selectedEleTauPairsByCharge
			  + process.VertexHistosAfterSel18
)

process.mypath19 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  (process.selectedEleTauPairs + process.selectedMuMETPairs) *
			  process.selectedEleTauPairsDeltaR
			  + process.VertexHistosAfterSel19
)

process.mypath20 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  (process.selectedEleTauPairs + process.selectedMuMETPairs) *
			  process.selectedEleTauPairsMT
			  + process.VertexHistosAfterSel20
)

process.mypath21 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  (process.selectedEleTauPairs + process.selectedMuMETPairs) *
			  process.selectedEleTauPairsPzeta
			  + process.VertexHistosAfterSel21
)

process.mypath22 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  (process.selectedEleTauPairs + process.selectedMuMETPairs) *
			  process.selectedEleTauPairsOnly1Pair
			  + process.VertexHistosAfterSel22
)

process.mypath23 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  (process.selectedEleTauPairs + process.selectedMuMETPairs) *
			  process.selectedMETMax
			  + process.VertexHistosAfterSel23
)

process.mypath24 = cms.Path(
			  process.hltHighLevelMuons +
 			  process.selectedPrimaryVertex +
			  process.genFilter +
			  (process.selectedEleTauPairs + process.selectedMuMETPairs) *
			  process.selectedPatJetsBtag
			  + process.VertexHistosAfterSel24
)

#process.outp1=cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

