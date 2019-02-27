# Neurofuzzy_project

The project is for ce448 Neural Fuzzy Networks 6-month project
To download the repository run:
```
git clone https://bitbucket.org/SotirisEvangelou/neurofuzzy_project.git
```

# Prerequisites

To run the program firstly you need to have a dir called Project outside the neurofuzzy_project dir.
Inside that directory you need to copy the file output_acm.txt with our input data.

Download citation-network v1 data by clicking this link: [Aminer](http://aminer.org/lab-datasets/citation/citation-network1.zip)

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
