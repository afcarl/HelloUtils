#include <algorithm>

// parse command line argument
// single-word option
// http://stackoverflow.com/questions/865668/how-to-parse-command-line-arguments-in-c

char* getCmdOption(char** begin, char** end, const string& option)
{
	char ** itr = find(begin, end, option);
	if (itr != end && ++itr != end)
	{
		return *itr;
	}
	return 0;
}

bool cmdOptionExists(char** begin, char** end, const string& option)
{
	return find(begin, end, option) != end;
}