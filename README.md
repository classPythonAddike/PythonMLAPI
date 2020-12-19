# Python API for Keras Neural Networks

## Introduction

This API was written to allow users to use the Keras API without having to download it. It takes arguments like the model name to save as, the parameters to pass when compiling, the layers of the neural network, the number of epochs, and of course, the training data. To test your model, simply pass the name of the model to test and the testing data (X).

## Setup

1. First download the repository with -
```bash
$ git clone https://github.com/classPythonAddike/PythonMLAPI.git
```

2. Then install the requirements with - 
```bash
$ pip install -r requirements.txt
```
NOTE: You can also install the requirements manually should you require specific versions. The modules used are-
a) Tensorflow
b) Flask
c) Flask-Restful

3. Finally, start the API with 
```bash
$ python app.py
```

You can use the file `app_tester.py` to test the API.
