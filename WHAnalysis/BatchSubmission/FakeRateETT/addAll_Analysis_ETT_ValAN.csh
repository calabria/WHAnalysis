#!/bin/bash

path=/lustre/cms/store/user/calabria/Data/Analisi_53X/ETT

rm $path/histo_*

for i in `cat ListDirectories2.txt`; do

	cd $path/$i
	#echo $path/$i
	hadd $path/histo_$i.root histo_*

done

cd $path

hadd histo_WZ_AN.root histo_WZ*AN*

hadd histo_ZZ_AN.root histo_ZZ*AN*

hadd histo_data_AN1.root histo_TauPlusX*AN1*
hadd histo_data_AN2.root histo_TauPlusX*AN2*
hadd histo_data_AN.root histo_TauPlusX*AN*
