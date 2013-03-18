#!/bin/bash

path=/cmshome/calabria/prog/TNP_53X/
path2=/lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_Data/
rm -r /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_Data/Sum
mkdir /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_Data/Sum

for i in `ls $path | grep 'SingleMu'`; do

	#echo $i
	#echo $i | sed 's/.\{4\}$//'
	name=`echo $i | sed 's/.\{4\}$//'`
	echo $name
	mkdir /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_Data/Sum/$name

	for j in `cat $path$i`; do

		echo $j
		cp $j /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_Data/Sum/$name

	done

	cd /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_Data/Sum/
	hadd testTagAndProbe_$name.root /lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_Data/Sum/$name/*.root

done
