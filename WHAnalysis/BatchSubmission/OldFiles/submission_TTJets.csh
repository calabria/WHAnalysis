#!/bin/bash

cd /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TTJets/

for batch in `ls /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/WHAnalysis/BatchSubmission/TTJets/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

