import FWCore.ParameterSet.Config as cms
from electronHistos_ett_cff import *

selectedElectronsDeltaR = cms.EDProducer('SelEleByDeltaR',
     			eleSrc = cms.untracked.InputTag("producesUserDefinedVarsEle"),
     			muonSrc = cms.untracked.InputTag("selectedMuonsIso"),                             
     			DeltaRCut = cms.untracked.double(0.3)
			)

eleMatching = cms.EDFilter("PATElectronSelector",
                         src = cms.InputTag("producesUserDefinedVarsEle"),
                         cut = cms.string("userInt('mcMatch') > 0.5"),
                         filter = cms.bool(True)
                         )

selectedElectronsPt = cms.EDFilter("PATElectronSelector",
                         src = cms.InputTag("electronVariables"),
                         cut = cms.string('pt > 24.'),
                         filter = cms.bool(True)
                         )

selectedElectronsEta = cms.EDFilter("PATElectronSelector",
                         src = cms.InputTag("selectedElectronsPt"),
                         cut = cms.string('abs(eta) < 2.1'),
                         filter = cms.bool(True)
                         )

selectedElectronsCrack = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsEta"),
			#cut = cms.string('!isEBEEGap'),
			cut = cms.string('abs(eta) < 1.4442 || abs(eta) > 1.566'),
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
    			cut = cms.string(simpleCutsWP95 + "&& userFloat('PFRelIsoDB04') < 0.3"),
    			filter = cms.bool(False)
)

selectedElectronsZeeVeto = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("electronVariables"),
    			cut = cms.string("pt > 20. && (abs(eta) < 1.4442 || abs(eta) > 1.566) && abs(eta) < 2.5"),
    			filter = cms.bool(False)
)

############################### FOR VETO ############################### 

elePreID = "userInt('antiConv') > 0.5 && userFloat('nHits') < 0.5 && abs(userFloat('dxyWrtPV')) < 0.02 && abs(userFloat('dzWrtPV')) < 0.1 && ((isEB && userFloat('sihih') < 0.01 && userFloat('dEta') < 0.007 && userFloat('dPhi') < 0.15 && userFloat('HoE') < 0.12) || (isEE && userFloat('sihih') < 0.03 && userFloat('dEta') < 0.009 && userFloat('dPhi') < 0.10 && userFloat('HoE') < 0.10))"

selectedElectronsPreID = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsCrack"),
    			#cut = cms.string("userInt('mvaPreselection') > 0.5"),
    			#cut = cms.string(elePreID),
    			#cut = cms.string("abs(userFloat('dxyWrtPV')) < 0.045 && abs(userFloat('dzWrtPV')) < 0.2"),
    			cut = cms.string("userInt('antiConv') > 0.5 && userFloat('nHits') < 0.5 && abs(userFloat('dxyWrtPV')) < 0.045 && abs(userFloat('dzWrtPV')) < 0.2"),
    			filter = cms.bool(True)
)

eleIDWW = '(userFloat("nHits") == 0 && userInt("antiConv") > 0.5 && (pt < 20 && (fbrem > 0.15 || (abs(superClusterPosition.Eta) < 1. && eSuperClusterOverP > 0.95)) && ((isEB && userFloat("sihih") < 0.01 && userFloat("dPhi") < 0.03 && userFloat("dEta") < 0.004 && userFloat("HoE") < 0.025) || (isEE && userFloat("sihih") < 0.03 && userFloat("dPhi") < 0.02 && userFloat("dEta") < 0.005 && userFloat("HoE") < 0.025))) || (pt >= 20 && ((isEB && userFloat("sihih") < 0.01 && userFloat("dPhi") < 0.06 && userFloat("dEta") < 0.004 && userFloat("HoE") < 0.04 ) || (isEE && userFloat("sihih") < 0.03 && userFloat("dPhi") < 0.03 && userFloat("dEta") < 0.007 && userFloat("HoE") < 0.025))))'

eleIDMVA = "((pt < 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.133) ||" + \
           "(pt < 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.465) ||" + \
           "(pt < 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.518) ||" + \
	   "(pt > 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.942) ||" + \
	   "(pt > 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.947) ||" + \
           "(pt > 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.878))"

