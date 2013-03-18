#!/bin/bash

path=/lustre/cms/store/user/calabria/Data/Analisi_53X/ETT

rm $path/histo_*

for i in `cat ListDirectories.txt`; do

	cd $path/$i
	#echo $path/$i
	hadd $path/histo_$i.root histo_*

done

cd $path
hadd histo_data.root histo_TauPlusX*

#cp $path/histo_data.root $CMSSW_BASE/src/WHAnalysis/HistoAdderFirstStep/ETT/

