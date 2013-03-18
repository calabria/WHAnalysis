#!/bin/bash

path=/lustre/cms/store/user/calabria/Data/Analisi_53X/ETT

#rm $path/histo_*

for i in `cat ListDirectories.txt`; do

	cd $path/$i
	#echo $path/$i
	hadd $path/histo_$i.root histo_*

done

cd $path
hadd histo_data_FR1.root histo_TauPlusX*FR1*
hadd histo_data_FR2.root histo_TauPlusX*FR2*
hadd histo_data_FR.root histo_TauPlusX*FR*
