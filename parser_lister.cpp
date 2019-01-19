#include <iostream>
#include <list>
#include <fstream>

using namespace std;

class Items_struct{
    public:
        Items_struct(){
            title = "";
            year = 0;
            index = -1;
        }
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

bool contains(list<int> ref_list, int item_to_search){
    int curr;

    for (list<int>::iterator it=ref_list.begin(); it != ref_list.end(); ++it) {
        curr = *it;
        if (curr == item_to_search){
            return true;
        }
    }
    return false;
}

int found_times(string line, string substring){
    int occurrences = 0;
    size_t start = 0;

    while ((start = line.find(substring, start)) != string::npos) {
        ++occurrences;
        start += substring.length();
    }
}

list<Items_struct> creating_list(){
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
            new_item.index = atoi(line.substr(found + 6, line.length()).c_str());
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

    return whole_list;
}
/*
int main(int argc, const char * argv[]){
    list<Items_struct> whole_list;
    Items_struct new_item;
    int counter = 0;
    
    whole_list = creating_list();
    cout << "Parsed the txt and created the list with all the items.\n\n";

    list<Items_struct> items_with_refs;
    list<int> significant_indexes;

    for (list<Items_struct>::iterator it=whole_list.begin(); it != whole_list.end(); ++it) {
        new_item = *it;
        if(new_item.id_refs.empty()){
            continue;
        }
        else{
            items_with_refs.push_back(new_item);
            significant_indexes.push_back(new_item.index);
        }
    }

    cout << "Created list with all the items that reference others, and one with all these indexes ("<<items_with_refs.size()<<")."<<endl;

    ofstream filetowrite;
    filetowrite.open("indexes_so_far.txt");
    for (list<int>::iterator it=significant_indexes.begin(); it != significant_indexes.end(); ++it){
        filetowrite << *it << "\n";
    }
    filetowrite.close();

    list<int> refs;
    int t0 = time(NULL);
    counter = 0;
    for (list<Items_struct>::iterator it=items_with_refs.begin(); it != items_with_refs.end(); ++it) {
        if ((counter % 100) == 0){
            int t1 = time(NULL);
            cout << counter <<" elements checked after " << t1-t0 << " seconds." << endl;
        }
        new_item = *it;
        refs = new_item.id_refs;
        for (list<int>::iterator ref=refs.begin(); ref != refs.end(); ++ref ){
            if (!contains(significant_indexes,*ref)){
                significant_indexes.push_back(*ref);
            }
        }
        counter++;
    } 

    ofstream indexes_f;
    indexes_f.open("indexes.txt");
    for (list<int>::iterator it=significant_indexes.begin(); it != significant_indexes.end(); ++it){
        indexes_f << *it << "\n";
    }   

    return 0;
}
*/