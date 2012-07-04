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

"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_10_1_T9A.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_11_1_dXd.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_12_1_7Qf.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_13_1_Bg3.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_14_1_Gh7.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_15_1_oU7.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_16_1_ixc.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_17_1_OsM.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_18_1_6xA.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_19_1_h8N.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_1_1_lZB.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_20_1_KHX.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_21_1_mQk.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_22_1_ED3.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_23_1_NCl.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_24_1_m1y.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_25_1_3XG.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_26_1_I43.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_27_1_hBZ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_28_1_HlI.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_29_1_FOK.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_2_1_ogk.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_30_1_fsS.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_31_1_G2j.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_32_1_5pA.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_33_1_1OG.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_34_1_F6f.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_35_1_glb.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_36_1_AN0.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_37_1_GLi.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_38_1_xoy.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_39_1_7p9.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_3_1_Sgz.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_40_1_4Jb.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_41_1_tM0.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_42_1_LQg.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_43_1_g1E.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_44_1_oUv.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_45_1_jjS.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_46_1_s9w.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_47_1_QXv.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_48_1_LZc.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_49_1_oQI.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_4_1_mu3.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_50_1_EKV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_51_1_ruV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_52_1_ZQp.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_53_1_v5z.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_54_1_Vxj.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_55_1_5Y1.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_56_1_zFV.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_57_1_59b.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_58_1_Ihu.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_59_1_UMc.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_5_1_lqW.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_60_1_ECW.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_61_1_EaK.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_62_1_Afp.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_63_1_Khv.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_64_1_In2.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_66_1_OYk.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_67_1_WYg.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_68_1_Hba.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_69_1_xUK.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_6_1_BrJ.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_70_1_OSR.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_71_1_OMN.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_72_1_EBm.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_73_1_6ui.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_74_1_djt.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_75_1_BGe.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_76_1_Hn3.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_77_1_GiR.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_78_1_TLK.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_79_1_37K.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_7_1_8pX.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_80_1_yl6.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_81_1_Poi.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_82_1_o70.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_83_1_Q1N.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_84_1_rmG.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_85_1_BWo.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_86_1_m6z.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_87_1_WmP.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_88_1_pC2.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_89_1_IrI.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_8_1_gVk.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_90_1_hGK.root",
"file:/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/DoubleMuPromptReco6_QCDTau/patTuple_9_1_WDk.root",

        )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

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

process.selectedMuonsForQCDTau = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("producesUserDefinedVarsMu"),
                        cut = cms.string("abs(eta) < 2.1 && userInt('muonID') > 0.5 && userFloat('PFRelIsoDB04v2') > 0.3 && abs(userFloat('dxyWrtPV')) < 0.02 && abs(userFloat('dzWrtPV')) < 0.2"),
                        filter = cms.bool(True)
                        )

process.selectedMuonsForVeto = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("producesUserDefinedVarsMu"),
                        cut = cms.string("pt > 5. && abs(eta) < 2.1 && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

process.leadSubLeadMuons = cms.EDProducer('LeadMuonsProducer',
    			lepSrc = cms.untracked.InputTag("selectedMuonsForQCDTau"),                                                               
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

process.selectedMETMax = cms.EDFilter("PATMETSelector",
     			src = cms.InputTag("patMETsPF"),
     			cut = cms.string('et < 20'),
     			filter = cms.bool(True)
			)

process.MuonHistosCheck = cms.EDAnalyzer("MuonHistManager",
  			muonSrc = cms.untracked.InputTag("selectedMuonsPt1"),
  			vertexSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS"),
  			MCDist = cms.untracked.vdouble(vecMC),
  			TrueDist2011 = cms.untracked.vdouble(vecData),
  			isMC = cms.untracked.bool(False),                                     
			)

process.muonSequence = cms.Sequence(
			process.producesUserDefinedVarsMu *
			process.selectedMuonsForQCDTau *
		  	process.selectedMuonsForVeto *
			process.leadSubLeadMuons *
			process.selectedMuonsPt1 *
			process.selectedMuonsPt2 *
			#process.selectedMuonsVeto *
			process.selectedMETMax *
			process.MuonHistosCheck
			)

process.selectedMuonsCorr1 = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuonsPt1"),
                        cut = cms.string("abs(userFloat('dxyWrtPV')) < 0.02 && abs(userFloat('dzWrtPV')) < 0.2"),
                        filter = cms.bool(True)
                        )

process.selectedMuonsCorr2 = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuonsPt2"),
                        cut = cms.string("abs(userFloat('dxyWrtPV')) < 0.02 && abs(userFloat('dzWrtPV')) < 0.2"),
                        filter = cms.bool(True)
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
# Jet Probe

process.selectedMuProbes1 = cms.EDProducer('MuonVetoProducer',
			lep1Src = cms.untracked.InputTag("producesUserDefinedVarsMu"), #collezione grande
			lep2Src = cms.untracked.InputTag("selectedMuonsCorr1"), #collezione piccola
			)

process.selectedMuProbes2 = cms.EDProducer('MuonVetoProducer',
			lep1Src = cms.untracked.InputTag("selectedMuProbes1"), #collezione grande
			lep2Src = cms.untracked.InputTag("selectedMuonsCorr2"), #collezione piccola
			)

process.selectedTagsBis = cms.EDProducer("CandViewMerger",
       			src = cms.VInputTag("selectedMuonsCorr1","selectedMuonsCorr1")
  			)

process.selectedTauProbesCharge = cms.EDProducer("TauObjSSProducer",
    			obj1Src = cms.untracked.InputTag("tauVariables"),
			obj2Src = cms.untracked.InputTag("selectedTagsBis"),
			)

process.selectedMuProbesChargeBis = cms.EDProducer("MuObjSSProducer",
    			obj1Src = cms.untracked.InputTag("selectedMuProbes2"),
			obj2Src = cms.untracked.InputTag("selectedTagsBis"),
			)

process.selectedEleProbesCharge = cms.EDProducer("EleObjSSProducer",
    			obj1Src = cms.untracked.InputTag("producesUserDefinedVarsEle"),
			obj2Src = cms.untracked.InputTag("selectedTagsBis"),
			)

process.selectedElectronsDeltaR = cms.EDProducer('SelEleByDeltaR',
     			eleSrc = cms.untracked.InputTag("selectedEleProbesCharge"),
     			muonSrc = cms.untracked.InputTag("muonVariables"),                             
     			DeltaRCut = cms.untracked.double(0.3)
			)

process.selectedTausByDeltaR = cms.EDProducer("EleMuSelTauByDeltaR",
     			tauSrc = cms.untracked.InputTag("selectedTauProbesCharge"),
     			lep1Src = cms.untracked.InputTag("electronVariables"),
     			lep2Src = cms.untracked.InputTag("muonVariables"),                             
     			DeltaRCut = cms.untracked.double(0.3)
			)

process.probeSequence = cms.Sequence(
			process.selectedMuProbes1 *
			process.selectedMuProbes2 *
			#process.selectedTags * 
			process.selectedTagsBis *
			#(process.selectedTauProbesCharge + process.selectedMuProbesCharge + process.selectedEleProbesCharge) *
			process.selectedMuProbesChargeBis *
			(process.selectedElectronsDeltaR + process.selectedTausByDeltaR)
			)

#################################################################################################################################
# Denominator

process.selectedProbesDenMuBis = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuProbesChargeBis"),
                        cut = cms.string("pt > 9. && abs(eta) < 2.1 && userInt('muonID') > 0.5 && abs(userFloat('dxyWrtPV')) < 0.02 && abs(userFloat('dzWrtPV')) < 0.2"),
                        filter = cms.bool(False)
                        )

