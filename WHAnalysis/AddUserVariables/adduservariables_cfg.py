import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA/SingleMuAug5_GRID/patTuple_100_1_ZdI.root',
	#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA/SingleMuAug5_GRID/patTuple_101_1_XkI.root',
	#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA/SingleMuAug5_GRID/patTuple_102_1_IuE.root',
	#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA/SingleMuAug5_GRID/patTuple_103_1_q9X.root',
	#'file:/lustre/cms/store/user/calabria/Data/PAT2011_NoSkim_DATA/SingleMuAug5_GRID/patTuple_104_1_CEG.root',

	'file:/cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/Configuration/test/CRAB/patTuple.root'

    )
)

process.myProducerLabel = cms.EDProducer('ElectronAddUserVariables',
    	objects = cms.InputTag("electronVariables"),
    	met = cms.InputTag("patMETsPF"),
    	triggerResults = cms.InputTag("patTriggerEvent"),
  	triggerPaths = cms.vstring("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v","HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v"), 
  	triggerObjNamesLeg1 = cms.vstring("hltEle17CaloIdLCaloIsoVLPixelMatchFilter","hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolFilter"), 
  	triggerObjNamesLeg2 = cms.vstring("hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter","hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolDoubleFilter"),
  	hltEventRanges = cms.VEventRange("160431:MIN-170901:MAX","171050:MIN-180252:MAX")
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
