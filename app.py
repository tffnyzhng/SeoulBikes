# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 01:47:37 2022

@author: Tiffany
"""

import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 0)

    return render_template('index.html', prediction_text='La prédiction du nombre de vélos loués est : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)