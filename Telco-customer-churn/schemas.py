from pydantic import BaseModel

class Churn(BaseModel):
    
    gender:                str
    SeniorCitizen:         int
    Partner:               str
    Dependents:            str
    tenure:                int
    PhoneService:          str
    MultipleLines:         str
    InternetService:       str
    OnlineSecurity:        str
    OnlineBackup:          str
    DeviceProtection:      str
    TechSupport:           str
    StreamingTV:           str
    StreamingMovies:       str
    Contract:              str
    PaperlessBilling:      str
    PaymentMethod:         str
    MonthlyCharges:      float
    TotalCharges:        float   

    class Config:
        schema_extra = {
                "example": {
                    "gender": "Male",
                    "SeniorCitizen": 0,
                    "Partner": "No",
                    "Dependents": "No",
                    "tenure": 34,
                    "PhoneService": "Yes",
                    "MultipleLines": "No",
                    "InternetService": "DSL",
                    "OnlineSecurity": "Yes",
                    "OnlineBackup": "No",
                    "DeviceProtection": "Yes",
                    "TechSupport": "No",
                    "StreamingTV": "No",
                    "StreamingMovies": "No",
                    "Contract": "One year",
                    "PaperlessBilling": "No",
                    "PaymentMethod": "Mailed check",
                    "MonthlyCharges": 56.95,
                    "TotalCharges": 1889.50
                    }
        }


class ChurnDriftInput(BaseModel):
    n_days_before: int

    class Config:
        schema_extra = {
            "example": {
                "n_days_before": 5,
            }
        }