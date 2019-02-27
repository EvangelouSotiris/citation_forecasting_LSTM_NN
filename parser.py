#* --- paperTitle -----> infotype = 1
#@ --- Authors -----> infotype = 2
#t ---- Year -----> infotype = 3
#c  --- publication venue -----> infotype = 4
#index 00---- index id of this paper -----> infotype = 5
#% ---- the id of references of this paper (there are multiple lines, with each indicating a reference)-----> infotype = 6
#! --- Abstract -----> infotype = 7

# THIS PROGRAM SAVES THE WHOLE PARSED TXT LIST OF ITEMS IN THE PICKLE FILE CALLED parsedtxt

import cPickle

class PaperInfo():
    def __init__(self, title):
        self.title = title
        self.id_refs = []
        self.year = ''
        self.index = 0

    def ret_title(self):
        return self.title
    def ret_index(self):
        return int(self.index)

    def set_author(self,name):
        self.authors.append(name)

    def set_year(self,year):
        self.year = year

    def ret_year(self):
        return int(self.year)

    def set_index(self,index):
        self.index = index

    def set_id_refs(self,id_ref):
        self.id_refs.append(int(id_ref))

    def ret_id_refs(self):
        return self.id_refs

    def print_item(self):
        print "Title: " + self.title
        print "Year: " + str(self.year)
        if self.index:
            print "Index: " + str(self.index)
        if self.id_refs:
            print "References: " + str(self.id_refs)


def splitter(line):
	if line.count('#*') != 0:
		return line.split('#*')[1],1
	elif line.count('#@') != 0:
		return line.split('#@')[1],2
	elif line.count('#t') != 0:
		return line.split('#t')[1],3
	elif line.count('#c') != 0:
		return line.split('#c')[1],4
	elif line.count('#index') != 0:
		return line.split('#index')[1],5
	elif line.count('#%') != 0:
		return line.split('#%')[1],6
	elif line.count('#!') != 0:
		return line.split('#!')[1],7
	else:
		return 'emptyline',0

def main():
    item_list = []
    whole_list = []
    with open('../Project/outputacm.txt','r') as inp:
        line = inp.readline()
        new_item = []
        citations = []
        authors = []
        while line:
            line = inp.readline()
            content,infotype = splitter(line)
            if infotype == 1:
                new_item = PaperInfo(content.split('\n')[0])
            elif infotype == 2:
                continue
            elif infotype == 3:
                new_item.set_year(content.split('\n')[0])
            elif infotype == 4:
                continue
            elif infotype == 5:
                if content:
                    new_item.set_index(content.split('\n')[0])
            elif infotype == 6:
                if content:
                    citations.append(content.split('\n')[0])
                    new_item.set_id_refs(content.split('\n')[0])
            elif infotype == 7:
                continue
            else:
                refs = new_item.ret_id_refs()
                if len(refs)!=0:
                    item_list.append(new_item)
                whole_list.append(new_item)
        print 'Initial list with ' +str(len(item_list))+' elements and wholelist with ' + str(len(whole_list)) +' elements.'
        return item_list,whole_list

if __name__ == '__main__':
    main()
