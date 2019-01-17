#include <iostream>
#include <list>
#include <fstream>

using namespace std;

class Items_struct{
    public:
        string title;
        int year;
        int index;
        list<int> id_refs;

    void print_item(){
        cout << "Printing item " << index << endl;
        cout << "Title: " << title << endl;
        cout << "Year: " << year << endl;
        cout << "Refs: [";
        for (int val : id_refs){
            cout << val << ",";
        }
        cout << "]" <<endl;
    }
};

int found_times(string line, string substring){
    int occurrences = 0;
    size_t start = 0;

    while ((start = line.find(substring, start)) != string::npos) {
        ++occurrences;
        start += substring.length();
    }
}

int splitter(string line){
    if(found_times(line,"#*") != 0){
        cout << line << ", #*" <<endl;
        return 1;
    }
    else if(found_times(line,"#@") != 0){
        return 2;
    }
    else if(found_times(line,"#t") != 0){
        return 3;
    }
    else if(found_times(line,"#c") != 0){
        return 4;
    }
    else if(found_times(line,"#index") != 0){
        return 5;
    }
    else if(found_times(line,"#%") != 0){
        return 6;
    }
    else if(found_times(line,"#!") != 0){
        return 7;
    }
    else {
        return 0;
    }
}

int main(int argc, const char * argv[]){
    ifstream fileinput ("../Project/outputacm.txt");
    string line;
    list<Items_struct> whole_list;
    
    list<string> linelist;
    
    if(fileinput.is_open()){
        Items_struct new_item;
        getline(fileinput,line);
        while (getline(fileinput,line)){
            linelist.push_back(line);
        }
    }
    
    fileinput.close();
    
    int found;
    Items_struct new_item;
    int counter = 0;

    for (list<string>::iterator it=linelist.begin(); it != linelist.end(); ++it) {
        line = *it;
        found = line.find("#*");
        if (found != -1) {
            new_item.title = line.substr(found + 2, line.length());
            continue;
        }
        found = line.find("#t");
        if (found != -1) {
            new_item.year = atoi(line.substr(found + 2, line.length()).c_str());
            continue;
        }
        found = line.find("#index");
        if (found != -1) {
            new_item.index = atoi(line.substr(found + 5, line.length()).c_str());
            continue;
        }
        found = line.find("#%");
        if (found != -1) {
            new_item.id_refs.push_back(atoi(line.substr(found + 2, line.length()).c_str()));
            continue;
        }
        if (line.compare("")==0){
            whole_list.push_back(new_item);
            new_item.title = "";
            new_item.year = 0;
            new_item.index = 0;
            new_item.id_refs.clear();
        }

    }

    whole_list.end()->print_item();

    return 0;
}
