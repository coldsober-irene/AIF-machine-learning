from keras.layers import SimpleRNN, Input
from keras.models import Model

# Define the input layer
input_layer = Input(shape=(None, input_dim))

# Define the RNN layer
rnn_layer = SimpleRNN(hidden_size)(input_layer)

# Define the output layer
output_layer = Dense(output_dim)(rnn_layer)

# Create the model
model = Model(input_layer, output_layer)
model.compile(optimizer='adam', loss='mse')
