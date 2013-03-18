import FWCore.ParameterSet.Config as cms

process = cms.Process("CazziEMazzi")

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.load("VHTauTau.TreeMaker.TreeCreator_cfi")
process.load("VHTauTau.TreeMaker.TreeWriter_cfi")
process.load("VHTauTau.TreeMaker.TreeContentConfig_cff")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string("START53_V16::All")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_34_1_nHK.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_35_1_Piz.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_36_1_Fwf.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_37_1_Bwt.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_38_1_zib.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_39_1_yrj.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_3_1_bqm.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_40_1_KaR.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_41_1_qJF.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_42_1_S20.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_43_1_gdQ.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_44_1_Ly4.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_45_1_JmZ.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_46_1_N4I.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_47_1_TqY.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_48_1_KY0.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_49_1_IEk.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_4_1_OEU.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_50_1_dVO.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_51_1_DiL.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_52_1_r9T.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_53_1_Wzu.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_54_1_8Qd.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_55_1_dKP.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_56_1_Eue.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_57_1_rvI.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_58_1_8Y7.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_59_1_eiJ.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_5_1_16q.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_60_1_9cq.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_61_1_bir.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_62_1_11n.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_63_1_6dH.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_64_1_3bG.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_65_1_dV8.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_66_1_3J1.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_67_1_Nwc.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_68_1_FfB.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_69_1_zZh.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_6_1_l8H.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_70_1_NW2.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_71_1_M9h.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_72_1_bbW.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_73_1_7Rv.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_74_1_y4q.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_75_1_XCz.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_76_1_SPo.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_77_1_6x5.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_78_1_ldl.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_79_1_jlY.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_7_1_lOO.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_80_1_hgp.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_81_1_qYl.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_82_1_stV.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_83_1_18X.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_84_1_FTp.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_85_1_dUo.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_86_1_74H.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_87_1_Y1r.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_88_1_daq.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_89_1_Qza.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_8_1_7wc.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_90_1_vy1.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_91_1_IMt.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_92_1_KKu.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_93_1_dxx.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_94_1_iOc.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_95_1_fKx.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_96_1_Nmy.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_97_1_CTA.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_98_1_Q8w.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_99_1_HEL.root',
'file:/lustre/cms/store/user/rosma/TauLife_537/DYTauTau/patTuple_9_1_oaf.root',

    )
)

process.selectedMuonsPt = cms.EDFilter("PATMuonSelector",
	src = cms.InputTag("skimmedMuons"),
	cut = cms.string("pt > 24. && userFloat('PFRelIsoDB04v2') < 0.1 && abs(eta) < 2.1"),
	filter = cms.bool(True)
)

process.selectedMuonsForVeto = cms.EDFilter("PATMuonSelector",
	src = cms.InputTag("muonVariables"),
	cut = cms.string('pt > 5.'),
	filter = cms.bool(False)
	)

process.NoExtraMuons= cms.EDFilter("PATCandViewCountFilter",
	src = cms.InputTag("selectedMuonsForVeto"),
	maxNumber = cms.uint32(1),
	minNumber = cms.uint32(1),
	filter = cms.bool(True)
	)

process.selectedTausPt = cms.EDFilter("PATTauSelector",
	src = cms.InputTag("skimmedTaus"),
	cut = cms.string('pt > 20.0 && abs(eta) < 2.3'),
	filter = cms.bool(True)
)

process.NoExtraTaus = cms.EDFilter("PATCandViewCountFilter",
	src = cms.InputTag("selectedTausPt"),
	maxNumber = cms.uint32(1),
	minNumber = cms.uint32(1),
	filter = cms.bool(True)
)

process.tauLifeVars = cms.EDProducer('AddUserTauLifeTimeVariables',
	tauSrc = cms.untracked.InputTag("selectedTausPt"),
	muonSrc = cms.untracked.InputTag("selectedMuonsPt"),
	vertexSrc = cms.untracked.InputTag("selectedPrimaryVertices"),
	srcBeamSpot= cms.untracked.InputTag("offlineBeamSpot")
)

