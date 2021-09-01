#!C:/Users/lx615/AppData/Local/Programs/Python/Python38-32/python

#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect, flash
from joblib import dump, load

# extensions
import numpy as np
import pandas as pd
import math
import time


#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL

#Define a route to hello function
@app.route('/',methods=['GET', 'POST'])
def hello():
    with open("counter.file","r",encoding="utf-8") as counter:
        count = counter.read()
    counter.close()
    return render_template('index.html', instruction = 'Finish the form and click \"Calculate\".',count = count)


@app.route('/calculate',methods=['GET', 'POST'])
def calculate():

        # Loading from the Form
        f1 = request.form['f1']
        f2 = request.form['f2']
        f3 = request.form['f3']
        f4 = request.form['f4']
        f5 = request.form['f5']
        f6 = request.form['f6']
        print("features loaded",f1,f2,f3,f4,f5,f6)
       

        # Calculation
        a = np.array([f1,f2,f3,f4,f5,f6])
        a = a.reshape(1, 6)
        df_test = pd.DataFrame(data=a,
                               columns=["f1","f2","f3","f4","f5","f6"])
        print('df created')
        model = load('model.joblib')
        pred = model.predict(df_test)
        print('Model Prediction is', pred)
        pred = pred.tolist()[0]

        # Rendering
        return render_template('index.html', instruction = 'Postoperative refraction prediction:', result = str("{:.2f}".format(pred)+' D'), count = str(count))


if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
