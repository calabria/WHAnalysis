#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/
cmsenv

cd /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuAug05_QCDFakeRate
hadd /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/histo_SingleMuAug05.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuMay10_QCDFakeRate
hadd /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/histo_SingleMuMay10.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuPromptReco4_QCDFakeRate
hadd /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/histo_SingleMuPromptReco4.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuPromptReco6_QCDFakeRate
hadd /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/histo_SingleMuPromptReco6.root histo_*
