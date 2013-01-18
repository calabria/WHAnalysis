## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

process.MessageLogger.cerr.FwkReport.reportEvery = 5000

process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

from PhysicsTools.PatAlgos.tools.coreTools import *

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')

#--------------------------------------------------------------------------------

################### Take inputs from crab.cfg file ##############
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
options.register ('isMC',
                  True,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "Sample Type: MC or data")

options.register ('channel',
                  'ett',
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.string,
                  "Desired channel: mtt, ett or none")    

options.register ('globaltag',
                  'START53_V7F::All',
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.string,
                  "Global Tag to use. Default: START53_V11::All")

options.register ('includeSim',
                  False,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "Include Sim. Default: False")

options.register ('includePatTrig',
                  False,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "Include PatTrig. Default: False")

import sys
print sys.argv

if len(sys.argv) > 0:
    last = sys.argv.pop()
    sys.argv.extend(last.split(","))
    print sys.argv

if hasattr(sys, "argv") == True:
	options.parseArguments()
isMC = options.isMC
channel = options.channel
globaltag = options.globaltag
includeSim = options.includeSim
includePatTrig = options.includePatTrig
print 'Using channel: %s' % channel

#--------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.tools.jetTools import *

jec = [ 'L1FastJet', 'L2Relative', 'L3Absolute' ]
if not isMC:
        jec.extend([ 'L2L3Residual' ])
switchJetCollection(process, cms.InputTag('ak5PFJets'),
     doJTA        = True,
     doBTagging   = True,
     jetCorrLabel = ('AK5PF', cms.vstring(jec)),
     doType1MET   = True,
     genJetCollection=cms.InputTag("ak5GenJets"),
     doJetID      = True,
     jetIdLabel   = 'ak5'
)

#--------------------------------------------------------------------------------

## remove certain objects from the default sequence
#removeAllPATObjectsBut(process, ['Muons', 'Electrons', 'Taus', 'METs'])
#removeSpecificPATObjects(process, ['Electrons', 'Muons', 'Taus'])

from PhysicsTools.PatAlgos.tools.tauTools import *
switchToPFTauHPS(process) # For HPS Taus
#switchToPFTauHPSpTaNC(process) # For HPS TaNC Taus  

process.patTaus.embedLeadPFCand = cms.bool(True)
process.patTaus.embedSignalPFCands = cms.bool(True)
process.patTaus.embedIsolationPFCands = cms.bool(True)
process.patTaus.embedLeadTrack = cms.bool(True)
process.patTaus.embedSignalTracks = cms.bool(True)
process.patTaus.embedIsolationTracks = cms.bool(True)
process.patTaus.embedIsolationPFChargedHadrCands = cms.bool(True)
process.patTaus.embedIsolationPFNeutralHadrCands = cms.bool(True)
process.patTaus.embedIsolationPFGammaCands = cms.bool(True)
process.patTaus.embedSignalPFChargedHadrCands = cms.bool(True)
process.patTaus.embedSignalPFNeutralHadrCands = cms.bool(True)
process.patTaus.embedSignalPFGammaCands = cms.bool(True)
process.patTaus.embedLeadPFChargedHadrCand = cms.bool(True)
process.patTaus.embedLeadPFNeutralCand = cms.bool(True)

#--------------------------------------------------------------------------------

from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFMuonIso, setupPFElectronIso

process.muIsoSequence       = setupPFMuonIso(process,'muons')
process.electronIsoSequence = setupPFElectronIso(process,'gsfElectrons')

from CommonTools.ParticleFlow.pfParticleSelection_cff import pfParticleSelectionSequence
process.pfParticleSelectionSequence = pfParticleSelectionSequence


