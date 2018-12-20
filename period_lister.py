#outputs a forecasting period of 20 years and a validation period of another 20 years. 
#E.g. for a paper of 1960.
#Forecasting period: 1960-1980.
#Validation period: 1980-2000

##So, EXCLUDED: items with years after 1978 

def period_lister(item, itemlist):
	year = item.ret_year()
	if year > 1980:
		#print 'Wrong year of the item, not consistent with the followed method: '+ str(year)
		return None,None
	else:
		forecasting = []
		validation = []
		for i in range(len(itemlist)):
			curr_year = itemlist[i].ret_year()
			if curr_year >= year and curr_year <= year + 15:
				forecasting.append(itemlist[i])
			elif curr_year > year + 15 and curr_year <= year + 30:
				validation.append(itemlist[i])
			else:
				continue
		return forecasting,validation

if __name__ == '__main__':
	period_lister()