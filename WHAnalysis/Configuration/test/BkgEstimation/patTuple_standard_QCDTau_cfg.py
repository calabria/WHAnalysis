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

#--------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.tools.jetTools import *

jec = [ 'L1FastJet', 'L2Relative', 'L3Absolute' ]
#if not isMC:
jec.extend([ 'L2L3Residual' ])
addJetCollection(process, cms.InputTag('ak5PFJets'),
     'AK5', 'PF',
     doJTA            = True,
     doBTagging       = True,
     jetCorrLabel     = ('AK5PF', cms.vstring(jec)),
     doType1MET       = False,
     doL1Cleaning     = True,
     doL1Counters     = False,
     genJetCollection = cms.InputTag("ak5GenJets"),
     doJetID          = True,
     jetIdLabel       = "ak5",
     outputModule     = ''
)

#--------------------------------------------------------------------------------

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

process.load('RecoJets.Configuration.RecoPFJets_cff')
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

## remove certain objects from the default sequence
# removeAllPATObjectsBut(process, ['Muons'])
# removeSpecificPATObjects(process, ['Electrons', 'Muons', 'Taus'])

from PhysicsTools.PatAlgos.tools.tauTools import *
switchToPFTauHPS(process) # For HPS Taus
#switchToPFTauHPSpTaNC(process) # For HPS TaNC Taus

addSelectedPFlowParticle(process)

