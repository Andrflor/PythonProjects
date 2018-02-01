# -*- coding: utf-8 -*-

import numpy as np
from keras.models import Sequential
from keras.optimizers import SGD
from keras.layers import Dense, Activation

epoch_nm = 50

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[0],[0],[1]])

network = Sequential()
#network.add(Dense(2, activation="sigmoid", input_dim = 2, init = "zeros"))
network.add(Dense(1, activation="sigmoid", input_dim = 2, init = "zeros"))
network.compile(loss = "mse", optimizer = 'SGD')

def fit():
    network.fit(X, Y, nb_epoch = epoch_nm)

def getAdequation(training_set,intended_result):

    res = network.predict_classes(training_set)==intended_result
    proba = 0

    for element in res:
            if(element[0]):
                proba += 1
    proba /= len(res)
    proba *= 100
    return proba

while (getAdequation(X,Y) <= 95):
    fit()

print(network.get_weights())
print("")
print("---------------------------------------")
print("Adequation percentage = %s" % getAdequation(X,Y), "%")
#print("Total number of epoch = %s" % network )
