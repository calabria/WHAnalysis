#!/bin/bash

rm out.txt

for folder1 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/05Aug2011-v1/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/05Aug2011-v1/${folder1}/`; do

		#echo $folder1 $folder2
		ls -l /lustre/cms/store/data/Run2011A/SingleMu/AOD/05Aug2011-v1/${folder1}/${folder2} | grep ' ? ' #>> out.txt

	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/May10ReReco-v1/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/May10ReReco-v1/${folder1}/`; do

		#echo $folder1 $folder2
		ls -l /lustre/cms/store/data/Run2011A/SingleMu/AOD/May10ReReco-v1/${folder1}/${folder2} | grep ' ? ' #>> out.txt

	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v4/000/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v4/000/${folder1}/`; do

		#echo ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v4/000/${folder1}/${folder2}
		var=$(ls -l /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v4/000/${folder1}/${folder2} | grep ' ? ') 
		if [ "$var" ] 
			then
				echo /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v4/000/${folder1}/${folder2}/$var #>> out.txt
		fi

	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v6/000/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v6/000/${folder1}/`; do

		#echo $folder1 $folder2
		var=$(ls -l /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v6/000/${folder1}/${folder2} | grep ' ? ')
		if [ "$var" ] 
			then
				echo /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v6/000/${folder1}/${folder2}/$var #>> out.txt
		fi

	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011B/SingleMu/AOD/PromptReco-v1/000/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011B/SingleMu/AOD/PromptReco-v1/000/${folder1}/`; do

		#echo $folder1 $folder2
		var=$(ls -l /lustre/cms/store/data/Run2011B/SingleMu/AOD/PromptReco-v1/000/${folder1}/${folder2} | grep ' ? ')

		if [ "$var" ] 
			then
				echo /lustre/cms/store/data/Run2011B/SingleMu/AOD/PromptReco-v1/000/${folder1}/${folder2}/$var #>> out.txt
		fi

	done
done
