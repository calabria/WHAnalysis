import FWCore.ParameterSet.Config as cms

################### Low Pt Assignment ################### 

eleMuPtAssignment = cms.EDProducer('EleMuPtAssignment',
     			 muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
     			 eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
			 )

leptonLowPt = cms.EDProducer("CandViewMerger",
       			 src = cms.VInputTag("eleMuPtAssignment:eleLowPt", "eleMuPtAssignment:muonLowPt")
  			 )

leptonLowPtTau = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt leptonLowPt"),                                     
                         roles = cms.vstring('tau', 'leptonLowPt'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

######################################################### 

selectedEleTauPairs = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt selectedElectronsTrk"),
			 roles = cms.vstring('tau', 'electron'),
			 cut = cms.string(""),
			 checkCharge = cms.bool(False)
                         )

selectedEleTauMuCand = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedEleTauPairs selectedMuonsIso"),
			 roles = cms.vstring('eletau', 'muon'),
			 cut = cms.string(""),
			 checkCharge = cms.bool(False)
                         )

selectedMuTauPairs = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt selectedMuonsIso"),
			 roles = cms.vstring('tau', 'mu'),
			 cut = cms.string(""),
			 checkCharge = cms.bool(False)
                         )

selectedMuMETPairs = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedMuonsIso patMETsPF"),
			 roles = cms.vstring('muon', 'MET'),
			 cut = cms.string(""),
			 checkCharge = cms.bool(False)
                         )

selectedEleMuPairs = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedMuonsIso selectedElectronsTrk"),                                     
                         roles = cms.vstring('mu', 'electron'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

################### MCTruth Assignment ################### 

mcMatching = cms.EDProducer('MCTruth',
     			genParticles = cms.untracked.InputTag("genParticles"),
     			muonSrc = cms.untracked.InputTag("selectedMuonsIso"),
     			eleSrc = cms.untracked.InputTag("selectedElectronsTrk"),
     			tauSrc = cms.untracked.InputTag("selectedTausHighestPt:TauHighestPt"),
     			deltaR = cms.untracked.double(0.1),
			 )

eleTauWrong = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt mcMatching:EleWGenMatch"),                                     
                         roles = cms.vstring('tau', 'electronW'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

eleTauCorrect = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt mcMatching:EleHGenMatch"),                                     
                         roles = cms.vstring('tau', 'electronH'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

muonTauWrong = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt mcMatching:MuWGenMatch"),                                     
                         roles = cms.vstring('tau', 'muonW'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

muonTauCorrect = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausHighestPt:TauHighestPt mcMatching:MuHGenMatch"),                                     
                         roles = cms.vstring('tau', 'muonH'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )



#####################################################################################################################

compositeCandidateSequence = cms.Sequence((selectedEleTauPairs * selectedEleTauMuCand) + 
					   selectedMuTauPairs + 
					   selectedMuMETPairs + 
					   selectedEleMuPairs
					 )

compositeCandidateSequenceMcAssignment = cms.Sequence(eleTauWrong + eleTauCorrect + muonTauWrong + muonTauCorrect)

compositeCandidateSequenceForEMT = cms.Sequence(eleMuPtAssignment * leptonLowPt * leptonLowPtTau)

