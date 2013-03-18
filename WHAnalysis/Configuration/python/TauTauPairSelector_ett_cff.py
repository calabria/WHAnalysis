import FWCore.ParameterSet.Config as cms
from ditauHistos_ett_cff import *

selectedTauTauPairsDeltaR = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("selectedTau1Tau2"),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

removeSameCand = cms.EDProducer('RemoveSameCand',
			DiTauTag = cms.untracked.InputTag("selectedTauTauPairsDeltaR:selectedCand1Cand2PairsDeltaR"),
			)

selectedTauTauPairsByCharge = cms.EDFilter('ChargeFilter',
			DiTauTag = cms.untracked.InputTag("removeSameCand"),
			ChargeCut = cms.untracked.int32(0),
                        filter = cms.bool(True)
			)

selectedTauTauPairsOnly1Pair = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedTauTauPairsByCharge:selectedCand1Cand2PairsByCharge"),
                     	minNumber = cms.uint32(1),
                     	maxNumber = cms.uint32(30),
                        filter = cms.bool(True)
                     	)

TauTauSequence = cms.Sequence(
			DiTauHistosBeforeDeltaR *
			selectedTauTauPairsDeltaR *
			removeSameCand *
			DiTauHistosBeforeCharge *
			selectedTauTauPairsByCharge *
			DiTauHistosBeforeOnePair *
			selectedTauTauPairsOnly1Pair *
			DiTauHistosFinalForTauTau 
			)

ztautauVeto = cms.EDFilter('ZTauTauVeto',
       			CompCandSrc = cms.untracked.InputTag("selectedEleTau1Tau2Cand"),
        		#PFMetTag = cms.untracked.InputTag('patMETsPF'),
        		PFMetTag = cms.untracked.InputTag('patPFMetByMVA'),
			cosCut1 = cms.untracked.double(-0.5),
			mtCut1 = cms.untracked.double(50),
			cosCut2 = cms.untracked.double(-0.5),
			mtCut2 = cms.untracked.double(50),
        		filter = cms.bool(True)
			)

selectedCompCandUW = cms.EDFilter("CompositeCandFilter",
       			CompCandSrc = cms.untracked.InputTag("ztautauVeto"),
			EtCut = cms.untracked.double(0),
			applyEMuCharge = cms.untracked.bool(False), #Charge (mu1,mu2)
        		filter = cms.bool(False)
			)

selectedCompCandNearZ = cms.EDFilter("ZEleTauVeto",
       			CompCandSrc = cms.untracked.InputTag("selectedEleTau1Tau2Cand"),
			cut = cms.untracked.double(6),
        		filter = cms.bool(True)
			)

#selectedNoEleTauPair = cms.EDFilter("PATCandViewCountFilter",
#                     	src = cms.InputTag("selectedCompCandNearZ"),
#                     	maxNumber = cms.uint32(0),
#                     	minNumber = cms.uint32(0),
#                        filter = cms.bool(True)
#			)

selectedNoEleTauMatch = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedEleTau1Tau2CandZeeStep4"),
                     	maxNumber = cms.uint32(0),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
			)