selLongDist = "(abs(daughter('mu').vz - daughter('tau').vz) < 0.14)"

process.selectedMuTauPairs = cms.EDProducer("DeltaRMinCandCombiner",
	decay = cms.string('selectedTausPt selectedMuonsPt'),
	cut = cms.string(selLongDist),
	roles = cms.vstring('tau', 'mu'), 
	deltaRMin = cms.double(0.3),
	checkCharge = cms.bool(False))

process.selectedMuTauPairsByChargeOS = cms.EDFilter('ChargeFilter',
	DiTauTag = cms.untracked.InputTag('selectedMuTauPairs'),
	ChargeCut = cms.untracked.int32(0),
	filter = cms.bool(True)
	)

process.selectedPairsByMTOS = cms.EDFilter('MtFilter',
	DiTauTag = cms.untracked.InputTag('selectedMuTauPairsByChargeOS:selectedCand1Cand2PairsByCharge'),
	PFMetTag = cms.untracked.InputTag('patPFMETsTypeIcorrected'),
	MTCut = cms.untracked.double(40),
	particle = cms.untracked.int32(1),
	invertCut = cms.untracked.bool(False),
	filter = cms.bool(True)
)

process.selectedPairsByPZetaOS = cms.EDFilter('PzetaFilter',
	DiTauTag = cms.untracked.InputTag('selectedPairsByMTOS:selectedCand1Cand2PairsMT2'),
	PFMetTag = cms.untracked.InputTag('patPFMETsTypeIcorrected'),
	PzetaCut = cms.untracked.double(-20),
 	#particle = cms.untracked.int32(1),
	CoeffPzeta = cms.untracked.double(1.0),
	CoeffPzetaVis = cms.untracked.double(-1.5),
	filter = cms.bool(True)
)

process.prova = cms.EDProducer("CandViewNtpProducer",
    src = cms.InputTag("tauLifeVars"),
    lazyParser = cms.untracked.bool(True),
    prefix = cms.untracked.string("TauLife"),
    eventInfo = cms.untracked.bool(True),
    variables = cms.VPSet(
    cms.PSet(
    tag = cms.untracked.string("Pt"),
    quantity = cms.untracked.string("pt")
    ),
    cms.PSet(
    tag = cms.untracked.string("Eta"),
    quantity = cms.untracked.string("eta")
    ),
    cms.PSet(
    tag = cms.untracked.string("Phi"),
    quantity = cms.untracked.string("phi")
    ),
    cms.PSet(
    tag = cms.untracked.string("IPxySigLead"),
    quantity = cms.untracked.string("userFloat('IPxySigLead')")
    ),
    cms.PSet(
    tag = cms.untracked.string("distSVPVRef"),
    quantity = cms.untracked.string("userFloat('distSV_PVRef')")
    ),
  )
 )

process.out = cms.OutputModule("PoolOutputModule",
	fileName = cms.untracked.string('myOutputFile.root'),
	outputCommands = cms.untracked.vstring(
		"keep *",
		"keep *_prova_*_*",
    ),
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("histoOS3.root") )  

process.DitauSequenceForOS = cms.Sequence(
	process.selectedMuTauPairsByChargeOS*
	process.selectedPairsByMTOS *
	process.selectedPairsByPZetaOS
	)

process.p = cms.Path(
	process.selectedMuonsPt *
	process.selectedTausPt *
	process.selectedMuTauPairs *
	process.DitauSequenceForOS *
        process.selectedMuonsForVeto *
	process.NoExtraMuons *
	process.NoExtraTaus *
	#process.tauLifeVars *
	#process.prova
	process.treeCreator *
	process.treeContentSequence *
	process.treeWriter 
)

#process.e = cms.EndPath(process.out)
