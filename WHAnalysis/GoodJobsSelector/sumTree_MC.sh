#!/bin/bash

path=/cmshome/calabria/prog/TNP_53X/
path2=/lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_MC_3/
rm -r /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_MC_3/Sum
mkdir /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_MC_3/Sum

for i in `ls $path`; do

	if grep 'SingleMu' $path$i
		then continue
	fi
	#echo $i
	#echo $i | sed 's/.\{4\}$//'
	name=`echo $i | sed 's/.\{4\}$//'`
	echo $name
	mkdir /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_MC_3/Sum/$name

	for j in `cat $path$i`; do

		echo $j
		cp $j /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_MC_3/Sum/$name

	done

	cd /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_MC_3/Sum/
	hadd testTagAndProbe_$name.root /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_MC_3/Sum/$name/*.root

done
