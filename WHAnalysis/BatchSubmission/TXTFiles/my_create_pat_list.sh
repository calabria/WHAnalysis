#!/bin/bash

ls -l  /lustre/cms/store/user/calabria/Data/PAT2012_MC_ETT_14Ott/ | grep root | awk '{print $9}'

back=$1

finalState=$2

if [ $? -eq 0 ]; then
input=`ls -l  /lustre/cms/store/user/calabria/Data/PAT2012_MC_ETT_14Ott/$back | grep patTuple | awk '{print $9}' `
ntotfiles=`ls -l  /lustre/cms/store/user/calabria/Data/PAT2012_MC_ETT_14Ott/$back | grep patTuple | awk '{print $9}' | wc -l`

echo $input > filelistData.txt
echo $ntotfiles

fi
rm $back$finalState.txt

filelist=`cat filelistData.txt`

echo Filelist $filelist

for filename in $filelist ; do
echo "/lustre/cms/store/user/calabria/Data/PAT2012_MC_ETT_14Ott/$back/$filename" >> $back$finalState.txt


done
