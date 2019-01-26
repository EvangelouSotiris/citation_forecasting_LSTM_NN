import parser

reflist, wholelist = parser.main()

refsforpapers = []
for i in range(len(wholelist)):
	years = []
	refsforpapers.append(years)

for item in reflist:
	year = item.ret_year()
	id_refs = item.ret_id_refs()
	for index in id_refs:
		refsforpapers[index].append(year)

indexes_with_over20 = []

for i in range(len(refsforpapers)):
	if len(refsforpapers[i]) >= 20:
		indexes_with_over20.append(i)

table_for_finaltxt = []

for i in indexes_with_over20:
	references = refsforpapers[i]
	year = wholelist[i].ret_year()
	index = wholelist[i].ret_index()
	timeseries = []
	for j in range(20):
		timeseries.append(0)
	for y in references:
		if y-year <= 19 and y-year >= 0:
			timeseries[y-year] += 1
	table_for_finaltxt.append((index,timeseries))

with open('final_input.txt','w') as f:
	for item in table_for_finaltxt:
		(ind,serie) = item
		f.write(str(ind) + ": " + str(serie) + "\n")


