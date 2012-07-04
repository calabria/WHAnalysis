import FWCore.ParameterSet.Config as cms
from weights_cff import *

DiTauHistosBeforeMET = cms.EDAnalyzer("DiTauHistManager",
       DiTauCand = cms.untracked.InputTag("selectedTau1Tau2"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       CoeffPzeta = cms.untracked.double(1.),
       CoeffPzetaVis = cms.untracked.double(-1.5),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
)

DiTauHistosBeforeDeltaR = cms.EDAnalyzer("DiTauHistManager",
   	DiTauCand = cms.untracked.InputTag("selectedTau1Tau2"),
  	PFMetTag = cms.untracked.InputTag('patMETsPF'),    
	CoeffPzeta = cms.untracked.double(1.),
	CoeffPzetaVis = cms.untracked.double(-1.5),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
	isMC = cms.untracked.bool(True),
)

DiTauHistosBeforeCharge = cms.EDAnalyzer("DiTauHistManager",
   	DiTauCand = cms.untracked.InputTag("removeSameCand"),
  	PFMetTag = cms.untracked.InputTag('patMETsPF'),    
	CoeffPzeta = cms.untracked.double(1.),
	CoeffPzetaVis = cms.untracked.double(-1.5),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
	isMC = cms.untracked.bool(True),
)

DiTauHistosBeforeOnePair = cms.EDAnalyzer("DiTauHistManager",
   	DiTauCand = cms.untracked.InputTag("selectedTauTauPairsByCharge:selectedCand1Cand2PairsByCharge"),
  	PFMetTag = cms.untracked.InputTag('patMETsPF'),   
	CoeffPzeta = cms.untracked.double(1.),
	CoeffPzetaVis = cms.untracked.double(-1.5),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
	isMC = cms.untracked.bool(True),
)

DiTauHistosFinalForTauTau = cms.EDAnalyzer("DiTauHistManager",
   	DiTauCand = cms.untracked.InputTag("selectedTauTauPairsByCharge:selectedCand1Cand2PairsByCharge"),
  	PFMetTag = cms.untracked.InputTag('patMETsPF'),
	CoeffPzeta = cms.untracked.double(1.),
	CoeffPzetaVis = cms.untracked.double(-1.5),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
	isMC = cms.untracked.bool(True),
)

DiTauHistosFinal = cms.EDAnalyzer("DiTauHistManager",
        DiTauCand = cms.untracked.InputTag("selectedTauTauPairsByCharge:selectedCand1Cand2PairsByCharge"),
        PFMetTag = cms.untracked.InputTag('patMETsPF'),
        CoeffPzeta = cms.untracked.double(1.),
        CoeffPzetaVis = cms.untracked.double(-1.5),
        MCDist = cms.untracked.vdouble(vecMC),
        TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

#####################################################################################################################

CompCandHistosBeforeSel = cms.EDAnalyzer('CompositeCandHistManager',
       CompCandSrc = cms.untracked.InputTag("selectedEleTau1Tau2Cand"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
       isFR = cms.untracked.bool(False),
)

CompCandHistosBeforeZttVeto = cms.EDAnalyzer('CompositeCandHistManager',
       CompCandSrc = cms.untracked.InputTag("selectedEleTau1Tau2Cand"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
       isFR = cms.untracked.bool(False),
)

CompCandHistosAfterSel = cms.EDAnalyzer('CompositeCandHistManager',
       CompCandSrc = cms.untracked.InputTag("ztautauVeto"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
       isFR = cms.untracked.bool(False),
)

#####################################################################################################################

eePairsVeto = cms.EDAnalyzer("DiTauHistManager",
       DiTauCand = cms.untracked.InputTag("selectedEle1Ele2"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       CoeffPzeta = cms.untracked.double(1.),
       CoeffPzetaVis = cms.untracked.double(-1.5),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
)

eePairsVetoNoCut = cms.EDAnalyzer("DiTauHistManager",
       DiTauCand = cms.untracked.InputTag("selectedEle1Ele2NoCut"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       CoeffPzeta = cms.untracked.double(1.),
       CoeffPzetaVis = cms.untracked.double(-1.5),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
)

eePairsVetoAfterSel = cms.EDAnalyzer("DiTauHistManager",
       DiTauCand = cms.untracked.InputTag("selectedEle1Ele2NoCut"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       CoeffPzeta = cms.untracked.double(1.),
       CoeffPzetaVis = cms.untracked.double(-1.5),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
)