process.patMuons.isoDeposits = cms.PSet(
    pfAllParticles   = cms.InputTag("muPFIsoDepositPUPFIso"),      # all PU   CH+MU+E
    pfChargedHadrons = cms.InputTag("muPFIsoDepositChargedPFIso"), # all noPU CH

    pfNeutralHadrons = cms.InputTag("muPFIsoDepositNeutralPFIso"), # all NH
    pfPhotons        = cms.InputTag("muPFIsoDepositGammaPFIso"),   # all PH

    user = cms.VInputTag(
    cms.InputTag("muPFIsoDepositChargedAllPFIso"),                 # all noPU CH+MU+E
    )
    )

process.patMuons.isolationValues = cms.PSet(
    pfAllParticles   = cms.InputTag("muPFIsoValuePU04PFIso"),
    pfChargedHadrons = cms.InputTag("muPFIsoValueCharged04PFIso"),

    pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral04PFIso"),
    pfPhotons        = cms.InputTag("muPFIsoValueGamma04PFIso"),

    user = cms.VInputTag(
    cms.InputTag("muPFIsoValueChargedAll04PFIso"),
    )
    )

process.patElectrons.isoDeposits = cms.PSet(
    pfAllParticles   = cms.InputTag("elPFIsoDepositPUPFIso"),      # all PU   CH+MU+E

    pfChargedHadrons = cms.InputTag("elPFIsoDepositChargedPFIso"), # all noPU CH
    pfNeutralHadrons = cms.InputTag("elPFIsoDepositNeutralPFIso"), # all NH

    pfPhotons        = cms.InputTag("elPFIsoDepositGammaPFIso"),   # all PH
    user = cms.VInputTag(
    cms.InputTag("elPFIsoDepositChargedAllPFIso"),                 # all noPU CH+MU+E

    )
    )
process.patElectrons.isolationValues = cms.PSet(
    pfAllParticles   = cms.InputTag("elPFIsoValuePU04PFIdPFIso"),
    pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04PFIdPFIso"),

    pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04PFIdPFIso"),
    pfPhotons        = cms.InputTag("elPFIsoValueGamma04PFIdPFIso"),

    user = cms.VInputTag(
    cms.InputTag("elPFIsoValueChargedAll04PFIdPFIso"),
    cms.InputTag("elPFIsoValueChargedAll04NoPFIdPFIso"),

    cms.InputTag("elPFIsoValuePU04NoPFIdPFIso"),
    cms.InputTag("elPFIsoValueCharged04NoPFIdPFIso"),
    cms.InputTag("elPFIsoValueGamma04NoPFIdPFIso"),

    cms.InputTag("elPFIsoValueNeutral04NoPFIdPFIso")
    )

    )

#--------------------------------------------------------------------------------

# require scraping filter
process.scrapingVeto = cms.EDFilter("FilterOutScraping",
	applyfilter = cms.untracked.bool(True),
	debugOn = cms.untracked.bool(False),
	numtrack = cms.untracked.uint32(10),
	thresh = cms.untracked.double(0.2)
	)

