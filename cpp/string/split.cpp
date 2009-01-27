#include <string>
#include <sstream>
#include <vector>

//http://stackoverflow.com/questions/236129/split-a-string-in-c

/********************************\
Note that this solution does not skip empty tokens, 
so the following will find 4 items, one of which is empty:

std::vector<std::string> x = split("one:two::three", ':');
\********************************/

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, elems);
    return elems;
}