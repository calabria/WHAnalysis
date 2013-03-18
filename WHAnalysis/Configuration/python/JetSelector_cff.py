import FWCore.ParameterSet.Config as cms
from jetHistos_cff import *

selectedPatJetsEt20 = cms.EDFilter("JetFilter",
    jetSrc = cms.untracked.InputTag("patJets"),                                                               
    cut = cms.untracked.string('et > 20.'), 
    filter = cms.bool(True)
)

selectedPatJetsEta = cms.EDFilter("JetFilter",
    jetSrc = cms.untracked.InputTag("selectedPatJetsEt20:selectedPatJetsForWH"),                                                               
    cut = cms.untracked.string('abs(eta) < 2.4'),
    filter = cms.bool(True)
)

selectedPatJetsBtag = cms.EDFilter("BTagFilter",             
     jetSrc = cms.untracked.InputTag("selectedPatJetsEta:selectedPatJetsForWH"),
     #bTaggingDiscriminator = cms.untracked.string("trackCountingHighEffBJetTags"),
     bTaggingDiscriminator = cms.untracked.string("combinedSecondaryVertexBJetTags"),
     #bTagThreshold = cms.untracked.double(3.3),
     bTagThreshold = cms.untracked.double(0.679),
     filter = cms.bool(True)
)

selectedNumJet = cms.EDFilter("PATCandViewCountFilter",
     src = cms.InputTag("selectedPatJetsEta:selectedPatJetsForWH"),
     maxNumber = cms.uint32(4000),
     minNumber = cms.uint32(1),
     filter = cms.bool(True)
)

selectedEvents1 = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/lustre/cms/store/user/calabria/Data/Events/EventsETT_Signal_MET/"),
        muonSrc = cms.untracked.InputTag("muonVariables"),
	eleSrc = cms.untracked.InputTag("electronVariables"),
	tauSrc = cms.untracked.InputTag("tauVariables"),
	jetSrc = cms.untracked.InputTag("selectedPatJetsEta:selectedPatJetsForWH")
)

jetSequence = cms.Sequence(JetHistosBeforeJetEt *
			   selectedPatJetsEt20 *
			   JetHistosBeforeJetEta *
			   selectedPatJetsEta *
			   #selectedEvents1 *
			   JetHistosBeforeJetBTag *
			   selectedPatJetsBtag *
			   JetHistosAfterJetBTag *
                           selectedNumJet *
                           JetHistosAfterNumJet
)
