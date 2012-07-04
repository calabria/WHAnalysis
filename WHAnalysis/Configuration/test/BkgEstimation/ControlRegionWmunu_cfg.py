import FWCore.ParameterSet.Config as cms
from WHAnalysis.Configuration.weights_cff import *

process = cms.Process("ControlRegionWmunu")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

		'file:/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/Configuration/test/CRAB/patTuple.root',

        )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#################################################################################################################################

process.load("WHAnalysis.Configuration.GenFilter_cff")

#################################################################################################################################

#PU Correction for MC samples only
isMCBool = cms.bool(False)

#################################################################################################################################

process.out = cms.OutputModule("PoolOutputModule",
                fileName = cms.untracked.string("test.root"),
		outputCommands = cms.untracked.vstring(
		'keep *',
		)
        )

#################################################################################################################################

process.selectedEvents = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/")
)

process.puDistribution = cms.EDAnalyzer('PuDistribution')

process.genFilter.process = cms.untracked.int32(1)

#################################################################################################################################
# Trigger

process.hltSelection = cms.EDFilter("TriggerFilter",
                        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                        HLTPaths = cms.vstring("HLT_IsoMu12_v","HLT_IsoMu17_v","HLT_IsoMu20_v","HLT_IsoMu24_v"),
			defaultTrigger = cms.string("HLT_IsoMu24_v"),
                        hltEventRanges = cms.VEventRange("160403:MIN-163261:MAX","163269:MIN-171178:MAX","171219:MIN-173692:MAX","175832:MIN-180252:MAX"),
                        filter = cms.bool(True)
                        )

#################################################################################################################################
# Vertex

process.selectedPrimaryVertex = cms.EDFilter("GoodVertexFilter",
                        vertexCollection = cms.InputTag('offlinePrimaryVerticesWithBS'),
                        minimumNDOF = cms.uint32(7) ,
                        maxAbsZ = cms.double(24),	
                        maxd0 = cms.double(2),
                 	filter = cms.bool(True)	
                        )

#################################################################################################################################
# Muon

process.producesUserDefinedVarsMu = cms.EDProducer('MuonAddUserVariables',
    			objects = cms.InputTag("muonVariables"),
    			met = cms.InputTag("patMETsPF"),
    			triggerResults = cms.InputTag("patTriggerEvent"),
  			triggerPaths = cms.vstring("HLT_DoubleMu7_v","HLT_Mu13_Mu8_v","HLT_Mu17_Mu8_v"), 
  			triggerObjNamesLeg1 =cms.vstring("hltDiMuonL3PreFiltered7","hltSingleMu13L3Filtered13","hltL1Mu3EG5L3Filtered17"), 
  			triggerObjNamesLeg2 = cms.vstring("hltDiMuonL3PreFiltered7","hltDiMuonL3PreFiltered8","hltDiMuonL3PreFiltered8"), 
  			hltEventRanges = cms.VEventRange("160431:MIN-163869:MAX","165088:MIN-178380:MAX","178420:MIN-180252:MAX")
			)

process.selectedMuonsForWmunu = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("producesUserDefinedVarsMu"),
                        cut = cms.string("pt > 20. && abs(eta) < 2.1 && userInt('muonID') > 0.5 && userFloat('PFRelIsoDB04v2') < 0.1 && userFloat('Mt') > 40"),
                        filter = cms.bool(True)
                        )

process.selectedMuonsForVeto = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("producesUserDefinedVarsMu"),
                        cut = cms.string("pt > 5. && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

process.selectedMuonsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedMuonsForVeto"),
                     	maxNumber = cms.uint32(1),
                       	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
                     	)

process.MuonHistosCheck = cms.EDAnalyzer("MuonHistManager",
  			muonSrc = cms.untracked.InputTag("selectedMuonsForWmunu"),
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),                                     
			)

process.muonSequence = cms.Sequence(
			process.producesUserDefinedVarsMu *
			process.selectedMuonsForWmunu *
		  	process.selectedMuonsForVeto *
			process.selectedMuonsVeto *
			process.MuonHistosCheck
			)

#################################################################################################################################
# Electrons

