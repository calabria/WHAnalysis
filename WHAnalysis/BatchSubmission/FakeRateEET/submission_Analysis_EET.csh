#!/bin/bash

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronAug5FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronMay10FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronPromptReco4FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronPromptReco6FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectron_Run2011B_PromptReco1FR1/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

###############################################################################################

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronAug5FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronMay10FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronPromptReco4FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronPromptReco6FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectron_Run2011B_PromptReco1FR2/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

###############################################################################################

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronAug5QCD/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronMay10QCD/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronPromptReco4QCD/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectronPromptReco6QCD/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/FakeRateEET/CFGFiles/EET/DoubleElectron_Run2011B_PromptReco1QCD/*.csh`; do
        chmod 775 ${batch}
        qsub -q veryshort ${batch}
        echo $batch "submitted"
done
