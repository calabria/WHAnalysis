#!/bin/bash

#rm -r /lustre/cms/store/user/calabria/Data/SKIMMING/ETT/
#mkdir /lustre/cms/store/user/calabria/Data/SKIMMING/
#mkdir /lustre/cms/store/user/calabria/Data/SKIMMING/ETT/

cd $CMSSW_BASE/src/WHAnalysis/SimpleCounter/

for i in `cat ListDirectories.txt`; do

	rm -r ./CFGFiles/ETT/$i
	mkdir ./CFGFiles/ETT/$i

done


cmsRun batchsubmission_Analysis_ETT_cfg.py
