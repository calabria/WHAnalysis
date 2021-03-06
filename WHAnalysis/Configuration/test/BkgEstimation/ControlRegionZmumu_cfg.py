import FWCore.ParameterSet.Config as cms
from WHAnalysis.Configuration.weights_cff import *

process = cms.Process("ControlRegionZmumu")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.PyReleaseValidation.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_100_1_0Si.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_101_1_cRc.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_102_1_4Ve.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_103_1_h1y.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_104_1_5dS.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_105_1_rR2.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_106_1_gwX.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_107_1_3NS.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_108_1_uAJ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_109_1_aTF.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_10_1_A7F.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_110_1_eTI.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_111_1_j8C.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_112_1_JU0.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_113_1_jOx.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_114_1_VxL.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_115_1_EbF.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_116_1_90q.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_117_1_nVs.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_118_1_kXT.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_119_1_dhV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_11_1_KFg.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_120_1_tYb.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_121_1_NbD.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_122_1_rh7.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_123_1_2nL.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_124_1_7Vs.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_125_1_zdA.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_126_1_6cS.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_126_2_0Mb.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_127_1_ZRO.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_128_1_kjK.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_129_1_QqS.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_12_1_CFG.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_130_1_raX.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_131_1_rZs.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_132_1_UIx.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_133_1_KSG.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_134_1_cYV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_135_1_p69.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_136_1_roR.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_137_1_JHs.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_138_1_1Fu.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_139_1_x14.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_13_1_wti.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_140_1_D8z.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_141_1_ns0.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_142_1_zGt.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_143_1_d9q.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_144_1_9Xd.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_145_1_yZY.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_146_1_XnL.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_147_1_7y3.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_148_1_K69.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_149_1_uD0.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_14_1_ESY.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_150_1_MDF.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_151_1_kje.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_152_1_jbj.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_153_1_zr2.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_154_1_DvC.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_155_1_Oa1.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_156_1_4kT.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_157_1_sRM.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_158_1_Gxq.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_159_1_nlG.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_15_1_1s4.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_160_1_Fqd.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_161_1_r8q.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_162_1_6MV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_163_1_ErR.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_164_1_yor.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_165_1_GsC.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_166_1_smo.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_167_1_pNY.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_168_1_9Rf.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_16_1_Dns.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_170_1_G1h.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_171_1_G1O.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_173_1_eW2.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_174_1_Wuf.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_175_1_1tI.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_176_1_Y3v.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_177_1_9VV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_178_1_6e2.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_179_1_odX.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_17_1_xo2.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_180_1_Y11.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_181_1_Z8d.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_182_1_XkW.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_183_1_GSo.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_184_1_EzJ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_185_1_acp.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_186_1_IFm.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_187_1_Zj7.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_188_1_LwI.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_189_1_ei4.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_18_1_VXi.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_190_1_tEr.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_191_1_h8r.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_192_1_cns.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_193_1_u0Y.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_194_1_sTq.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_195_1_DiB.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_196_1_psj.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_197_1_k6t.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_198_1_zsx.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_199_1_k8Y.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_19_1_5rQ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_1_1_pWB.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_200_1_igO.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_201_1_Qh4.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_202_1_A2Q.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_203_1_umF.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_204_1_qnm.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_205_1_lwr.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_206_1_q89.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_207_1_PMu.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_208_1_mYV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_209_1_zhy.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_20_1_4AU.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_210_1_iie.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_211_1_1qr.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_212_1_AmK.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_213_1_JFJ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_214_1_tUR.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_215_1_HR7.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_216_1_B2p.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_217_1_7P6.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_218_1_Tb7.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_219_1_U2b.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_21_1_eoq.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_220_1_AQv.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_221_1_G7J.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_222_1_lqP.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_223_1_WCp.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_224_1_1C3.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_225_1_3B9.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_226_1_QCb.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_227_1_JOL.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_228_1_Wpy.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_22_1_H3U.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_23_1_Hkz.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_24_1_gyT.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_25_1_1P8.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_26_1_pN4.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_27_1_9lU.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_28_1_Exf.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_29_1_r9L.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_2_1_alv.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_30_1_L5z.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_31_1_uGz.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_32_1_AC6.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_33_1_vsU.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_34_1_85Y.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_35_1_PDT.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_36_1_wSz.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_37_1_p0K.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_38_1_O2I.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_39_1_Dn4.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_3_1_3bt.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_40_1_Ptf.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_41_1_ok7.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_42_1_j96.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_43_1_j7V.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_44_1_HAo.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_45_1_xGC.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_46_1_rme.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_47_1_4Tu.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_48_1_QZr.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_49_1_eSF.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_4_1_zZG.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_50_1_iB8.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_51_1_kXw.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_52_1_9zQ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_53_1_pbA.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_54_1_IqJ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_55_1_6t6.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_56_1_eYV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_57_1_oIB.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_58_1_99s.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_59_1_EEz.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_5_1_fTQ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_60_1_hzZ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_61_1_3Hz.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_62_1_Tb5.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_63_1_thN.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_64_1_vb7.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_65_1_HOK.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_66_1_08b.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_67_1_N5i.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_68_1_gj9.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_69_1_9df.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_6_1_hn9.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_70_1_qaE.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_71_1_jZ6.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_72_1_7jo.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_73_1_SeG.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_74_1_Kxz.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_75_1_Hq9.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_76_1_xET.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_77_1_iPx.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_78_1_RvE.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_79_1_vXV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_7_1_CAX.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_80_1_mn2.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_81_1_Cmu.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_82_1_WRz.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_83_1_O3q.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_84_1_nC8.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_85_1_sdS.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_86_1_xBf.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_87_1_aqF.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_88_1_ae5.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_89_1_WUg.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_8_1_Xmk.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_90_1_mwe.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_91_1_4b9.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_92_1_QgQ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_93_1_t01.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_94_1_z39.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_95_1_b2x.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_96_1_7lA.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_97_1_elI.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_98_1_ALS.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_99_1_1yw.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMu_Run2011B_PromptReco1_Zmumu/patTuple_9_1_LGQ.root",

        )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#################################################################################################################################

