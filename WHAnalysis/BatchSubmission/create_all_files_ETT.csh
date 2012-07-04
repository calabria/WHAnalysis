#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/

rm -r ./CFGFiles/ETT/DYJetsToLL
rm -r ./CFGFiles/ETT/DYToEE
rm -r ./CFGFiles/ETT/DYToTauTau
rm -r ./CFGFiles/ETT/GVJets
rm -r ./CFGFiles/ETT/TauPlusXAug5
rm -r ./CFGFiles/ETT/TauPlusXMay10
rm -r ./CFGFiles/ETT/TauPlusXPromptReco4
rm -r ./CFGFiles/ETT/TauPlusXPromptReco6
rm -r ./CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1
rm -r ./CFGFiles/ETT/QCD20_30_BCtoE
rm -r ./CFGFiles/ETT/QCD20_30_EM
rm -r ./CFGFiles/ETT/QCD30_80_BCtoE
rm -r ./CFGFiles/ETT/QCD30_80_EM
rm -r ./CFGFiles/ETT/QCD80_170_BCtoE
rm -r ./CFGFiles/ETT/QCD80_170_EM
rm -r ./CFGFiles/ETT/WJets
rm -r ./CFGFiles/ETT/WW
rm -r ./CFGFiles/ETT/WZ
rm -r ./CFGFiles/ETT/ZZ
rm -r ./CFGFiles/ETT/TTJets
rm -r ./CFGFiles/ETT/WH_110
rm -r ./CFGFiles/ETT/ZH_110
rm -r ./CFGFiles/ETT/TTH_110
rm -r ./CFGFiles/ETT/WH_115
rm -r ./CFGFiles/ETT/ZH_115
rm -r ./CFGFiles/ETT/TTH_115
rm -r ./CFGFiles/ETT/WH_120
rm -r ./CFGFiles/ETT/ZH_120
rm -r ./CFGFiles/ETT/TTH_120
rm -r ./CFGFiles/ETT/WH_125
rm -r ./CFGFiles/ETT/ZH_125
rm -r ./CFGFiles/ETT/TTH_125
rm -r ./CFGFiles/ETT/WH_130
rm -r ./CFGFiles/ETT/ZH_130
rm -r ./CFGFiles/ETT/TTH_130
rm -r ./CFGFiles/ETT/WH_135
rm -r ./CFGFiles/ETT/ZH_135
rm -r ./CFGFiles/ETT/TTH_135

mkdir ./CFGFiles/ETT/DYJetsToLL
mkdir ./CFGFiles/ETT/DYToEE
mkdir ./CFGFiles/ETT/DYToTauTau
mkdir ./CFGFiles/ETT/GVJets
mkdir ./CFGFiles/ETT/TauPlusXAug5
mkdir ./CFGFiles/ETT/TauPlusXMay10
mkdir ./CFGFiles/ETT/TauPlusXPromptReco4
mkdir ./CFGFiles/ETT/TauPlusXPromptReco6
mkdir ./CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1
mkdir ./CFGFiles/ETT/QCD20_30_BCtoE
mkdir ./CFGFiles/ETT/QCD20_30_EM
mkdir ./CFGFiles/ETT/QCD30_80_BCtoE
mkdir ./CFGFiles/ETT/QCD30_80_EM
mkdir ./CFGFiles/ETT/QCD80_170_BCtoE
mkdir ./CFGFiles/ETT/QCD80_170_EM
mkdir ./CFGFiles/ETT/TTJets
mkdir ./CFGFiles/ETT/WJets
mkdir ./CFGFiles/ETT/WW
mkdir ./CFGFiles/ETT/WZ
mkdir ./CFGFiles/ETT/ZZ
mkdir ./CFGFiles/ETT/WH_110
mkdir ./CFGFiles/ETT/ZH_110
mkdir ./CFGFiles/ETT/TTH_110
mkdir ./CFGFiles/ETT/WH_115
mkdir ./CFGFiles/ETT/ZH_115
mkdir ./CFGFiles/ETT/TTH_115
mkdir ./CFGFiles/ETT/WH_120
mkdir ./CFGFiles/ETT/ZH_120
mkdir ./CFGFiles/ETT/TTH_120
mkdir ./CFGFiles/ETT/WH_125
mkdir ./CFGFiles/ETT/ZH_125
mkdir ./CFGFiles/ETT/TTH_125
mkdir ./CFGFiles/ETT/WH_130
mkdir ./CFGFiles/ETT/ZH_130
mkdir ./CFGFiles/ETT/TTH_130
mkdir ./CFGFiles/ETT/WH_135
mkdir ./CFGFiles/ETT/ZH_135
mkdir ./CFGFiles/ETT/TTH_135

cmsRun batchsubmission_Analysis_ETT_cfg.py
