# Given a list, either the forecasting or the validation period, and an index
#this program calculates the total citations of index in that period.

def counter(index, list):

	total_citations = 0
	non_empty = 0

	for i in range(len(list)):
		id_refs = list[i].ret_id_refs()
		if id_refs:
			non_empty += 1
		for j in range(len(id_refs)):
			if index == int(id_refs[j]):
				print 'Referenced by Index '+str(list[i].ret_index())+' ,a paper written in: ' + str(list[i].ret_year())
				total_citations += 1

	#print non_empty
	return total_citations