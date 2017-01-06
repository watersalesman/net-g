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

	//Read time in between checks form config file
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
		sleeptime = "3";
	}

	//Create const char variable to store sleep command
	string sleepstring	= "sleep " + sleeptime;
	const char *sleepcommand = sleepstring.c_str();

	//Begin daemon
	while( true ) {
		cout << "DAEMON: Running netg...";
		system("netg");
		cout << "DAEMON: Sleeping...";
		system(sleepcommand);
	}

	return 0;
}
