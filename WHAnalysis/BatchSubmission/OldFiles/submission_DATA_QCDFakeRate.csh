#!/bin/bash

rm -r /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuAug05_QCDFakeRate/
rm -r /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuMay10_QCDFakeRate/
rm -r /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuPromptReco4_QCDFakeRate/
rm -r /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuPromptReco6_QCDFakeRate/

mkdir /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuAug05_QCDFakeRate/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuMay10_QCDFakeRate/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuPromptReco4_QCDFakeRate/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_QCDFakeRateSingleMu/SingleMuPromptReco6_QCDFakeRate/

cd /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/SingleMuAug05_QCDFakeRate/

for batch in `ls /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/SingleMuAug05_QCDFakeRate/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/SingleMuMay10_QCDFakeRate/

for batch in `ls /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/SingleMuMay10_QCDFakeRate/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done


cd /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/SingleMuPromptReco4_QCDFakeRate/

for batch in `ls /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/SingleMuPromptReco4_QCDFakeRate/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/SingleMuPromptReco6_QCDFakeRate/

for batch in `ls /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/SingleMuPromptReco6_QCDFakeRate/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done
