import parser
import period_lister as pr
import citation_counter as cit

print 'Parsing input text file...\n'
itemlist = parser.main()

print 'Input has been parsed and itemlist has been created.'
#print 'Searching for paper with index 214163...\n'
#for i in range(len(itemlist)):
#	if itemlist[i].ret_index() == 214163:
#		print 'Found item with year index %d in year %d' %(itemlist[i].ret_index(),itemlist[i].ret_year())
#		item_found = itemlist[i]
#		break

for i in range(len(itemlist)):
	item_found = itemlist[i]
	if item_found.ret_year() >1980 or item_found.ret_year() == -1:
		continue
	print ''
	item_found.print_item()

	forecasting,validation = pr.period_lister(item_found , itemlist)
	if not forecasting:
		continue

	minyr = 3000
	maxyr = 0
	print '~~~forecasting list: %d items~~~' %len(forecasting)
	for i in range(len(forecasting)):
		if forecasting[i].ret_year() < minyr:
			minyr = forecasting[i].ret_year()
		if forecasting[i].ret_year() > maxyr:
			maxyr = forecasting[i].ret_year()
	print 'year range = (%d,%d)\n' %(minyr,maxyr)

	print '~~~validation list: %d items~~~' %len(validation)
	minyr = 3000
	maxyr = 0
	for i in range(len(validation)):
		if validation[i].ret_year() < minyr:
			minyr = validation[i].ret_year()
		if validation[i].ret_year() > maxyr:
			maxyr = validation[i].ret_year()
	print 'year range = (%d,%d)\n' %(minyr,maxyr)
		
	print 'Counting the citations of index in forecasting period: %d' %cit.counter(int(item_found.ret_index()) , forecasting)

	print 'Counting the citations of index in validation period: %d' %cit.counter(int(item_found.ret_index()) , validation)

