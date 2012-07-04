#!/bin/bash

cd /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/G_Pt-1800/

for batch in `ls /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/BatchSubmission/G_Pt-1800/*.csh`; do
        chmod 775 ${batch}
        qsub -q local ${batch}
        echo $batch "submitted"
done

