#!/bin/bash

path=/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_42X_MC/
path_data=/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_42X_Data/
channel=ETT

./myList.sh $path DYJetsToLL_ETT_Fall11 $channel
./myList.sh $path DYToEE_ETT_Fall11 $channel
./myList.sh $path DYToMuMu_ETT_Fall11 $channel
./myList.sh $path DYToTauTau_ETT_Fall11 $channel
./myList.sh $path GVJets_ETT_Fall11 $channel
./myList.sh $path TTJets_ETT_Fall11 $channel
./myList.sh $path W1Jets_ETT_Fall11 $channel
./myList.sh $path W2Jets_ETT_Fall11 $channel
./myList.sh $path W3Jets_ETT_Fall11 $channel
./myList.sh $path W4Jets_ETT_Fall11 $channel
./myList.sh $path WH_125_ETT_Fall11_NoSkim $channel
./myList.sh $path WH_110_ETT_Fall11 $channel
./myList.sh $path WH_115_ETT_Fall11 $channel
./myList.sh $path WH_120_ETT_Fall11 $channel
./myList.sh $path WH_125_ETT_Fall11 $channel
./myList.sh $path WH_130_ETT_Fall11 $channel
./myList.sh $path WH_135_ETT_Fall11 $channel
./myList.sh $path WH_140_ETT_Fall11 $channel
./myList.sh $path WH_145_ETT_Fall11 $channel
./myList.sh $path WH_150_ETT_Fall11 $channel
./myList.sh $path WH_160_ETT_Fall11 $channel
./myList.sh $path WJets_ETT_Fall11 $channel
./myList.sh $path WW_ETT_Fall11 $channel
./myList.sh $path WZ_ETT_Fall11 $channel
./myList.sh $path ZZ_ETT_Fall11 $channel

./myList.sh $path_data TauPlusXAug5 $channel
./myList.sh $path_data TauPlusXMay10 $channel
./myList.sh $path_data TauPlusXPromptReco4 $channel
./myList.sh $path_data TauPlusXPromptReco6 $channel
./myList.sh $path_data TauPlusX_Run2011B_PromptReco1 $channel

