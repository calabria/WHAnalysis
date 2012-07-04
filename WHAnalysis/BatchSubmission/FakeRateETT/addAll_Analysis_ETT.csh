#!/bin/csh

#cd /cmshome/calabria/Code_42X_TauIDNov_Indara/CMSSW_4_2_8_patch7/src/
#cmsenv
#rm /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusXAug5FR1
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusXAug5FR1.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusXMay10FR1
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusXMay10FR1.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusXPromptReco4FR1
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusXPromptReco4FR1.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusXPromptReco6FR1
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusXPromptReco6FR1.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusX_Run2011B_PromptReco1FR1
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusX_Run2011B_PromptReco1FR1.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusXAug5FR2
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusXAug5FR2.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusXMay10FR2
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusXMay10FR2.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusXPromptReco4FR2
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusXPromptReco4FR2.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusXPromptReco6FR2
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusXPromptReco6FR2.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/TauPlusX_Run2011B_PromptReco1FR2
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusX_Run2011B_PromptReco1FR2.root histo_*

cd /lustre/cms/store/user/calabria/Data/Analisi/ETT/
hadd /lustre/cms/store/user/calabria/Data/Analisi/ETT/histo_TauPlusX_FakeRate.root histo_*