process.load("WHAnalysis.Configuration.GenFilter_cff")

#################################################################################################################################

#PU Correction for MC samples only
isMCBool = cms.bool(False)

#################################################################################################################################

process.out = cms.OutputModule("PoolOutputModule",
                fileName = cms.untracked.string("test.root"),
		outputCommands = cms.untracked.vstring(
		'keep *',
		)
        )

#################################################################################################################################

process.selectedEvents = cms.EDAnalyzer('SelectedEvents',
	path = cms.untracked.string("/cmshome/calabria/")
)

#################################################################################################################################
# Trigger

process.hltSelection = cms.EDFilter("TriggerFilter",
                        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                        HLTPaths = cms.vstring("HLT_DoubleMu7_v","HLT_Mu13_Mu8_v","HLT_Mu17_Mu8_v"),
			defaultTrigger = cms.string("HLT_DoubleMu7_v"),
                        hltEventRanges = cms.VEventRange("160431:MIN-163869:MAX","165088:MIN-178380:MAX","178420:MIN-180252:MAX"),
                        filter = cms.bool(True)
                        )

#################################################################################################################################
# Vertex

process.selectedPrimaryVertex = cms.EDFilter("GoodVertexFilter",
                        vertexCollection = cms.InputTag('offlinePrimaryVerticesWithBS'),
                        minimumNDOF = cms.uint32(7) ,
                        maxAbsZ = cms.double(24),	
                        maxd0 = cms.double(2),
                 	filter = cms.bool(True)	
                        )

#################################################################################################################################
# Muon

process.producesUserDefinedVarsMu = cms.EDProducer('MuonAddUserVariables',
    			objects = cms.InputTag("muonVariables"),
    			met = cms.InputTag("patMETsPF"),
    			triggerResults = cms.InputTag("patTriggerEvent"),
  			triggerPaths = cms.vstring("HLT_DoubleMu7_v","HLT_Mu13_Mu8_v","HLT_Mu17_Mu8_v"), 
  			triggerObjNamesLeg1 =cms.vstring("hltDiMuonL3PreFiltered7","hltSingleMu13L3Filtered13","hltL1Mu3EG5L3Filtered17"), 
  			triggerObjNamesLeg2 = cms.vstring("hltDiMuonL3PreFiltered7","hltDiMuonL3PreFiltered8","hltDiMuonL3PreFiltered8"), 
  			hltEventRanges = cms.VEventRange("160431:MIN-163869:MAX","165088:MIN-178380:MAX","178420:MIN-180252:MAX")
			)

