"""
This module's purpose is to provide two significant functions (for the training part).
First, it reads the input_dataset.txt and creates the input datasets that our neural network will use.
Second, it provides a function that randomly chooses one of the datasets to give as input to the nn.

Also!
Professor's test set reader is availiable.

"""
from random import shuffle

def parse_timeseries(line):
	curr_timeseries = []
	i = 0
	while True:
		try:
			citation = int(line.split(',')[i])
			curr_timeseries.append(citation)
			i += 1
		except IndexError:
			return curr_timeseries

def create_datasets():
	# reading input_dataset.txt and creating a list with the lines to be parsed later on.
	lines = []
	with open('final_input.txt','r') as input_dataset:
		newline = input_dataset.readline()
		while newline:
			lines.append(newline)
			newline = input_dataset.readline()
	input_dataset.close()
	# end
	#parsing lines list and creating tuple list with tuple being (index, time series list)
	all_datasets = []
	for line in lines:
		curr_index = int(line.split(':')[0])
		curr_timeseries = parse_timeseries(line.split('[')[1].split(']')[0])
		all_datasets.append((curr_index,curr_timeseries))
	return all_datasets

def professors_test_set(filename, datalength):
	with open(filename,'r') as profs_input:
		line = profs_input.readline()
	timeseries = parse_timeseries(line,datalength)	
	profs_input.close()
	return timeseries

def take_training_sets():
	all_datasets = create_datasets()
	indexes = []
	timeseries = []
	for dataset in all_datasets:
		indexes.append(dataset[0])
		timeseries.append(dataset[1])
	return indexes,timeseries