import requests # To make get and post requests
import json # To serialize data

# URL for the API
BASE = "http://127.0.0.1:5000/"

'''
Data to pass as arguments
1. name: model name
2. compile_parameter: parameters to pass when compiling the model. It must be in this format:
json.dumps([(Param1, Value), (Param2, Value), etc.])
3. layers: Layers for the neural network. It must be in this format:
json.dumps([('Flatten', INPUT_SHAPE), ('Dense', neurons, activation), ('Activation', activiation), etc.])
4. train_X: training X data (in a list, NOT a NumPy array), in the following format:
json.dumps([data here])
train_y: training Y data (in a list, NOT a NumPy array), in the following format:
json.dumps([data here])
epochs: Number of epochs (integer)
'''
data = {
	'name': 'ME',
	'compile_parameters': json.dumps([('optimizer', 'adam'), ('loss', 'sparse_categorical_crossentropy'), ('metrics', ['accuracy'])]),
	'layers': json.dumps([('Flatten', (2)), ('Dense', 16, 'relu'), ('Dense', 16, 'softmax')]),
	'train_X': json.dumps([[1, 1], [12, 3]]),
	'train_y': json.dumps([2, 15]),
	'epochs': 10
}

# Use get requests to train a model
args = requests.get(BASE + "api", data)
print(args.json())

# Use post requests to test/evaluate a model, using the model name and test_X
b = requests.post(BASE + "api", {'name': 'ME', 'test_X': json.dumps([[1, 3], [12, 3]])})
print(b.json())