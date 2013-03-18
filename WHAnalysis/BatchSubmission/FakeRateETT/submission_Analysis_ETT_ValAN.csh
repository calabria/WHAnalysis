#!/bin/bash

path=$CMSSW_BASE/src/WHAnalysis/BatchSubmission/FakeRateETT/CFGFiles/ETT_ValAN

for i in `cat ListDirectories2.txt`; do

	cd $path/$i
	for batch in `ls $path/$i/*.csh`; do

        	chmod 775 ${batch}
        	qsub -q local ${batch}
        	echo $batch "submitted"

	done

done
