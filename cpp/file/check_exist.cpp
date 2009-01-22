#include <fstream>

using namespace std;

bool checkExist(const string& filename)
{
	ifstream file(filename);
	if (!file)
		return false;
	else
		return true;
}