## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

from PhysicsTools.PatAlgos.tools.coreTools import *

process.load('JetMETCorrections.Configuration.DefaultJEC_cff')

#--------------------------------------------------------------------------------
#
# configure Jet Energy Corrections
#
process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.jec = cms.ESSource("PoolDBESSource",
     DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
     ),
     timetype = cms.string('runnumber'),
     toGet = cms.VPSet(
       cms.PSet(
           record = cms.string('JetCorrectionsRecord'),
           tag    = cms.string('JetCorrectorParametersCollection_Jec11V2_AK5PF'),
           label  = cms.untracked.string('AK5PF')
       ),
       cms.PSet(
           record = cms.string('JetCorrectionsRecord'),
           tag    = cms.string('JetCorrectorParametersCollection_Jec11V2_AK5Calo'),
           label  = cms.untracked.string('AK5Calo')
       )
    ),
    connect = cms.string('sqlite_fip:TauAnalysis/Configuration/data/Jec11V2.db')
)
process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'jec')

#--------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.tools.jetTools import *

jec = [ 'L1FastJet', 'L2Relative', 'L3Absolute' ]
#if not isMC:
jec.extend([ 'L2L3Residual' ])
switchJetCollection(process, cms.InputTag('ak5PFJets'),
     doJTA        = True,
     doBTagging   = True,
     jetCorrLabel = ('AK5PF', cms.vstring(jec)),
     doType1MET   = False,
     genJetCollection=cms.InputTag("ak5GenJets"),
     doJetID      = True,
     jetIdLabel   = 'ak5'
)

#--------------------------------------------------------------------------------

## remove certain objects from the default sequence
#removeAllPATObjectsBut(process, ['Muons', 'Electrons', 'Taus', 'METs'])
#removeSpecificPATObjects(process, ['Electrons', 'Muons', 'Taus'])

from PhysicsTools.PatAlgos.tools.tauTools import *
#switchToPFTauHPS(process) # For HPS Taus
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
        target = cms.string("2012Data"),

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
	isMC = cms.bool(False),
	doMVAMIT = cms.bool(True),
	doMVAPOG = cms.bool(True),
	doMVAIso = cms.bool(True),
        target = cms.string("2012Data"),

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
          	cut = cms.string('pt >= 15. && abs(eta) < 2.5 && tauID("decayModeFinding") > 0.5 && tauID("byTightCombinedIsolationDeltaBetaCorr") > 0.5'),
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
process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3Residual")
#process.pfMEtMVA.srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatTaus")
process.pfMEtMVA.srcLeptons = cms.VInputTag('cleanPatElectrons', 'cleanPatMuons', 'cleanPatTaus')

process.patPFMetByMVA = process.patMETs.clone(
  		metSource = cms.InputTag('pfMEtMVA'),
  		addMuonCorrections = cms.bool(False),
  		addGenMET = cms.bool(False),
  		genMETSource = cms.InputTag('genMetTrue')
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
	process.patDefaultSequence *
	process.muonVariables *
	process.electronVariables *
	process.tauVariables *
	process.puJetIdSqeuence *
	process.pfMEtMVAsequence *
	process.patPFMetByMVA *
	process.skimmedElectrons *
	process.skimmedTaus *
	process.numTaus
	)
                       
# load the coreTools of PAT
from PhysicsTools.PatAlgos.tools.metTools import *
addTcMET(process, 'TC')
addPfMET(process, 'PF')

## remove MC matching from the default sequence
#removeMCMatching(process, ['All'])
#runOnData(process)

# Switch on PAT trigger
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger( process )
process.patTriggerEvent.processName = '*'

if hasattr(process,"patTrigger"):
    process.patTrigger.processName = '*'

## remove MC matching from the default sequence
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


