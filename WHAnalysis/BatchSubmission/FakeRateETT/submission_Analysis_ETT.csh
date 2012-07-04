#!/bin/bash

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXAug5FR1/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXAug5FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXMay10FR1/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXMay10FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXPromptReco4FR1/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXPromptReco4FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXPromptReco6FR1/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXPromptReco6FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1FR1/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

###############################################################################################

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXAug5FR2/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXAug5FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXMay10FR2/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXMay10FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXPromptReco4FR2/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXPromptReco4FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXPromptReco6FR2/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusXPromptReco6FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1FR2/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

