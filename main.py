import uvicorn
import pickle
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis : float
    entropy : float

# create a app object
app = FastAPI()
pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)

# Index route, open automatically 
@app.get('/')
def index():
    return {'Message':'Hello'}

@app.get('/name')
def get_name(name:str):
    return {'message': f'Hello, {name}'}

@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    print(model.predict([[variance,skewness,curtosis,entropy]]))
    print('Hello')
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    if prediction[0] > 0.5:
        prediction = 'Fake note'
    else:
        prediction = 'Its a Bank note'

    return {
        'prediction' : prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port = 8000)

