python
# Using Keras to define a simple neural network
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential()
model.add(Dense(units=32, activation='relu', input_dim=8))
# Simple feedforward model
