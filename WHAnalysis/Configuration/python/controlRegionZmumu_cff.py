import FWCore.ParameterSet.Config as cms
from WHAnalysis.Configuration.weights_cff import *

#################################################################################################################################
# Trigger

hltSelection = cms.EDFilter("TriggerFilter",
                        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                        HLTPaths = cms.vstring("HLT_DoubleMu7_v","HLT_Mu13_Mu8_v","HLT_Mu17_Mu8_v"),
			defaultTrigger = cms.string("HLT_DoubleMu7_v"),
                        hltEventRanges = cms.VEventRange("160431:MIN-163869:MAX","165088:MIN-178380:MAX","178420:MIN-180252:MAX"),
                        filter = cms.bool(True)
                        )

#################################################################################################################################
# Vertex

selectedPrimaryVertex = cms.EDFilter("GoodVertexFilter",
                        vertexCollection = cms.InputTag('offlinePrimaryVerticesWithBS'),
                        minimumNDOF = cms.uint32(7) ,
                        maxAbsZ = cms.double(24),	
                        maxd0 = cms.double(2),
                 	filter = cms.bool(True)	
                        )

#################################################################################################################################
# Muon

producesUserDefinedVarsMu = cms.EDProducer('MuonAddUserVariables',
    			objects = cms.InputTag("muonVariables"),
    			met = cms.InputTag("patMETsPF"),
    			triggerResults = cms.InputTag("patTriggerEvent"),
  			triggerPaths = cms.vstring("HLT_DoubleMu7_v","HLT_Mu13_Mu8_v","HLT_Mu17_Mu8_v"), 
  			triggerObjNamesLeg1 =cms.vstring("hltDiMuonL3PreFiltered7","hltSingleMu13L3Filtered13","hltL1Mu3EG5L3Filtered17"), 
  			triggerObjNamesLeg2 = cms.vstring("hltDiMuonL3PreFiltered7","hltDiMuonL3PreFiltered8","hltDiMuonL3PreFiltered8"), 
  			hltEventRanges = cms.VEventRange("160431:MIN-163869:MAX","165088:MIN-178380:MAX","178420:MIN-180252:MAX")
			)

selectedMuonsForZmumu = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("producesUserDefinedVarsMu"),
                        cut = cms.string("abs(eta) < 2.1 && userInt('muonID') > 0.5 && userFloat('PFRelIsoDB04v2') < 0.1"),
                        filter = cms.bool(True)
                        )

selectedMuonsForVeto = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("producesUserDefinedVarsMu"),
                        cut = cms.string("pt > 5. && abs(eta) < 2.1 && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

leadSubLeadMuons = cms.EDProducer('LeadMuonsProducer',
    			lepSrc = cms.untracked.InputTag("selectedMuonsForZmumu"),                                                               
			)

selectedMuonsPt1 = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("leadSubLeadMuons:leadingLeptons"),
                        cut = cms.string('pt > 20.'),
                        filter = cms.bool(True)
                        )

selectedMuonsPt2 = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("leadSubLeadMuons:subleadingLeptons"),
                        cut = cms.string('pt > 10.'),
                        filter = cms.bool(True)
                        )

selectedMuonsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedMuonsForVeto"),
                     	maxNumber = cms.uint32(2),
                       	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
                     	)

MuonHistosCheck = cms.EDAnalyzer("MuonHistManager",
  			muonSrc = cms.untracked.InputTag("selectedMuonsPt2"),
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),                                     
			)

muonSequence = cms.Sequence(
			producesUserDefinedVarsMu *
			selectedMuonsForZmumu *
		  	selectedMuonsForVeto *
			leadSubLeadMuons *
			selectedMuonsPt1 *
			selectedMuonsPt2 *
			#selectedMuonsVeto *
			MuonHistosCheck
			)

#################################################################################################################################
# Electrons

producesUserDefinedVarsEle = cms.EDProducer('ElectronAddUserVariables',
    			objects = cms.InputTag("electronVariables"),
    			met = cms.InputTag("patMETsPF"),
    			triggerResults = cms.InputTag("patTriggerEvent"),
  			triggerPaths = cms.vstring("HLT_Mu17_Ele8_CaloIdL_v","HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_v"), 
  			triggerObjNamesLeg1 =cms.vstring("hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter","hltMu17Ele8CaloIdTPixelMatchFilter"), 
  			triggerObjNamesLeg2 = cms.vstring("hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter","hltMu17Ele8CaloIdTPixelMatchFilter"),
  			hltEventRanges = cms.VEventRange("160431:MIN-176469:MAX","176545:MIN-180252:MAX")
			)