#
process.GlobalTag.globaltag = "GR_R_52_V9D::All" ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                               ##
process.source.fileNames = [                    ##
	
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/00577492-8BA6-E111-BCA4-002618943876.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/047B6D14-A2A6-E111-A38A-00261894396B.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/0618A719-92A6-E111-BC38-002618FDA207.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/06851CD7-ABA6-E111-83EB-003048678FAE.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/06C6DC61-ACA6-E111-9733-00261894397A.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/08532E80-F3A6-E111-80CE-003048678F74.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/0CD9D44C-D3A6-E111-8101-002354EF3BDB.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/12BFE524-A4A6-E111-9F82-00304867C1BC.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/18510A28-85A6-E111-B359-001A92810AC6.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/1C98D0F1-B8A6-E111-86C4-002618943957.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/1CA90FBF-8CA6-E111-9B20-0026189438B5.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/24FE2A22-B6A6-E111-ACD4-002618943831.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/26394151-A2A6-E111-970E-002618943972.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/284DB467-8FA6-E111-B705-0030486791F2.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/28A440F7-C6A6-E111-93AD-002354EF3BDB.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/2A4ACF38-A9A6-E111-A5A7-00248C55CC62.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/2C471DBD-87A6-E111-BCF2-0026189438BD.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/2CF284CB-A7A6-E111-A4A3-002618943868.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/3066CFEA-9DA6-E111-985F-002618943923.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/30D20630-ECA6-E111-8FAF-003048678B72.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/32033AEB-A2A6-E111-9883-00261894387E.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/34F73D48-C9A6-E111-8C82-00304867C04E.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/3835DE4C-97A6-E111-A530-00261894396D.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/38FB494B-B7A6-E111-ACEE-0026189438BA.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/3E656F5E-96A6-E111-BEB1-003048678FE0.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/4612590F-B0A6-E111-8249-00261894383E.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/465EFA41-D1A6-E111-BAEA-00261894383B.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/4A64B430-A6A6-E111-A3B9-002618943875.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/4E8CF32E-83A6-E111-8136-002618943934.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/5055B3CB-9CA6-E111-9E51-001A92971B7C.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/541D0906-D7A6-E111-BFA2-003048FFD754.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/58FBB0FF-9EA6-E111-8C08-00248C55CC40.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/5A2ECF77-0AA7-E111-9CFB-00261894386C.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/5CE07F43-D5A6-E111-81A1-00304867915A.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/5E947FFE-B4A6-E111-8B13-003048678B94.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/5EE7569E-E0A6-E111-B772-003048FFCB6A.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/5EEAA147-E4A6-E111-A44C-002618943856.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/6459B481-91A6-E111-940C-002618943980.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/660C1EE9-14A7-E111-8FCF-003048FF86CA.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/66BC83BD-99A6-E111-AFFB-002618943860.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/66DDEAF0-A1A6-E111-BDCE-00261894392B.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/6A4D17F8-9AA6-E111-901F-002618943964.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/6C62AA7A-AFA6-E111-8722-003048D15DDA.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/6E81AFE5-A0A6-E111-AA22-0026189438DB.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/721010D4-CDA6-E111-9D92-003048678F78.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/72B54C50-DEA6-E111-8811-003048678FD6.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/72CFBD5B-C0A6-E111-B5B9-003048679228.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/742D34BA-A4A6-E111-8BFA-0026189438D5.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/7436562E-9CA6-E111-8822-0026189438B4.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/78E3CED0-C5A6-E111-9FD5-002618943980.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/7A66146F-9EA6-E111-A645-0026189437F0.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/7CB948A4-A8A6-E111-9B8A-00304867D838.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/7EE3DCB8-92A6-E111-88A2-002618943944.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/80DD08AD-8AA6-E111-899E-002618FDA21D.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/849DA184-9CA6-E111-9F8D-002618943951.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/8612E7A2-B2A6-E111-9996-00261894390C.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/925769ED-DAA6-E111-9382-00248C55CC97.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/945F1A71-A1A6-E111-9AF3-003048D15D04.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/94B017B6-C2A6-E111-A49F-003048FFD720.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/94BB1DFA-90A6-E111-A09A-002618943930.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/A0BCC1F1-C4A6-E111-A9F1-002354EF3BCE.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/AA6C1E85-89A6-E111-B71F-00261894386B.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/AEFDC7A8-AEA6-E111-8E81-0026189438C4.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/B0EF7828-94A6-E111-BD4E-002618943922.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/B85FDF36-98A6-E111-915E-00261894380A.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/BC3B5536-BBA6-E111-9175-00304867C29C.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/BE0FBF8D-ABA6-E111-8690-002618943880.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/C8281951-93A6-E111-9A68-0018F3D0969A.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/C847A9D1-A9A6-E111-83EB-0026189438BF.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/C8D60EEF-9CA6-E111-B00F-0026189438B4.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/D0E50F77-B1A6-E111-81C2-002618943831.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/D2C3A4E5-DCA6-E111-9E93-003048678FD6.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/D4955C48-CBA6-E111-A5E9-00248C0BE005.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/D628A16D-95A6-E111-BF5F-002618943905.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/D6C7416D-A6A6-E111-B39C-002618943945.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/E2050131-B1A6-E111-91A3-0026189438F4.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/E20C8C56-90A6-E111-9603-003048678FC6.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/E47ED283-A3A6-E111-A4E5-0026189438CC.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/E83F4559-BEA6-E111-81F0-0026189438DB.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/EC1BBD65-AAA6-E111-AE0F-0026189438CF.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/EC2372DC-9EA6-E111-928D-001A92971BDA.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/ECBE0F4A-ADA6-E111-9898-002618943911.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/FA40BA3F-A5A6-E111-B1A4-00261894384F.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/FAB04844-8EA6-E111-951F-003048678A6A.root',
	'/store/data/Run2012A/ElectronHad/AOD/23May2012-v2/0000/FCAD083F-FCA6-E111-B5C8-0026189438B5.root',


   ]                                            ##  (e.g. 'file:AOD.root')
#                                               ##
process.maxEvents.input = 100                    ##  (e.g. -1 to run on all events)
#                                               ##
process.out.outputCommands = [ #'keep *'
			       #'keep *_genParticles_*_*',
			       'keep patMuons_*_*_*',
			       'keep patElectrons_*_*_*', 
			       'keep patTaus_*_*_*', 
			       'keep patJets_*_*_*', 
			       #'keep CaloTowers_*_*_*',
			       'keep patMETs_*_*_*', 
			       'keep doubles_ak5PFJets_*_*', 
			       'keep floatedmValueMap_*_*_*', 
			       'keep recoVertexs_*_*_*',
			       'keep recoTracks_*_*_*',
			       'keep *_TriggerResults_*_*',
			       'keep *_patTrigger_*_*',
			       #'keep PileupSummaryInfos_*_*_*',
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