EGammaMVALoose = "((pt < 20 && abs(superClusterPosition.Eta) < 0.8 && userFloat('mvaPOGNonTrig') > 0.925) ||" + \
           "(pt < 20 && abs(superClusterPosition.Eta) > 0.8 && abs(superClusterPosition.Eta) < 1.479 && userFloat('mvaPOGNonTrig') > 0.915) ||" + \
           "(pt < 20 && abs(superClusterPosition.Eta) > 1.479 && userFloat('mvaPOGNonTrig') > 0.965) ||" + \
           "(pt > 20 && abs(superClusterPosition.Eta) < 0.8 && userFloat('mvaPOGNonTrig') > 0.905) ||" + \
           "(pt > 20 && abs(superClusterPosition.Eta) > 0.1 && abs(superClusterPosition.Eta) < 1.479 && userFloat('mvaPOGNonTrig') > 0.955) ||" + \
           "(pt > 20 && abs(superClusterPosition.Eta) > 1.479 && userFloat('mvaPOGNonTrig') > 0.975))"

EGammaMVATight = "((pt > 20 && abs(superClusterPosition.Eta) < 0.8 && userFloat('mvaPOGNonTrig') > 0.925) ||" + \
           "(pt > 20 && abs(superClusterPosition.Eta) > 0.8 && abs(superClusterPosition.Eta) < 1.479 && userFloat('mvaPOGNonTrig') > 0.975) ||" + \
           "(pt > 20 && abs(superClusterPosition.Eta) > 1.479 && userFloat('mvaPOGNonTrig') > 0.985))"

selectedElectronsID = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsPreID"),
    			#cut = cms.string(eleIDWW),
			#cut = cms.string(eleIDMVA),
			cut = cms.string(EGammaMVATight),
    			filter = cms.bool(True)
)

selectedElectronsIso = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsID"),
    			#cut = cms.string("userFloat('PFRelIsoDB04v2') < 0.1"),
    			cut = cms.string("(isEB && userFloat('PFRelIsoDB04') < 0.15) || (isEE && userFloat('PFRelIsoDB04') < 0.1)"),
    			filter = cms.bool(True)
)

selectedElectronsTrk = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsIso"),
    			cut = cms.string('gsfTrack.isNonnull'),
    			filter = cms.bool(True)
)

selectedElectronsAdditional = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsIso"),
    			cut = cms.string(''),
    			filter = cms.bool(True)
)

selectedElectronsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedElectronsWP95"),
                     	maxNumber = cms.uint32(1),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
)

############################### FOR VETO ############################### 

selectedEle1Ele2NoCut = cms.EDProducer("CandViewShallowCloneCombiner",
                        decay = cms.string("electronVariables@+ electronVariables@-"),                                     
                        roles = cms.vstring('ele1', 'ele2'),
                        cut =  cms.string("deltaR(daughter(0).eta,daughter(0).phi,daughter(1).eta,daughter(1).phi) > 0.5"),
                        checkCharge = cms.bool(True)
                        )

selectedEle1Ele2 = cms.EDProducer("CandViewShallowCloneCombiner",
                        decay = cms.string("electronVariables@+ electronVariables@-"),                                     
                        roles = cms.vstring('ele1', 'ele2'),
                        #cut =  cms.string("abs(mass-91.1876) < 12.476 && deltaR(daughter(0).eta,daughter(0).phi,daughter(1).eta,daughter(1).phi) > 0.5"),
                        #cut =  cms.string("(abs(mass-91.1876) < 12.476 || abs(((daughter(0).pt - daughter(1).pt)/(daughter(0).pt + daughter(1).pt))) < 0.25) && deltaR(daughter(0).eta,daughter(0).phi,daughter(1).eta,daughter(1).phi) > 0.5"),
			cut =  cms.string("abs(mass-91.1876) < 25 && deltaR(daughter(0).eta,daughter(0).phi,daughter(1).eta,daughter(1).phi) > 0.5"),
                        checkCharge = cms.bool(True)
                        )

selectedEle1Ele2OnePair = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedEle1Ele2"),
                     	maxNumber = cms.uint32(0),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
			)

electronSequence = cms.Sequence(#EleHistosBeforeDeltaR *
                                #selectedElectronsDeltaR *
				#eleMatching *
				EleHistosBeforeElePt *
				selectedElectronsPt *
				EleHistosBeforeEleEta *
				selectedElectronsEta *
				#EleHistosBeforeEleCrack *
				selectedElectronsCrack *
				EleHistosBeforeEleID * #
				selectedElectronsWP95 *
				selectedElectronsZeeVeto *
				selectedElectronsPreID * #
				EleHistosAfterPreEleID *
				selectedElectronsID *
				EleHistosAfterEleID *
				selectedElectronsIso *
				#EleHistosBeforeEleTrk *
				selectedElectronsTrk *
				#EleHistosBeforeOneEle *
				#selectedElectronsVeto *
				selectedElectronsAdditional *
				EleHistosBeforeTauTauPairs
)
