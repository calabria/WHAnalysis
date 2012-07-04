import FWCore.ParameterSet.Config as cms

process = cms.Process("PAT")

## MessageLogger
process.load("VertexSelector_cff")
process.load("TauSelector_cff")
process.load("ElectronSelector_cff")
process.load("MuonSelector_cff")
process.load("JetSelector_cff")
process.load("METSelector_cff")
process.load("MuMETPairSelector_cff")
process.load("EleTauPairSelector_cff")

process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

process.hltHighLevelMuons.TriggerResultsTag = cms.InputTag("TriggerResults","","REDIGI311X")
process.hltHighLevelMuons.HLTPaths = cms.vstring('HLT_Mu21_v1')
process.TriggerHistos.hltResultsSource = cms.InputTag('TriggerResults::REDIGI311X')
process.TriggerHistos.hltPaths = cms.vstring('HLT_Mu21_v1')

#process.hltHighLevelMuons.TriggerResultsTag=cms.InputTag("TriggerResults","","HLT")
#process.TriggerHistos.hltResultsSource=cms.InputTag("TriggerResults","","HLT")
#process.hltHighLevelMuons.HLTPaths = cms.vstring('HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v2') 
#process.TriggerHistos.hltPaths = cms.vstring('HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v2') 

## Options and Output Report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

	#'/store/relval/CMSSW_3_10_0/RelValQCD_FlatPt_15_3000/GEN-SIM-DIGI-RECO/MC_310_V3_FastSim-v1/0051/DCC43514-BB0E-E011-AA59-0018F3D0965C.root'
	#'/store/data/Run2011A/SingleElectron/AOD/PromptReco-v1/000/160/998/2E032978-FA55-E011-A141-001617C3B6CC.root',
	'/store/mc/Spring11/TT_TuneZ2_7TeV-pythia6-tauola/AODSIM/PU_S1_START311_V1G1-v1/0024/982B532F-FE51-E011-B624-00215E222220.root'
    )
    
)

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )
process.load("Configuration.StandardSequences.MagneticField_cff")

## Standard PAT Configuration File
process.load("PhysicsTools.PatAlgos.patSequences_cff")

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

################################################################################################
###    P r e p a r a t i o n      o f    t h e    P A T    O b j e c t s   f r o m    A O D  ###
################################################################################################

## pat sequences to be loaded:
#process.load("PhysicsTools.PFCandProducer.PF2PAT_cff")
#process.load("PhysicsTools.PatAlgos.patSequences_cff")
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
process.patElectrons.usePV = cms.bool(False)
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

process.p = cms.Path(     process.scrapingVeto *
    			  process.PFTau *
			  process.patDefaultSequence *
			  process.vertexSequence *
			  process.muonSequence *
			  process.electronSequence *
			  process.tauSequence *
			  (process.selectedEleTauPairs + process.selectedMuMETPairs) *
			  process.eleTauSequence *
			  process.muMetSequence *
			  process.selectedPatJetsBtag *
			  process.selectedMETMax
)

## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('patTuple.root'),
                               # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('keep *', *patEventContent )
                               )

## remove MC matching from the default sequence
from PhysicsTools.PatAlgos.tools.coreTools import *
#removeMCMatching(process, ['All'])
#removeMCMatching(process, ['METs'], "TC")
#removeMCMatching(process, ['METs'], "PF")
#runOnData(process)

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo.root") )

#process.outpath = cms.EndPath(process.out)

