import FWCore.ParameterSet.Config as cms
from ditauHistos_mmt_cff import *

selectedMuTauPairsByCharge = cms.EDFilter('ChargeFilter',
			DiTauTag = cms.untracked.InputTag('selectedMu2Tau'),
			ChargeCut = cms.untracked.int32(0),
                        filter = cms.bool(True)
			)

selectedMuTauPairsDeltaR = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag('selectedMuTauPairsByCharge:selectedCand1Cand2PairsByCharge'),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

selectedMuTauPairsOnly1Pair = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedMuTauPairsDeltaR:selectedCand1Cand2PairsDeltaR"),
                     	minNumber = cms.uint32(1),
                     	maxNumber = cms.uint32(1),
                        filter = cms.bool(True)
                     	)

muTauSequence = cms.Sequence(
			DiTauHistosBeforeCharge *
			selectedMuTauPairsByCharge *
			DiTauHistosBeforeDeltaR *
			selectedMuTauPairsDeltaR *
			DiTauHistosBeforeOnePair *
			selectedMuTauPairsOnly1Pair *
			DiTauHistosFinalForMuTau 
)

selectedCompCandUW = cms.EDFilter("CompositeCandFilter",
       			CompCandSrc = cms.untracked.InputTag("selectedMu2TauMu1Cand"),
			EtCut = cms.untracked.double(80),
			applyEMuCharge = cms.untracked.bool(True), #Charge (mu1,mu2)
        		filter = cms.bool(True)
			)