selectedElectronsForVeto = cms.EDFilter("PATElectronSelector",
     			src = cms.InputTag("producesUserDefinedVarsEle"),
                        cut = cms.string("pt > 10. && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

selectedElectronsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedElectronsForVeto"),
                     	maxNumber = cms.uint32(0),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
			)

electronSequence = cms.Sequence(
			producesUserDefinedVarsEle *
			selectedElectronsForVeto 
			#selectedElectronsVeto
			)

#################################################################################################################################
# Taus

selectedTausForVeto = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("tauVariables"),
                        cut = cms.string("pt > 20.0 && abs(eta) < 2.5 && tauID('decayModeFinding') > 0.5 && tauID('byLooseCombinedIsolationDeltaBetaCorr') > 0.5"),
                        filter = cms.bool(False)
                        )

selectedTausVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedTausForVeto"),
                     	maxNumber = cms.uint32(0),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
			)

tauSequence = cms.Sequence(
			selectedTausForVeto 
			#selectedTausVeto
			)

#################################################################################################################################
# Jets

selectedPatJetsForVeto = cms.EDFilter("PATJetSelector",
    			src = cms.InputTag("patJetsAK5PF"),                                                               
    			cut = cms.string("et > 20. && abs(eta) < 2.5 && bDiscriminator('trackCountingHighEffBJetTags') > 3.3"), 
    			filter = cms.bool(False)
			)

selectedJetsVeto = cms.EDFilter("PATCandViewCountFilter",
    			src = cms.InputTag("selectedPatJetsForVeto"),
     			maxNumber = cms.uint32(0),
     			minNumber = cms.uint32(0),
     			filter = cms.bool(True)
			)

jetSequence = cms.Sequence(
			selectedPatJetsForVeto *
			selectedJetsVeto
			)

#################################################################################################################################
# Zmumu

selectedMu1Mu2 = cms.EDProducer("CandViewShallowCloneCombiner",
                        decay = cms.string("selectedMuonsPt1 selectedMuonsPt2"),                                     
                        roles = cms.vstring('mu1', 'mu2'),
                        cut =  cms.string("mass > 85 && mass < 95"),
                        checkCharge = cms.bool(False)
                        )

selectedMu1Mu2Charge = cms.EDFilter("ChargeFilter",
			DiTauTag = cms.untracked.InputTag("selectedMu1Mu2"),
			ChargeCut = cms.untracked.int32(0),
                        filter = cms.bool(True)
			)

selectedMETMax = cms.EDFilter("PATMETSelector",
     			src = cms.InputTag("patMETsPF"),
     			cut = cms.string('et < 20'),
     			filter = cms.bool(True)
			)

DiTauHistosZmumu = cms.EDAnalyzer("DiTauHistManager",
       			DiTauCand = cms.untracked.InputTag("selectedMu1Mu2"),
       			PFMetTag = cms.untracked.InputTag('patMETsPF'),
       			CoeffPzeta = cms.untracked.double(1.),
       			CoeffPzetaVis = cms.untracked.double(-1.5),
       			MCDist = cms.untracked.vdouble(vecMC),
       			TrueDist2011 = cms.untracked.vdouble(vecData),
       			isMC = cms.untracked.bool(False),
			)

zmumuSequence = cms.Sequence(
			selectedMu1Mu2 *
			selectedMu1Mu2Charge *
			selectedMETMax *
			DiTauHistosZmumu
			)

#################################################################################################################################
# Jet Probe

selectedProbes1 = cms.EDProducer('MuonVetoProducer',
			lep1Src = cms.untracked.InputTag("producesUserDefinedVarsMu"), #collezione grande
			lep2Src = cms.untracked.InputTag("selectedMuonsPt1"), #collezione piccola
)

selectedProbes2 = cms.EDProducer('MuonVetoProducer',
			lep1Src = cms.untracked.InputTag("selectedProbes1"), #collezione grande
			lep2Src = cms.untracked.InputTag("selectedMuonsPt2"), #collezione piccola
)

selectedMuProbesMT = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedProbes2"),
                        cut = cms.string("userFloat('Mt') < 20."),
                        filter = cms.bool(True)
                        )

selectedEleProbesMT = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("producesUserDefinedVarsEle"),
                        cut = cms.string("userFloat('Mt') < 20."),
                        filter = cms.bool(True)
                        )

probeSequence = cms.Sequence(
			selectedProbes1 * 
			selectedProbes2 *
			selectedMuProbesMT *
			selectedEleProbesMT
			)

#################################################################################################################################
# Denominator

selectedProbesDenMu = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuProbesMT"),
                        cut = cms.string("pt > 9. && abs(eta) < 2.1 && (isGlobalMuon || isTrackerMuon) && globalTrack.isNonnull && globalTrack.hitPattern.numberOfValidPixelHits >= 1"),
                        filter = cms.bool(False)
                        )

