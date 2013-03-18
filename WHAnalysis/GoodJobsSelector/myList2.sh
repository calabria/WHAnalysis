#!/bin/bash

path=$1
sampleName=$2
channel=$3

if [ $? -eq 0 ]; then
input=`ls -l $path/$sampleName | grep testTagAndProbe | awk '{print $9}'`
ntotfiles=`ls -l  $path/$sampleName | grep testTagAndProbe | wc -l`

echo $input
echo Nfiles: $ntotfiles
rm list_${sampleName}_${channel}.txt
ls -l $path/$sampleName | grep testTagAndProbe | awk '{print $5 " " $6 " " $7 " " $8 " " $9}' >& list_${sampleName}_${channel}.txt

fi

g++ selectFile2.cpp -o selectFile2
./selectFile2 list_${sampleName}_${channel}.txt $path$sampleName >& ./TNP_53X/${sampleName}_${channel}.txt

rm list_*
