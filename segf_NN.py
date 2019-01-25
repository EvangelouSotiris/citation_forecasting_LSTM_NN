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
from sklearn.preprocessing import MinMaxScaler

def get_timeseries(timeseries_size):
    indexes,timeseries = ip.take_training_sets()
    return np.array(indexes),np.array(timeseries)

def get_datasets(timeseries_size):
    indexes,timeseries = get_timeseries(10)
    pandas.DataFrame(timeseries[2201:]).to_csv("Testing_timeseries.csv", index=False)
    timeseries = timeseries[:2201]
    return timeseries

def save_model(model):
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model.h5")
    print("Saved model.")

def load_model():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("model.h5")
    model.compile(loss='mean_squared_error', optimizer='adam')
    print("Loaded model...")

    return model

def prepare_XY(scaler,input_size):
    timeseries = get_datasets(10)
    X = []
    y = []
    for serie in timeseries:
        X.append(serie[:input_size])
        y.append(serie[input_size])
    X = np.array(X)
    X = X.astype('float64')
    y = np.array(y)
    y = y.astype('float64')
    #X = scaler.fit_transform(X)
    #y = y.reshape(-1,1)
    #y = scaler.fit_transform(y)
    return X,y

def train():

    scaler = MinMaxScaler(feature_range = (0,1))
    X,y = prepare_XY(scaler,10)
    X = X.reshape(X.shape[0],X.shape[1],1)
    
    model = Sequential()
    model.add(LSTM(100, input_shape=(10,1),return_sequences=True, stateful=False))
    model.add(LSTM(50,stateful=False))
    model.add(Dense(1))
    adam = keras.optimizers.Adam(lr=0.003, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
    model.compile(loss='mean_squared_error',metrics=['acc'], optimizer=adam)
    early_stopping_monitor = EarlyStopping(monitor="loss",patience=15, min_delta=0.00001)

    for i in range(10):
        model.fit(X, y, epochs=100, batch_size=10, verbose=1, shuffle=False, callbacks=[early_stopping_monitor])
        model.reset_states()

    save_model(model)
    return scaler

def train_more():

    scaler = MinMaxScaler(feature_range = (0,1))
    n_batch = 1
    model = load_model()
    X,y = prepare_XY(scaler)
    early_stopping_monitor = EarlyStopping(monitor="loss",patience=4, min_delta=0.000005)

    for j in range(1):  # epochs
        model.fit(X, y, epochs=10, batch_size=n_batch, verbose=1, shuffle=False, callbacks=[early_stopping_monitor])
        X,y = prepare_XY(scaler)

    return scaler