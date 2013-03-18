#!/bin/bash

#rm -r /lustre/cms/store/user/calabria/Data/Analisi_53X/ETT_ValAN/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_53X/
mkdir /lustre/cms/store/user/calabria/Data/Analisi_53X/ETT_ValAN/

cd $CMSSW_BASE/src/WHAnalysis/BatchSubmission/FakeRateETT/

for i in `cat ListDirectories2.txt`; do

	rm -r ./CFGFiles/ETT_ValAN/$i
	mkdir ./CFGFiles/ETT_ValAN/$i

done


cmsRun batchsubmission_ValAN_ETT_cfg.py
