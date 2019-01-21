# @author: Sotiris Evangelou 
# @author: Giorgos Fragkias

import input_provider as ip
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers.core import Dense, Activation, Dropout

def graph_timeseries(index,timeseries):
	plt.figure(figsize = (8, 5))
	plt.plot(timeseries, label = "Citations in the first 15 years")
	plt.xlabel("Years")
	plt.ylabel("Citations")
	plt.title("Yearly citations of index " + str(index))
	plt.legend()
	plt.show()

def generate_dataset(timeseries_size):
	indexes,x,y,timeseries = ip.take_training_sets(timeseries_size)
	rand = np.random.randint(0,len(indexes))
	return indexes[rand], np.array(x[rand]), np.array(y[rand]), np.array(timeseries[rand])