process.producesUserDefinedVarsEle = cms.EDProducer('ElectronAddUserVariables',
    			objects = cms.InputTag("electronVariables"),
    			met = cms.InputTag("patMETsPF"),
    			triggerResults = cms.InputTag("patTriggerEvent"),
  			triggerPaths = cms.vstring("HLT_Mu17_Ele8_CaloIdL_v","HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_v"), 
  			triggerObjNamesLeg1 =cms.vstring("hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter","hltMu17Ele8CaloIdTPixelMatchFilter"), 
  			triggerObjNamesLeg2 = cms.vstring("hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter","hltMu17Ele8CaloIdTPixelMatchFilter"),
  			hltEventRanges = cms.VEventRange("160431:MIN-176469:MAX","176545:MIN-180252:MAX")
			)

process.selectedElectronsForVeto = cms.EDFilter("PATElectronSelector",
     			src = cms.InputTag("producesUserDefinedVarsEle"),
                        cut = cms.string("pt > 10. && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

process.selectedElectronsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedElectronsForVeto"),
                     	maxNumber = cms.uint32(0),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
			)

process.electronSequence = cms.Sequence(
			process.producesUserDefinedVarsEle *
			process.selectedElectronsForVeto *
			process.selectedElectronsVeto
			)

#################################################################################################################################
# Taus

process.selectedTausForVeto = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("tauVariables"),
                        cut = cms.string("pt > 20.0 && abs(eta) < 2.5 && tauID('decayModeFinding') > 0.5 && tauID('byLooseCombinedIsolationDeltaBetaCorr') > 0.5"),
                        filter = cms.bool(False)
                        )

process.selectedTausVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedTausForVeto"),
                     	maxNumber = cms.uint32(0),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
			)

process.tauSequence = cms.Sequence(
			process.selectedTausForVeto *
			process.selectedTausVeto
			)

#################################################################################################################################
# Jets

process.selectedPatJetsForVeto = cms.EDFilter("PATJetSelector",
    			src = cms.InputTag("patJetsAK5PF"),                                                               
    			cut = cms.string("et > 20. && abs(eta) < 2.5 && bDiscriminator('trackCountingHighEffBJetTags') > 3.3"), 
    			filter = cms.bool(False)
			)

process.selectedJetsVeto = cms.EDFilter("PATCandViewCountFilter",
    			src = cms.InputTag("selectedPatJetsForVeto"),
     			maxNumber = cms.uint32(0),
     			minNumber = cms.uint32(0),
     			filter = cms.bool(True)
			)

process.jetSequence = cms.Sequence(
			process.selectedPatJetsForVeto *
			process.selectedJetsVeto
			)

#################################################################################################################################
# Jet Probe

process.selectedMuProbes = cms.EDProducer('MuonVetoProducer',
			lep1Src = cms.untracked.InputTag("producesUserDefinedVarsMu"), #collezione grande
			lep2Src = cms.untracked.InputTag("selectedMuonsForWmunu"), #collezione piccola
			)

process.selectedMuProbesCharge = cms.EDProducer("MuObjSSProducer",
    			obj1Src = cms.untracked.InputTag("selectedMuProbes"),
			obj2Src = cms.untracked.InputTag("selectedMuonsForWmunu"),
			)

process.selectedEleProbesCharge = cms.EDProducer("EleObjSSProducer",
    			obj1Src = cms.untracked.InputTag("producesUserDefinedVarsEle"),
			obj2Src = cms.untracked.InputTag("selectedMuonsForWmunu"),
			)

process.probeSequence = cms.Sequence(
			process.selectedMuProbes *
			(process.selectedMuProbesCharge + process.selectedEleProbesCharge)
			)

#################################################################################################################################
# Denominator

process.selectedProbesDenMu = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuProbesCharge"),
                        cut = cms.string("pt > 9. && abs(eta) < 2.1 && (isGlobalMuon || isTrackerMuon) && globalTrack.isNonnull && globalTrack.hitPattern.numberOfValidPixelHits >= 1 && (userInt('triggerMatchingLeg1') || userInt('triggerMatchingLeg2'))"),
                        filter = cms.bool(False)
                        )

process.selectedProbesDenEle = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedEleProbesCharge"),
                        cut = cms.string("pt > 9. && abs(eta) < 2.5 && userFloat('nHits') <= 1 && userInt('antiConv') > 0.5 && (userInt('triggerMatchingLeg1') || userInt('triggerMatchingLeg2'))"),
                        filter = cms.bool(False)
                        )

process.selectedProbesDenTau = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("selectedProbesCharge"),
                        cut = cms.string("pt > 10.0 && abs(eta) < 2.5"),
                        filter = cms.bool(False)
                        )

