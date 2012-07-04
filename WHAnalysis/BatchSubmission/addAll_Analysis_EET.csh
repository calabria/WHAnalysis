#!/bin/csh

cd /cmshome/calabria/Code_42X_TauIDNov/CMSSW_4_2_8_patch7/src/
cmsenv
rm /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/DoubleElectronAug5
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_DoubleElectronAug5.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/DoubleElectronMay10
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_DoubleElectronMay10.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/DoubleElectronPromptReco4
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_DoubleElectronPromptReco4.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/DoubleElectronPromptReco6
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_DoubleElectronPromptReco6.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/DoubleElectron_Run2011B_PromptReco1
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_DoubleElectron_Run2011B_PromptReco1.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/DYJetsToLL
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_DYJetsToLL.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/GVJets
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_GVJets.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/QCD20_30_BCtoE
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_QCD20_30_BCtoE.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/QCD20_30_EM
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_QCD20_30_EM.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/QCD30_80_BCtoE
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_QCD30_80_BCtoE.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/QCD30_80_EM
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_QCD30_80_EM.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/QCD80_170_BCtoE
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_QCD80_170_BCtoE.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/QCD80_170_EM
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_QCD80_170_EM.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/TTJets
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_TTJets.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/WJets
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_WJets.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/WW
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_WW.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/WZ
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_WZ.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/ZZ
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_ZZ.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/WH_110
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_WH_110.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/ZH_110
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_ZH_110.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/TTH_110
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_TTH_110.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/WH_115
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_WH_115.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/ZH_115
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_ZH_115.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/TTH_115
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_TTH_115.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/WH_120
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_WH_120.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/ZH_120
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_ZH_120.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/TTH_120
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_TTH_120.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/WH_125
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_WH_125.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/ZH_125
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_ZH_125.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/TTH_125
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_TTH_125.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/WH_130
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_WH_130.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/ZH_130
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_ZH_130.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/TTH_130
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_TTH_130.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/WH_135
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_WH_135.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/ZH_135
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_ZH_135.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/EET/TTH_135
hadd /lustre/cms/store/user/calabria/Data/Analisi/EET/histo_TTH_135.root histo_*

