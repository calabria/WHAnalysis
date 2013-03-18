#!/bin/bash

#rm -r /lustre/cms/store/user/calabria/Data/Analisi_53X/ETT_ValFR/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_53X/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_53X/ETT_ValFR/

cd $CMSSW_BASE/src/WHAnalysis/BatchSubmission/FakeRateETT/

for i in `cat ListDirectories.txt`; do

	rm -r ./CFGFiles/ETT_ValFR/$i
	mkdir ./CFGFiles/ETT_ValFR/$i

done


cmsRun batchsubmission_ValFR_ETT_cfg.py
