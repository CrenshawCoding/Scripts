#include <fstream>
#include <string>
#include <iostream>
using namespace std;
ifstream inFile;
ofstream outFile("converted-2.txt");
string fileName = "";
string inFilePath = "komplett-kondensiert.txt";

inline std::string trim(std::string& str) {
    str.erase(0, str.find_first_not_of(' '));       //prefixing spaces
    str.erase(str.find_last_not_of(' ')+1);         //surfixing spaces
    return str;
}

string convertLineToLatex(string line) {
	line = trim(line);
	string returnString = "";
	char firstSymbol = line[0];
	char lastSymbol = line[0];
	if (line.length() == 1) {
		returnString.append("\\end{itemize}\n\n");
	}
	else if(firstSymbol == '*') {
			returnString.append("\t\\item{");
			returnString.append(line.substr(2, line.length() - 1));
			returnString.insert(returnString.length() - 1, "}");
	}
	else if(line.substr(0, 2) == "->") {
		returnString.append("\\begin{itemize}\n");
		returnString.append("\t\\item{");
		returnString.append(line.substr(3, line.length() - 1));
		returnString.insert(returnString.length() - 1, "}");
		returnString.append("\\end{itemize}\n");
	}
	else if(line.substr(0,3) == "###") {
		returnString.append("\\section{");
		returnString.append(line.substr(4, line.length() - 1));
		returnString.insert(returnString.length() - 1, "}\n");
	}
	else if(line.substr(0,2) == "##") {
		returnString.append("\\subsection{");
		returnString.append(line.substr(3, line.length() - 1));
		returnString.insert(returnString.length() - 1, "}\n");
	}
	else if(line.substr(0,1) == "#") {
		returnString.append("\\subsubsubsection{");
		returnString.append(line.substr(2, line.length() - 1));
		returnString.insert(returnString.length() - 1, "}\n");
	}
	else if(line.find(":")!=string::npos) {
		returnString.append("\\textbf{" + line);
		returnString.insert(returnString.length() - 1, "}");
		returnString.append("\\begin{itemize}\n");
	}
  else if(line.substr(0, 2) == "!!") {
      returnString.append("\\includegraphics[width=0.8\\textwidth]{");
      returnString.append(line.substr(2, line.length() - 3)); // for some reason -3 instead of -1, newline or sth
      returnString.push_back('}');
      returnString.push_back('\n');
      returnString.push_back('\n');
  }
  else {
		returnString = line;
		returnString.push_back('\\');
		returnString.push_back('\\');
	}
	return returnString;
}

int main() {
	cout << "Reading file\n";
	inFile.open(inFilePath);
	if (!inFile) {
		cerr << "Unable to open file";
		exit(1);   // call system to stop
	}
	int lineCounter = 0;
	string x;
	while(getline(inFile, x)) {
			cout  << x << '\n';
			cout << convertLineToLatex(x);
			outFile << convertLineToLatex(x);
	}
	return 0;
}
