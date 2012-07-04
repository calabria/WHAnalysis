#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/
cmsenv

rm -r DYToEE
rm -r DYToMuMu
rm -r DYToTauTau
rm -r GVJets
rm -r G_Pt-0to15
rm -r G_Pt-120to170
rm -r G_Pt-1400to1800
rm -r G_Pt-15to30
rm -r G_Pt-170to300
rm -r G_Pt-1800
rm -r G_Pt-300to470
rm -r G_Pt-30to50
rm -r G_Pt-470to800
rm -r G_Pt-50to80
rm -r G_Pt-800to1400
rm -r G_Pt-80to120
rm -r MuEGAug05
rm -r MuEGMay10
rm -r MuEGPromptReco4
rm -r MuEGPromptReco6
rm -r MuEG_Run2011B_PromptReco1
rm -r QCD20_30_BCtoE
rm -r QCD20_30_EM
rm -r QCD30_80_BCtoE
rm -r QCD30_80_EM
rm -r QCD80_170_BCtoE
rm -r QCD80_170_EM
rm -r QCD_20_MU
rm -r WJets
rm -r WW
rm -r WZ
rm -r ZZ
rm -r TTJets
rm -r WH_110
rm -r ZH_110
rm -r TTH_110
rm -r WH_115
rm -r ZH_115
rm -r TTH_115
rm -r WH_120
rm -r ZH_120
rm -r TTH_120
rm -r WH_125
rm -r ZH_125
rm -r TTH_125
rm -r WH_130
rm -r ZH_130
rm -r TTH_130
rm -r WH_135
rm -r ZH_135
rm -r TTH_135

mkdir DYToEE
mkdir DYToMuMu
mkdir DYToTauTau
mkdir GVJets
mkdir G_Pt-0to15
mkdir G_Pt-120to170
mkdir G_Pt-1400to1800
mkdir G_Pt-15to30
mkdir G_Pt-170to300
mkdir G_Pt-1800
mkdir G_Pt-300to470
mkdir G_Pt-30to50
mkdir G_Pt-470to800
mkdir G_Pt-50to80
mkdir G_Pt-800to1400
mkdir G_Pt-80to120
mkdir MuEGAug05
mkdir MuEGMay10
mkdir MuEGPromptReco4
mkdir MuEGPromptReco6
mkdir MuEG_Run2011B_PromptReco1
mkdir QCD20_30_BCtoE
mkdir QCD20_30_EM
mkdir QCD30_80_BCtoE
mkdir QCD30_80_EM
mkdir QCD80_170_BCtoE
mkdir QCD80_170_EM
mkdir QCD_20_MU
mkdir TTJets
mkdir WJets
mkdir WW
mkdir WZ
mkdir ZZ
mkdir WH_110
mkdir ZH_110
mkdir TTH_110
mkdir WH_115
mkdir ZH_115
mkdir TTH_115
mkdir WH_120
mkdir ZH_120
mkdir TTH_120
mkdir WH_125
mkdir ZH_125
mkdir TTH_125
mkdir WH_130
mkdir ZH_130
mkdir TTH_130
mkdir WH_135
mkdir ZH_135
mkdir TTH_135

##cmsRun batchsubmission_DYToEE_cfg.py
#cmsRun batchsubmission_DYToMuMu_cfg.py
#cmsRun batchsubmission_DYToTauTau_cfg.py
#cmsRun batchsubmission_GVJets_cfg.py
##cmsRun batchsubmission_G_Pt-0to15_cfg.py
##cmsRun batchsubmission_G_Pt-120to170_cfg.py
##cmsRun batchsubmission_G_Pt-1400to1800_cfg.py
##cmsRun batchsubmission_G_Pt-15to30_cfg.py
##cmsRun batchsubmission_G_Pt-170to300_cfg.py
##cmsRun batchsubmission_G_Pt-1800_cfg.py
##cmsRun batchsubmission_G_Pt-300to470_cfg.py
##cmsRun batchsubmission_G_Pt-30to50_cfg.py
##cmsRun batchsubmission_G_Pt-470to800_cfg.py
##cmsRun batchsubmission_G_Pt-50to80_cfg.py
##cmsRun batchsubmission_G_Pt-800to1400_cfg.py
##cmsRun batchsubmission_G_Pt-80to120_cfg.py
#cmsRun batchsubmission_MuEGAug05_cfg.py
#cmsRun batchsubmission_MuEGMay10_cfg.py
#cmsRun batchsubmission_MuEGPromptReco4_cfg.py
#cmsRun batchsubmission_MuEGPromptReco6_cfg.py
#cmsRun batchsubmission_MuEG_Run2011B_PromptReco1_cfg.py
#cmsRun batchsubmission_QCD20_30_BCtoE_cfg.py
#cmsRun batchsubmission_QCD20_30_EM_cfg.py
#cmsRun batchsubmission_QCD30_80_BCtoE_cfg.py
#cmsRun batchsubmission_QCD30_80_EM_cfg.py
#cmsRun batchsubmission_QCD80_170_BCtoE_cfg.py
#cmsRun batchsubmission_QCD80_170_EM_cfg.py
#cmsRun batchsubmission_QCD_20_MU_cfg.py
#cmsRun batchsubmission_TTJets_cfg.py
#cmsRun batchsubmission_WJets_cfg.py
#cmsRun batchsubmission_WW_cfg.py
#cmsRun batchsubmission_WZ_cfg.py
#cmsRun batchsubmission_ZZ_cfg.py
#cmsRun batchsubmission_TTH_cfg.py
cmsRun batchsubmission_WH_cfg.py
#cmsRun batchsubmission_ZH_cfg.py
