import FWCore.ParameterSet.Config as cms

goodMuonMCMatch = cms.EDProducer("MCTruthDeltaRMatcherNew",
     src = cms.InputTag("patMuons"),
     matched = cms.InputTag("genParticles"),
     distMin = cms.double(0.15),
     matchPDGId = cms.vint32( 13 ) # muons
)

goodElectronMCMatch = cms.EDProducer("MCTruthDeltaRMatcherNew",
     src = cms.InputTag("patElectrons"),
     matched = cms.InputTag("genParticles"),
     distMin = cms.double(0.15),
     matchPDGId = cms.vint32( 11 ) # electrons
)

goodTauMCMatch = cms.EDProducer("MCTruthDeltaRMatcherNew",
     src = cms.InputTag("patTaus"),
     matched = cms.InputTag("genParticles"),
     distMin = cms.double(0.15),
     matchPDGId = cms.vint32( 15 ) # taus
)

mcMatchSequence = cms.Sequence(goodMuonMCMatch + goodElectronMCMatch + goodTauMCMatch)
