{
	
   string line_content;
   char line[350];

   ifstream fileor0("files.txt"); 
   if (fileor0.is_open()){//Check if file_list is open

     	while (fileor0.getline(line,350)){//Loop over the lines contained in file_list

       		std::string fileName = std::string(line);
		TFile *f1 = TFile::Open(fileName.c_str());

		f1->cd("demo");
		int nEvents_Tot = N_eventi_Tot->GetBinContent(1);
		int nEvents_Filtered = N_eventi_Filtered->GetBinContent(1);
		if(nEvents_Tot){

			double effSkim = 100*nEvents_Filtered/nEvents_Tot;
			double errEffSkim = 1;
		 	std::cout<<fileName<<" "<<nEvents_Filtered<<" "<<nEvents_Tot<<" "<<effSkim<<std::endl;

		}

   	}

   }

}
