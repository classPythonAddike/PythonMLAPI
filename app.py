from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle
import json
import tensorflow as tf
from trainer import train_model

app = Flask(__name__)
api = Api(app)

layersHelp = "Layers to construct the keras.Sequential() with. Example: [('Flatten', (1024, 1024)), ('Dense', 128, 'relu'), ('Activation', 'relu'), ('Dense', 100, 'softmax')]"

data_args = reqparse.RequestParser()
data_args.add_argument("name", type = str, help = "Name of your model", required = True)
data_args.add_argument("compile_parameters", type = list, help = "Parameters to pass to the model when compiling.", required = True)
data_args.add_argument("layers", type = list, help = layersHelp, required = True)
data_args.add_argument("epochs", type = int, help = "Number of epochs")
data_args.add_argument("train_X", type = list, help = "Please select the training_data => train_X", required = True)
data_args.add_argument("train_y", type = list, help = "Please select the training_data => train_y", required = True)

test_args = reqparse.RequestParser()
test_args.add_argument("name", type = str, help = "Name of your model")
test_args.add_argument("test_X", type = list, help = "Testing X")

class KerasTrain(Resource):
	
	def get(self):
		args = data_args.parse_args()
		clean_args = {
		'name': args['name'],
		"compile_parameters": json.loads("".join(args['compile_parameters'])),
		"layers": json.loads("".join(args['layers'])),
		"train_X": json.loads("".join(args['train_X'])),
		'train_y':json.loads("".join(args['train_y'])),
		'epochs': args['epochs']}

		s = train_model(**clean_args)
		if s != -1:
			s.save(f"models\\{clean_args['name']}")

			return {"message": "Successfully trained model!"}, 200
		else:
			return {"message": "There was an error during training. Please check the arguments you have provided."}
		
	def post(self):
		args = test_args.parse_args()
		clean_args = {
		'name': args['name'],
		"test_X": json.loads("".join(args['test_X'])),
		}
		model = tf.keras.models.load_model(f"models\\{clean_args['name']}")
		try:
			p = model.predict(clean_args['test_X'])
		except:
			return "hi"

		return {"prediction": p.tolist()}, 200

api.add_resource(KerasTrain, "/api")

if __name__ == "__main__":
	app.run(debug=True)