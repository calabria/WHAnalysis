#!/bin/bash

mkdir /lustre/cms/store/user/calabria/Data/Analisi_Indara/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_Indara/ETT/

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/DYJetsToLL/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/DYJetsToLL/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/DYToEE/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/DYToEE/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/DYToTauTau/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/DYToTauTau/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/GVJets/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/GVJets/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD20_30_BCtoE/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD20_30_BCtoE/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD20_30_EM/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD20_30_EM/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD30_80_BCtoE/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD30_80_BCtoE/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD30_80_EM/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD30_80_EM/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD80_170_BCtoE/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD80_170_BCtoE/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD80_170_EM/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/QCD80_170_EM/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_110/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_110/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_115/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_115/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_120/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_120/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_125/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_125/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_130/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_130/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_135/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTH_135/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_110/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_110/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_115/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_115/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_120/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_120/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_125/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_125/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_130/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_130/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_135/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WH_135/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_110/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_110/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_115/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_115/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_120/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_120/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_125/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_125/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_130/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_130/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_135/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZH_135/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTJets/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TTJets/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WJets/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WJets/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WW/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WW/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WZ/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/WZ/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZZ/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/ZZ/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusXAug5/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusXAug5/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusXMay10/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusXMay10/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusXPromptReco4/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusXPromptReco4/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusXPromptReco6/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusXPromptReco6/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/CFGFiles/ETT/TauPlusX_Run2011B_PromptReco1/*.csh`; do
        chmod 775 ${batch}
        qsub -q  local ${batch}
        echo $batch "submitted"
done