process.selectedMuonsForZmumu = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("producesUserDefinedVarsMu"),
                        cut = cms.string("abs(eta) < 2.1 && userInt('muonID') > 0.5 && userFloat('PFRelIsoDB04v2') < 0.1"),
                        filter = cms.bool(True)
                        )

process.selectedMuonsForVeto = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("producesUserDefinedVarsMu"),
                        cut = cms.string("pt > 5. && abs(eta) < 2.1 && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

process.leadSubLeadMuons = cms.EDProducer('LeadMuonsProducer',
    			lepSrc = cms.untracked.InputTag("selectedMuonsForZmumu"),                                                               
			)

process.selectedMuonsPt1 = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("leadSubLeadMuons:leadingLeptons"),
                        cut = cms.string('pt > 20.'),
                        filter = cms.bool(True)
                        )

process.selectedMuonsPt2 = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("leadSubLeadMuons:subleadingLeptons"),
                        cut = cms.string('pt > 10.'),
                        filter = cms.bool(True)
                        )

process.selectedMuonsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedMuonsForVeto"),
                     	maxNumber = cms.uint32(2),
                       	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
                     	)

process.MuonHistosCheck = cms.EDAnalyzer("MuonHistManager",
  			muonSrc = cms.untracked.InputTag("selectedMuonsPt2"),
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),                                     
			)

process.muonSequence = cms.Sequence(
			process.producesUserDefinedVarsMu *
			process.selectedMuonsForZmumu *
		  	process.selectedMuonsForVeto *
			process.leadSubLeadMuons *
			process.selectedMuonsPt1 *
			process.selectedMuonsPt2 *
			#process.selectedMuonsVeto *
			process.MuonHistosCheck
			)

#################################################################################################################################
# Electrons

process.producesUserDefinedVarsEle = cms.EDProducer('ElectronAddUserVariables',
    			objects = cms.InputTag("electronVariables"),
    			met = cms.InputTag("patMETsPF"),
    			triggerResults = cms.InputTag("patTriggerEvent"),
  			triggerPaths = cms.vstring("HLT_Mu17_Ele8_CaloIdL_v","HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_v"), 
  			triggerObjNamesLeg1 =cms.vstring("hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter","hltMu17Ele8CaloIdTPixelMatchFilter"), 
  			triggerObjNamesLeg2 = cms.vstring("hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter","hltMu17Ele8CaloIdTPixelMatchFilter"),
  			hltEventRanges = cms.VEventRange("160431:MIN-176469:MAX","176545:MIN-180252:MAX")
			)

process.selectedElectronsForVeto = cms.EDFilter("PATElectronSelector",
     			src = cms.InputTag("producesUserDefinedVarsEle"),
                        cut = cms.string("pt > 10. && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

process.selectedElectronsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedElectronsForVeto"),
                     	maxNumber = cms.uint32(0),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
			)

process.electronSequence = cms.Sequence(
			process.producesUserDefinedVarsEle *
			process.selectedElectronsForVeto
			#process.selectedElectronsVeto
			)

#################################################################################################################################
# Taus

process.selectedTausForVeto = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("tauVariables"),
                        cut = cms.string("pt > 20.0 && abs(eta) < 2.5 && tauID('decayModeFinding') > 0.5 && tauID('byLooseCombinedIsolationDeltaBetaCorr') > 0.5"),
                        filter = cms.bool(False)
                        )

process.selectedTausVeto = cms.EDFilter("PATCandViewCountFilter",
                     	src = cms.InputTag("selectedTausForVeto"),
                     	maxNumber = cms.uint32(0),
                     	minNumber = cms.uint32(0),
                        filter = cms.bool(True)
			)

process.tauSequence = cms.Sequence(
			process.selectedTausForVeto
			#process.selectedTausVeto
			)

#################################################################################################################################
# Jets

process.selectedPatJetsForVeto = cms.EDFilter("PATJetSelector",
    			src = cms.InputTag("patJetsAK5PF"),                                                               
    			cut = cms.string("et > 20. && abs(eta) < 2.5 && bDiscriminator('trackCountingHighEffBJetTags') > 3.3"), 
    			filter = cms.bool(False)
			)

process.selectedJetsVeto = cms.EDFilter("PATCandViewCountFilter",
    			src = cms.InputTag("selectedPatJetsForVeto"),
     			maxNumber = cms.uint32(0),
     			minNumber = cms.uint32(0),
     			filter = cms.bool(True)
			)

process.jetSequence = cms.Sequence(
			process.selectedPatJetsForVeto *
			process.selectedJetsVeto
			)

