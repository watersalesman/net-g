#include <iostream>
#include <fstream>
#include <stdlib.h>
int system(const char *command);
using namespace std;

int main() {
	//Declare some variables
	string confpath = "/etc/netg/netg.conf";
	string sleeptime;
	string line;
	ifstream configFile (confpath);

	//Read how long to sleep between checks from config file
	if( configFile.is_open() ) {
		int counter = 1;
		while (getline (configFile,line)) {
			if( counter == 3) {
				sleeptime = line;
			}
			counter++;
		}
		configFile.close();
	}

	else {
		sleeptime = "600";
	}

	//Create const char variable to store sleep command
	string sleepstring	= "sleep " + sleeptime;
	const char *sleepcommand = sleepstring.c_str();

	//Main loop
	while( true ) {
		system("netg");
		system(sleepcommand);
	}

	return 0;
}
