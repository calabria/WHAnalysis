## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *
from WHAnalysis.Configuration.customizePAT import *

process.MessageLogger.cerr.FwkReport.reportEvery = 5000

process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

## ------------------------------------------------------
#  NOTE: you can use a bunch of core tools of PAT to
#  taylor your PAT configuration; for a few examples
#  uncomment the lines below
## ------------------------------------------------------
from PhysicsTools.PatAlgos.tools.coreTools import *

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')

process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")
process.pfJetMETcorr.offsetCorrLabel = cms.string("ak5PFL1Fastjet")
process.pfJetMETcorr.jetCorrLabel = cms.string("ak5PFL1FastL2L3Residual")

#--------------------------------------------------------------------------------

#process.load('RecoJets.Configuration.RecoPFJets_cff')
process.kt6PFJets.doRhoFastjet = True
process.kt6PFJets.Rho_EtaMax = cms.double(4.4)
#process.kt6PFJets.Ghost_EtaMax = cms.double(5.0)
process.ak5PFJets.doAreaFastjet = True
process.ak5PFJets.Rho_EtaMax = cms.double(4.4)
#process.ak5PFJets.Ghost_EtaMax = cms.double(5.0)

## re-run kt4PFJets within lepton acceptance to compute rho
process.load('RecoJets.JetProducers.kt4PFJets_cfi')
process.kt6PFJetsCentral = process.kt4PFJets.clone( rParam = 0.6, doRhoFastjet = True )
process.kt6PFJetsCentral.Rho_EtaMax = cms.double(2.5)

process.fjSequence = cms.Sequence(process.kt6PFJets+process.ak5PFJets+process.kt6PFJetsCentral)

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
switchToPFTauHPS(process) # For HPS Taus
#switchToPFTauHPSpTaNC(process) # For HPS TaNC Taus  

# require scraping filter
process.scrapingVeto = cms.EDFilter("FilterOutScraping",
	applyfilter = cms.untracked.bool(True),
	debugOn = cms.untracked.bool(False),
	numtrack = cms.untracked.uint32(10),
	thresh = cms.untracked.double(0.2)
)

addSelectedPFlowParticle(process)

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
        target = cms.string("2011Data"),

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
        target = cms.string("2011Data"),

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
process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3Residual")
#process.pfMEtMVA.srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatTaus")
process.pfMEtMVA.srcLeptons = cms.VInputTag('cleanPatElectrons', 'cleanPatMuons', 'cleanPatTaus')

process.patPFMetByMVA = process.patMETs.clone(
	metSource = cms.InputTag('pfMEtMVA'),
	addMuonCorrections = cms.bool(False),
	addGenMET = cms.bool(False),
	genMETSource = cms.InputTag('genMetTrue')
)

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
    	process.PFTau *
    	process.fjSequence *
    	process.patDefaultSequence *
  	process.producePFMETCorrections *
    	process.muonVariables *
    	process.electronVariables *
    	process.tauVariables *
    	process.puJetIdSqeuence *
    	process.pfMEtMVAsequence *
    	process.patPFMetByMVA *
	process.patPFMETsTypeIcorrected *
    	process.skimmedElectrons *
    	process.skimmedTaus *
    	process.numTaus
)

## remove MC matching from the default sequence
#removeMCMatching(process, ['All'])
#runOnData(process)

addPFMuonIsolation(process,process.patMuons)
addPFElectronIsolation(process,process.patElectrons)

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

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
process.GlobalTag.globaltag =  "GR_R_42_V23::All"     ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                          ##
process.source.fileNames = [               ##

	'/store/data/Run2011A/DoubleElectron/AOD/May10ReReco-v1/0000/FEC58701-A07B-E011-A797-001A92971BC8.root'


   ]                                       ##  (e.g. 'file:AOD.root')
#                                          ##
process.maxEvents.input = 500              ##  (e.g. -1 to run on all events)
#                                          ##
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
			     ]             ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                          ##
process.out.fileName = 'patTuple.root'     ##  (e.g. 'myTuple.root')
#                                          ##
process.options.wantSummary = False        ##  (to suppress the long output at the end of the job)    

