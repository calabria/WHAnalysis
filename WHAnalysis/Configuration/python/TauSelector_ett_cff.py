import FWCore.ParameterSet.Config as cms
from tauHistos_ett_cff import *

selectedTausByDeltaR = cms.EDProducer("EleEleSelTauByDeltaR",
     			tauSrc = cms.untracked.InputTag("producesUserDefinedVarsTau"),
     			lep1Src = cms.untracked.InputTag("selectedElectronsWP95"),
     			lep2Src = cms.untracked.InputTag("selectedElectronsWP95"),                             
     			DeltaRCut = cms.untracked.double(0.5)
			)

deltaRCut = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
                         cut = cms.string('pt > 0.0'),
                         filter = cms.bool(True)
                         )

leadSubLeadTaus = cms.EDProducer('LeadTausProducer',
    			 lepSrc = cms.untracked.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),                                                               
			 )

################################ TAU1 ################################ 

selectedTausPt1 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
                         cut = cms.string('pt > 25.0'),
                         filter = cms.bool(True)
                         )

selectedTausEta = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausPt1"),
                         #cut = cms.string('abs(eta) < 2.5 && !(1.4442 < abs(eta) < 1.566)'),
                         cut = cms.string("abs(eta) < 2.3 && abs(userFloat('dzWrtPV')) < 0.2"),
                         filter = cms.bool(True)
                         )

selectedTausID = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausEta"),
                         cut = cms.string('tauID("decayModeFinding") > 0.5'),
                         filter = cms.bool(True)
                        )

selectedTausIso = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausID"),
                         cut = cms.string('tauID("byTightCombinedIsolationDeltaBetaCorr") > 0.5'),
                         filter = cms.bool(True)
                        )

selectedTausMuonVeto = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausIso"),
                         cut = cms.string('tauID("againstMuonTight") > 0.5'),
                         filter = cms.bool(True)
                        )

selectedTausEleVeto = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausMuonVeto"),
                         cut = cms.string('tauID("againstElectronMVA") > 0.5'),
                         #cut = cms.string('tauID("againstElectronLoose") > 0.5'),
                         filter = cms.bool(True)
                        )

#selectedTausHighestPt = cms.EDProducer("LeptonHighestPt",
#    			tauSrc = cms.untracked.InputTag("selectedTausEleVeto")
#  			)

################################ TAU2 ################################ 

skimmedPairsPre2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausEleVeto selectedTausByDeltaR:TauSelByDeltaR"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

skimmedPairsDeltaRPre2 = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("skimmedPairsPre2"),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

selectedTausPt2 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
                         cut = cms.string('pt > 20.0'),
                         filter = cms.bool(True)
                         )

skimmedPairsPt2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausEleVeto selectedTausPt2"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

skimmedPairsDeltaRPt2 = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("skimmedPairsPt2"),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

##################################################################### 

selectedTausEta2 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausPt2"),
                         #cut = cms.string('abs(eta) < 2.5 && !(1.4442 < abs(eta) < 1.566)'),
                         cut = cms.string("abs(eta) < 2.3 && abs(userFloat('dzWrtPV')) < 0.2"),
                         filter = cms.bool(True)
                         )

skimmedPairsEta2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausEleVeto selectedTausEta2"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

skimmedPairsDeltaREta2 = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("skimmedPairsEta2"),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

##################################################################### 

selectedTausID2 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausEta2"),
                         cut = cms.string('tauID("decayModeFinding") > 0.5'),
                         filter = cms.bool(True)
                        )

skimmedPairsID2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausEleVeto selectedTausID2"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

skimmedPairsDeltaRID2 = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("skimmedPairsID2"),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

##################################################################### 

selectedTausIso2 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausID2"),
                         cut = cms.string('tauID("byMediumCombinedIsolationDeltaBetaCorr") > 0.5'),
                         filter = cms.bool(True)
                        )

skimmedPairsIso2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausEleVeto selectedTausIso2"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

skimmedPairsDeltaRIso2 = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("skimmedPairsIso2"),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

##################################################################### 

selectedTausMuonVeto2 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausIso2"),
                         cut = cms.string('tauID("againstMuonTight") > 0.5'),
                         filter = cms.bool(True)
                        )

skimmedPairsMuVeto2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausEleVeto selectedTausMuonVeto2"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

skimmedPairsDeltaRMuVeto2 = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("skimmedPairsMuVeto2"),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

##################################################################### 

selectedTausEleVeto2 = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("selectedTausMuonVeto2"),
                         cut = cms.string('tauID("againstElectronMVA") > 0.5'),
                         #cut = cms.string('tauID("againstElectronMedium") > 0.5'),
                         filter = cms.bool(True)
                        )

skimmedPairsEleVeto2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("selectedTausEleVeto selectedTausEleVeto2"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

skimmedPairsDeltaREleVeto2 = cms.EDFilter('DeltaRFilter',
			DiTauTag = cms.untracked.InputTag("skimmedPairsEleVeto2"),
			DeltaRCut = cms.untracked.double(0.5),
                        filter = cms.bool(True)
			)

##################################################################### 

#subtractTaus = cms.EDProducer('TauVetoProducer',
#			lep1Src = cms.untracked.InputTag("selectedTausEleVeto2"), #collezione grande
#			lep2Src = cms.untracked.InputTag("selectedTausHighestPt"), #collezione piccola
#			)

#selectedTausHighestPt2 = cms.EDProducer("LeptonHighestPt",
#    			tauSrc = cms.untracked.InputTag("subtractTaus")
#  			)

tauSequence = cms.Sequence(TauHistosBeforeDeltaR *
			   selectedTausByDeltaR *
			   deltaRCut *
			   #leadSubLeadTaus *
			   #TAU1
			   TauHistosBeforeTauPt1 *
			   selectedTausPt1 *
			   TauHistosBeforeTauEta *
			   selectedTausEta *
			   TauHistosBeforeTauID *
			   selectedTausID *
			   TauHistosBeforeTauIso *
			   selectedTausIso *
			   TauHistosBeforeMuonVeto *
			   selectedTausMuonVeto *
			   TauHistosBeforeEleVeto *
			   selectedTausEleVeto *
			   TauHistosAfterTau1Sequence *
			   #selectedTausHighestPt *
			   #TAU2
				skimmedPairsPre2 *
				skimmedPairsDeltaRPre2 *
			   TauHistosBeforeTauPt2 *
			   selectedTausPt2 *
				skimmedPairsPt2 *
				skimmedPairsDeltaRPt2 *
			   TauHistosBeforeTauEta2 *
			   selectedTausEta2 *
				skimmedPairsEta2 *
				skimmedPairsDeltaREta2 *
			   TauHistosBeforeTauID2 *
			   selectedTausID2 *
				skimmedPairsID2 *
				skimmedPairsDeltaRID2 *
			   TauHistosBeforeTauIso2 *
			   selectedTausIso2 *
				skimmedPairsIso2 *
				skimmedPairsDeltaRIso2 *
			   TauHistosBeforeMuonVeto2 *
			   selectedTausMuonVeto2 *
				skimmedPairsMuVeto2 *
				skimmedPairsDeltaRMuVeto2 *
			   TauHistosBeforeEleVeto2 *
			   selectedTausEleVeto2 *
				skimmedPairsEleVeto2 *
				skimmedPairsDeltaREleVeto2 *
			   TauHistosAfterTau2Sequence 
			   #subtractTaus * 
			   #selectedTausHighestPt2
)
