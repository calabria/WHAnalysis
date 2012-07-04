import FWCore.ParameterSet.Config as cms
from weights_cff import *

JetHistosBeforeJetEt = cms.EDAnalyzer("JetHistManager",
  jetSrc = cms.untracked.InputTag("patJetsAK5PF"),
  bTaggingDiscriminator = cms.untracked.string("trackCountingHighEffBJetTags"),
  bTagThreshold = cms.untracked.double(3.3),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

JetHistosBeforeJetEta = cms.EDAnalyzer("JetHistManager",
  jetSrc = cms.untracked.InputTag("selectedPatJetsEt20:selectedPatJetsForWH"),
  bTaggingDiscriminator = cms.untracked.string("trackCountingHighEffBJetTags"),
  bTagThreshold = cms.untracked.double(3.3),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

JetHistosBeforeJetBTag = cms.EDAnalyzer("JetHistManager",
  jetSrc = cms.untracked.InputTag("selectedPatJetsEta:selectedPatJetsForWH"),
  bTaggingDiscriminator = cms.untracked.string("trackCountingHighEffBJetTags"),
  bTagThreshold = cms.untracked.double(3.3),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

JetHistosAfterJetBTag = cms.EDAnalyzer("JetHistManager",
  jetSrc = cms.untracked.InputTag("selectedPatJetsEta:selectedPatJetsForWH"),
  bTaggingDiscriminator = cms.untracked.string("trackCountingHighEffBJetTags"),
  bTagThreshold = cms.untracked.double(3.3),
  MCDist = cms.untracked.vdouble(vecMC),
  TrueDist2011 = cms.untracked.vdouble(vecData),
  isMC = cms.untracked.bool(True),
)

JetHistosAfterNumJet = cms.EDAnalyzer("JetHistManager",
   jetSrc = cms.untracked.InputTag("selectedPatJetsEta:selectedPatJetsForWH"),
   bTaggingDiscriminator = cms.untracked.string("trackCountingHighEffBJetTags"),
   bTagThreshold = cms.untracked.double(3.3),
   MCDist = cms.untracked.vdouble(vecMC),
   TrueDist2011 = cms.untracked.vdouble(vecData),
   isMC = cms.untracked.bool(True),
)
