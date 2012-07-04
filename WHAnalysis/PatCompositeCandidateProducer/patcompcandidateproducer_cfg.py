import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_85_2_wps.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_86_3_iXN.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_87_2_oXJ.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_88_1_uFP.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_8_1_1UJ.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_90_1_1xk.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_92_1_uqo.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_93_2_br2.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_95_1_Hpt.root',
		'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_MC_ETT/WH_120_ETT_3/patTuple_96_1_zns.root',

    )
)

process.myProducerLabel = cms.EDProducer('EleTauTauPatCompositeCandidateProducer',
  	lep1Src = cms.untracked.InputTag("electronVariables"),
  	lep2Src = cms.untracked.InputTag("tauVariables"),
  	lep3Src = cms.untracked.InputTag("tauVariables"),
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
