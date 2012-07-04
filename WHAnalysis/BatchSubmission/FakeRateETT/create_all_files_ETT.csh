#!/bin/csh

rm -r ./CFGFiles/ETT/TauPlusXAug5FR1
rm -r ./CFGFiles/ETT/TauPlusXMay10FR1
rm -r ./CFGFiles/ETT/TauPlusXPromptReco4FR1
rm -r ./CFGFiles/ETT/TauPlusXPromptReco6FR1
rm -r ./CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1FR1

rm -r ./CFGFiles/ETT/TauPlusXAug5FR2
rm -r ./CFGFiles/ETT/TauPlusXMay10FR2
rm -r ./CFGFiles/ETT/TauPlusXPromptReco4FR2
rm -r ./CFGFiles/ETT/TauPlusXPromptReco6FR2
rm -r ./CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1FR2

rm -r ./CFGFiles/ETT/TauPlusXAug5DC
rm -r ./CFGFiles/ETT/TauPlusXMay10DC
rm -r ./CFGFiles/ETT/TauPlusXPromptReco4DC
rm -r ./CFGFiles/ETT/TauPlusXPromptReco6DC
rm -r ./CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1DC

mkdir ./CFGFiles/ETT/TauPlusXAug5FR1
mkdir ./CFGFiles/ETT/TauPlusXMay10FR1
mkdir ./CFGFiles/ETT/TauPlusXPromptReco4FR1
mkdir ./CFGFiles/ETT/TauPlusXPromptReco6FR1
mkdir ./CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1FR1

mkdir ./CFGFiles/ETT/TauPlusXAug5FR2
mkdir ./CFGFiles/ETT/TauPlusXMay10FR2
mkdir ./CFGFiles/ETT/TauPlusXPromptReco4FR2
mkdir ./CFGFiles/ETT/TauPlusXPromptReco6FR2
mkdir ./CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1FR2

mkdir ./CFGFiles/ETT/TauPlusXAug5DC
mkdir ./CFGFiles/ETT/TauPlusXMay10DC
mkdir ./CFGFiles/ETT/TauPlusXPromptReco4DC
mkdir ./CFGFiles/ETT/TauPlusXPromptReco6DC
mkdir ./CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1DC

cmsRun batchsubmission_Analysis_ETT_cfg.py
