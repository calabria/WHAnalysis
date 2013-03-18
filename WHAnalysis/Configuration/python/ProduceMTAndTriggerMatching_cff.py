import FWCore.ParameterSet.Config as cms

producesUserDefinedVarsEle = cms.EDProducer('ElectronAddUserVariables',
    			objects = cms.InputTag("electronVariables"),
     			genParticles = cms.untracked.InputTag("genParticles"),
			isMC = cms.bool(False),
			particleId = cms.int32(11),
    			met = cms.InputTag("patPFMetByMVA"),
    			triggerResults = cms.InputTag("patTriggerEvent"),
  			triggerPaths = cms.vstring("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v",
					    	   "HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v"), 
  			triggerObjNamesLeg1 =cms.vstring("hltL1sL1EG18erJetCCen28Tau20dPhi1ORL1IsoEG18erJetCCen32Tau24dPhi1",
							 "HLTEle22WP90RhoSequence"), 
  			triggerObjNamesLeg2 = cms.vstring("hltOverlapFilterIsoEle20LooseIsoPFTau20L1Jet",
							  "HLTIsoEleLooseIsoPFTauSequence"),
  			hltEventRanges = cms.VEventRange("190456:MIN-193680:MAX",
						         "193752:MIN-208357:MAX")
			)

producesUserDefinedVarsTau = cms.EDProducer('TauAddUserVariables',
    			objects = cms.InputTag("tauVariables"),
     			genParticles = cms.untracked.InputTag("genParticles"),
			isMC = cms.bool(False),
			particleId = cms.int32(15),
    			met = cms.InputTag("patPFMetByMVA"),
    			triggerResults = cms.InputTag("patTriggerEvent"),
  			triggerPaths = cms.vstring("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v",
					    	   "HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v"), 
  			triggerObjNamesLeg1 =cms.vstring("hltL1sL1EG18erJetCCen28Tau20dPhi1ORL1IsoEG18erJetCCen32Tau24dPhi1",
							 "HLTEle22WP90RhoSequence"), 
  			triggerObjNamesLeg2 = cms.vstring("hltOverlapFilterIsoEle20LooseIsoPFTau20L1Jet",
							  "HLTIsoEleLooseIsoPFTauSequence"),
  			hltEventRanges = cms.VEventRange("190456:MIN-193680:MAX",
						         "193752:MIN-208357:MAX")
			)

producesUserDefinedVarsMu = cms.EDProducer('MuonAddUserVariables',
    			objects = cms.InputTag("muonVariables"),
    			met = cms.InputTag("patPFMetByMVA"),
    			triggerResults = cms.InputTag("patTriggerEvent"),
  			triggerPaths = cms.vstring("HLT_IsoMu24_2p1_v"), 
  			triggerObjNamesLeg1 =cms.vstring("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15"), 
  			triggerObjNamesLeg2 = cms.vstring("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15"), 
  			hltEventRanges = cms.VEventRange("190456:MIN-208357:MAX")
			)
