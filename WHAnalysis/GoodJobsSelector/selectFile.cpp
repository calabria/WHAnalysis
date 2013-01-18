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
   int size = 0;
   std::string fileName;
   std::string month;
   int day;
   std::string hour;
   std::vector<int> allSizes;
   std::vector<int> allDays;
   std::vector<string> allHours;
   std::vector<string> allNames;
   std::vector<string> allMonths;
   std::vector<string> newNameVec;

   //std::cout<<argv[1]<<std::endl;
   std::string nameTXT(argv[1]);
   std::string path(argv[2]);
   //std::cout<<nameTXT<<std::endl;

   fileName.clear();
   allNames.clear();
   ifstream fileor0(nameTXT.c_str()); 

   if (fileor0.is_open()){

	while (fileor0.getline(line0,150)){
         	std::stringstream iss;
         	iss<<line0;
         	iss>>size>>month>>day>>hour>>fileName;
         	//std::cout<<fileName<<" "<<size<<" "<<month<<" "<<day<<" "<<hour<<std::endl;
		allNames.push_back(fileName);
		allSizes.push_back(size);
		allMonths.push_back(month);
		allDays.push_back(day);
		allHours.push_back(hour);
      	}
   }

   fileor0.close();

   int sizeVec = allNames.size();
   //std::cout<<"Size: "<<sizeVec<<std::endl;

   for(int i = 0; i < sizeVec; i++){

	if(allNames[i] == "passaAvanti") continue;
	//std::cout<<allNames[i]<<" "<<allSizes[i]<<std::endl;
	std::string stringNameTMP1 = allNames[i];
      	stringNameTMP1.erase(stringNameTMP1.end()-11,stringNameTMP1.end());
	//std::cout<<allNames[i]<<" "<<stringNameTMP1<<" "<<allSizes[i]<<std::endl;

	for(int j = 0; j < sizeVec; j++){

		if(allNames[j] == "passaAvanti") continue;
		if(i != j ) {

			if(allNames[i] == "passaAvanti") continue;
			std::string stringNameTMP2 = allNames[j];
      			stringNameTMP2.erase(stringNameTMP2.end()-11,stringNameTMP2.end());
			//std::cout<<allNames[j]<<" "<<stringNameTMP2<<" "<<allSizes[j]<<std::endl;

 			bool flag1 = stringNameTMP2 == stringNameTMP1 ? true : false;
			bool flag2 = allSizes[i] > allSizes[j] ? true : false;

			if(flag1 & flag2) allNames[j] = "passaAvanti";
			else if(flag1 & !flag2) allNames[i] = "passaAvanti";

		}

	}

   }

   std::string reducedPath = path.erase(0,11);
   for(int i = 0; i < sizeVec; i++){

	//if(allNames[i] != "passaAvanti") std::cout<<allNames[i]<<" "<<allSizes[i]<<std::endl;
	//if(allNames[i] != "passaAvanti") std::cout<<path<<"/"<<allNames[i]<<std::endl;
	if(allNames[i] != "passaAvanti") std::cout<<reducedPath<<"/"<<allNames[i]<<std::endl;

   }

   return 0;

}
