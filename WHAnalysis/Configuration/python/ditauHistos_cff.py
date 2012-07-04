import FWCore.ParameterSet.Config as cms
from weights_cff import *

DiTauHistosBeforeMET = cms.EDAnalyzer("DiTauHistManager",
       DiTauCand = cms.untracked.InputTag("leptonLowPtTau"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       CoeffPzeta = cms.untracked.double(1.),
       CoeffPzetaVis = cms.untracked.double(-1.5),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
)

DiTauHistosBeforeCharge = cms.EDAnalyzer("DiTauHistManager",
   	DiTauCand = cms.untracked.InputTag("leptonLowPtTau"),
  	PFMetTag = cms.untracked.InputTag('patMETsPF'),    
	CoeffPzeta = cms.untracked.double(1.),
	CoeffPzetaVis = cms.untracked.double(-1.5),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
	isMC = cms.untracked.bool(True),
)

DiTauHistosBeforeDeltaR = cms.EDAnalyzer("DiTauHistManager",
   	DiTauCand = cms.untracked.InputTag("selectedEleTauPairsByCharge:selectedCand1Cand2PairsByCharge"),
  	PFMetTag = cms.untracked.InputTag('patMETsPF'),    
	CoeffPzeta = cms.untracked.double(1.),
	CoeffPzetaVis = cms.untracked.double(-1.5),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
	isMC = cms.untracked.bool(True),
)

DiTauHistosBeforeOnePair = cms.EDAnalyzer("DiTauHistManager",
   	DiTauCand = cms.untracked.InputTag("selectedEleTauPairsDeltaR:selectedCand1Cand2PairsDeltaR"),
  	PFMetTag = cms.untracked.InputTag('patMETsPF'),   
	CoeffPzeta = cms.untracked.double(1.),
	CoeffPzetaVis = cms.untracked.double(-1.5),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
	isMC = cms.untracked.bool(True),
)

DiTauHistosFinalForEleTau = cms.EDAnalyzer("DiTauHistManager",
   	DiTauCand = cms.untracked.InputTag("selectedEleTauPairsDeltaR:selectedCand1Cand2PairsDeltaR"),
  	PFMetTag = cms.untracked.InputTag('patMETsPF'),
	CoeffPzeta = cms.untracked.double(1.),
	CoeffPzetaVis = cms.untracked.double(-1.5),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
	isMC = cms.untracked.bool(True),
)

DiTauHistosFinal = cms.EDAnalyzer("DiTauHistManager",
        DiTauCand = cms.untracked.InputTag("selectedEleTauPairsDeltaR:selectedCand1Cand2PairsDeltaR"),
        PFMetTag = cms.untracked.InputTag('patMETsPF'),
        CoeffPzeta = cms.untracked.double(1.),
        CoeffPzetaVis = cms.untracked.double(-1.5),
        MCDist = cms.untracked.vdouble(vecMC),
        TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

#####################################################################################################################

massEleWTau = cms.EDAnalyzer("DiTauHistManager",
        DiTauCand = cms.untracked.InputTag("eleTauWrong"),
        PFMetTag = cms.untracked.InputTag('patMETsPF'),
        CoeffPzeta = cms.untracked.double(1.),
        CoeffPzetaVis = cms.untracked.double(-1.5),
        MCDist = cms.untracked.vdouble(vecMC),
        TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(False),
)

massEleHTau = cms.EDAnalyzer("DiTauHistManager",
        DiTauCand = cms.untracked.InputTag("eleTauCorrect"),
        PFMetTag = cms.untracked.InputTag('patMETsPF'),
        CoeffPzeta = cms.untracked.double(1.),
        CoeffPzetaVis = cms.untracked.double(-1.5),
        MCDist = cms.untracked.vdouble(vecMC),
        TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(False),
)

massMuonWTau = cms.EDAnalyzer("DiTauHistManager",
        DiTauCand = cms.untracked.InputTag("muonTauWrong"),
        PFMetTag = cms.untracked.InputTag('patMETsPF'),
        CoeffPzeta = cms.untracked.double(1.),
        CoeffPzetaVis = cms.untracked.double(-1.5),
        MCDist = cms.untracked.vdouble(vecMC),
        TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(False),
)

massMuonHTau = cms.EDAnalyzer("DiTauHistManager",
        DiTauCand = cms.untracked.InputTag("muonTauCorrect"),
        PFMetTag = cms.untracked.InputTag('patMETsPF'),
        CoeffPzeta = cms.untracked.double(1.),
        CoeffPzetaVis = cms.untracked.double(-1.5),
        MCDist = cms.untracked.vdouble(vecMC),
        TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(False),
)

massEleLowPtTau = cms.EDAnalyzer("DiTauHistManager",
        DiTauCand = cms.untracked.InputTag("eleLowPtTau"),
        PFMetTag = cms.untracked.InputTag('patMETsPF'),
        CoeffPzeta = cms.untracked.double(1.),
        CoeffPzetaVis = cms.untracked.double(-1.5),
        MCDist = cms.untracked.vdouble(vecMC),
        TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(False),
)

massMuonLowPtTau = cms.EDAnalyzer("DiTauHistManager",
        DiTauCand = cms.untracked.InputTag("muonLowPtTau"),
        PFMetTag = cms.untracked.InputTag('patMETsPF'),
        CoeffPzeta = cms.untracked.double(1.),
        CoeffPzetaVis = cms.untracked.double(-1.5),
        MCDist = cms.untracked.vdouble(vecMC),
        TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(False),
)

massPlotsMcAssignment = cms.Sequence(massEleWTau + massEleHTau + massMuonWTau + massMuonHTau)
massPlotsLowPtLepton = cms.Sequence(massEleLowPtTau + massMuonLowPtTau)

#####################################################################################################################

CompCandHistosBeforeSel = cms.EDAnalyzer('CompositeCandHistManager',
       CompCandSrc = cms.untracked.InputTag("selectedEleTauMuCand"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
)

CompCandHistosAfterSel = cms.EDAnalyzer('CompositeCandHistManager',
       CompCandSrc = cms.untracked.InputTag("selectedEleTauMuCand"),
       PFMetTag = cms.untracked.InputTag('patMETsPF'),
       MCDist = cms.untracked.vdouble(vecMC),
       TrueDist2011 = cms.untracked.vdouble(vecData),
       isMC = cms.untracked.bool(True),
)

