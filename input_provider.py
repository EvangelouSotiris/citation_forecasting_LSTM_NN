"""
This module's purpose is to provide two significant functions (for the training part).
First, it reads the input_dataset.txt and creates the input datasets that our neural network will use.
Second, it provides a function that randomly chooses one of the datasets to give as input to the nn.

Also!
Professor's test set reader is availiable.

"""
from random import shuffle

def parse_timeseries(line, num = -1):
	curr_timeseries = []
	i=0
	while True:
		try:
			citation = int(line.split(',')[i])
			curr_timeseries.append(citation)
			i += 1
			if (num == i):
				target_next_yr = int(line.split(',')[i])
				target_after_5 = int(line.split(',')[i+4])
				return curr_timeseries, target_next_yr, target_after_5
		except IndexError:
			return curr_timeseries,-1,-1

def create_datasets(datalength = None):
	# reading input_dataset.txt and creating a list with the lines to be parsed later on.
	lines = []
	with open('input_dataset.txt','r') as input_dataset:
		newline = input_dataset.readline()
		while newline:
			lines.append(newline)
			newline = input_dataset.readline()
	input_dataset.close()
	# end

	#parsing lines list and creating tuple list with tuple being (index, time series list)
	tuplelist = []
	for line in lines:
		curr_index = int(line.split(':')[0])
		curr_timeseries,target_next_yr,target_after_5 = parse_timeseries(line.split('[')[1].split(']')[0], datalength)
		tuplelist.append((curr_index,curr_timeseries,target_next_yr,target_after_5))
	return tuplelist

def professors_test_set(filename, datalength):
	with open(filename,'r') as profs_input:
		line = profs_input.readline()
	timeseries = parse_timeseries(line,datalength)	
	profs_input.close()
	return timeseries

def take_random_training_set(set_length):
	tuplelist = create_datasets(set_length)
	shuffle(tuplelist)
	index,timeseries,first_t,fifth_t = tuplelist[0]
	if first_t == -1 or fifth_t == -1:
		print("The dataset isnt long enough to see one or both of the targets.")
		print("Choose a smaller timeseries length as arg.")
		exit(1)
	else:
		return index,timeseries,first_t,fifth_t