process.tauVariables = cms.EDProducer('TausUserEmbedded',
	tauTag = cms.InputTag("patTausTriggerMatch"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS")
)

print 'Using isMC: %s' % isMC
if isMC:
	targetString = "Fall11MC"
else:
	targetString = "2012Data"

print 'Using target: %s' % targetString
process.muonVariables = cms.EDProducer('MuonsUserEmbedded',
	muonTag = cms.InputTag("patMuonsTriggerMatch"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS"),
	doMuIdMVA = cms.bool(True),
	doMuIsoMVA = cms.bool(True),
	doMuIsoRingsRadMVA = cms.bool(True),
	doMuIdIsoCombMVA = cms.bool(True),
        target = cms.string(targetString),

	inputFileName0 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDMVA_sixie-BarrelPt5To10_V0_BDTG.weights.xml"),
	inputFileName1 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDMVA_sixie-EndcapPt5To10_V0_BDTG.weights.xml"),
	inputFileName2 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDMVA_sixie-BarrelPt10ToInf_V0_BDTG.weights.xml"),
	inputFileName3 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDMVA_sixie-EndcapPt10ToInf_V0_BDTG.weights.xml"),
	inputFileName4 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDMVA_sixie-Tracker_V0_BDTG.weights.xml"),
	inputFileName5 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDMVA_sixie-Global_V0_BDTG.weights.xml"),

	inputFileName0v2 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-BarrelPt5To10_V0_BDTG.weights.xml"),
	inputFileName1v2 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-EndcapPt5To10_V0_BDTG.weights.xml"),
	inputFileName2v2 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-BarrelPt10ToInf_V0_BDTG.weights.xml"),
	inputFileName3v2 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-EndcapPt10ToInf_V0_BDTG.weights.xml"),
	inputFileName4v2 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-Tracker_V0_BDTG.weights.xml"),
	inputFileName5v2 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-Global_V0_BDTG.weights.xml"),

	inputFileName0v3 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-BarrelPt5To10_V1_BDTG.weights.xml"),
	inputFileName1v3 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-EndcapPt5To10_V1_BDTG.weights.xml"),
	inputFileName2v3 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-BarrelPt10ToInf_V1_BDTG.weights.xml"),
	inputFileName3v3 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-EndcapPt10ToInf_V1_BDTG.weights.xml"),
	inputFileName4v3 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-Tracker_V1_BDTG.weights.xml"),
	inputFileName5v3 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIsoMVA_sixie-Global_V1_BDTG.weights.xml"),

	inputFileName0v4 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDIsoCombinedMVA_V0_barrel_lowpt.weights.xml"),
	inputFileName1v4 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDIsoCombinedMVA_V0_endcap_lowpt.weights.xml"),
	inputFileName2v4 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDIsoCombinedMVA_V0_barrel_highpt.weights.xml"),
	inputFileName3v4 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDIsoCombinedMVA_V0_endcap_highpt.weights.xml"),
	inputFileName4v4 = cms.FileInPath("Muon/MuonAnalysisTools/data/MuonIDIsoCombinedMVA_V0_tracker.weights.xml"),
)

process.electronVariables = cms.EDProducer('ElectronsUserEmbedder',
	electronTag = cms.InputTag("patElectronsTriggerMatch"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS"),
	isMC = cms.bool(isMC),
	doMVAMIT = cms.bool(True),
	doMVAPOG = cms.bool(True),
	doMVAIso = cms.bool(True),
        target = cms.string(targetString),

	inputFileName0 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet0LowPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName1 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet1LowPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName2 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet2LowPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName3 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet0HighPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName4 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet1HighPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName5 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet2HighPt_NoIPInfo_BDTG.weights.xml"),

	inputFileName0v2 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_TrigV0_Cat1.weights.xml'),
    	inputFileName1v2 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_TrigV0_Cat2.weights.xml'),
    	inputFileName2v2 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_TrigV0_Cat3.weights.xml'),
    	inputFileName3v2 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_TrigV0_Cat4.weights.xml'),
    	inputFileName4v2 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_TrigV0_Cat5.weights.xml'),
    	inputFileName5v2 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_TrigV0_Cat6.weights.xml'),

    	inputFileName0v3 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_NonTrigV0_Cat1.weights.xml'),
    	inputFileName1v3 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_NonTrigV0_Cat2.weights.xml'),
    	inputFileName2v3 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_NonTrigV0_Cat3.weights.xml'),
    	inputFileName3v3 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_NonTrigV0_Cat4.weights.xml'),
    	inputFileName4v3 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_NonTrigV0_Cat5.weights.xml'),
    	inputFileName5v3 = cms.FileInPath('EGamma/EGammaAnalysisTools/data/Electrons_BDTG_NonTrigV0_Cat6.weights.xml'),

    	inputFileName0v4 = cms.FileInPath('UserCode/sixie/EGamma/EGammaAnalysisTools/data/ElectronIso_BDTG_V0_BarrelPt5To10.weights.xml'),
    	inputFileName1v4 = cms.FileInPath('UserCode/sixie/EGamma/EGammaAnalysisTools/data/ElectronIso_BDTG_V0_EndcapPt5To10.weights.xml'),
    	inputFileName2v4 = cms.FileInPath('UserCode/sixie/EGamma/EGammaAnalysisTools/data/ElectronIso_BDTG_V0_BarrelPt10ToInf.weights.xml'),
    	inputFileName3v4 = cms.FileInPath('UserCode/sixie/EGamma/EGammaAnalysisTools/data/ElectronIso_BDTG_V0_EndcapPt10ToInf.weights.xml'),
)

#--------------------------------------------------------------------------------

# PAT Muons
process.patMuons.embedTrack = cms.bool(True) # Embed tracks for muon ID cuts to be done offline

# PAT Electrons
process.patElectrons.embedTrack = cms.bool(True)
process.patElectrons.embedGsfTrack = cms.bool(True)

#--------------------------------------------------------------------------------

# Trigger and Trigger matching
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger(process)

process.patMuonTriggerMatchHLTIsoMu24 = cms.EDProducer('PATTriggerMatcherDRDPtLessByR',
        src = cms.InputTag("patMuons"),
        matched = cms.InputTag("patTrigger"),
        matchedCuts = cms.string('path("HLT_IsoMu24_v*")'),
        maxDPtRel = cms.double(0.5),
        maxDeltaR = cms.double(0.5),
        resolveAmbiguities = cms.bool(True),
        resolveByMatchQuality = cms.bool(True))
process.patMuonTriggerMatchHLTIsoMu24eta2p1 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patMuons"),
        matchedCuts = cms.string('path("HLT_IsoMu24_eta2p1_v*")'))
process.patMuonTriggerMatchHLTMu40 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patMuons"),
        matchedCuts = cms.string('path("HLT_Mu40_v*")'))

process.patElectronTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau15 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patElectrons"),
        matchedCuts = cms.string('path("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v*")'))
