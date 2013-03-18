#!/bin/bash

path=/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/
path_data=/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/
channel=ETT
channel2=MTT

./myList.sh $path DYJetsToLL_ETT $channel
./myList.sh $path DYToEE_ETT $channel
./myList.sh $path DYToMuMu_ETT $channel
./myList.sh $path DYToTauTau_ETT $channel

./myList.sh $path DYToEE_ETT_HS $channel
#./myList.sh $path DYToMuMu_ETT_HS $channel
./myList.sh $path DYToTauTau_ETT_HS $channel
./myList.sh $path DYToEE_MTT_HS $channel2
./myList.sh $path DYToMuMu_MTT_HS $channel2
./myList.sh $path DYToTauTau_MTT_HS $channel2
./myList.sh $path WH_110_ETT_LepDecay $channel
./myList.sh $path WH_115_ETT_LepDecay $channel
./myList.sh $path WH_120_ETT_LepDecay $channel
./myList.sh $path WH_125_ETT_LepDecay $channel
./myList.sh $path WH_130_ETT_LepDecay $channel
./myList.sh $path WH_135_ETT_LepDecay $channel
./myList.sh $path WH_140_ETT_LepDecay $channel
./myList.sh $path WH_145_ETT_LepDecay $channel
./myList.sh $path WH_110_MTT_LepDecay $channel2
./myList.sh $path WH_115_MTT_LepDecay $channel2
./myList.sh $path WH_120_MTT_LepDecay $channel2
./myList.sh $path WH_125_MTT_LepDecay $channel2
./myList.sh $path WH_130_MTT_LepDecay $channel2
./myList.sh $path WH_135_MTT_LepDecay $channel2
./myList.sh $path WH_140_MTT_LepDecay $channel2
./myList.sh $path WH_145_MTT_LepDecay $channel2

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

