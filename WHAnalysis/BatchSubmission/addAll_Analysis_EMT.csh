#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/
cmsenv
rm /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/MuEGAug5
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_MuEGAug5.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/MuEGMay10
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_MuEGMay10.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/MuEGPromptReco4
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_MuEGPromptReco4.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/MuEGPromptReco6
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_MuEGPromptReco6.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/MuEG_Run2011B_PromptReco1
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_MuEG_Run2011B_PromptReco1.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/DYJetsToLL
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_DYJetsToLL.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/GVJets
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_GVJets.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/QCD20_30_BCtoE
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_QCD20_30_BCtoE.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/QCD20_30_EM
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_QCD20_30_EM.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/QCD30_80_BCtoE
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_QCD30_80_BCtoE.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/QCD30_80_EM
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_QCD30_80_EM.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/QCD80_170_BCtoE
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_QCD80_170_BCtoE.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/QCD80_170_EM
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_QCD80_170_EM.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/QCD_20_MU
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_QCD_20_MU.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/TTJets
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_TTJets.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/WJets
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_WJets.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/WW
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_WW.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/WZ
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_WZ.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/ZZ
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_ZZ.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/WH_110
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_WH_110.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/ZH_110
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_ZH_110.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/TTH_110
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_TTH_110.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/WH_115
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_WH_115.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/ZH_115
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_ZH_115.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/TTH_115
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_TTH_115.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/WH_120
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_WH_120.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/ZH_120
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_ZH_120.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/TTH_120
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_TTH_120.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/WH_125
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_WH_125.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/ZH_125
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_ZH_125.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/TTH_125
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_TTH_125.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/WH_130
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_WH_130.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/ZH_130
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_ZH_130.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/TTH_130
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_TTH_130.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/WH_135
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_WH_135.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/ZH_135
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_ZH_135.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EMT/TTH_135
hadd /lustre/cms/store/user/calabria/Data/Analisi/EMT/histo_TTH_135.root histo_*