process.tauVariables = cms.EDProducer('TausUserEmbedded',
	tauTag = cms.InputTag("patTaus"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS")
)

process.muonVariables = cms.EDProducer('MuonsUserEmbedded',
	muonTag = cms.InputTag("patMuons"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS")
)

process.electronVariables = cms.EDProducer('ElectronsUserEmbedder',
	electronTag = cms.InputTag("patElectrons"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS"),
	isMC = cms.bool(False),
	doMVA = cms.bool(True),
	inputFileName0 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet0LowPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName1 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet1LowPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName2 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet2LowPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName3 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet0HighPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName4 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet1HighPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName5 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet2HighPt_NoIPInfo_BDTG.weights.xml"),
)

# require scraping filter
process.scrapingVeto = cms.EDFilter("FilterOutScraping",
                                    applyfilter = cms.untracked.bool(True),
                                    debugOn = cms.untracked.bool(False),
                                    numtrack = cms.untracked.uint32(10),
                                    thresh = cms.untracked.double(0.2)
                                    )

process.load("WHAnalysis.Configuration.controlRegionQCDTau_cff")

## let it run
process.p = cms.Path(
    process.scrapingVeto *
    process.PFTau *
    process.fjSequence *
    process.patDefaultSequence *
    process.muonVariables *
    process.electronVariables *
    process.tauVariables *
    process.qcdTauSequence
    )

################################################################################################
###    P r e p a r a t i o n      o f    t h e    P A T    O b j e c t s   f r o m    A O D  ###
################################################################################################

## pat sequences to be loaded:
#process.load("PhysicsTools.PFCandProducer.PF2PAT_cff")
process.load("PhysicsTools.PatAlgos.patSequences_cff")
#process.load("PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff")
                       
# load the coreTools of PAT
from PhysicsTools.PatAlgos.tools.metTools import *
addTcMET(process, 'TC')
addPfMET(process, 'PF')

## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## modify the final pat sequence: keep only electrons + METS (muons are needed for met corrections)
process.load("RecoEgamma.EgammaIsolationAlgos.egammaIsolationSequence_cff")
#process.patElectronIsolation = cms.Sequence(process.egammaIsolationSequence)

process.patElectrons.isoDeposits = cms.PSet()
process.patElectrons.userIsolation = cms.PSet()
process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
    simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
    simpleEleId80relIso= cms.InputTag("simpleEleId80relIso"),
    simpleEleId70relIso= cms.InputTag("simpleEleId70relIso"),
    simpleEleId60relIso= cms.InputTag("simpleEleId60relIso"),
    simpleEleId95cIso= cms.InputTag("simpleEleId95cIso"),
    simpleEleId90cIso= cms.InputTag("simpleEleId90cIso"),
    simpleEleId85cIso= cms.InputTag("simpleEleId85cIso"),
    simpleEleId80cIso= cms.InputTag("simpleEleId80cIso"),
    simpleEleId70cIso= cms.InputTag("simpleEleId70cIso"),
    simpleEleId60cIso= cms.InputTag("simpleEleId60cIso"),    
    )
##
process.patElectrons.addGenMatch = cms.bool(False)
process.patElectrons.embedGenMatch = cms.bool(False)
#process.patElectrons.usePV = cms.bool(False)
##
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")
# you have to tell the ID that it is data
process.simpleEleId95relIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId90relIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId85relIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId80relIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId70relIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId60relIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId95cIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId90cIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId85cIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId80cIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId70cIso.dataMagneticFieldSetUp = cms.bool(True)
process.simpleEleId60cIso.dataMagneticFieldSetUp = cms.bool(True)
#
process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.makePatElectrons = cms.Sequence(process.patElectronIDs*process.patElectrons)
# process.makePatMuons may be needed depending on how you calculate the MET
#process.makePatCandidates = cms.Sequence(process.makePatElectrons+process.makePatMETs)
#process.patDefaultSequence = cms.Sequence(process.makePatCandidates)
##
##  ################################################################################

# Switch on PAT trigger
from PhysicsTools.PatAlgos.tools.trigTools import switchOnTrigger
#switchOnTrigger( process )

addPFMuonIsolation(process,process.patMuons)
addPFElectronIsolation(process,process.patElectrons)

## remove MC matching from the default sequence
removeMCMatching(process, ['All'])
removeMCMatching(process, ['METs'], "TC")
removeMCMatching(process, ['METs'], "PF")

process.patDefaultSequence.remove(process.patJetPartonMatch)
process.patDefaultSequence.remove(process.patJetPartonMatchAK5PF)
process.patDefaultSequence.remove(process.patJetGenJetMatchAK5PF)
process.patDefaultSequence.remove(process.patJetFlavourId)
process.patDefaultSequence.remove(process.patJetPartons)
process.patDefaultSequence.remove(process.patJetPartonAssociation)
process.patDefaultSequence.remove(process.patJetPartonAssociationAK5PF)
process.patDefaultSequence.remove(process.patJetFlavourAssociation)
process.patDefaultSequence.remove(process.patJetFlavourAssociationAK5PF)

runOnData(process)

from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger( process )
process.patTriggerEvent.processName = '*'

if hasattr(process,"patTrigger"):
    process.patTrigger.processName = '*'

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#   process.GlobalTag.globaltag =  ...     ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                          ##
process.source.fileNames = [               ##

	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/0091950D-688B-E011-9A67-003048D2BB90.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/02549944-5E8B-E011-8C5E-001D09F24EE3.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/0A725875-1B8B-E011-B034-001D09F25438.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/0A92BC74-B08B-E011-8191-000423D33970.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/160936CD-158B-E011-8237-001D09F241B9.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/18E33E52-B08B-E011-ACE1-001617DC1F70.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/322CAC42-638B-E011-8FF2-001D09F25438.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/428EF007-1F8B-E011-ACD2-001D09F24353.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/4E0F1105-1F8B-E011-8EB5-001D09F25401.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/4EAB76D3-A38B-E011-AA3A-003048F024E0.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/54D58C97-998B-E011-B998-001D09F2437B.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/5CCF7A58-208B-E011-AA65-001D09F29114.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/600351F9-B18B-E011-8C83-0030487CAEAC.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/6473A1D4-A38B-E011-8D22-0030487C8CB6.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/7EADAB63-4D8B-E011-AA8A-001D09F24D67.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/8097E591-2B8B-E011-A176-0019B9F730D2.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/8EF2FE21-288B-E011-A378-001D09F295FB.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/989F4093-868B-E011-8111-003048F117B6.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/9EC08D3C-B98B-E011-AF0F-003048F118C6.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/B4451B50-918B-E011-96FE-003048D2C1C4.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/C832283D-B98B-E011-9E11-003048F11C28.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/CE9CA5F4-CD8B-E011-B4B3-0030487A1884.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/DEF71D3A-508B-E011-8EE8-0030487CD7E0.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/EE71F5AC-538B-E011-A97B-001D09F25041.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/EE870205-1F8B-E011-9A48-003048F11942.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/F6BE07E4-238B-E011-83DA-003048F1C832.root',
	'/store/data/Run2011A/DoubleMu/AOD/PromptReco-v4/000/165/993/F8F79DEB-C28B-E011-AFBB-0030487CD906.root',


   ]                                       ##  (e.g. 'file:AOD.root')
#                                          ##
process.maxEvents.input = 1000             ##  (e.g. -1 to run on all events)
#                                          ##
process.out.outputCommands = [ 'keep *'      
			     ]             ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                          ##
process.out.fileName = 'patTuple.root'     ##  (e.g. 'myTuple.root')
#                                          ##
process.options.wantSummary = False        ##  (to suppress the long output at the end of the job)    

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'histo.root'

	)
)

