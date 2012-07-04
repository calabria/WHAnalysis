import FWCore.ParameterSet.Config as cms

selectedMu2Tau = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt selectedMuonsPt2"),                                     
                         roles = cms.vstring('tau', 'mu2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

selectedMu1Tau = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt selectedMuonsPt1"),                                     
                         roles = cms.vstring('tau', 'mu1'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

selectedMu2TauMu1Cand = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedMu2Tau selectedMuonsPt1"),
			 roles = cms.vstring('mu2tau', 'mu1'),
			 cut = cms.string(""),
			 checkCharge = cms.bool(False)
                         )

compositeCandidateSequenceForMMT = cms.Sequence(selectedMu1Tau + selectedMu2Tau + selectedMu2TauMu1Cand)
