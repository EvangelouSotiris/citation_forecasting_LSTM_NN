from sys import argv
from segf_NN import get_datasets
from segf_NN import train
from segf_NN import save_model
from segf_NN import load_model
from input_provider import parse_timeseries
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import keras
import pandas
from keras.models import model_from_json
from progress.bar import Bar

def graph_timeseries(given,test,predictions,ts_length):
    plt.figure(figsize = (10, 6))
    plt.style.use('ggplot')
    plt.plot([ts_length],predictions[0],'ro',markersize=5)
    plt.plot([ts_length+4],predictions[1],'ro',markersize=5)
    plt.plot(given,color='blue', label = "Given Citations")
    if len(test) >= ts_length:
	    plt.plot([ts_length],test[ts_length],'o',color='magenta',markersize=4)
	    if len(test) >= ts_length + 5:
	    	plt.plot([ts_length+4],test[ts_length+4],'o',color='magenta',markersize=4)
    plt.plot(test, linestyle='dashed',color='magenta', label = "Real timeseries")
    #plt.plot(predictions, color='red',label="Predictions")
    plt.xlabel("Years")
    plt.ylabel("Citations")
    plt.title("CE448 Neural Networks and Fuzzy logic - Project\nTime series Forecasting - Test suite graph")
    plt.legend()
    plt.show()


def train_new():
	train()

def new_test_run(ts_length, test_timeserie = None):  # Add capability to open files and take tests from there.

	model = load_model("model1_10batch")
	model5 = load_model("model5_10batch")

	if test_timeserie == None:
		df = pandas.read_csv("Testing_timeseries.csv")
		ts = df.values
		np.random.shuffle(ts)
		test_timeserie = ts[0]

	testX = test_timeserie[:ts_length]
	testy = test_timeserie[ts_length]

	testX = np.array(testX)
	testX = testX.astype('float64')
	testy = np.array(testy)
	testy = testy.astype('float64')

	testX = testX.reshape(1,10,1)

	y1 = model.predict(testX, batch_size=1, verbose=0)
	y5 = model5.predict(testX, batch_size=1,verbose=0)
	print(y1,y5)
	predictions=[y1,y5]
	testX = testX.reshape(10,1)
	graph_timeseries(testX,test_timeserie,predictions,ts_length)

if __name__ == '__main__':

	if len(argv) <= 1:
		print("Please enter keywords 'test' or 'train' while calling the test_suite.")
		print("'test' keyword can be followed by a filename of format 'timeseriesXX.txt' to test the predictions of the timeseries included.")
		exit(1)
	elif argv[1] == 'train':
		train_new()
	elif argv[1] == 'test':
		if len(argv) == 3:
			filename = argv[2]
			try:
				f = open(filename, 'r')
				timeseries = parse_timeseries(f.readline())
				new_test_run(10,timeseries)
				exit(0)
			except FileNotFoundError:
				print('The file mentioned does not exist.(At least in this directory)')
				exit(1)
		for i in range(5):
			new_test_run(10)