#################################################################################################################################
# Zmumu

process.selectedMu1Mu2 = cms.EDProducer("CandViewShallowCloneCombiner",
                        decay = cms.string("selectedMuonsPt1 selectedMuonsPt2"),                                     
                        roles = cms.vstring('mu1', 'mu2'),
                        cut =  cms.string("mass > 85 && mass < 95"),
                        checkCharge = cms.bool(False)
                        )

process.selectedMu1Mu2Charge = cms.EDFilter("ChargeFilter",
			DiTauTag = cms.untracked.InputTag("selectedMu1Mu2"),
			ChargeCut = cms.untracked.int32(0),
                        filter = cms.bool(True)
			)

process.selectedMETMax = cms.EDFilter("PATMETSelector",
     			src = cms.InputTag("patMETsPF"),
     			cut = cms.string('et < 20'),
     			filter = cms.bool(True)
			)

process.DiTauHistosZmumu = cms.EDAnalyzer("DiTauHistManager",
       			DiTauCand = cms.untracked.InputTag("selectedMu1Mu2"),
       			PFMetTag = cms.untracked.InputTag('patMETsPF'),
       			CoeffPzeta = cms.untracked.double(1.),
       			CoeffPzetaVis = cms.untracked.double(-1.5),
       			MCDist = cms.untracked.vdouble(vecMC),
       			TrueDist2011 = cms.untracked.vdouble(vecData),
       			isMC = cms.untracked.bool(False),
			)

process.zmumuSequence = cms.Sequence(
			process.selectedMu1Mu2 *
			process.selectedMu1Mu2Charge *
			process.selectedMETMax *
			process.DiTauHistosZmumu
			)

#################################################################################################################################
# Jet Probe

process.selectedProbes1 = cms.EDProducer('MuonVetoProducer',
			lep1Src = cms.untracked.InputTag("producesUserDefinedVarsMu"), #collezione grande
			lep2Src = cms.untracked.InputTag("selectedMuonsPt1"), #collezione piccola
)

process.selectedProbes2 = cms.EDProducer('MuonVetoProducer',
			lep1Src = cms.untracked.InputTag("selectedProbes1"), #collezione grande
			lep2Src = cms.untracked.InputTag("selectedMuonsPt2"), #collezione piccola
)

process.selectedMuProbesMT = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedProbes2"),
                        cut = cms.string("userFloat('Mt') < 20."),
                        filter = cms.bool(True)
                        )

process.selectedElectronsDeltaR = cms.EDProducer('SelEleByDeltaR',
     			eleSrc = cms.untracked.InputTag("producesUserDefinedVarsEle"),
     			muonSrc = cms.untracked.InputTag("muonVariables"),                             
     			DeltaRCut = cms.untracked.double(0.3)
			)

process.selectedEleProbesMT = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsDeltaR:EleSelByDeltaR"),
                        cut = cms.string("userFloat('Mt') < 20."),
                        filter = cms.bool(True)
                        )

process.selectedTausByDeltaR = cms.EDProducer("EleMuSelTauByDeltaR",
     			tauSrc = cms.untracked.InputTag("tauVariables"),
     			lep1Src = cms.untracked.InputTag("electronVariables"),
     			lep2Src = cms.untracked.InputTag("muonVariables"),                             
     			DeltaRCut = cms.untracked.double(0.3)
			)

process.probeSequence = cms.Sequence(
			#process.selectedProbes1 * 
			#process.selectedProbes2 *
			process.selectedMuProbesMT *
			process.selectedElectronsDeltaR *
			process.selectedEleProbesMT *
			process.selectedTausByDeltaR
			)

#################################################################################################################################
# Denominator

process.selectedProbesDenMuBis = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuProbesMT"),
                        cut = cms.string("pt > 9. && abs(eta) < 2.1 && userInt('muonID') > 0.5"),
                        filter = cms.bool(False)
                        )

elePreID = "(userInt('antiConv') > 0.5 && userFloat('nHits') < 0.5 && userFloat('dxyWrtPV') < 0.02 && userFloat('dzWrtPV') < 0.1 && ((isEB && userFloat('sihih') < 0.01 && userFloat('dEta') < 0.007 && userFloat('dPhi') < 0.15 && userFloat('HoE') < 0.12) || (isEE && userFloat('sihih') < 0.03 && userFloat('dEta') < 0.009 && userFloat('dPhi') < 0.10 && userFloat('HoE') < 0.10)))"

