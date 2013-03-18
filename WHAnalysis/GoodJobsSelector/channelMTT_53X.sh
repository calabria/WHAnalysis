#!/bin/bash

path=/lustre/cms/store/user/rosma/PatTuples_WH_3Jan2013_MC/
path_data=/lustre/cms/store/user/rosma/PatTuples_WH_3Jan2013_Data/
channel=MTT


./myList.sh $path_data SingleMu_RunD_PRv1_V2 $channel

