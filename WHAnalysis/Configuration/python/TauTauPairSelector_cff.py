import FWCore.ParameterSet.Config as cms
from ditauHistos_mtt_cff import *

selectedTauTauPairsByCharge = cms.EDFilter('ChargeFilter',
			DiTauTag = cms.untracked.InputTag('selectedTau1Tau2'),
			ChargeCut = cms.untracked.int32(0),
                        filter = cms.bool(True)
			)

selectedTauTauPairsDeltaR = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag('selectedTauTauPairsByCharge:selectedCand1Cand2PairsByCharge'),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

selectedTauTauPairsOnly1Pair = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedTauTauPairsDeltaR:selectedCand1Cand2PairsDeltaR"),
                     	minNumber = cms.uint32(1),
                     	maxNumber = cms.uint32(1),
                        filter = cms.bool(True)
                     	)

TauTauSequence = cms.Sequence(
			DiTauHistosBeforeCharge *
			selectedTauTauPairsByCharge *
			DiTauHistosBeforeDeltaR *
			selectedTauTauPairsDeltaR *
			DiTauHistosBeforeOnePair *
			selectedTauTauPairsOnly1Pair *
			DiTauHistosFinalForTauTau 
			)

selectedCompCandUW = cms.EDFilter("CompositeCandFilter",
       			CompCandSrc = cms.untracked.InputTag("selectedMuTau1Tau2Cand"),
			EtCut = cms.untracked.double(80),
			applyEMuCharge = cms.untracked.bool(True), #Charge (mu1,mu2)
        		filter = cms.bool(True)
			)
