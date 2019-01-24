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
    np.random.shuffle(timeseries)
    all_timeseries_online = []
    for serie in timeseries:
        for observation in serie:
            all_timeseries_online.append(observation)
    return np.array(all_timeseries_online)

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

def prepare_XY(scaler):
    timeseries = get_datasets(10)
    ts = timeseries
    ts = ts.reshape((len(ts),1))
    ts = scaler.fit_transform(ts)
    df = pandas.DataFrame(ts)
    df = pandas.concat([df, df.shift(1)], axis=1)
    df.dropna(inplace=True)
    values = df.values
    X,y = values[:, 0], values[:, 1]
    X = X.reshape(len(X), 1, 1)
    return X,y

def train():

    scaler = MinMaxScaler(feature_range = (0,1))
    n_batch = 1
    X,y = prepare_XY(scaler)

    model = Sequential()
    model.add(LSTM(n_batch, batch_input_shape=(n_batch, X.shape[1], X.shape[2]), stateful=True))
    model.add(Dense(1))
    adam = keras.optimizers.Adam(lr=0.003, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
    model.compile(loss='mean_squared_error', optimizer=adam)
    early_stopping_monitor = EarlyStopping(monitor="loss",patience=2, min_delta=0.00001)

    for j in range(5):  # epochs
        model.fit(X, y, epochs=200, batch_size=n_batch, verbose=1, shuffle=False, callbacks=[early_stopping_monitor])
        X,y = prepare_XY(scaler)

    save_model(model)
    return scaler

def train_more():

    scaler = MinMaxScaler(feature_range = (0,1))
    n_batch = 1
    model = load_model()
    X,y = prepare_XY(scaler)
    early_stopping_monitor = EarlyStopping(monitor="loss",patience=5, min_delta=0.000005)

    for j in range(5):  # epochs
        model.fit(X, y, epochs=200, batch_size=n_batch, verbose=1, shuffle=False, callbacks=[early_stopping_monitor])
        X,y = prepare_XY(scaler)

    return scaler