import FWCore.ParameterSet.Config as cms

# Give the process a name
process = cms.Process("PickEvent")

# Tell the process which files to use as the source
process.source = cms.Source ("PoolSource",
          fileNames = cms.untracked.vstring(
		#"file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/163/42BAD075-D38E-E011-A19D-003048D2BCA2.root"

		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/06DAE77C-3F8F-E011-ADFE-001D09F25217.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/6EEB3D76-178F-E011-8F6B-003048F024E0.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/C8A2B244-4F8F-E011-8887-0030487CD178.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/08303DCE-4A8F-E011-A0EE-001D09F2960F.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/7E9CA5C4-5E8F-E011-8BBE-003048F110BE.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/CA3878E1-228F-E011-8538-003048D2BE12.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/12B08BF8-7E8F-E011-85FF-003048D3750A.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/82983076-598F-E011-AD2A-003048F1C832.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/D402EC33-658F-E011-94FA-003048F118DE.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/149FEA89-848F-E011-8F10-0030487A1884.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/884DC4B6-838F-E011-9829-0030487A1990.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/E40FFFDA-748F-E011-A677-003048D2BE12.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/3081C731-398F-E011-821D-0030487A17B8.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/8E2C1372-628F-E011-A130-001D09F23174.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/E8A3FDE4-7E8F-E011-A993-003048F1182E.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/4404A762-738F-E011-9AC1-001D09F28F25.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/AA619512-498F-E011-AA78-0030487CD6E6.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/EA812071-2C8F-E011-979C-001D09F253C0.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/4AB88631-658F-E011-B6D8-003048F118C4.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/B2623A43-158F-E011-AB45-003048D2BB58.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/F8C48AFD-488F-E011-B83B-003048F1C58C.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/4EBCCFDA-748F-E011-9BD3-003048678098.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/BE49F41D-A18F-E011-8A2C-00304879FA4C.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/FAEF9E1F-138F-E011-9933-001D09F2441B.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/6019E963-278F-E011-984A-001D09F2AF96.root',
		#'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/166/380/C6903382-598F-E011-9BB9-0030487C6A66.root',

		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/04AE8355-67A3-E011-A356-E0CB4E4408C4.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/7AD79F22-52A3-E011-A307-BCAEC5364C93.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/C401528D-61A3-E011-85BB-BCAEC5329707.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/10C071EC-41A3-E011-8319-BCAEC5329710.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/7ECF8635-48A3-E011-9D7B-485B39897227.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/C48FEB30-6EA3-E011-9A22-003048F118C4.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/12352AEA-41A3-E011-9B7B-BCAEC5329717.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/8833691E-4BA3-E011-BBA7-0030486780EC.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/C689DCB4-5CA3-E011-90FA-E0CB4E55365D.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/12A18856-56A3-E011-AB0A-BCAEC53296F9.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/8E6A4E7A-72A3-E011-8BDF-BCAEC518FF8A.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/E82AEF20-52A3-E011-BE33-E0CB4E4408D1.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/1C4A6E57-67A3-E011-9037-BCAEC5329709.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/A687E455-67A3-E011-B40C-485B3989721B.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/EA0D3E52-56A3-E011-B67A-BCAEC5329705.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/28E86A01-71A3-E011-AB9B-003048D2BC42.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/AC80951E-6CA3-E011-B95A-003048D3756A.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/EC9F892C-8DA3-E011-975A-003048F118D2.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/469F3D86-D0A3-E011-B66E-003048D37560.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/AE30A489-77A3-E011-89BD-BCAEC5329700.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/F639E9B2-49A3-E011-BEEF-BCAEC532970D.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/7679559A-45A3-E011-BB02-BCAEC5364C93.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/C083B7A5-6FA3-E011-BE70-BCAEC53296FF.root',
		'file:/lustre/cms/store/data/Run2011A/MuEG/AOD/PromptReco-v4/000/167/898/FA2EFB30-7AA3-E011-91D9-003048F118AC.root',

),
          eventsToProcess = cms.untracked.VEventRange('166163:21535313',
						      '166380:1570830562',
						      '167284:482525686',
						      '167898:1936669536',
						      '171156:408963773',
						      '171315:134426527',),
)

# tell the process to only run over 100 events (-1 would mean run over
#  everything
process.maxEvents = cms.untracked.PSet(
            input = cms.untracked.int32(-1)

)

# Tell the process what filename to use to save the output
process.Out = cms.OutputModule("PoolOutputModule",
         fileName = cms.untracked.string("events_A_2.root")
)

# make sure everything is hooked up
process.end = cms.EndPath(process.Out)

