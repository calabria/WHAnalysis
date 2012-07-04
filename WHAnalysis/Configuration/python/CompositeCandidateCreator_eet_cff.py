import FWCore.ParameterSet.Config as cms

selectedEle2Tau = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt selectedElectronsPt2"),                                     
                         roles = cms.vstring('tau', 'ele2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

selectedEle1Tau = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt selectedElectronsPt1"),                                     
                         roles = cms.vstring('tau', 'ele1'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

selectedEle2TauEle1Cand = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedEle2Tau selectedElectronsPt1"),
			 roles = cms.vstring('ele2tau', 'ele1'),
			 cut = cms.string(""),
			 checkCharge = cms.bool(False)
                         )

compositeCandidateSequenceForEET = cms.Sequence(selectedEle1Tau + selectedEle2Tau + selectedEle2TauEle1Cand)
