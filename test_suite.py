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
    plt.figure(figsize = (8, 5))
    plt.style.use('seaborn-darkgrid')
    markers = [ts_length,ts_length+4]
    plt.plot(given, label = "Given Citations", markevery=markers)
    plt.plot(test, linestyle='dashed', label = "Real timeseries", markevery=markers)
    plt.plot(predictions, label = "Predictions")
    plt.xlabel("Years")
    plt.ylabel("Citations")
    plt.title("PLS WERK")
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
	for test in ts:
		counter += 1
		if counter == 10:
			break
		print("\n~~New Test~~")
		test = test.astype('float32')
		test = test.reshape((len(test),1))
		test = scaler.fit_transform(test)
		df = pandas.DataFrame(test)
		df = pandas.concat([df, df.shift(-1)], axis=1)
		df.dropna(inplace=True)
		values = df.values
		X,y = values[:, 0], values[:, 1]
		X = X.reshape(len(X), 1, 1)
		preds = []
		given_vals = []
		preds.append(0.0)
		for i in range(ts_length):
			testX = X[i]
			testy = y[i]
			testX = testX.reshape(len(testX), 1, 1)
			
			yhat = model.predict(testX, batch_size=1, verbose=0)
			given_vals.append(testX)
			preds.append(yhat)
			#print('>Expected=%.1f, Predicted=%.1f' %(testy, yhat))

		for i in range(4):
			temp = yhat
			temp = temp.reshape(1,1,1)
			yhat = model.predict(temp,batch_size=1,verbose=0)
			preds.append(yhat)

		preds = np.array(preds)
		given_vals = np.array(given_vals)
		preds = preds.reshape((ts_length+5,1))
		given_vals = given_vals.reshape((len(given_vals),1))
		#print(preds)
		test = scaler.inverse_transform(test)
		given_vals = scaler.inverse_transform(given_vals)
		preds = scaler.inverse_transform(preds)
		print('<1 Year after> Expected=%.1f, Predicted=%.1f' %(test[ts_length], preds[ts_length]))
		print('<5 Years after> Expected=%.1f, Predicted=%.1f' %(test[ts_length+4], preds[ts_length+4]))
		graph_timeseries(given_vals,test,preds,ts_length)

#scaler = train_new()
#scaler = train_more()
scaler = MinMaxScaler(feature_range = (0,1))
new_test_run(10,scaler)