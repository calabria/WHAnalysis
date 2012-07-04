#!/bin/csh
setenv VO_CMS_SW_DIR /opt/exp_soft/cms
source $VO_CMS_SW_DIR/cmsset_default.csh
limit vmem unlim
mkdir /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/GenFilter

cd /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/GenFilter
setenv SCRAM_ARCH slc5_amd64_gcc434
eval `scramv1 runtime -csh`
cd -
cmsRun genfilter_cfg_1.py

cd /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/GenFilter
set rootFiles=(`/bin/ls histo_*.root`)
foreach rootFile (${rootFiles})
	scp ${rootFile} /cmshome/calabria/Code_42X_TauIDJune/CMSSW_4_2_4_patch2/src/WHAnalysis/GenFilter
end
