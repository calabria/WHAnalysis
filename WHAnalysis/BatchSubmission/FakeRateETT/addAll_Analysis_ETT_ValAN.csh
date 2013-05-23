#!/bin/bash

path=/lustre/cms/store/user/calabria/Data/Analisi_53X/ETT

rm $path/histo_*AN*

for i in `cat ListDirectories2.txt`; do

	cd $path/$i
	#echo $path/$i
	hadd $path/histo_$i.root histo_*

done

cd $path

hadd histo_data_AN1.root histo_TauPlusX*AN1*