process.patElectronTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patElectrons"),
        matchedCuts = cms.string('path("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*")'))
process.patElectronTriggerMatchHLTEle18CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patElectrons"),
        matchedCuts = cms.string('path("HLT_Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*")'))
process.patElectronTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTTightIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patElectrons"),
        matchedCuts = cms.string('path("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TightIsoPFTau20_v*")'))
process.patElectronTriggerMatchHLTEle18CaloIdVTCaloIsoTTrkIdTTrkIsoTMediumIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patElectrons"),
        matchedCuts = cms.string('path("HLT_Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v*")'))
process.patElectronTriggerMatchHLTEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTMediumIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patElectrons"),
        matchedCuts = cms.string('path("HLT_Ele20_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v*")'))
process.patElectronTriggerMatchHLTEle20CaloIdVTCaloIsoRhoTTrkIdTTrkIsoTLooseIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patElectrons"),
        matchedCuts = cms.string('path("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*")'))
process.patElectronTriggerMatchHLTEle22eta2p1WP90RhoLooseIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patElectrons"),
        matchedCuts = cms.string('path("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*")'))

process.patTauTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau15 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patTaus"),
        matchedCuts = cms.string('path("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v*")'))
process.patTauTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patTaus"),
        matchedCuts = cms.string('path("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*")'))
process.patTauTriggerMatchHLTEle18CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patTaus"),
        matchedCuts = cms.string('path("HLT_Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*")'))
process.patTauTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTTightIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patTaus"),
        matchedCuts = cms.string('path("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TightIsoPFTau20_v*")'))
process.patTauTriggerMatchHLTEle18CaloIdVTCaloIsoTTrkIdTTrkIsoTMediumIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patTaus"),
        matchedCuts = cms.string('path("HLT_Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v*")'))
process.patTauTriggerMatchHLTEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTMediumIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patTaus"),
        matchedCuts = cms.string('path("HLT_Ele20_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v*")'))
