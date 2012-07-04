import FWCore.ParameterSet.Config as cms
from vertexHistos_cff import *

sumPtProducer = cms.EDProducer('VertexProducer',
	vertexSrc = cms.untracked.InputTag('offlinePrimaryVerticesWithBS'),
)

selectedPrimaryVertex = cms.EDFilter("GoodVertexFilter",
                                   vertexCollection = cms.InputTag('sumPtProducer'),
                                   minimumNDOF = cms.uint32(7) ,
                                   maxAbsZ = cms.double(24),	
                                   maxd0 = cms.double(2),
                      		   filter = cms.bool(True)	
                                   )

vertexSequence = cms.Sequence(
			      sumPtProducer *
			      VertexHistosBeforeSel *
 			      selectedPrimaryVertex *
			      VertexHistosAfterSel
)
