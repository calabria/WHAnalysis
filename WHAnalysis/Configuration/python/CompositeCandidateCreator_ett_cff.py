import FWCore.ParameterSet.Config as cms

selectedTau1Tau2 = cms.EDProducer("CandViewShallowCloneCombiner",
	decay = cms.string("selectedTausEleVeto selectedTausEleVeto2"),
	roles = cms.vstring('tau1', 'tau2'),
	cut =  cms.string(""),
	checkCharge = cms.bool(False)
      	)

selLongDist = "(abs(daughter('ele').vz - daughter('tau1tau2').daughter(0).vz) < 0.14 && abs(daughter('ele').vz - daughter('tau1tau2').daughter(1).vz) < 0.14)"

selectedEleTau1Tau2Cand = cms.EDProducer("CandViewShallowCloneCombiner",
	decay = cms.string("selectedElectronsTrk selectedTauTauPairsByCharge:selectedCand1Cand2PairsByCharge"),
	roles = cms.vstring('ele', 'tau1tau2'),
	cut = cms.string(selLongDist),
	checkCharge = cms.bool(False)
  	)

isOS1 = "(daughter('ele').charge*daughter('tau1tau2').daughter(0).charge < 0 && deltaR(daughter('ele').eta,daughter('ele').phi,daughter('tau1tau2').daughter(0).eta,daughter('tau1tau2').daughter(0).phi) < 0.01)"

isOS2 = "(daughter('ele').charge*daughter('tau1tau2').daughter(1).charge < 0 && deltaR(daughter('ele').eta,daughter('ele').phi,daughter('tau1tau2').daughter(1).eta,daughter('tau1tau2').daughter(1).phi) < 0.01)"

selectedEleTau1Tau2CandZeeStep4 = cms.EDProducer("CandViewShallowCloneCombiner",
	decay = cms.string("selectedElectronsTrk selectedTauTauPairsByCharge:selectedCand1Cand2PairsByCharge"),
	roles = cms.vstring('ele', 'tau1tau2'),
	cut = cms.string(selLongDist + " && (" + isOS1 + " || " + isOS1 + ")"),
	checkCharge = cms.bool(False)
  	)

compositeCandidateSequenceForETT = cms.Sequence(selectedTau1Tau2 + selectedEleTau1Tau2Cand)