process.patTauTriggerMatchHLTEle20CaloIdVTCaloIsoRhoTTrkIdTTrkIsoTLooseIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patTaus"),
        matchedCuts = cms.string('path("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*")'))
process.patTauTriggerMatchHLTEle22eta2p1WP90RhoLooseIsoPFTau20 = process.patMuonTriggerMatchHLTIsoMu24.clone(
        src = cms.InputTag("patTaus"),
        matchedCuts = cms.string('path("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*")'))

switchOnTriggerMatchEmbedding(process, [
                'patMuonTriggerMatchHLTIsoMu24',
                'patMuonTriggerMatchHLTIsoMu24eta2p1',
                'patMuonTriggerMatchHLTMu40',

                'patElectronTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau15',
                'patElectronTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20',
                'patElectronTriggerMatchHLTEle18CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20',
                'patElectronTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTTightIsoPFTau20',
                'patElectronTriggerMatchHLTEle18CaloIdVTCaloIsoTTrkIdTTrkIsoTMediumIsoPFTau20',
                'patElectronTriggerMatchHLTEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTMediumIsoPFTau20',
                'patElectronTriggerMatchHLTEle20CaloIdVTCaloIsoRhoTTrkIdTTrkIsoTLooseIsoPFTau20',
                'patElectronTriggerMatchHLTEle22eta2p1WP90RhoLooseIsoPFTau20',

                'patTauTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau15',
                'patTauTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20',
                'patTauTriggerMatchHLTEle18CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20',
                'patTauTriggerMatchHLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTTightIsoPFTau20',
                'patTauTriggerMatchHLTEle18CaloIdVTCaloIsoTTrkIdTTrkIsoTMediumIsoPFTau20',
                'patTauTriggerMatchHLTEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTMediumIsoPFTau20',
                'patTauTriggerMatchHLTEle20CaloIdVTCaloIsoRhoTTrkIdTTrkIsoTLooseIsoPFTau20',
                'patTauTriggerMatchHLTEle22eta2p1WP90RhoLooseIsoPFTau20',
        ])

#--------------------------------------------------------------------------------

process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    	src = cms.InputTag("offlinePrimaryVertices"),
    	cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
    	filter = cms.bool(True)
    	)

simpleCutsWP95 = "(userFloat('nHits')<=1"+ \
                 " && (" + \
                 " (isEB && userFloat('sihih')<0.010 && userFloat('dPhi')<0.80 && "+ \
                 "          userFloat('dEta') <0.007 && userFloat('HoE') <0.15)"   + \
                 " || "  + \
                 " (isEE && userFloat('sihih')<0.030 && userFloat('dPhi')<0.70 && "+ \
                 "          userFloat('dEta') <0.010 && userFloat('HoE') <0.07)"   + \
                 "     )"+ \
                 ")"

process.skimmedMuons = cms.EDFilter("PATMuonSelector",
	src = cms.InputTag("muonVariables"),
	cut = cms.string("pt >= 20. && abs(eta) < 2.5 && isGlobalMuon && userFloat('PFRelIsoDB04v2') < 0.3"),
	filter = cms.bool(True)
)

process.skimmedElectrons = cms.EDFilter("PATElectronSelector",
	src = cms.InputTag("electronVariables"),
	cut = cms.string("pt >= 20. && abs(eta) < 2.5 &&" + simpleCutsWP95 + "&& userFloat('PFRelIsoDB04') < 0.3"),
	filter = cms.bool(True)
)

process.skimmedTaus = cms.EDFilter("PATTauSelector",
	src = cms.InputTag("tauVariables"),
	cut = cms.string("pt >= 20. && abs(eta) < 2.3 && tauID('decayModeFinding') > 0.5"),
	filter = cms.bool(True)
)

process.numTaus = cms.EDFilter("PATCandViewCountFilter",
	src = cms.InputTag("skimmedTaus"),
	maxNumber = cms.uint32(2000),
	minNumber = cms.uint32(2),
	filter = cms.bool(True)
)

