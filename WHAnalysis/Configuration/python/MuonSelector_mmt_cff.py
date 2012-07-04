import FWCore.ParameterSet.Config as cms
from muonHistos_mmt_cff import *

selectedMuonsEta = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("muonVariables"),
                         cut = cms.string('abs(eta) < 2.1'),
                         filter = cms.bool(True)
                         )

selectedMuonsID = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("selectedMuonsEta"),
                         cut = cms.string("userInt('muonID') > 0.5 && abs(userFloat('dxyWrtPV')) < 0.02 && abs(userFloat('dzWrtPV')) < 0.2"),
                         filter = cms.bool(True)
                         )

selectedMuonsForVeto = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("muonVariables"),
                         cut = cms.string("pt > 5."),
                         filter = cms.bool(True)
                         )

selectedMuonsIso = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("selectedMuonsID"),
                         cut = cms.string("userFloat('PFRelIsoDB04v2') < 0.3"),
                         filter = cms.bool(True)
                         )

leadSubLeadMuons = cms.EDProducer('LeadMuonsProducer',
    			 lepSrc = cms.untracked.InputTag("selectedMuonsIso"),                                                               
			 )

selectedMuonsPt1 = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("leadSubLeadMuons:leadingLeptons"),
                         cut = cms.string('pt > 20.'),
                         filter = cms.bool(True)
                         )

selectedMuonsPt2 = cms.EDFilter("PATMuonSelector",
                         src = cms.InputTag("leadSubLeadMuons:subleadingLeptons"),
                         cut = cms.string('pt > 10.'),
                         filter = cms.bool(True)
                         )

############################### FOR VETO ############################### 

selectedMuonsVeto = cms.EDFilter("PATCandViewCountFilter",
                     	 src = cms.InputTag("selectedMuonsForVeto"),
                     	 maxNumber = cms.uint32(2),
                       	 minNumber = cms.uint32(0),
                         filter = cms.bool(True)
                     	 )

############################### FOR VETO ############################### 

muonSequence = cms.Sequence(selectedMuonsForVeto *
			    MuonHistosBeforeMuonEta *
			    selectedMuonsEta *
			    MuonHistosBeforeMuonID *
			    selectedMuonsID *
			    MuonHistosBeforeMuonIso *
		      	    selectedMuonsIso *
			    MuonHistosAfterMuonIso *
			    leadSubLeadMuons *
			    MuonHistosBeforeMuonPt1 *
			    selectedMuonsPt1 * 
			    MuonHistosAfterMuonPt1 *
			    MuonHistosBeforeMuonPt2 *
			    selectedMuonsPt2 *
			    MuonHistosAfterMuonPt2 *
			    selectedMuonsVeto *
			    MuonHistosBeforeEleSequence
)
