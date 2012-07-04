#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/
cmsenv

rm -r SingleMuAug05_QCDFakeRate
rm -r SingleMuMay10_QCDFakeRate
rm -r SingleMuPromptReco4_QCDFakeRate
rm -r SingleMuPromptReco6_QCDFakeRate

mkdir SingleMuAug05_QCDFakeRate
mkdir SingleMuMay10_QCDFakeRate
mkdir SingleMuPromptReco4_QCDFakeRate
mkdir SingleMuPromptReco6_QCDFakeRate

cmsRun batchsubmission_DATA_QCDFakeRate_cfg.py
