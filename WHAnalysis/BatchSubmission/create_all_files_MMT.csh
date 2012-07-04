#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/

rm -r ./CFGFiles/MMT/DYJetsToLL
rm -r ./CFGFiles/MMT/DoubleMuAug5
rm -r ./CFGFiles/MMT/DoubleMuMay10
rm -r ./CFGFiles/MMT/DoubleMuPromptReco4
rm -r ./CFGFiles/MMT/DoubleMuPromptReco6
rm -r ./CFGFiles/MMT/DoubleMu_Run2011B_PromptReco1
rm -r ./CFGFiles/MMT/QCD_20_MU
rm -r ./CFGFiles/MMT/WJets
rm -r ./CFGFiles/MMT/WW
rm -r ./CFGFiles/MMT/WZ
rm -r ./CFGFiles/MMT/ZZ
rm -r ./CFGFiles/MMT/TTJets
rm -r ./CFGFiles/MMT/WH_110
rm -r ./CFGFiles/MMT/ZH_110
rm -r ./CFGFiles/MMT/TTH_110
rm -r ./CFGFiles/MMT/WH_115
rm -r ./CFGFiles/MMT/ZH_115
rm -r ./CFGFiles/MMT/TTH_115
rm -r ./CFGFiles/MMT/WH_120
rm -r ./CFGFiles/MMT/ZH_120
rm -r ./CFGFiles/MMT/TTH_120
rm -r ./CFGFiles/MMT/WH_125
rm -r ./CFGFiles/MMT/ZH_125
rm -r ./CFGFiles/MMT/TTH_125
rm -r ./CFGFiles/MMT/WH_130
rm -r ./CFGFiles/MMT/ZH_130
rm -r ./CFGFiles/MMT/TTH_130
rm -r ./CFGFiles/MMT/WH_135
rm -r ./CFGFiles/MMT/ZH_135
rm -r ./CFGFiles/MMT/TTH_135

mkdir ./CFGFiles/MMT/DYJetsToLL
mkdir ./CFGFiles/MMT/DoubleMuAug5
mkdir ./CFGFiles/MMT/DoubleMuMay10
mkdir ./CFGFiles/MMT/DoubleMuPromptReco4
mkdir ./CFGFiles/MMT/DoubleMuPromptReco6
mkdir ./CFGFiles/MMT/DoubleMu_Run2011B_PromptReco1
mkdir ./CFGFiles/MMT/QCD_20_MU
mkdir ./CFGFiles/MMT/TTJets
mkdir ./CFGFiles/MMT/WJets
mkdir ./CFGFiles/MMT/WW
mkdir ./CFGFiles/MMT/WZ
mkdir ./CFGFiles/MMT/ZZ
mkdir ./CFGFiles/MMT/WH_110
mkdir ./CFGFiles/MMT/ZH_110
mkdir ./CFGFiles/MMT/TTH_110
mkdir ./CFGFiles/MMT/WH_115
mkdir ./CFGFiles/MMT/ZH_115
mkdir ./CFGFiles/MMT/TTH_115
mkdir ./CFGFiles/MMT/WH_120
mkdir ./CFGFiles/MMT/ZH_120
mkdir ./CFGFiles/MMT/TTH_120
mkdir ./CFGFiles/MMT/WH_125
mkdir ./CFGFiles/MMT/ZH_125
mkdir ./CFGFiles/MMT/TTH_125
mkdir ./CFGFiles/MMT/WH_130
mkdir ./CFGFiles/MMT/ZH_130
mkdir ./CFGFiles/MMT/TTH_130
mkdir ./CFGFiles/MMT/WH_135
mkdir ./CFGFiles/MMT/ZH_135
mkdir ./CFGFiles/MMT/TTH_135

cmsRun batchsubmission_Analysis_MMT_cfg.py
