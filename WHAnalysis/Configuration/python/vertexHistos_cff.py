import FWCore.ParameterSet.Config as cms
from weights_cff import *

VertexHistosBeforeMCFilter= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

VertexHistosBeforeMCFilter2= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

VertexHistosBeforeMCFilter3= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

VertexHistosBeforeMCFilter4= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

VertexHistosBeforeMCFilter5= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

VertexHistosBeforeSel= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

VertexHistosAfterSel= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

VertexHistosForPU= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
        isMC = cms.untracked.bool(True),
)

###################################################################################

VertexHistosAfterSel1= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel2= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel3= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel4= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel5= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel6= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel7= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel8= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel9= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel10= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel11= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel12= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel13= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel14= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel15= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel16= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel17= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel18= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel19= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel20= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel21= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel22= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel23= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

VertexHistosAfterSel24= cms.EDAnalyzer("VertexHistManager",
   	src = cms.InputTag("offlinePrimaryVerticesWithBS"),
  	MCDist = cms.untracked.vdouble(vecMC),
  	TrueDist2011 = cms.untracked.vdouble(vecData),
)

###################################################################################