selectedProbesDenEle = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedEleProbesMT"),
                        cut = cms.string("pt > 9. && abs(eta) < 2.5 && userFloat('nHits') <= 1 && userInt('antiConv') > 0.5"),
                        filter = cms.bool(False)
                        )

selectedProbesDenTau = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("tauVariables"),
                        cut = cms.string("pt > 10.0 && abs(eta) < 2.5"),
                        filter = cms.bool(False)
                        )

#################################################################################################################################
# Numerator

selectedProbesNumMu = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuProbesMT"),
                        cut = cms.string(selectedProbesDenMu.cut.value() + "&& userInt('muonID') > 0.5 && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

elePreID = "(userInt('antiConv') > 0.5 && userFloat('nHits') < 0.5 && userFloat('dxyWrtPV') < 0.02 && userFloat('dzWrtPV') < 0.1 && ((isEB && userFloat('sihih') < 0.01 && userFloat('dEta') < 0.007 && userFloat('dPhi') < 0.15 && userFloat('HoE') < 0.12) || (isEE && userFloat('sihih') < 0.03 && userFloat('dEta') < 0.009 && userFloat('dPhi') < 0.10 && userFloat('HoE') < 0.10)))"

eleIDMVA = "((pt < 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.133) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.465) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.518) || (pt > 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.942) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.947) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.878))"

selectedProbesNumEle = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedEleProbesMT"),
                        cut = cms.string(selectedProbesDenEle.cut.value() + "&&" + elePreID + " && " + eleIDMVA),
                        filter = cms.bool(False)
                        )

selectedProbesNumTau = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("tauVariables"),
                        cut = cms.string(selectedProbesDenTau.cut.value() + "&& tauID('decayModeFinding') > 0.5 && tauID('byLooseCombinedIsolationDeltaBetaCorr') > 0.5"),
                        filter = cms.bool(False)
                        )

fakeRateDenNum = cms.Sequence(
			selectedProbesDenMu + 
			selectedProbesNumMu +
			selectedProbesDenEle + 
			selectedProbesNumEle +
			selectedProbesDenTau + 
			selectedProbesNumTau
			)

#################################################################################################################################
#Plots

MuonHistosDenMu = cms.EDAnalyzer("MuonHistManager",
  			muonSrc = cms.untracked.InputTag("selectedProbesDenMu"),
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),                                     
			)

MuonHistosNumMu = cms.EDAnalyzer("MuonHistManager",
		  	muonSrc = cms.untracked.InputTag("selectedProbesNumMu"),
		  	vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
		  	MCDist = cms.untracked.vdouble(vecMC),
		 	TrueDist2011 = cms.untracked.vdouble(vecData),
		 	isMC = cms.untracked.bool(False),                                     
			)

EleHistosDenEle = cms.EDAnalyzer("ElectronHistManager",
  			electronSrc = cms.untracked.InputTag("selectedProbesDenEle"),
  			muonSrc  = cms.untracked.InputTag("muonVariables"),                                     
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
 		 	MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),
			)

EleHistosNumEle = cms.EDAnalyzer("ElectronHistManager",
  			electronSrc = cms.untracked.InputTag("selectedProbesNumEle"),
  			muonSrc  = cms.untracked.InputTag("muonVariables"),                                     
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),
			)

TauHistosDenTau = cms.EDAnalyzer("TauHistManager",
  			tauSrc = cms.untracked.InputTag("selectedProbesDenTau"),
  			lep1Src = cms.untracked.InputTag("electronVariables"),
  			lep2Src = cms.untracked.InputTag("muonVariables"),   
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),       
  			isMC = cms.untracked.bool(False),            
			)

TauHistosNumTau = cms.EDAnalyzer("TauHistManager",
  			tauSrc = cms.untracked.InputTag("selectedProbesNumTau"),
  			lep1Src = cms.untracked.InputTag("electronVariables"),
  			lep2Src = cms.untracked.InputTag("muonVariables"),   
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),       
  			isMC = cms.untracked.bool(False),            
			)

plotSequence = cms.Sequence(
			MuonHistosDenMu + 
			MuonHistosNumMu + 
			EleHistosDenEle + 
			EleHistosNumEle +
			TauHistosDenTau + 
			TauHistosNumTau
			)

#################################################################################################################################

zmumuSequence = cms.Sequence(
			hltSelection *
			selectedPrimaryVertex *
			muonSequence *
			electronSequence *
			tauSequence *
			jetSequence *
			zmumuSequence *
			probeSequence *
			fakeRateDenNum *
			plotSequence
			)

