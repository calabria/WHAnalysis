import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(500) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
		'file:/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/Configuration/test/CRAB/patTuple.root',
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_1.root',
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_2.root',
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_3.root',
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_4.root',
		#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA_New/patTuple_WH120_lustre_5.root',
    )
)

process.myProducerLabel1 = cms.EDProducer('LeadMuonsProducer',
    lepSrc = cms.untracked.InputTag("muonVariables"),   
)

process.myProducerLabel2 = cms.EDProducer('LeadElectronsProducer',
    lepSrc = cms.untracked.InputTag("electronVariables"),
)

process.myProducerLabel3 = cms.EDProducer('LeadTausProducer',
    lepSrc = cms.untracked.InputTag("tauVariables"),                                     
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.myProducerLabel3)

process.e = cms.EndPath(process.out)
