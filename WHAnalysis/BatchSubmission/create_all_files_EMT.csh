#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/

rm -r ./CFGFiles/EMT/DYJetsToLL
rm -r ./CFGFiles/EMT/GVJets
rm -r ./CFGFiles/EMT/MuEGAug5
rm -r ./CFGFiles/EMT/MuEGMay10
rm -r ./CFGFiles/EMT/MuEGPromptReco4
rm -r ./CFGFiles/EMT/MuEGPromptReco6
rm -r ./CFGFiles/EMT/MuEG_Run2011B_PromptReco1
rm -r ./CFGFiles/EMT/QCD20_30_BCtoE
rm -r ./CFGFiles/EMT/QCD20_30_EM
rm -r ./CFGFiles/EMT/QCD30_80_BCtoE
rm -r ./CFGFiles/EMT/QCD30_80_EM
rm -r ./CFGFiles/EMT/QCD80_170_BCtoE
rm -r ./CFGFiles/EMT/QCD80_170_EM
rm -r ./CFGFiles/EMT/QCD_20_MU
rm -r ./CFGFiles/EMT/WJets
rm -r ./CFGFiles/EMT/WW
rm -r ./CFGFiles/EMT/WZ
rm -r ./CFGFiles/EMT/ZZ
rm -r ./CFGFiles/EMT/TTJets
rm -r ./CFGFiles/EMT/WH_110
rm -r ./CFGFiles/EMT/ZH_110
rm -r ./CFGFiles/EMT/TTH_110
rm -r ./CFGFiles/EMT/WH_115
rm -r ./CFGFiles/EMT/ZH_115
rm -r ./CFGFiles/EMT/TTH_115
rm -r ./CFGFiles/EMT/WH_120
rm -r ./CFGFiles/EMT/ZH_120
rm -r ./CFGFiles/EMT/TTH_120
rm -r ./CFGFiles/EMT/WH_125
rm -r ./CFGFiles/EMT/ZH_125
rm -r ./CFGFiles/EMT/TTH_125
rm -r ./CFGFiles/EMT/WH_130
rm -r ./CFGFiles/EMT/ZH_130
rm -r ./CFGFiles/EMT/TTH_130
rm -r ./CFGFiles/EMT/WH_135
rm -r ./CFGFiles/EMT/ZH_135
rm -r ./CFGFiles/EMT/TTH_135

mkdir ./CFGFiles/EMT/DYJetsToLL
mkdir ./CFGFiles/EMT/GVJets
mkdir ./CFGFiles/EMT/MuEGAug5
mkdir ./CFGFiles/EMT/MuEGMay10
mkdir ./CFGFiles/EMT/MuEGPromptReco4
mkdir ./CFGFiles/EMT/MuEGPromptReco6
mkdir ./CFGFiles/EMT/MuEG_Run2011B_PromptReco1
mkdir ./CFGFiles/EMT/QCD20_30_BCtoE
mkdir ./CFGFiles/EMT/QCD20_30_EM
mkdir ./CFGFiles/EMT/QCD30_80_BCtoE
mkdir ./CFGFiles/EMT/QCD30_80_EM
mkdir ./CFGFiles/EMT/QCD80_170_BCtoE
mkdir ./CFGFiles/EMT/QCD80_170_EM
mkdir ./CFGFiles/EMT/QCD_20_MU
mkdir ./CFGFiles/EMT/TTJets
mkdir ./CFGFiles/EMT/WJets
mkdir ./CFGFiles/EMT/WW
mkdir ./CFGFiles/EMT/WZ
mkdir ./CFGFiles/EMT/ZZ
mkdir ./CFGFiles/EMT/WH_110
mkdir ./CFGFiles/EMT/ZH_110
mkdir ./CFGFiles/EMT/TTH_110
mkdir ./CFGFiles/EMT/WH_115
mkdir ./CFGFiles/EMT/ZH_115
mkdir ./CFGFiles/EMT/TTH_115
mkdir ./CFGFiles/EMT/WH_120
mkdir ./CFGFiles/EMT/ZH_120
mkdir ./CFGFiles/EMT/TTH_120
mkdir ./CFGFiles/EMT/WH_125
mkdir ./CFGFiles/EMT/ZH_125
mkdir ./CFGFiles/EMT/TTH_125
mkdir ./CFGFiles/EMT/WH_130
mkdir ./CFGFiles/EMT/ZH_130
mkdir ./CFGFiles/EMT/TTH_130
mkdir ./CFGFiles/EMT/WH_135
mkdir ./CFGFiles/EMT/ZH_135
mkdir ./CFGFiles/EMT/TTH_135

cmsRun batchsubmission_Analysis_EMT_cfg.py
