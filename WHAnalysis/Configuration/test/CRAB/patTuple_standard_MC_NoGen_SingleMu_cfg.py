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
#        jec.extend([ 'L2L3Residual' ])
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
#removeAllPATObjectsBut(process, ['Muons', 'Electrons', 'Taus', 'METs'])
# removeSpecificPATObjects(process, ['Electrons', 'Muons', 'Taus'])

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
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS")
)

process.electronVariables = cms.EDProducer('ElectronsUserEmbedder',
	electronTag = cms.InputTag("patElectrons"),
	vertexTag = cms.InputTag("offlinePrimaryVerticesWithBS"),
	isMC = cms.bool(True),
	doMVA = cms.bool(True),
	inputFileName0 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet0LowPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName1 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet1LowPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName2 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet2LowPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName3 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet0HighPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName4 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet1HighPt_NoIPInfo_BDTG.weights.xml"),
	inputFileName5 = cms.FileInPath("UserCode/MitPhysics/data/ElectronMVAWeights/Subdet2HighPt_NoIPInfo_BDTG.weights.xml"),

)

process.skimmedMuons = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("muonVariables"),
                         cut = cms.string('pt >= 7. && abs(eta) < 2.5'),
                         filter = cms.bool(True)
                         )

process.skimmedTaus = cms.EDFilter("PATTauSelector",
                         src = cms.InputTag("tauVariables"),
                         cut = cms.string('pt >= 7. && abs(eta) < 2.5'),
                         filter = cms.bool(True)
                         )

process.numTaus = cms.EDFilter("PATCandViewCountFilter",
                     	 src = cms.InputTag("skimmedTaus"),
                     	 maxNumber = cms.uint32(2000000),
                       	 minNumber = cms.uint32(2),
                         filter = cms.bool(True)
                     	 )

## let it run
process.p = cms.Path(
    process.scrapingVeto *
    process.PFTau *
    process.fjSequence *
    process.patDefaultSequence *
    process.muonVariables *
    process.electronVariables *
    process.tauVariables *
    process.skimmedMuons *
    process.skimmedTaus *
    process.numTaus
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

## remove MC matching from the default sequence
#removeMCMatching(process, ['All'])
#runOnData(process)

addPFMuonIsolation(process,process.patMuons)
addPFElectronIsolation(process,process.patElectrons)

#
#process.GlobalTag.globaltag = "START41_V0::All" ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                               ##
process.source.fileNames = [                    ##
	
	#'/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/FED85C0E-A89C-E011-A90D-E0CB4E19F9B7.root',
	#'file:vh120_emt_emu_events.root'
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/5E6BB841-A7F8-E011-95AE-485B39800C1B.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/905B0FB0-A1F8-E011-9293-E0CB4E19F9BD.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/1EB7FB80-B4F8-E011-89B1-001EC9D81A4A.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/BC4089C3-A8F8-E011-921A-00261834B548.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/0870F5FC-B9F8-E011-B97A-E0CB4EA0A8EA.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/12D19FBC-9EF8-E011-8FA3-90E6BAE8CC1C.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/167A26E4-A7F8-E011-B653-00261834B5B1.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/0E9F1594-96F8-E011-9F0A-E0CB4E1A118D.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/58FFDB31-97F8-E011-B89E-485B398971EA.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/4A36FE0C-ADF8-E011-8A08-20CF300E9ECF.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/12A2EBEA-ADF8-E011-B8F7-485B39800BDA.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/BAC098B6-AAF8-E011-949F-90E6BA0D099E.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/C6FBA935-B0F8-E011-9567-00261834B529.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/B864105B-B5F8-E011-B346-E0CB4E19F982.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/364EE1D2-9BF8-E011-AE0D-90E6BA0D0989.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/6C4A5277-AEF8-E011-BAEE-0022198F5AF7.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/50056D35-AAF8-E011-9176-90E6BA0D0996.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/FE743448-A3F8-E011-8BE4-E0CB4E29C513.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/9C8E989B-A7F8-E011-B90C-485B39800C17.root',
	'/store/mc/Fall11/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/AODSIM/PU_S6_START42_V14B-v1/0000/72C689D4-BAF8-E011-B8DD-90E6BA442F0C.root',


   ]                                            ##  (e.g. 'file:AOD.root')
#                                               ##
process.maxEvents.input = 100                    ##  (e.g. -1 to run on all events)
#                                               ##
process.out.outputCommands = [ #'keep *'
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
			       'drop *_genParticles_*_*',
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
			       'drop patMuons_skimmedMuons_*_*',
			       'drop patTaus_skimmedTaus_*_*',
			     ]                  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                               ##
process.out.fileName = 'patTuple.root'          ##  (e.g. 'myTuple.root')
#                                               ##
process.options.wantSummary = False             ##  (to suppress the long output at the end of the job)    



