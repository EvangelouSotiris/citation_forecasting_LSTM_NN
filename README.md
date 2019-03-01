# Scientific paper citation forecasting 

To download the repository run:
```
git clone https://github.com/EvangelouSotiris/citation_forecasting_LSTM_NN.git
```

# Prerequisites

To run the program firstly you need to have a dir called "Project" outside the repository's dir.
Inside that directory you need to copy the file output_acm.txt with our input data.

Download citation-network v1 data by clicking this link: [Aminer](http://aminer.org/lab-datasets/citation/citation-network1.zip)

Download the libraries used by the program (keras/pandas/tensorflow etc.) with pip:
```
pip install <name of the library>
```
# Timeseries length VS features used by NN

Since Keras cannot handle multiple length batches the predictions in relevance to the timeseries length:
* Is based on the last 5 years, for timeseries of length < 10
* Is based on the last 10 years, for timeseries of length >= 10 and < 15
* Is based on the last 15 years, for timeseries of length >= 15 

The above three models and their weights after training are included in the repository.
# Running

The user can act by using test_suite.py.
To train the network run:
```
python3 test_suite.py train
```
To test on untrained data included in Testing_timeseries.csv (created after train-test split) run:
```
python3 test_suite.py test
```
To make predictions on your own custom timeseries, create a .txt file containing the timeseries in format:
```
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```
Then run:
```
python3 test_suite.py test [FILE_PATH]
```
where [FILE_PATH] is your .txt's full path.

# Authors
* **Evangelou Sotiris** - *Developer* - [Github](https://github.com/EvangelouSotiris)
* **Fragkias Giorgos** - *Developer*
