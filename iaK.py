# -*- coding: utf-8 -*-

import numpy as np
from keras.models import Sequential
from keras.optimizers import SGD
from keras.layers import Dense, Activation

epoch_nm = 3000

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[0],[0],[1]])

network = Sequential()
network.add(Dense(1, input_dim = 2, init = "zeros"))
network.add(Activation("sigmoid"))
network.compile(loss = "mse", optimizer = 'SGD')

network.fit(X, Y, nb_epoch = epoch_nm)
res = network.predict_classes(X)==Y

print(network.get_weights())
print("---------------------------------------")
print("Adequate stick = %s" % res)
print()
