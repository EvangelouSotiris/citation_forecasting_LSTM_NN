#include <iostream>
#include <list>
#include <fstream>
#include "parser_lister.cpp"

using namespace std;

int *count_citations(list<Items_struct> cit_items, int *references){
	list<int> curr_ref_table;
	
	for (list<Items_struct>::iterator it=cit_items.begin(); it != cit_items.end(); ++it){
		curr_ref_table = it->id_refs;
		for (list<int>::iterator curr=curr_ref_table.begin(); curr != curr_ref_table.end(); ++curr){
			references[*curr]++;
		}
	}
	return references;
}

int main(int argc, char *argv[]){
	list<Items_struct> all_items = creating_list();

	Items_struct new_item;
	list<Items_struct> cit_items;

	for (list<Items_struct>::iterator it=all_items.begin(); it != all_items.end(); ++it) {
        new_item = *it;
        if(new_item.id_refs.empty()){
            continue;
        }
        else{
            cit_items.push_back(new_item);
        }
    }

    ifstream sign_file ("indexes.txt");
    string line;
    list<int> indexes;

    if(sign_file.is_open()){
        getline(sign_file,line);
        while (getline(sign_file,line)){
            indexes.push_back(atoi(line.c_str()));
        }
    }
    sign_file.close();

    indexes.sort();
    
    int i=0;
    int end = indexes.size();
    list<Items_struct> intermediate_list;

    Items_struct* all_items_array = new Items_struct[all_items.size()];
	int array_counter = 0;
	
	for(list<Items_struct>::iterator it=all_items.begin(); it != all_items.end(); ++it){
		new_item = *it;
		all_items_array[i] = new_item;
		i++;
	} //kataskeyasa to array wste na epistrefw mpam ta stoixeia me vash th thesh

	i=0;
    for(list<int>::iterator it=indexes.begin(); it != indexes.end(); ++it){
    	new_item = all_items_array[*it];
    	intermediate_list.push_back(new_item);
    	i++;
    }
    int* references;
    references = (int*) malloc(629814*sizeof(int));
    for (i=0; i < 629814; i++){
    	references[i] = 0;
    }
    references = count_citations(cit_items, references);
    list<Items_struct> final_list;

    for (i=0; i < 629814; i++){
    	if (references[i] > 30) {
    		final_list.push_back(all_items_array[i]);
    	}
    }

    cout << final_list.size() << " items with above 30 citations."<< endl;
    ofstream filetowrite;
	filetowrite.open("final_list.txt");
    for (list<Items_struct>::iterator it=final_list.begin(); it != final_list.end(); ++it) {
    	filetowrite << it->index << "\n";
    }
	filetowrite.close();
	return 0;
}