eleIDMVA = "((pt < 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.133) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.465) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.518) || (pt > 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.942) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.947) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.878))"

process.selectedProbesDenEleBis = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedEleProbesMT"),
                        cut = cms.string("pt > 9. && abs(eta) < 2.5 && " + elePreID + " && " + eleIDMVA),
                        filter = cms.bool(False)
                        )

process.selectedProbesDenTauBis = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
                        cut = cms.string("pt > 10.0 && abs(eta) < 2.5 && tauID('decayModeFinding') > 0.5"),
                        filter = cms.bool(False)
                        )

#################################################################################################################################
# Numerator

process.selectedProbesNumMuBis = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuProbesMT"),
                        cut = cms.string(process.selectedProbesDenMuBis.cut.value() + " && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

process.selectedProbesNumEleBis = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedEleProbesMT"),
                        cut = cms.string(process.selectedProbesDenEleBis.cut.value() + " && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

process.selectedProbesNumTauBis = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
                        cut = cms.string(process.selectedProbesDenTauBis.cut.value() + "&& tauID('byLooseCombinedIsolationDeltaBetaCorr') > 0.5"),
                        filter = cms.bool(False)
                        )

process.fakeRateDenNum = cms.Sequence(
			process.selectedProbesDenMuBis + 
			process.selectedProbesNumMuBis +
			process.selectedProbesDenEleBis + 
			process.selectedProbesNumEleBis +
			process.selectedProbesDenTauBis + 
			process.selectedProbesNumTauBis
			)

#################################################################################################################################
#Plots

process.MuonHistosDenMu = cms.EDAnalyzer("MuonHistManager",
  			muonSrc = cms.untracked.InputTag("selectedProbesDenMuBis"),
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),                                     
			)

process.MuonHistosNumMu = cms.EDAnalyzer("MuonHistManager",
		  	muonSrc = cms.untracked.InputTag("selectedProbesNumMuBis"),
		  	vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
		  	MCDist = cms.untracked.vdouble(vecMC),
		 	TrueDist2011 = cms.untracked.vdouble(vecData),
		 	isMC = cms.untracked.bool(False),                                     
			)

process.EleHistosDenEle = cms.EDAnalyzer("ElectronHistManager",
  			electronSrc = cms.untracked.InputTag("selectedProbesDenEleBis"),
  			muonSrc  = cms.untracked.InputTag("muonVariables"),                                     
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
 		 	MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),
			)

process.EleHistosNumEle = cms.EDAnalyzer("ElectronHistManager",
  			electronSrc = cms.untracked.InputTag("selectedProbesNumEleBis"),
  			muonSrc  = cms.untracked.InputTag("muonVariables"),                                     
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),
			)

process.TauHistosDenTau = cms.EDAnalyzer("TauHistManager",
  			tauSrc = cms.untracked.InputTag("selectedProbesDenTauBis"),
  			lep1Src = cms.untracked.InputTag("electronVariables"),
  			lep2Src = cms.untracked.InputTag("muonVariables"),   
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),       
  			isMC = cms.untracked.bool(False),            
			)

process.TauHistosNumTau = cms.EDAnalyzer("TauHistManager",
  			tauSrc = cms.untracked.InputTag("selectedProbesNumTauBis"),
  			lep1Src = cms.untracked.InputTag("electronVariables"),
  			lep2Src = cms.untracked.InputTag("muonVariables"),   
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),       
  			isMC = cms.untracked.bool(False),            
			)

process.plotSequence = cms.Sequence(
			process.MuonHistosDenMu + 
			process.MuonHistosNumMu + 
			process.EleHistosDenEle + 
			process.EleHistosNumEle +
			process.TauHistosDenTau +
			process.TauHistosNumTau
			)

#################################################################################################################################

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'histo_DoubleMu_Run2011B_PromptReco1_Zmumu.root'

	)
)

process.mypath = cms.Path(
			#process.hltSelection *
			#process.selectedPrimaryVertex *
			#process.muonSequence *
			#process.electronSequence *
			#process.tauSequence *
			#process.jetSequence *
			#process.zmumuSequence *
			process.probeSequence *
			process.fakeRateDenNum *
			process.plotSequence
)

#process.outp1=cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('savep1.root'),
#        SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring('mypath')
#                )
#        )   

#process.outpath = cms.EndPath(process.out)

