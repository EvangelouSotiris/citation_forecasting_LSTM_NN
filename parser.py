#* --- paperTitle -----> infotype = 1
#@ --- Authors -----> infotype = 2
#t ---- Year -----> infotype = 3
#c  --- publication venue -----> infotype = 4
#index 00---- index id of this paper -----> infotype = 5
#% ---- the id of references of this paper (there are multiple lines, with each indicating a reference)-----> infotype = 6
#! --- Abstract -----> infotype = 7

# THIS PROGRAM SAVES THE WHOLE PARSED TXT LIST OF ITEMS IN THE PICKLE FILE CALLED parsedtxt

import cPickle

class Items_struct():
    def __init__(self, title):
        self.title = title
        self.authors = []
        self.id_refs = []
        self.year = ''
        self.index = 0
        self.abstract = ''

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

    def set_pub_venue(self,pub_venue):
        self.pub_venue = pub_venue

    def set_index(self,index):
        self.index = index

    def set_id_refs(self,id_ref):
        self.id_refs.append(id_ref)

    def ret_id_refs(self):
        return self.id_refs

    def set_abstract(self,abstract):
        self.abstract = abstract

    def print_item(self):
        print '~Printing item ...'
        print self.title
        print self.authors
        print self.year
        if self.pub_venue:
            print self.pub_venue
        if self.index:
            print self.index
        if self.id_refs:
            print self.id_refs
        if self.abstract:
            print self.abstract
        print '\n'


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

	with open('../Project/outputacm.txt','r') as inp:
		line = inp.readline()
		new_item = []
		citations = []
		authors = []
		while line:
			line = inp.readline()
			content,infotype = splitter(line)
			if infotype == 1:
				new_item = Items_struct(content.split('\n')[0])
			elif infotype == 2:
				for i in range(content.count(',')):
					new_item.set_author(content.split(',')[i])
				new_item.set_author(content.split(',')[content.count(',')].split('\n')[0])
			elif infotype == 3:
				new_item.set_year(content.split('\n')[0])
			elif infotype == 4:
				if content:
					new_item.set_pub_venue(content.split('\n')[0])
			elif infotype == 5:
				if content:
					new_item.set_index(content.split('\n')[0])
			elif infotype == 6:
				if content:
					citations.append(content.split('\n')[0])
					new_item.set_id_refs(content.split('\n')[0])
			elif infotype == 7:
				if content:
					new_item.set_abstract(content.split('\n')[0])
			else:
                            if len(new_item.ret_id_refs()) == 0 and new_item.ret_year() > 1990:
                                continue
                            else:
                                item_list.append(new_item)

		inp.close()
        with open("parsedtxt" , "wb") as f:
            cPickle.dump(item_list, f)
        return item_list

if __name__ == '__main__':
	main()
