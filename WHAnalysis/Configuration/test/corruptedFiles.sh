#!/bin/bash

#rm out.txt

for folder1 in `ls /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/05Aug2011-v1/`; do
	#for folder2 in `ls /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/05Aug2011-v1/${folder1}/`; do
		for file in `ls -l /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/05Aug2011-v1/${folder1}/ | grep ' ? ' | awk '{print $7}' `; do

		#echo $folder1 $folder2
		echo /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/05Aug2011-v1/${folder1}/${file}
		done
	#done
done

for folder1 in `ls /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/May10ReReco-v1/`; do
	#for folder2 in `ls /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/May10ReReco-v1/${folder1}/`; do
		for file in `ls -l /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/May10ReReco-v1/${folder1}/ | grep ' ? ' | awk '{print $7}' `; do

		#echo $folder1 $folder2
		echo /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/May10ReReco-v1/${folder1}/${file}
		done
	#done
done

for folder1 in `ls /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/PromptReco-v4/000/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/PromptReco-v4/000/${folder1}/`; do
		for file in `ls -l /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/PromptReco-v4/000/${folder1}/${folder2}/ | grep ' ? ' | awk '{print $7}' `; do

		#echo $folder1 $folder2
		echo /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/PromptReco-v4/000/${folder1}/${folder2}/${file}
		done
	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/PromptReco-v6/000/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/PromptReco-v6/000/${folder1}/`; do
		for file in `ls -l /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/PromptReco-v6/000/${folder1}/${folder2}/ | grep ' ? ' | awk '{print $7}' `; do

		#echo $folder1 $folder2
		echo /lustre/cms/store/data/Run2011A/DoubleElectron/AOD/PromptReco-v6/000/${folder1}/${folder2}/${file}
		done
	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011B/DoubleElectron/AOD/PromptReco-v1/000/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011B/DoubleElectron/AOD/PromptReco-v1/000/${folder1}/`; do
		for file in `ls -l /lustre/cms/store/data/Run2011B/DoubleElectron/AOD/PromptReco-v1/000/${folder1}/${folder2}/ | grep ' ? ' | awk '{print $7}' `; do

		#echo $folder1 $folder2
		echo /lustre/cms/store/data/Run2011B/DoubleElectron/AOD/PromptReco-v1/000/${folder1}/${folder2}/${file}
		done
	done
done
