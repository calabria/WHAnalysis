#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/

rm -r ./CFGFiles/EET/DYJetsToLL
rm -r ./CFGFiles/EET/GVJets
rm -r ./CFGFiles/EET/DoubleElectronAug5
rm -r ./CFGFiles/EET/DoubleElectronMay10
rm -r ./CFGFiles/EET/DoubleElectronPromptReco4
rm -r ./CFGFiles/EET/DoubleElectronPromptReco6
rm -r ./CFGFiles/EET/DoubleElectron_Run2011B_PromptReco1
rm -r ./CFGFiles/EET/QCD20_30_BCtoE
rm -r ./CFGFiles/EET/QCD20_30_EM
rm -r ./CFGFiles/EET/QCD30_80_BCtoE
rm -r ./CFGFiles/EET/QCD30_80_EM
rm -r ./CFGFiles/EET/QCD80_170_BCtoE
rm -r ./CFGFiles/EET/QCD80_170_EM
rm -r ./CFGFiles/EET/WJets
rm -r ./CFGFiles/EET/WW
rm -r ./CFGFiles/EET/WZ
rm -r ./CFGFiles/EET/ZZ
rm -r ./CFGFiles/EET/TTJets
rm -r ./CFGFiles/EET/WH_110
rm -r ./CFGFiles/EET/ZH_110
rm -r ./CFGFiles/EET/TTH_110
rm -r ./CFGFiles/EET/WH_115
rm -r ./CFGFiles/EET/ZH_115
rm -r ./CFGFiles/EET/TTH_115
rm -r ./CFGFiles/EET/WH_120
rm -r ./CFGFiles/EET/ZH_120
rm -r ./CFGFiles/EET/TTH_120
rm -r ./CFGFiles/EET/WH_125
rm -r ./CFGFiles/EET/ZH_125
rm -r ./CFGFiles/EET/TTH_125
rm -r ./CFGFiles/EET/WH_130
rm -r ./CFGFiles/EET/ZH_130
rm -r ./CFGFiles/EET/TTH_130
rm -r ./CFGFiles/EET/WH_135
rm -r ./CFGFiles/EET/ZH_135
rm -r ./CFGFiles/EET/TTH_135

mkdir ./CFGFiles/EET/DYJetsToLL
mkdir ./CFGFiles/EET/GVJets
mkdir ./CFGFiles/EET/DoubleElectronAug5
mkdir ./CFGFiles/EET/DoubleElectronMay10
mkdir ./CFGFiles/EET/DoubleElectronPromptReco4
mkdir ./CFGFiles/EET/DoubleElectronPromptReco6
mkdir ./CFGFiles/EET/DoubleElectron_Run2011B_PromptReco1
mkdir ./CFGFiles/EET/QCD20_30_BCtoE
mkdir ./CFGFiles/EET/QCD20_30_EM
mkdir ./CFGFiles/EET/QCD30_80_BCtoE
mkdir ./CFGFiles/EET/QCD30_80_EM
mkdir ./CFGFiles/EET/QCD80_170_BCtoE
mkdir ./CFGFiles/EET/QCD80_170_EM
mkdir ./CFGFiles/EET/TTJets
mkdir ./CFGFiles/EET/WJets
mkdir ./CFGFiles/EET/WW
mkdir ./CFGFiles/EET/WZ
mkdir ./CFGFiles/EET/ZZ
mkdir ./CFGFiles/EET/WH_110
mkdir ./CFGFiles/EET/ZH_110
mkdir ./CFGFiles/EET/TTH_110
mkdir ./CFGFiles/EET/WH_115
mkdir ./CFGFiles/EET/ZH_115
mkdir ./CFGFiles/EET/TTH_115
mkdir ./CFGFiles/EET/WH_120
mkdir ./CFGFiles/EET/ZH_120
mkdir ./CFGFiles/EET/TTH_120
mkdir ./CFGFiles/EET/WH_125
mkdir ./CFGFiles/EET/ZH_125
mkdir ./CFGFiles/EET/TTH_125
mkdir ./CFGFiles/EET/WH_130
mkdir ./CFGFiles/EET/ZH_130
mkdir ./CFGFiles/EET/TTH_130
mkdir ./CFGFiles/EET/WH_135
mkdir ./CFGFiles/EET/ZH_135
mkdir ./CFGFiles/EET/TTH_135

cmsRun batchsubmission_Analysis_EET_cfg.py
