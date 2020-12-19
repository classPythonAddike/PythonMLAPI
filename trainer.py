import tensorflow as tf
from tensorflow import keras

def train_model(name, train_X, train_y, layers, compile_parameters, epochs):
	model = keras.Sequential()

	params = {}
	for i, e in enumerate(compile_parameters):
		if e[0] != 'epochs':
			params[e[0]] = compile_parameters[i][1]

	for i in layers:
		try:
			if i[0] == 'Flatten':
				model.add(keras.layers.Flatten(input_shape = (i[1],)))
			elif i[0] == 'Dense':
				model.add(keras.layers.Dense(i[1], activation = i[2]))
			elif i[0] == 'Activation':
				model.add(keras.layers.Activation(i[1]))
			else:
				pass
		except Exception as e:
			print(e, "Processing")
			return -1

	try:
		model.compile(**params)
		model.fit(train_X, train_y, epochs = epochs)
		return model
	except Exception as e:
		print(e, "Training")
		return -1