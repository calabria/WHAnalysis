#!/bin/bash

pathCMSSW=$CMSSW_BASE/src
pathComp=$pathCMSSW/WHAnalysis/SimpleCounter/CFGFiles/ETT/
cd $pathCMSSW/WHAnalysis/SimpleCounter/CFGFiles/ETT/

for i in `ls -l | awk '{print $9}' | grep 'HS'`; do

	cd $pathComp$i
	echo $PWD
	for batch in `ls $pathComp$i/*.csh`; do

        	chmod 775 ${batch}
        	qsub -q local ${batch}
        	echo $batch "submitted"

	done

done

