from segf_NN import get_datasets
from segf_NN import train
from segf_NN import train_more
from segf_NN import save_model
from segf_NN import load_model
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import keras
import pandas
from keras.models import model_from_json
from progress.bar import Bar
from sklearn.preprocessing import MinMaxScaler

n_batch = 1

def graph_timeseries(given,test,predictions,ts_length):
    plt.figure(figsize = (10, 6))
    plt.style.use('ggplot')
    plt.plot([ts_length],predictions,'ro',markersize=4)
    plt.plot(given,color='blue', label = "Given Citations")
    if len(test) >= ts_length:
	    plt.plot([ts_length],test[ts_length],'o',color='magenta',markersize=4)
	    if len(test) >= ts_length + 5:
	    	plt.plot([ts_length+4],test[ts_length+4],'o',color='magenta',markersize=4)
    plt.plot(test, linestyle='dashed',color='magenta', label = "Real timeseries")
    plt.plot(predictions, color='red',label="Predictions")
    plt.xlabel("Years")
    plt.ylabel("Citations")
    plt.title("CE448 Neural Networks and Fuzzy logic - Project\nTime series Forecasting - Test suite graph")
    plt.legend()
    plt.show()


def train_new():
	scaler = train()
	return scaler

def train_loaded():
	scaler = train_more()
	return scaler

def new_test_run(ts_length,scaler, filename = None):  # Add capability to open files and take tests from there.

	model = load_model()
	df = pandas.read_csv("Testing_timeseries.csv")
	ts = df.values
	counter = 0
	np.random.shuffle(ts)

	test_timeserie = ts[0]
	testX = test_timeserie[:ts_length]
	testy = test_timeserie[ts_length]

	testX = np.array(testX)
	testX = testX.astype('float64')
	testy = np.array(testy)
	testy = testy.astype('float64')

	testX = testX.reshape(1,10,1)

	yhat = model.predict(testX, batch_size=10, verbose=0)
	
	print('>Expected=%.1f, Predicted=%.1f' %(testy, yhat))

	#testy = scaler.inverse_transform(testy)
	#yhat = scaler.inverse_transform(yhat)
	#if len(test) >= ts_length:
	#	print('<1 Year after> Expected=%.1f, Predicted=%.1f' %(testy, yhat))
	#else:
	#	print('<1 Year after> Predicted=%.1f' %(yhat))	
	testX = testX.reshape(10,1)
	graph_timeseries(testX,test_timeserie,yhat,ts_length)

scaler = train_new()
#scaler = train_more()
scaler = MinMaxScaler(feature_range = (0,1))
new_test_run(10,scaler)