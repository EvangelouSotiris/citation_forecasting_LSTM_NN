from sys import argv
from segf_NN import get_datasets,train,save_model,load_model
from input_provider import parse_timeseries
import matplotlib.pyplot as plt
import numpy as np
import keras
import pandas
from keras.models import model_from_json
import time

def graph_timeseries(test,predictions,ts_length, slide=False):
    plt.figure(figsize = (10, 6))
    plt.style.use('ggplot')
    if slide == True:
    	plt.plot([len(test)],predictions[0],'bo',markersize=6)
    	plt.plot([len(test)+4],predictions[1],'bo',markersize=6)
    else:
    	plt.plot([ts_length],predictions[0],'bo',markersize=6)
    	plt.plot([ts_length+4],predictions[1],'bo',markersize=6)
    	if len(test) >= ts_length:
    		plt.plot([ts_length],test[ts_length],'o',color='magenta',markersize=4)
    		if len(test) >= ts_length + 5:
    			plt.plot([ts_length+4],test[ts_length+4],'o',color='magenta',markersize=4)
    plt.plot(test, linestyle='dashed',color='magenta', label = "Real timeseries")
    plt.xlabel("Years")
    plt.ylabel("Citations")
    plt.title("Citation Time series Forecasting - Test suite graph")
    plt.legend()
    plt.show()


def train_new():
	train()

def new_test_run(ts_length,model,model5, test_timeserie = None):  # Add capability to open files and take tests from there.
	custom_test_flag = 0
	if test_timeserie == None:
		df = pandas.read_csv("Testing_timeseries.csv")
		ts = df.values
		np.random.shuffle(ts)
		test_timeserie = ts[0]
		testX = test_timeserie[:ts_length]
	else:
		custom_test_flag = 1
		length = len(test_timeserie)
		testX = test_timeserie[length-ts_length:]

	testX = np.array(testX)
	testX = testX.astype('float64')

	testX = testX.reshape(1,ts_length,1)

	y1 = model.predict(testX, batch_size=1, verbose=0)
	y5 = model5.predict(testX, batch_size=1,verbose=0)
	print(y1,y5)
	predictions=[y1,y5]
	testX = testX.reshape(ts_length,1)
	if custom_test_flag:
		graph_timeseries(test_timeserie,predictions,ts_length,True)
	else:
		graph_timeseries(test_timeserie,predictions,ts_length)


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
				if len(timeseries) >= 10 and len(timeseries) < 15:
					print("Loading models for input of length 10")
					model = load_model("model1_10batch")
					model5 = load_model("model5_10batch")
					new_test_run(10,model,model5,timeseries)
				elif len(timeseries) >= 15:
					print("Loading models for input of length 15")
					model = load_model("model1_15batch")
					model5 = load_model("model5_15batch")
					new_test_run(15,model,model5,timeseries)
				elif len(timeseries) >= 5 and len(timeseries) < 10:
					print("Loading models for input of length 5")	
					model = load_model("model1_5batch")
					model5 = load_model("model5_5batch")
					new_test_run(5,model,model5,timeseries)
				exit(0)
			except FileNotFoundError:
				print('The file mentioned does not exist.(At least in this directory)')
				exit(1)
		start_time = time.time()

		model = load_model("model1_10batch")
		model5 = load_model("model5_10batch")
		for i in range(10):
			new_test_run(10,model,model5)
		elapsedtime = time.time() - start_time
		print("Elapsed time: " + str(elapsedtime) + " secs")
