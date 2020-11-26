from flask import Flask, request, url_for, redirect, render_template, jsonify
from pycaret.classification import *
import pandas as pd
import logging
import os
from logging.handlers import RotatingFileHandler
import pickle
import numpy


# initialize our Flask application and the model
app = Flask(__name__)
model = load_model('model_cbc')
cols = ['Mean of the integrated profile', 'Standard deviation of the integrated profile',
		'Excess kurtosis of the integrated profile', 'Skewness of the integrated profile',
		'Mean of the DM-SNR curve', 'Standard deviation of the DM-SNR curve',
		'Excess kurtosis of the DM-SNR curv', 'Skewness of the DM-SNR curve']


handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.route("/")
def index():
	return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
	int_features = [x for x in request.form.values()]
	final = np.array(int_features)
	data_unseen = pd.DataFrame([final], columns=cols)
	prediction = predict_model(model, data=data_unseen, round=0)
	prediction = int(prediction.Label[0])
	return render_template('index.html', pred='HTRU2 {}'.format(prediction))


# @app.route('/predict_api', methods=['POST'])
# def predict_api():
# 	data = request.get_json(force=True)
#     data_unseen = pd.DataFrame([data])
#     prediction = predict_model(model, data=data_unseen)
#     output = prediction.Label[0]
#     return jsonify(output)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == '__main__':
	print(("* Loading the model and Flask starting server..."
		"please wait until server has fully started"))
	port = int(os.environ.get('PORT', 8180))
	app.run(host='0.0.0.0', debug=True, port=port)


