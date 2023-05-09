from flask import Flask, render_template, request 
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

predModel = pickle.load(open('LinearRegressionModel.pkl','rb'))
car = pd.read_csv("Cleaned_Cardata.csv")

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse = True)
    fueltypes = sorted(car['fuel_type'].unique())

    return render_template('index.html', companies = companies, models = models, years = years, fueltypes = fueltypes)

@app.route('/predict', methods = ['POST'])
def predict():
    company=request.form.get('company')
    car_model=request.form.get('model')
    year=request.form.get('year')
    fuel_type=request.form.get('fuel_type')
    driven=request.form.get('kms_driven')
    prediction=predModel.predict(pd.DataFrame(columns=['company', 'name', 'year', 'kms_driven', 'fuel_type'], data=np.array([company, car_model,year,driven,fuel_type]).reshape(1, 5)))
    print(prediction)

    return str(np.round(prediction[0],2))

if __name__ == "__main__":
    app.run(debug = True)