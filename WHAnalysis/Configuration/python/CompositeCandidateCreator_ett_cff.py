import FWCore.ParameterSet.Config as cms

selectedTau1Tau2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausEleVeto selectedTausEleVeto2"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

selectedEleTau1Tau2Cand = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedElectronsTrk selectedTauTauPairsByCharge:selectedCand1Cand2PairsByCharge"),
			 roles = cms.vstring('ele', 'tau1tau2'),
			 cut = cms.string(""),
			 checkCharge = cms.bool(False)
                         )

compositeCandidateSequenceForETT = cms.Sequence(selectedTau1Tau2 + selectedEleTau1Tau2Cand)
