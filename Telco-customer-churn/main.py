import models
import pandas as pd
from utils import *
import os
import pickle


from database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, Request
from schemas import Churn, ChurnDriftInput

app = FastAPI()

@app.post("/prediction/churn/knn")
async def predict_churn(req: Churn,  db: Session = Depends(get_db)):

    knn_model = get_model("knn_model")
    print(type(knn_model))
    pred = get_prediction(model=knn_model, request=req.dict())[0]
    proba = get_prediction(model=knn_model, request=req.dict())[1]

    return {"prediction": pred, 'probability': proba
    }

    
@app.post("/prediction/churn/svm")
async def predict_churn(req: Churn,  db: Session = Depends(get_db)):

    svm_model = get_model("svm_model")

    pred = get_prediction(model=svm_model,request=req.dict())[0]
    proba = get_prediction(model=svm_model,request=req.dict())[1]
    
    return {"prediction": pred, 'probability': proba
    }

@app.post("/prediction/churn/rf")
async def predict_churn(req: Churn,  db: Session = Depends(get_db)):

    rf_model = get_model("rf_model")

    pred = get_prediction(model=rf_model,request=req.dict())[0]
    proba = get_prediction(model=rf_model,request=req.dict())[1]
    return {"prediction": pred, 'probability': proba
    }

@app.post("/prediction/churn/lr")
async def predict_churn(req: Churn,  db: Session = Depends(get_db)):

    lr_model = get_model("lr_model")

    pred = get_prediction(model=lr_model,request=req.dict())[0]
    proba = get_prediction(model=lr_model,request=req.dict())[1]
    return {"prediction": pred, 'probability': proba
    }