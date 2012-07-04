import FWCore.ParameterSet.Config as cms
from electronHistos_mtt_cff import *

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

selectedElectronsDeltaR = cms.EDProducer('SelEleByDeltaR',
     			eleSrc = cms.untracked.InputTag("electronVariables"),
     			muonSrc = cms.untracked.InputTag("selectedMuonsIso"),                             
     			DeltaRCut = cms.untracked.double(0.3)
			)

selectedElectronsWP95 = cms.EDFilter("PATElectronSelector",
                         #src = cms.InputTag("selectedElectronsDeltaR:EleSelByDeltaR"),
     			 src = cms.InputTag("electronVariables"),
                         cut = cms.string(simpleCutsWP95 + "&& userFloat('PFRelIsoDB04v2') < 0.3"),
			 #cut = cms.string("pt > 10. && abs(eta) < 2.5 && " + simpleCutsWP95 + "&& userFloat('PFRelIsoDB04v2') < 0.3"),
                         filter = cms.bool(False)
                         )

selectedElectronsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedElectronsWP95"),
                     	maxNumber = cms.uint32(0),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
)


electronSequence = cms.Sequence(EleHistosBeforeDeltaR *
                                #selectedElectronsDeltaR *
				selectedElectronsWP95 *
				selectedElectronsVeto *
				EleHistosBeforeTauSquence
)
