#!/bin/bash

ls -l  /lustre/cms/store/user/calabria/Data/FakeRateFunction_4/ | grep root | awk '{print $9}'

back=$1 

if [ $? -eq 0 ]; then
input=`ls -l  /lustre/cms/store/user/calabria/Data/FakeRateFunction_4/$back | grep root | awk '{print $9}' `
ntotfiles=`ls -l  /lustre/cms/store/user/calabria/Data/FakeRateFunction_4/$back | grep root | awk '{print $9}' | wc -l`

echo $input > filelistData.txt
echo $ntotfiles

fi
rm $back.txt

filelist=`cat filelistData.txt`

echo Filelist $filelist

for filename in $filelist ; do
echo "/lustre/cms/store/user/calabria/Data/FakeRateFunction_4/$back/$filename" >> $back.txt


done
