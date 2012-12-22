import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string("START53_V11::All")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_100_1_NQH.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_101_1_ECF.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_102_1_Wyc.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_103_2_Scl.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_104_1_Bh4.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_105_1_pnt.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_106_1_xTC.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_107_1_Gry.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_108_1_j4z.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_109_1_ruT.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_10_1_lAG.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_110_1_MwY.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_111_1_vfx.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_112_1_lzV.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_113_1_bVM.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_114_1_9Am.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_115_1_LXb.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_116_1_5WC.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_117_1_pTr.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_119_1_oMq.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_11_1_bwl.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_120_1_iF8.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_121_1_lUm.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_123_1_Obt.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_124_1_6BK.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_126_1_C6R.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_127_1_j13.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_128_1_vnJ.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_129_1_8Qh.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_12_1_QBf.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_130_1_Tnf.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_131_1_W82.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_132_1_l16.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_133_1_pQp.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_134_1_SAT.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_135_1_Tug.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_136_2_kfX.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_137_2_DFc.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_138_2_upA.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_139_2_Kc8.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_13_1_rPN.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_140_2_4PV.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_141_2_cFm.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_142_2_CJE.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_143_2_pCX.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_144_2_GUy.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_145_2_9Ty.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_146_2_1FI.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_147_2_AzW.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_149_2_6AV.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_14_1_lSr.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_150_2_JN5.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_151_2_I9R.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_152_2_GW6.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_153_2_jWq.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_154_2_qyb.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_155_2_GKC.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_156_2_mDR.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_157_2_YJA.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_158_2_fXR.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_159_2_30d.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_15_1_UeO.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_160_2_Qtx.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_161_2_DR9.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_162_2_gwm.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_163_2_BMe.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_164_2_KDa.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_165_2_IP2.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_166_2_qxX.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_167_2_96D.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_168_2_etR.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_169_2_Kcf.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_16_1_wg1.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_170_2_vCi.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_171_2_Seh.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_172_2_dTj.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_173_2_u0u.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_174_2_hAj.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_175_2_DLv.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_176_2_wzk.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_177_2_Ag5.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_178_2_PIf.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_179_2_sm7.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_17_1_F0t.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_180_2_Zuq.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_181_2_hhh.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_182_2_1WI.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_183_2_48r.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_184_2_klk.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_185_2_jpe.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_186_2_Ewk.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_187_2_FkS.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_188_2_HSC.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_189_2_fNz.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_18_1_SWz.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_190_2_NIr.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_191_2_xQb.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_192_2_nmn.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_193_2_83j.root', 
	'file:/lustre/cms/store/user/rosma/TauLife_53X/DYTauTau/patTuple_194_2_7BZ.root', 


    )
)


process.tauLifeVars = cms.EDProducer('AddUserTauLifeTimeVariables',
    tauSrc = cms.untracked.InputTag("skimmedTaus"),
    muonSrc = cms.untracked.InputTag("skimmedMuons"),
    vertexSrc = cms.untracked.InputTag("selectedPrimaryVertices"),
    srcBeamSpot= cms.untracked.InputTag("offlineBeamSpot")

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
      "drop *",
      "keep *_prova_*_*",
    ),
)

  
process.p = cms.Path(process.tauLifeVars * process.prova)

process.e = cms.EndPath(process.out)
