#!/bin/bash

rm -r /lustre/cms/store/user/calabria/Data/Analisi_53X/ETT/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_53X/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_53X/ETT/

cd $CMSSW_BASE/src/WHAnalysis/BatchSubmission/

for i in `cat ListDirectories.txt`; do

	rm -r ./CFGFiles/ETT/$i
	mkdir ./CFGFiles/ETT/$i

done


cmsRun batchsubmission_Analysis_ETT_cfg.py
