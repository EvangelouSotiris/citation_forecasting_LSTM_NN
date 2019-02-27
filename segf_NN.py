# @author: Sotiris Evangelou 
# @author: Giorgos Fragkias

import input_provider as ip
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers.core import Dense, Activation, Dropout
import pandas
import time
from progress.bar import Bar
import keras.optimizers
from keras.models import model_from_json
from keras.callbacks import EarlyStopping
import time

def get_timeseries(timeseries_size):
    indexes,timeseries = ip.take_training_sets()
    return np.array(indexes),np.array(timeseries)

def get_datasets(timeseries_size):
    indexes,timeseries = get_timeseries(10)
    return timeseries

def save_model(model, name):
    model_json = model.to_json()
    with open(name+".json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights(name+".h5")
    print("Saved model.")

def load_model(name):
    # load json and create model
    json_file = open(name+'.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights(name+".h5")
    model.compile(loss='mean_squared_error', optimizer='adam')
    print("Loaded model...")
    return model

def prepare_XY(input_size):
    timeseries = get_datasets(10)
    #np.random.shuffle(timeseries)
    X = []
    y1 = []
    y5 = []
    for serie in timeseries:
            if sum(serie[:input_size]) >= 5:
                X.append(serie[:input_size])
                y1.append(serie[input_size])
                y5.append(serie[input_size+4])
    X = np.array(X)
    X = X.astype('float64')
    y1 = np.array(y1)
    y1 = y1.astype('float64')
    y5 = np.array(y5)
    y5 = y5.astype('float64')
    return X,y1,y5

def train():

    input_size = 10 # input timeseries length

    adam = keras.optimizers.Adam(lr=0.003, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
    #early_stopping_monitor = EarlyStopping(monitor="loss",patience=10, min_delta=0.00001)
    
    model = Sequential()
    model.add(LSTM(50, input_shape=(input_size,1),return_sequences=False, stateful=False))
    model.add(Dense(10, activation = 'relu'))
    model.add(Dense(1))
    model.compile(loss='mae',metrics=['acc'], optimizer=adam)
    
    model5 = Sequential()
    model5.add(LSTM(50, input_shape=(input_size,1),return_sequences=False, stateful=False))
    model5.add(Dense(10, activation = 'relu'))
    model5.add(Dense(1))
    model5.compile(loss='mae',metrics=['acc'], optimizer=adam)
    
    X,y1,y5 = prepare_XY(input_size)
    X = X.reshape(X.shape[0],X.shape[1],1)
    start_time = time.time()
    history = model.fit(X, y1, epochs=250, batch_size=20, verbose=1,shuffle=True)#,callbacks=[early_stopping_monitor])
    elapsed_time = time.time() - start_time
    print('Elapsed_time: %d' % elapsed_time + " secs")
    save_model(model,"model1_10batch")
    plt.plot(history.history['acc'])
    plt.show()

    history5 = model5.fit(X, y5, epochs=250, batch_size=20, verbose=1,shuffle=True)#, callbacks=[early_stopping_monitor])
    save_model(model5,"model5_10batch")