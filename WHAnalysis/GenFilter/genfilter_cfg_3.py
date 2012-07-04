import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_560_4_ijD.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_561_2_we2.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_562_2_Irn.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_563_4_Fuz.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_564_1_IMK.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_565_2_fPd.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_566_4_rOH.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_567_2_8NW.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_568_4_Tln.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_569_2_fb9.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_56_2_9nf.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_570_1_t7p.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_571_4_iZT.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_572_4_yEp.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_573_2_3rI.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_574_4_Pf6.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_575_2_o1U.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_576_1_Wvw.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_577_2_Aqg.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_578_2_KHV.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_579_2_vrc.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_57_4_x3p.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_580_4_o7O.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_581_2_KOh.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_582_4_243.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_583_2_vkj.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_584_4_7mR.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_585_2_BO1.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_586_2_bT5.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_587_2_3nv.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_588_4_kLA.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_589_4_wdb.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_58_2_URd.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_590_2_SD4.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_591_4_bNB.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_592_4_agH.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_593_4_8hU.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_594_2_uFW.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_595_2_wVy.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_596_4_YaI.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_597_4_hDi.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_598_4_mGS.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_599_3_Sz6.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_59_1_l4C.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_5_2_ktB.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_600_2_gfa.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_601_1_Aq2.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_602_1_Rlo.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_60_2_E6T.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_61_1_682.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_62_1_xF7.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_63_1_EKs.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_64_3_hnO.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_65_1_lkL.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_66_1_rQp.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_67_1_Xaf.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_68_2_iD9.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_69_1_q0a.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_6_2_31h.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_70_2_ZbU.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_71_2_nf4.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_72_2_zOV.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_73_2_hhi.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_74_2_A4D.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_75_4_sbf.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_76_1_vhd.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_77_1_GWQ.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_78_2_id1.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_79_1_mX2.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_7_1_CTX.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_80_1_xUD.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_81_1_lIw.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_82_1_R09.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_83_4_A81.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_84_1_7vE.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_85_1_2uS.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_86_1_aoX.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_87_4_xMc.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_88_2_2Rh.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_89_2_k8E.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_8_2_VTE.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_90_2_dc7.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_91_2_t6u.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_92_2_bdl.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_93_2_jHc.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_94_1_6b8.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_95_1_O5G.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_96_4_gmY.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_97_1_R5M.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_98_4_QpL.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_99_4_5Lh.root",
"file:/lustre/cms/store/user/calabria/Data/PAT2011/WHHZ/patTuple_9_4_QTa.root",

    )
)

process.load("WHAnalysis.Configuration.VertexSelector_cff")

process.particleListDrawer = cms.EDAnalyzer("ParticleListDrawer",
    	printOnlyHardInteraction = cms.untracked.bool(True),
    	maxEventsToPrint = cms.untracked.int32(-1),
    	src = cms.InputTag('genParticles')
  )

process.demoWH = cms.EDFilter("GenFilter",
	genParticles = cms.untracked.InputTag('genParticles'),
	#particles = cms.untracked.vdouble(24, -24),
	process = cms.untracked.int32(1),
    	filter = cms.bool(False)
)

process.demoTTH = cms.EDFilter("GenFilter",
	genParticles = cms.untracked.InputTag('genParticles'),
	#particles = cms.untracked.vdouble(6, -6),
	process = cms.untracked.int32(3),
    	filter = cms.bool(False)
)

process.demoZH = cms.EDFilter("GenFilter",
	genParticles = cms.untracked.InputTag('genParticles'),
	#particles = cms.untracked.vdouble(23),
	process = cms.untracked.int32(2),
    	filter = cms.bool(False)
)


process.p1 = cms.Path(process.demoWH *
		      process.VertexHistosBeforeSel
		     #* process.particleListDrawer
		     )

process.p2 = cms.Path(process.demoTTH  *
		      process.VertexHistosBeforeSel
		     #* process.particleListDrawer
		     )

process.p3 = cms.Path(process.demoZH *
		      process.VertexHistosBeforeSel
		     #* process.particleListDrawer
		     )

process.TFileService = cms.Service("TFileService", fileName = cms.string(

		"histo.root"

	)
)
