#!/bin/bash

for i in `ls -l /lustre/cms/store/user/calabria/Data/SKIMMING/ETT/ | awk '{print $9}'`; do

	#echo `ls -l /lustre/cms/store/user/calabria/Data/SKIMMING/ETT/ | awk '{print $9}'`
	echo $i
	hadd ./SKIMMING/$i.root /lustre/cms/store/user/calabria/Data/SKIMMING/ETT/$i/*.root

done

