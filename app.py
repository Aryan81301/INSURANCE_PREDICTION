import joblib
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import gunicorn
from sklearn.preprocessing import StandardScaler

filename = 'model.pkl'
classifier = pickle.load(open(filename,'rb'))
model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__,template_folder='Template')

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values())
        new_l=[]
        for x in to_predict_list:
            if x=='male':
                new_l.append(1)
            elif x=='female':
                new_l.append(0)
            elif x=='yes':
                new_l.append(1)
            elif x=='no':
                new_l.append(0)
            else:
                new_l.append(x)
        #ss=StandardScaler()
        #new_l=ss.fit_transform([new_l])
        new_l = list(map(float, new_l))
        result = ValuePredictor(new_l)
        if int(result)== 1:
            prediction ='YES , PERSON CAN CLAIM INSURANCE.......THANKS FOR CHECKING.........'
        else:
            prediction ='''NO , PERSON WILL NOT CLAIM INSURANCE
            .......THANKS FOR CHECKING.........'''            
    return render_template("result.html", prediction = prediction) 

            

if __name__ == "__main__":
    app.run(debug=True)
