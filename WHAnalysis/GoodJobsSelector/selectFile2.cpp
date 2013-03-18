#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
   char line0[150];

   std::vector<int> allSizes;
   std::vector<string> allDays;
   std::vector<string> allHours;
   std::vector<string> allNames;
   std::vector<string> allMonths;
   std::vector<string> newNameVec;

   //std::cout<<argv[1]<<std::endl;
   std::string nameTXT(argv[1]);
   std::string path(argv[2]);
   //std::cout<<nameTXT<<std::endl;

   allMonths.clear();
   allSizes.clear();
   allDays.clear();
   allHours.clear();
   allNames.clear();
   ifstream fileor0(nameTXT.c_str()); 

   if (fileor0.is_open()){

	while (fileor0.getline(line0,150)){

		std::string line = line0; 
		if(line.find("?") != std::string::npos) continue;

   		std::string size;
   		std::string fileName;
   		std::string month;
   		std::string day;
   		std::string hour;
         	//std::cout<<line0<<" "<<line<<std::endl;
         	std::stringstream iss;
         	iss<<line0;
         	//std::cout<<iss.str()<<std::endl;
         	iss>>size>>month>>day>>hour>>fileName;
         	//std::cout<<fileName<<" "<<size<<" "<<month<<" "<<day<<" "<<hour<<std::endl;

		std::stringstream issConv;
		issConv<<size;
		int sizeConv;
		issConv>>sizeConv;

		allNames.push_back(fileName);
		allSizes.push_back(sizeConv);
		allMonths.push_back(month);
		allDays.push_back(day);
		allHours.push_back(hour);

      	}
   }

   fileor0.close();

   int sizeVec = allNames.size();
   //std::cout<<"Size: "<<sizeVec<<" "<<allSizes.size()<<std::endl;

   for(int i = 0; i < sizeVec; i++){

	//if(allSizes[i] == 0) allNames[i] = "passaAvanti";
	if(allNames[i] == "passaAvanti") continue;
	//std::cout<<allNames[i]<<" "<<allSizes[i]<<std::endl;
	std::string stringNameTMP1 = allNames[i];
      	stringNameTMP1.erase(stringNameTMP1.end()-11,stringNameTMP1.end());
	int size1 = stringNameTMP1.size();
	std::string::reverse_iterator rit1 = stringNameTMP1.rbegin();
	//std::cout<<"minkia "<<*rit1<<std::endl;
	std::string lastChar1;
	lastChar1 = *rit1;
	//std::cout<<"lastChar1 "<<lastChar1<<std::endl;
	if(lastChar1 == "_") stringNameTMP1.erase(stringNameTMP1.end()-1,stringNameTMP1.end());
	//std::cout<<allNames[i]<<" "<<stringNameTMP1<<" "<<allSizes[i]<<std::endl;

	for(int j = 0; j < sizeVec; j++){

		if(allNames[j] == "passaAvanti") continue;
		if(i != j ) {

			if(allNames[i] == "passaAvanti") continue;
			std::string stringNameTMP2 = allNames[j];
      			stringNameTMP2.erase(stringNameTMP2.end()-11,stringNameTMP2.end());
			std::string::reverse_iterator rit2 = stringNameTMP2.rbegin();
			//std::cout<<"minkia "<<*rit2<<std::endl;
			std::string lastChar2;
			lastChar2 = *rit2;
			//std::cout<<"lastChar2 "<<lastChar2<<std::endl;
			if(lastChar2 == "_") stringNameTMP2.erase(stringNameTMP2.end()-1,stringNameTMP2.end());
			//std::cout<<allNames[j]<<" "<<stringNameTMP2<<" "<<allSizes[j]<<std::endl;

 			bool flag1 = stringNameTMP2 == stringNameTMP1 ? true : false;
			bool flag2 = allSizes[i] > allSizes[j] ? true : false;

			if(flag1 & flag2) allNames[j] = "passaAvanti";
			else if(flag1 & !flag2) allNames[i] = "passaAvanti";

		}

	}

   }

   std::string reducedPath = path;
   reducedPath.erase(0,11);
   for(int i = 0; i < sizeVec; i++){

	//if(allNames[i] != "passaAvanti") std::cout<<allNames[i]<<" "<<allSizes[i]<<std::endl;
	if(allNames[i] != "passaAvanti") std::cout<<path<<"/"<<allNames[i]<<std::endl;
	//if(allNames[i] != "passaAvanti") std::cout<<reducedPath<<"/"<<allNames[i]<<std::endl;

   }

   return 0;

}
