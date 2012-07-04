import FWCore.ParameterSet.Config as cms
from ditauHistos_cff import *

selectedEleTauPairsByCharge = cms.EDFilter('ChargeFilter',
			DiTauTag = cms.untracked.InputTag('leptonLowPtTau'),
			ChargeCut = cms.untracked.int32(0),
                        filter = cms.bool(True)
			)

selectedEleTauPairsDeltaR = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag('selectedEleTauPairsByCharge:selectedCand1Cand2PairsByCharge'),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

selectedEleTauPairsOnly1Pair = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedEleTauPairsDeltaR:selectedCand1Cand2PairsDeltaR"),
                     	minNumber = cms.uint32(1),
                     	maxNumber = cms.uint32(1),
                        filter = cms.bool(True)
                     	)

eleTauSequence = cms.Sequence(
			DiTauHistosBeforeCharge *
			selectedEleTauPairsByCharge *
			DiTauHistosBeforeDeltaR *
			selectedEleTauPairsDeltaR *
			DiTauHistosBeforeOnePair *
			selectedEleTauPairsOnly1Pair *
			DiTauHistosFinalForEleTau 
			)

selectedCompCandUW = cms.EDFilter("CompositeCandFilter",
       			CompCandSrc = cms.untracked.InputTag("selectedEleTauMuCand"),
			EtCut = cms.untracked.double(80),
			applyEMuCharge = cms.untracked.bool(True),
        		filter = cms.bool(True)
			)
