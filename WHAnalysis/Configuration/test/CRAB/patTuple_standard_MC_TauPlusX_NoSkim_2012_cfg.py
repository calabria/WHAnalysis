## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

process.MessageLogger.cerr.FwkReport.reportEvery = 5000

process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

from PhysicsTools.PatAlgos.tools.coreTools import *

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')

#--------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.tools.jetTools import *

jec = [ 'L1FastJet', 'L2Relative', 'L3Absolute' ]
#if not isMC:
#        jec.extend([ 'L2L3Residual' ])
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
	tauTag = cms.InputTag("patTaus"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS")
)

process.muonVariables = cms.EDProducer('MuonsUserEmbedded',
	muonTag = cms.InputTag("patMuons"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS"),
	doMuIdMVA = cms.bool(True),
	doMuIsoMVA = cms.bool(True),
	doMuIsoRingsRadMVA = cms.bool(True),
	doMuIdIsoCombMVA = cms.bool(True),
        target = cms.string("Fall11MC"),

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
	electronTag = cms.InputTag("patElectrons"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS"),
	isMC = cms.bool(True),
	doMVAMIT = cms.bool(True),
	doMVAPOG = cms.bool(True),
	doMVAIso = cms.bool(True),
        target = cms.string("Fall11MC"),

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

process.skimmedElectrons = cms.EDFilter("PATElectronSelector",
	src = cms.InputTag("electronVariables"),
	cut = cms.string('pt >= 15. && abs(eta) < 2.5'),
	filter = cms.bool(True)
)

process.skimmedTaus = cms.EDFilter("PATTauSelector",
	src = cms.InputTag("tauVariables"),
	cut = cms.string('pt >= 15. && abs(eta) < 2.5 && tauID("decayModeFinding") > 0.5 && tauID("byLooseCombinedIsolationDeltaBetaCorr") > 0.5'),
	filter = cms.bool(True)
)

process.numTaus = cms.EDFilter("PATCandViewCountFilter",
	src = cms.InputTag("skimmedTaus"),
	maxNumber = cms.uint32(2000),
	minNumber = cms.uint32(2),
	filter = cms.bool(True)
)

# load the PU JetID sequence
process.load("CMGTools.External.pujetidsequence_cff")

# MVA MET
process.load("RecoMET/METProducers/mvaPFMET_cff")
process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3")
process.pfMEtMVA.srcLeptons = cms.VInputTag('cleanPatElectrons', 'cleanPatMuons', 'cleanPatTaus')

process.patPFMetByMVA = process.patMETs.clone(
	metSource = cms.InputTag('pfMEtMVA'),
	addMuonCorrections = cms.bool(False),
	addGenMET = cms.bool(False),
	genMETSource = cms.InputTag('genMetTrue')
)

process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")
process.pfJetMETcorr.offsetCorrLabel = cms.string("ak5PFL1Fastjet")
process.pfJetMETcorr.jetCorrLabel = cms.string("ak5PFL1FastL2L3")

# load the coreTools of PAT
from PhysicsTools.PatAlgos.tools.metTools import *
addTcMET(process, 'TC')
addPfMET(process, 'PF')
process.patMETsPF.metSource = cms.InputTag("pfMet")

process.patPFMETsTypeIcorrected = process.patMETs.clone(
	metSource = cms.InputTag('pfType1CorrectedMet'),
	addMuonCorrections = cms.bool(False),
	genMETSource = cms.InputTag('genMetTrue'),
	addGenMET = cms.bool(False)
)

process.counter = cms.EDAnalyzer('SimpleCounter')
process.TFileService = cms.Service("TFileService", fileName = cms.string('histo_counter.root'))

## let it run
process.p = cms.Path(
	process.counter *
	process.scrapingVeto *
	process.pfParticleSelectionSequence *
	process.muIsoSequence *
	process.electronIsoSequence *
  	process.producePFMETCorrections *
	process.patDefaultSequence *
	process.muonVariables *
	process.electronVariables *
	process.tauVariables *
	process.puJetIdSqeuence *
	process.pfMEtMVAsequence *
	process.patPFMetByMVA *
	process.patPFMETsTypeIcorrected 
	#process.skimmedElectrons *
	#process.skimmedTaus *
	#process.numTaus
)
                

## remove MC matching from the default sequence
#removeMCMatching(process, ['All'])
#runOnData(process)

#
process.GlobalTag.globaltag = "START52_V10::All" ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                               ##
process.source.fileNames = [                    ##
	
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/0A439819-32A5-E111-9129-00215E22190E.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/10742526-52A5-E111-BFD4-00215E222394.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/1C2A5C22-71A5-E111-A25C-E41F1318162C.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/222DF664-1DA5-E111-A49B-E41F13181590.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/2C294C00-3AA5-E111-A1E2-00215E21F18A.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/2ECCC4B9-30A5-E111-9B6C-00215E21DD3E.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/4651C43B-8AA5-E111-8996-00215E2216EC.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/4822140A-35A5-E111-8A5C-00215E222268.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/5689DE6B-39A5-E111-8083-E41F1318148C.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/58CCD4BA-68A5-E111-BD7B-00215E22225C.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/6259E128-75A5-E111-B2B4-00215E2211BE.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/689F5EF8-6DA5-E111-BDDE-00215E21DBE8.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/6A87F91D-37A5-E111-A8E3-00215E21DC78.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/6C5C018E-33A5-E111-91EC-00215E221A28.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/6CC27C38-39A5-E111-BF1A-00215E221B48.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/6E0B482C-2FA5-E111-B5D4-00215E21D9A8.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/700852B6-32A5-E111-89D9-00215E221812.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/722B2B43-70A5-E111-A12C-00215E21D56A.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/7C0527B8-A7A5-E111-BDBA-00215E2223D0.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/A0168152-2EA5-E111-9F38-00215E21EBAE.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/A66547CF-31A5-E111-90C4-00215E21D516.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/A672137E-36A5-E111-ACB9-E61F13191893.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/AED9558C-35A5-E111-A5E0-E41F13181580.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/B863FD0C-38A5-E111-A288-1CC1DE003978.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/B8AF3B4A-34A5-E111-A32C-00215E93EDA4.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/C2CE71F3-35A5-E111-A450-00215E2223E2.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/C817A2A1-35A5-E111-9C05-00215E2227F0.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/CCA7787F-6FA5-E111-9E36-00215E21D942.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/D0EFB84A-3BA5-E111-B96A-00215E2222D4.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/EA005B7B-6AA5-E111-828E-00215E221EEA.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/EC9CC179-30A5-E111-90BD-E41F1318174C.root',
	'/store/mc/Summer12/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/AODSIM/PU_S7_START52_V9-v2/0000/F2293D71-34A5-E111-8EA7-00215E222808.root',


   ]                                            ##  (e.g. 'file:AOD.root')
#                                               ##
process.maxEvents.input = 500                    ##  (e.g. -1 to run on all events)
#                                               ##
process.out.outputCommands = [ #'keep *'
			       'keep *_genParticles_*_*',
			       'keep patMuons_*_*_*',
			       'keep patElectrons_*_*_*', 
			       'keep patTaus_*_*_*', 
			       'keep patJets_*_*_*', 
			       #'keep CaloTowers_*_*_*',
			       'keep patMETs_*_*_*', 
			       #'keep doubles_ak5PFJets_*_*', 
			       'keep floatedmValueMap_*_*_*', 
			       'keep recoVertexs_*_*_*',
			       'keep recoTracks_*_*_*',
			       'keep *_TriggerResults_*_*',
			       'keep PileupSummaryInfos_*_*_*',
			       'keep *_puJetId_*_*', # input variables
			       'keep *_puJetMva_*_*', # final MVAs and working point flags
			       'drop recoPFJets_*_*_*', 
			       'drop *_MEtoEDMConverter_*_*',
			       'drop patMuons_selectedPatMuons_*_*',
			       'drop patMuons_patMuons_*_*',
			       'drop patElectrons_selectedPatElectrons_*_*', 
			       'drop patTaus_selectedPatTaus_*_*', 
			       'drop patJets_patJets_*_*', 
			       'drop patJets_selectedPatJets_*_*', 
			       'drop patJets_selectedPatJetsAK5PF_*_*', 
			       'drop patJets_cleanPatJetsAK5PF_*_*', 
			       'drop recoPFJets_*_*_*', 
			       'drop patMETs_selectedPatMETs_*_*', 
			       'drop patMETs_patMETs_*_*', 
			       'drop patMETs_patMETsTC_*_*', 
			       'drop patMuons_cleanPatMuons_*_*',
			       'drop patElectrons_cleanPatElectrons_*_*', 
			       'drop patElectrons_patElectrons_*_*', 
			       'drop patTaus_cleanPatTaus_*_*', 
			       'drop patTaus_patTaus_*_*', 
			       'drop patJets_cleanPatJets_*_*', 
			       'drop patMETs_cleanPatMETs_*_*', 
			       'drop floatedmValueMap_eidLoose_*_*',
			       'drop floatedmValueMap_eidRobustLoose_*_*',
			       'drop floatedmValueMap_eidRobustHighEnergy_*_*',
			       'drop floatedmValueMap_eidTight_*_*',
			       'drop floatedmValueMap_eidRobustTight_*_*',
			       'drop recoTracks_cosmicMuons_*_*',
			       'drop recoTracks_cosmicMuons1Leg_*_*',
			       'drop recoTracks_globalCosmicMuons_*_*',
			       'drop recoTracks_globalCosmicMuons1Leg_*_*',
			       'drop recoTracks_regionalCosmicTracks_*_*',
			       'drop recoTracks_tevMuons_*_*',
			       'drop recoTracks_impactParameterTagInfosAK5PF_*_*',
			       'drop recoVertexs_recoTauPileUpVertices_*_*',
			       'drop recoTracks_ckfInOutTracksFromConversions_*_*',
			       'drop recoTracks_ckfOutInTracksFromConversions_*_*',
			       'drop edmTriggerResults_TriggerResults_*_PAT',
			       'drop edmTriggerResults_TriggerResults_*_RECO',
			       'drop patElectrons_skimmedElectrons_*_*',
			       'drop patTaus_skimmedTaus_*_*',
			     ]                  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                               ##
process.out.fileName = 'patTuple.root'          ##  (e.g. 'myTuple.root')
#                                               ##
process.options.wantSummary = False             ##  (to suppress the long output at the end of the job)    

