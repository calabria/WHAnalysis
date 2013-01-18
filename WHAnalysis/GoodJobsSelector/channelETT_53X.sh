#!/bin/bash

path=/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/
path_data=/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/
channel=ETT

./myList.sh $path DYJetsToLL_ETT $channel
./myList.sh $path DYToEE_ETT $channel
./myList.sh $path DYToMuMu_ETT $channel
./myList.sh $path DYToTauTau_ETT $channel
./myList.sh $path TTJets_ETT $channel
./myList.sh $path W1Jets_ETT $channel
./myList.sh $path W2Jets_ETT $channel
./myList.sh $path W3Jets_ETT $channel
./myList.sh $path W4Jets_ETT $channel
./myList.sh $path WH125_ETT_NoSkim $channel
./myList.sh $path WH_110_ETT $channel
./myList.sh $path WH_115_ETT $channel
./myList.sh $path WH_120_ETT $channel
./myList.sh $path WH_125_ETT $channel
./myList.sh $path WH_130_ETT $channel
./myList.sh $path WH_135_ETT $channel
./myList.sh $path WH_140_ETT $channel
./myList.sh $path WH_145_ETT $channel
./myList.sh $path WH_150_ETT $channel
./myList.sh $path WH_155_ETT $channel
./myList.sh $path WH_160_ETT $channel
./myList.sh $path WJets_ETT_v1 $channel
./myList.sh $path WJets_ETT_v2 $channel
./myList.sh $path WW_ETT $channel
./myList.sh $path WZ_ETT $channel
./myList.sh $path ZZ_ETT $channel

./myList.sh $path_data TauPlusX_RunA_06Aug2012 $channel
./myList.sh $path_data TauPlusX_RunA_13Jul2012 $channel
./myList.sh $path_data TauPlusX_RunB_13Jul2012 $channel
./myList.sh $path_data TauPlusX_RunC_24Aug2012 $channel
./myList.sh $path_data TauPlusX_RunC_PRv2 $channel
./myList.sh $path_data TauPlusX_RunD_PRv1 $channel

