import FWCore.ParameterSet.Config as cms
from electronHistos_eet_cff import *

#selectedElectronsDeltaR = cms.EDProducer('SelEleByDeltaR',
#     			eleSrc = cms.untracked.InputTag("electronVariables"),
#     			muonSrc = cms.untracked.InputTag("muonVariables"),                             
#     			DeltaRCut = cms.untracked.double(0.3)
#			)

selectedElectronsEta = cms.EDFilter("PATElectronSelector",
                         src = cms.InputTag("electronVariables"),
                         cut = cms.string('abs(eta) < 2.5'),
                         filter = cms.bool(True)
                         )

selectedElectronsCrack = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsEta"),
			#cut = cms.string('!isEBEEGap'),
			cut = cms.string(''),
    			filter = cms.bool(True)
)

############################### FOR VETO ############################### 

simpleCutsWP95 = "(userFloat('nHits')<=1"+ \
                 " && (" + \
                 " (isEB && userFloat('sihih')<0.010 && userFloat('dPhi')<0.80 && "+ \
                 "          userFloat('dEta') <0.007 && userFloat('HoE') <0.15)"   + \
                 " || "  + \
                 " (isEE && userFloat('sihih')<0.030 && userFloat('dPhi')<0.70 && "+ \
                 "          userFloat('dEta') <0.010 && userFloat('HoE') <0.07)"   + \
                 "     )"+ \
                 ")"

selectedElectronsWP95 = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsCrack"),
    			cut = cms.string(simpleCutsWP95 + "&& userFloat('PFRelIsoDB04v2') < 0.3"),
    			filter = cms.bool(False)
)

############################### FOR VETO ############################### 

elePreID = "userInt('antiConv') > 0.5 && userFloat('nHits') < 0.5 && abs(userFloat('dxyWrtPV')) < 0.02 && abs(userFloat('dzWrtPV')) < 0.1 && ((isEB && userFloat('sihih') < 0.01 && userFloat('dEta') < 0.007 && userFloat('dPhi') < 0.15 && userFloat('HoE') < 0.12) || (isEE && userFloat('sihih') < 0.03 && userFloat('dEta') < 0.009 && userFloat('dPhi') < 0.10 && userFloat('HoE') < 0.10))"

selectedElectronsPreID = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsCrack"),
    			#cut = cms.string("userInt('mvaPreselection') > 0.5"),
    			cut = cms.string(elePreID),
    			filter = cms.bool(True)
)

eleIDWW = '(userFloat("nHits") == 0 && userInt("antiConv") > 0.5 && (pt < 20 && (fbrem > 0.15 || (abs(superClusterPosition.Eta) < 1. && eSuperClusterOverP > 0.95)) && ((isEB && userFloat("sihih") < 0.01 && userFloat("dPhi") < 0.03 && userFloat("dEta") < 0.004 && userFloat("HoE") < 0.025) || (isEE && userFloat("sihih") < 0.03 && userFloat("dPhi") < 0.02 && userFloat("dEta") < 0.005 && userFloat("HoE") < 0.025))) || (pt >= 20 && ((isEB && userFloat("sihih") < 0.01 && userFloat("dPhi") < 0.06 && userFloat("dEta") < 0.004 && userFloat("HoE") < 0.04 ) || (isEE && userFloat("sihih") < 0.03 && userFloat("dPhi") < 0.03 && userFloat("dEta") < 0.007 && userFloat("HoE") < 0.025))))'

eleIDMVA = "(pt < 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.133) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.465) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.518) || (pt > 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.942) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.947) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.878)"

selectedElectronsID = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsPreID"),
    			#cut = cms.string(eleIDWW),
			cut = cms.string(eleIDMVA),
    			filter = cms.bool(True)
)

selectedElectronsIso = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsID"),
    			cut = cms.string("userFloat('PFRelIsoDB04v2') < 0.3"),
    			filter = cms.bool(True)
			)

selectedElectronsTrk = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsIso"),
    			cut = cms.string('gsfTrack.isNonnull'),
    			filter = cms.bool(True)
			)

leadSubLeadElectrons = cms.EDProducer('LeadElectronsProducer',
    			lepSrc = cms.untracked.InputTag("selectedElectronsTrk"),                                                               
			)

selectedElectronsPt1 = cms.EDFilter("PATElectronSelector",
			src = cms.InputTag("leadSubLeadElectrons:leadingLeptons"),
                        cut = cms.string('pt > 20.'),
                        filter = cms.bool(True)
                        )

selectedElectronsPt2 = cms.EDFilter("PATElectronSelector",
			src = cms.InputTag("leadSubLeadElectrons:subleadingLeptons"),
                        cut = cms.string('pt > 10.'),
                        filter = cms.bool(True)
                        )

############################### FOR VETO ############################### 

selectedElectronsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedElectronsWP95"),
                     	maxNumber = cms.uint32(2),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
			)

############################### FOR VETO ############################### 


electronSequence = cms.Sequence(#EleHistosBeforeDeltaR *
                                #selectedElectronsDeltaR *
				EleHistosBeforeEleEta *
				selectedElectronsEta *
				EleHistosBeforeEleCrack *
				selectedElectronsCrack *
				EleHistosBeforeEleID *
				selectedElectronsWP95 *
				selectedElectronsPreID *
				EleHistosAfterPreEleID *
				selectedElectronsID *
				EleHistosAfterEleID *
				selectedElectronsIso *
				EleHistosBeforeEleTrk *
				selectedElectronsTrk *
				leadSubLeadElectrons *
				EleHistosBeforeElePt1 *
				selectedElectronsPt1 *
				EleHistosAfterElePt1 *
				EleHistosBeforeElePt2 *
				selectedElectronsPt2 *
				EleHistosAfterElePt2 *
				EleHistosBeforeOneEle *
				selectedElectronsVeto *
				EleHistosBeforeMuonSequence
)
