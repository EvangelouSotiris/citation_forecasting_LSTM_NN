# @author: Sotiris Evangelou 
# @author: Giorgos Fragkias

import input_provider as ip
import tensorflow as tf

def get_training_dataset(timeseries_size):
	index,timeseries,t1,t5 = ip.take_random_training_set(timeseries_size)
	print("Testing paper with index: " + str(index))
	print("The citation list of its first " + str(timeseries_size) + " years is: " + str(timeseries))
	print("The target of the next year's citation number is: " + str(t1))
	print("The target of the citation number after 5 years is: " + str(t5))

get_training_dataset(10)