if(channel == "mtt"):
  	process.theSkim = cms.Sequence(
		process.goodOfflinePrimaryVertices +
    		process.skimmedMuons + 
		process.skimmedTaus +
		process.numTaus
  	)
if(channel == "ett"):
  	process.theSkim = cms.Sequence(
		process.goodOfflinePrimaryVertices +
    		process.skimmedElectrons + 
		process.skimmedTaus +
		process.numTaus
  	)
if(channel == "none"):
  	process.theSkim = cms.Sequence(
  	)

#--------------------------------------------------------------------------------

# MVA MET

process.load('JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff')
if isMC:
	process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3")
else: 
	process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3Residual")
#process.pfMEtMVA.srcLeptons = cms.VInputTag('isolatedPatElectrons', 'isolatedPatMuons', 'isolatedPatTaus')

process.patPFMetByMVA = process.patMETs.clone(
	metSource = cms.InputTag('pfMEtMVA'),
	addMuonCorrections = cms.bool(False),
	addGenMET = cms.bool(False),
	genMETSource = cms.InputTag('genMetTrue')
)

#--------------------------------------------------------------------------------

process.load("RecoJets.JetProducers.PileupJetID_cfi")
process.pileupJetIdProducer.jets = cms.InputTag('ak5PFJets')
process.pileupJetIdProducerChs.jets = cms.InputTag('ak5PFJets')
process.pileupJetIdProducer.applyJec = cms.bool(True)
process.pileupJetIdProducer.inputIsCorrected = cms.bool(False)

# Embed into PAT jets as userdata
process.patJets.userData.userFloats.src = cms.VInputTag(
	cms.InputTag('pileupJetIdProducer', 'fullDiscriminant'),
	cms.InputTag('pileupJetIdProducer', 'cutbasedDiscriminant'),
	cms.InputTag('pileupJetIdProducer', 'philv1Discriminant'))
process.patJets.userData.userInts.src = cms.VInputTag(
	cms.InputTag('pileupJetIdProducer', 'fullId'),
	cms.InputTag('pileupJetIdProducer', 'cutbasedId'),
	cms.InputTag('pileupJetIdProducer', 'philv1Id'))

#--------------------------------------------------------------------------------

process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")
process.pfJetMETcorr.offsetCorrLabel = cms.string("ak5PFL1Fastjet")
if isMC:
	process.pfJetMETcorr.jetCorrLabel = cms.string("ak5PFL1FastL2L3")
else:
	process.pfJetMETcorr.jetCorrLabel = cms.string("ak5PFL1FastL2L3Residual")

# load the coreTools of PAT
from PhysicsTools.PatAlgos.tools.metTools import *
addTcMET(process, 'TC')
addPfMET(process, 'PF')
process.patMETsPF.metSource = cms.InputTag("pfMet")

process.load("JetMETCorrections.Type1MET.pfMETCorrectionType0_cfi")
process.pfType1CorrectedMet.applyType0Corrections = cms.bool(False)
process.pfType1CorrectedMet.srcType1Corrections = cms.VInputTag(
    	cms.InputTag('pfMETcorrType0'),
    	cms.InputTag('pfJetMETcorr', 'type1')        
)

process.patPFMETsTypeIcorrected = process.patMETs.clone(
	metSource = cms.InputTag('pfType1CorrectedMet'),
	addMuonCorrections = cms.bool(False),
	genMETSource = cms.InputTag('genMetTrue'),
	addGenMET = cms.bool(False)
)

#--------------------------------------------------------------------------------

#process.counter = cms.EDAnalyzer('SimpleCounter')
#process.TFileService = cms.Service("TFileService", fileName = cms.string('histo_counter.root'))

# Event count producers
process.nEventsTotal = cms.EDProducer('EventCountProducer')
process.nEventsFiltered = cms.EDProducer('EventCountProducer')

