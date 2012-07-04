import FWCore.ParameterSet.Config as cms
from jetHistos_cff import *

selectedPatJetsEt20 = cms.EDFilter("JetFilter",
    jetSrc = cms.untracked.InputTag("patJetsAK5PF"),                                                               
    cut = cms.untracked.string('et > 20.'), 
    filter = cms.bool(True)
)

selectedPatJetsEta = cms.EDFilter("JetFilter",
    jetSrc = cms.untracked.InputTag("selectedPatJetsEt20:selectedPatJetsForWH"),                                                               
    cut = cms.untracked.string('abs(eta) < 2.5'),
    filter = cms.bool(True)
)

selectedPatJetsBtag = cms.EDFilter("BTagFilter",             
     jetSrc = cms.untracked.InputTag("selectedPatJetsEta:selectedPatJetsForWH"),
     bTaggingDiscriminator = cms.untracked.string("trackCountingHighEffBJetTags"),
     bTagThreshold = cms.untracked.double(3.3),
     filter = cms.bool(True)
)

selectedNumJet = cms.EDFilter("PATCandViewCountFilter",
     src = cms.InputTag("selectedPatJetsEta:selectedPatJetsForWH"),
     maxNumber = cms.uint32(4000),
     minNumber = cms.uint32(1),
     filter = cms.bool(True)
)

jetSequence = cms.Sequence(JetHistosBeforeJetEt *
			   selectedPatJetsEt20 *
			   JetHistosBeforeJetEta *
			   selectedPatJetsEta *
			   JetHistosBeforeJetBTag *
			   selectedPatJetsBtag *
			   JetHistosAfterJetBTag *
                           selectedNumJet *
                           JetHistosAfterNumJet
)