elePreID = "(userInt('antiConv') > 0.5 && userFloat('nHits') < 0.5 && abs(userFloat('dxyWrtPV')) < 0.02 && abs(userFloat('dzWrtPV')) < 0.1 && ((isEB && userFloat('sihih') < 0.01 && userFloat('dEta') < 0.007 && userFloat('dPhi') < 0.15 && userFloat('HoE') < 0.12) || (isEE && userFloat('sihih') < 0.03 && userFloat('dEta') < 0.009 && userFloat('dPhi') < 0.10 && userFloat('HoE') < 0.10)))"

eleIDMVA = "((pt < 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.133) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.465) || (pt < 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.518) || (pt > 20 && abs(superClusterPosition.Eta) >= 0.0 && abs(superClusterPosition.Eta) < 1.0 && userFloat('mva') > 0.942) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.0 && abs(superClusterPosition.Eta) < 1.5 && userFloat('mva') > 0.947) || (pt > 20 && abs(superClusterPosition.Eta) >= 1.5 && abs(superClusterPosition.Eta) < 2.5 && userFloat('mva') > 0.878))"

process.selectedProbesDenEleBis = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsDeltaR:EleSelByDeltaR"),
                        cut = cms.string("pt > 9. && abs(eta) < 2.5 && " + elePreID + " && " + eleIDMVA),
                        filter = cms.bool(False)
                        )

process.selectedProbesDenTauBis = cms.EDFilter("PATTauSelector",
                        src = cms.InputTag("selectedTausByDeltaR:TauSelByDeltaR"),
                        cut = cms.string("pt > 9. && abs(eta) < 2.5 && tauID('decayModeFinding') > 0.5 && tauID('againstMuonTight') > 0.5 && tauID('againstElectronMVA') > 0.5"),
                        filter = cms.bool(False)
                        )

#################################################################################################################################
# Numerator

process.selectedProbesNumMuBis = cms.EDFilter("PATMuonSelector",
                        src = cms.InputTag("selectedMuProbesChargeBis"),
                        cut = cms.string(process.selectedProbesDenMuBis.cut.value() + " && userFloat('PFRelIsoDB04v2') < 0.3"),
                        filter = cms.bool(False)
                        )

process.selectedProbesNumEleBis = cms.EDFilter("PATElectronSelector",
                        src = cms.InputTag("selectedElectronsDeltaR:EleSelByDeltaR"),
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

	'histo_DoubleMuPromptReco6_QCDTau_eleFR.root'

	)
)

process.mypath = cms.Path(
			#process.hltSelection *
			#process.selectedPrimaryVertex *
			#process.muonSequence *
			#process.electronSequence *
			#process.tauSequence *
			#process.jetSequence *
			process.selectedMuonsCorr1 *
			process.selectedMuonsCorr2 *
			process.selectedMuonsVeto *
			#process.selectedElectronsVeto *
			process.selectedTausVeto *
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

