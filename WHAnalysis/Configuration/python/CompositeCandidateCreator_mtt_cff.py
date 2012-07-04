import FWCore.ParameterSet.Config as cms

selectedTau1Tau2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausPt1 selectedTausPt2"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

selectedMuTau1Tau2Cand = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTau1Tau2 selectedMuonsIso"),
			 roles = cms.vstring('tau1tau2', 'mu'),
			 cut = cms.string(""),
			 checkCharge = cms.bool(False)
                         )

compositeCandidateSequenceForMTT = cms.Sequence(selectedTau1Tau2 + selectedMuTau1Tau2Cand)
