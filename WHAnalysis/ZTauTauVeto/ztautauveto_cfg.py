import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )
from WHAnalysis.Configuration.weights_cff import *

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_1.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_2.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_3.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_4.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_5.root',
        
    )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.EleHistosBeforeMCMatcher = cms.EDAnalyzer("ElectronHistManager",
  	electronSrc = cms.untracked.InputTag("electronVariables"),
  	muonSrc  = cms.untracked.InputTag("muonVariables"),                                     
  	vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
  	isMC = cms.untracked.bool(False),
)

process.selectedTau1Tau2 = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("tauVariables tauVariables"),                                     
                         roles = cms.vstring('tau1', 'tau2'),
                         cut =  cms.string(""),
                         checkCharge = cms.bool(False)
                         )

process.selectedEleTau1Tau2Cand = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("electronVariables selectedTau1Tau2"),
			 roles = cms.vstring('ele', 'tau1tau2'),
			 cut = cms.string(""),
			 checkCharge = cms.bool(False)
                         )

process.myProducerLabel = cms.EDFilter('ZTauTauVeto',
       			CompCandSrc = cms.untracked.InputTag("selectedEleTau1Tau2Cand"),
        		PFMetTag = cms.untracked.InputTag('patMETsPF'),
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo_prova.root") )

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)
  
process.p = cms.Path(process.EleHistosBeforeMCMatcher * process.selectedTau1Tau2 * process.selectedEleTau1Tau2Cand * process.myProducerLabel)

process.e = cms.EndPath(process.out)
