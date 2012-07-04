#!/bin/bash

for folder1 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/05Aug2011-v1/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/05Aug2011-v1/${folder1}/`; do

		#echo /lustre/cms/store/data/Run2011A/SingleMu/AOD/05Aug2011-v1/${folder1}/${folder2}
		ls -l /lustre/cms/store/data/Run2011A/SingleMu/AOD/05Aug2011-v1/${folder1}/${folder2} | grep ' ? ' 

	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/May10ReReco-v1/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/May10ReReco-v1/${folder1}/`; do

		#echo /lustre/cms/store/data/Run2011A/SingleMu/AOD/May10ReReco-v1/${folder1}/${folder2}
		ls -l /lustre/cms/store/data/Run2011A/SingleMu/AOD/May10ReReco-v1/${folder1}/${folder2} | grep ' ? ' 

	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v4/000/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v4/000/${folder1}/`; do

		#echo /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v4/000/${folder1}/${folder2}
		ls -l /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v4/000/${folder1}/${folder2} | grep ' ? '

	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v6/000/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v6/000/${folder1}/`; do

		#echo /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v6/000/${folder1}/${folder2}
		ls -l /lustre/cms/store/data/Run2011A/SingleMu/AOD/PromptReco-v6/000/${folder1}/${folder2} | grep ' ? '

	done
done

for folder1 in `ls /lustre/cms/store/data/Run2011B/SingleMu/AOD/PromptReco-v1/000/`; do
	for folder2 in `ls /lustre/cms/store/data/Run2011B/SingleMu/AOD/PromptReco-v1/000/${folder1}/`; do

		#echo /lustre/cms/store/data/Run2011B/SingleMu/AOD/PromptReco-v1/000/${folder1}/${folder2}
		ls -l /lustre/cms/store/data/Run2011B/SingleMu/AOD/PromptReco-v1/000/${folder1}/${folder2} | grep ' ? '

	done
done
