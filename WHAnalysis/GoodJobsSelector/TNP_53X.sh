#!/bin/bash

path=/lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_MC_3/
path_data=/lustre/cms/store/user/calabria/Data/MuToTau_30Jan2013_Data/
channel=TNP

#./myList2.sh $path DYJetsToLL_TNP $channel
./myList2.sh $path DYToEE_TNP $channel
./myList2.sh $path DYToMuMu_TNP $channel
./myList2.sh $path DYToTauTau_TNP $channel
./myList2.sh $path TTJets_TNP $channel
./myList2.sh $path WJets_TNP_v1 $channel
./myList2.sh $path WJets_TNP_v2 $channel
./myList2.sh $path WW_TNP $channel
./myList2.sh $path WZ_TNP $channel
./myList2.sh $path ZZ_TNP $channel

#./myList2.sh $path_data SingleMu_RunA_06Aug2012 $channel
#./myList2.sh $path_data SingleMu_RunA_13Jul2012 $channel
#./myList2.sh $path_data SingleMu_RunB_13Jul2012 $channel
#./myList2.sh $path_data SingleMu_RunC_24Aug2012 $channel
#./myList2.sh $path_data SingleMu_RunC_PRv2 $channel
#./myList2.sh $path_data SingleMu_RunD_PRv1 $channel
