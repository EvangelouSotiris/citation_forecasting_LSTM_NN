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
    
    if(fileinput.is_open()){
        printf("opened outputacm.txt\n");
        int counter = 0;
        while (getline(fileinput,line)){
            cout << counter << ": " << line << endl;
            int infotype = splitter(line);
            if(infotype == 1) {
                Items_struct new_item;
                new_item.title = line.substr(2,line.length());
                cout << new_item.title;
                return 0;
            }
            else if(infotype == 2) {

            }
            else if(infotype == 3) {

            }
            else if(infotype == 4) {

            }
            else if(infotype == 5) {

            }
            else if(infotype == 6) {

            }
            else if(infotype == 7) {

            }
            else{

            }
        }
    }
    fileinput.close();
    return 0;
}
