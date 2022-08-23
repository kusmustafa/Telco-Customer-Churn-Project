import models
import os
import pickle
import logging
from sklearn.preprocessing import StandardScaler


def save_model(model):
    try:
        # save the model to disk
        filename = f'{model}.sav'
        pickle.dump(model, open(filename, 'wb'))
        
    except Exception as e:
        raise logging.exception(e)

def get_model(model):
    try:
        loaded_model = pickle.load(open(f'{model}.sav', 'rb'))
        print(f"model {model} is loaded!")

        return loaded_model

    except Exception as e:
        raise logging.exception(e)


def object_to_int(payload):

    if payload in ["Male", "No", "DSL", "Month-to-month", "Bank transfer (automatic)"]:
        payload = 0
    elif payload in ["Female", "Yes", "No phone service", "Fiber optic", "No internet service",
                    "One year", "Credit card (automatic)"]:
        payload = 1
    else:
        payload = 2

    return payload

scaler= StandardScaler()

def get_prediction(model, request):

    gender=object_to_int(request["gender"])
    SeniorCitizen = object_to_int(request["SeniorCitizen"])
    Partner = object_to_int(request["Partner"])
    Dependents = object_to_int(request["Dependents"])
    tenure = scaler.fit_transform([[request["tenure"]]])
    PhoneService = object_to_int(request["PhoneService"])
    MultipleLines = object_to_int(request["MultipleLines"])
    InternetService = object_to_int(request["InternetService"])
    OnlineSecurity = object_to_int(request["OnlineSecurity"])
    OnlineBackup = object_to_int(request["OnlineBackup"])
    DeviceProtection = object_to_int(request["DeviceProtection"])
    TechSupport = object_to_int(request["TechSupport"])
    StreamingTV = object_to_int(request["StreamingTV"])
    StreamingMovies = object_to_int(request["StreamingMovies"])
    Contract = object_to_int(request["Contract"])
    PaperlessBilling = object_to_int(request["PaperlessBilling"])
    PaymentMethod = object_to_int(request["PaymentMethod"])
    MonthlyCharges = scaler.fit_transform([[request["MonthlyCharges"]]])
    TotalCharges = scaler.fit_transform([[request["TotalCharges"]]])

    full_data = [[gender, SeniorCitizen, Partner, Dependents, tenure,
                  PhoneService, MultipleLines, InternetService,
                  OnlineSecurity, OnlineBackup
                  , DeviceProtection, TechSupport, StreamingTV
                  , StreamingMovies, Contract, PaperlessBilling
                  , PaymentMethod, MonthlyCharges, TotalCharges
                  ]]

    pred = model.predict(full_data).tolist()[0]
    prob = model.predict_proba(full_data)[0][1]

    return [pred,prob]


def insert_data(request, prediction, proba, db):
    new_data = models.Churn(

        gender=request['gender'],
        SeniorCitizen = request["SeniorCitizen"],
        Partner = request["Partner"],
        Dependents = request["Dependents"],
        tenure = request["tenure"],
        PhoneService = request["PhoneService"],
        MultipleLines = request["MultipleLines"],
        InternetService = request["InternetService"],
        OnlineSecurity = request["OnlineSecurity"],
        OnlineBackup = request["OnlineBackup"],
        DeviceProtection = request["DeviceProtection"],
        TechSupport = request["TechSupport"],
        StreamingTV = request["StreamingTV"],
        StreamingMovies = request["StreamingMovies"],
        Contract = request["Contract"],
        PaperlessBilling = request["PaperlessBilling"],
        PaymentMethod = request["PaymentMethod"],
        MonthlyCharges = request["MonthlyCharges"],
        TotalCharges = request["TotalCharges"],
        prediction_proba=proba,
        prediction=prediction
    )

    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