## let it run
process.p = cms.Path(
	#process.counter *
	process.nEventsTotal *
	process.scrapingVeto *
	process.pfParticleSelectionSequence *
	process.muIsoSequence *
	process.electronIsoSequence *
    	process.pileupJetIdProducer *
	process.type0PFMEtCorrection *
  	process.producePFMETCorrections *
	process.patDefaultSequence *
	process.muonVariables *
	process.electronVariables *
	process.tauVariables *
	process.patPFMETsTypeIcorrected *
	process.pfMEtMVAsequence *
	process.patPFMetByMVA *
	process.theSkim *
	process.nEventsFiltered
)

#--------------------------------------------------------------------------------

## remove MC matching from the default sequence
if not isMC:
	removeMCMatching(process, ['All'])
	removeMCMatching(process, ['METs'], "TC")
	removeMCMatching(process, ['METs'], "PF")
	process.patDefaultSequence.remove(process.patJetPartonMatch)
	#process.patDefaultSequence.remove(process.patJetPartonMatchAK5PF)
	#process.patDefaultSequence.remove(process.patJetGenJetMatchAK5PF)
	process.patDefaultSequence.remove(process.patJetFlavourId)
	process.patDefaultSequence.remove(process.patJetPartons)
	process.patDefaultSequence.remove(process.patJetPartonAssociation)
	#process.patDefaultSequence.remove(process.patJetPartonAssociationAK5PF)
	process.patDefaultSequence.remove(process.patJetFlavourAssociation)
	#process.patDefaultSequence.remove(process.patJetFlavourAssociationAK5PF)
	runOnData(process)

if not isMC:
	process.patTriggerEvent.processName = '*'
	if hasattr(process,"patTrigger"):
    		process.patTrigger.processName = '*'

#--------------------------------------------------------------------------------

#
print 'Using Global Tag: %s' % globaltag
process.GlobalTag.globaltag = globaltag         ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                               ##
process.source.fileNames = [                    ##
	
	'/store/mc/Summer12_DR53X/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v2/0002/FEAC0369-F0F0-E111-A459-001E6739702B.root'
	#'/store/data/Run2012A/ElectronHad/AOD/13Jul2012-v1/00000/FEFA63C4-D4D0-E111-9F90-002618943857.root'

   ]                                            ##  (e.g. 'file:AOD.root')
#                                               ##
process.maxEvents.input = 100                   ##  (e.g. -1 to run on all events)
#
process.out.outputCommands = [ #'keep *'
			       'keep patMuons_muonVariables_*_*',
			       'keep patElectrons_electronVariables_*_*', 
			       'keep patTaus_tauVariables_*_*', 
			       'keep patJets_patJets_*_*',
			       'keep patMETs_patMETsPF_*_*',
			       'keep patMETs_patPFMETsTypeIcorrected_*_*',
			       'keep patMETs_patPFMetByMVA_*_*',
			       'keep recoVertexs_offlinePrimaryVertices_*_*',
			       'keep recoVertexs_offlinePrimaryVerticesWithBS_*_*',
			       'keep recoVertexs_goodOfflinePrimaryVertices_*_*',
			       'keep recoTracks_generalTracks_*_*',
			       'keep *_TriggerResults_*_HLT',
			       'keep PileupSummaryInfos_*_*_*',
			       'keep *_offlineBeamSpot_*_*',
			       'keep L1GlobalTriggerReadoutRecord_*_*_*',
			       'keep recoPFJets_ak5PFJets_*_*',
			       'keep *_nEventsTotal_*_*',
			       'keep *_nEventsFiltered_*_*',
			     ]                  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)          
if includeSim:
	process.out.outputCommands.extend(['keep *_genParticles_*_*'])
if includePatTrig:
	process.out.outputCommands.extend(['keep *_patTrigger_*_*',
					   'keep patTriggerEvent_*_*_*'])
#                                               ##
process.out.fileName = 'patTuple.root'          ##  (e.g. 'myTuple.root')
#                                               ##
process.options.wantSummary = False             ##  (to suppress the long output at the end of the job)    

