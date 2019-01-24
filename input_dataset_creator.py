import parser

def cits_by_year(itemlist,wholelist, index, year):
    cit = 0
    for item in itemlist:
        refs = item.ret_id_refs()
        for ref in refs:
            if item.ret_year() == year and int(ref) == index:
                cit += 1
    return cit

linelist = []
with open("final_list.txt", "r") as f:
	line = f.readline()
	while (line):
		linelist.append(line)
		line = f.readline()
f.close()

final_list_indexes = []
for i in range(len(linelist)):
	final_list_indexes.append(int(linelist[i]))

ref_list , whole_list = parser.main()

final_list = []

for index in final_list_indexes:
	final_list.append(whole_list[index])
lines_to_write = []
final_list_cits = []
i=0
counter = 0
for item in final_list:
    ten_year_cits = []
    year = item.ret_year()
    index = item.ret_index()
    for i in range(year,year+25):
        ten_year_cits.append(cits_by_year(ref_list,whole_list,index, i))
    final_list_cits.append(ten_year_cits)
    lines_to_write.append( str(index) + ": " + str(ten_year_cits)+"\n")
    print("("+str(counter)+"/"+str(len(final_list))+") " + lines_to_write[counter])
    counter += 1

with open("input_dataset.txt", "w") as f:
    for line in lines_to_write:
        f.write(line)

f.close()