#################################################################################################################################
# Numerator

process.selectedProbesNumMu = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuProbesCharge"),
                        cut = cms.string(process.selectedProbesDenMu.cut.value() + "&& userInt('muonID') > 0.5 && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

elePreID = "(userInt('antiConv') > 0.5 && userFloat('nHits') < 0.5 && userFloat('dxyWrtPV') < 0.02 && userFloat('dzWrtPV') < 0.1 && ((isEB && userFloat('sihih') < 0.01 && userFloat('dEta') < 0.007 && userFloat('dPhi') < 0.15 && userFloat('HoE') < 0.12) || (isEE && userFloat('sihih') < 0.03 && userFloat('dEta') < 0.009 && userFloat('dPhi') < 0.10 && userFloat('HoE') < 0.10)))"

eleIDMVA = "((pt < 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.133) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.465) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.518) || (pt > 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.942) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.947) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.878))"

process.selectedProbesNumEle = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedEleProbesCharge"),
                        cut = cms.string(process.selectedProbesDenEle.cut.value() + "&&" + elePreID + " && " + eleIDMVA),
                        filter = cms.bool(False)
                        )

process.selectedProbesNumTau = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("selectedProbesCharge"),
                        cut = cms.string(selectedProbesDenTau.cut.value() + "&& tauID('decayModeFinding') > 0.5 && tauID('byLooseCombinedIsolationDeltaBetaCorr') > 0.5"),
                        filter = cms.bool(False)
                        )

process.fakeRateDenNum = cms.Sequence(
			process.selectedProbesDenMu + 
			process.selectedProbesNumMu +
			process.selectedProbesDenEle + 
			process.selectedProbesNumEle +
			process.selectedProbesDenTau +
			process.selectedProbesNumTau
			)

#################################################################################################################################
#Plots

process.MuonHistosDenMu = cms.EDAnalyzer("MuonHistManager",
  			muonSrc = cms.untracked.InputTag("selectedProbesDenMu"),
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),                                     
			)

process.MuonHistosNumMu = cms.EDAnalyzer("MuonHistManager",
		  	muonSrc = cms.untracked.InputTag("selectedProbesNumMu"),
		  	vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
		  	MCDist = cms.untracked.vdouble(vecMC),
		 	TrueDist2011 = cms.untracked.vdouble(vecData),
		 	isMC = cms.untracked.bool(False),                                     
			)

process.EleHistosDenEle = cms.EDAnalyzer("ElectronHistManager",
  			electronSrc = cms.untracked.InputTag("selectedProbesDenEle"),
  			muonSrc  = cms.untracked.InputTag("muonVariables"),                                     
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
 		 	MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),
			)

process.EleHistosNumEle = cms.EDAnalyzer("ElectronHistManager",
  			electronSrc = cms.untracked.InputTag("selectedProbesNumEle"),
  			muonSrc  = cms.untracked.InputTag("muonVariables"),                                     
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),
			)

process.TauHistosDenTau = cms.EDAnalyzer("TauHistManager",
  			tauSrc = cms.untracked.InputTag("selectedProbesDenTau"),
  			lep1Src = cms.untracked.InputTag("electronVariables"),
  			lep2Src = cms.untracked.InputTag("muonVariables"),   
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),       
  			isMC = cms.untracked.bool(False),            
			)

process.TauHistosNumTau = cms.EDAnalyzer("TauHistManager",
  			tauSrc = cms.untracked.InputTag("selectedProbesNumTau"),
  			lep1Src = cms.untracked.InputTag("electronVariables"),
  			lep2Src = cms.untracked.InputTag("muonVariables"),   
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),       
  			isMC = cms.untracked.bool(False),            
			)

process.plotSequence = cms.Sequence(
			process.MuonHistosDenMu + 
			process.MuonHistosNumMu + 
			process.EleHistosDenEle + 
			process.EleHistosNumEle +
			process.TauHistosDenTau +
			process.TauHistosNumTau
			)

#################################################################################################################################

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'histo.root'

	)
)

process.mypath = cms.Path(
			process.hltSelection *
			process.selectedPrimaryVertex *
			process.muonSequence *
			process.electronSequence *
			process.tauSequence *
			process.jetSequence *
			process.probeSequence *
			process.fakeRateDenNum *
			process.plotSequence
)

#process.outp1=cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

