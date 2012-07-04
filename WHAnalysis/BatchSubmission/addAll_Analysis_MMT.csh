#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/
cmsenv
rm /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/DoubleMuAug5
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_DoubleMuAug5.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/DoubleMuMay10
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_DoubleMuMay10.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/DoubleMuPromptReco4
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_DoubleMuPromptReco4.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/DoubleMuPromptReco6
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_DoubleMuPromptReco6.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/DoubleMu_Run2011B_PromptReco1
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_DoubleMu_Run2011B_PromptReco1.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/DYJetsToLL
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_DYJetsToLL.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/QCD_20_MU
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_QCD_20_MU.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/TTJets
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_TTJets.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/WJets
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_WJets.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/WW
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_WW.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/WZ
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_WZ.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/ZZ
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_ZZ.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/WH_110
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_WH_110.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/ZH_110
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_ZH_110.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/TTH_110
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_TTH_110.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/WH_115
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_WH_115.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/ZH_115
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_ZH_115.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/TTH_115
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_TTH_115.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/WH_120
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_WH_120.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/ZH_120
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_ZH_120.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/TTH_120
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_TTH_120.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/WH_125
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_WH_125.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/ZH_125
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_ZH_125.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/TTH_125
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_TTH_125.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/WH_130
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_WH_130.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/ZH_130
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_ZH_130.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/TTH_130
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_TTH_130.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/WH_135
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_WH_135.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/ZH_135
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_ZH_135.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/MMT/TTH_135
hadd /lustre/cms/store/user/calabria/Data/Analisi/MMT/histo_TTH_135.root histo_*

