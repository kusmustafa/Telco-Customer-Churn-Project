from database import Base
from sqlalchemy import Column, String, Integer, Float, DateTime, BINARY
from sqlalchemy.sql import func


class Churn(Base):
    __tablename__ = "telco_data"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, autoincrement=True, primary_key=True)
    customerID = Column(String(20))
    gender = Column(String(20))
    SeniorCitizen = Column(Integer)
    Partner = Column(BINARY)
    Dependents = Column(BINARY)
    tenure = Column(Integer)
    PhoneService = Column(BINARY)
    MultipleLines = Column(String(20))
    InternetService = Column(String(20))
    OnlineSecurity = Column(String(20))
    OnlineBackup = Column(String(20))
    DeviceProtection = Column(String(20))
    TechSupport = Column(String(20))
    StreamingTV = Column(String(20))
    StreamingMovies = Column(String(20))
    Contract = Column(String(20))
    PaperlessBilling = Column(BINARY)
    PaymentMethod = Column(String(20))
    MonthlyCharges = Column(Float)
    TotalCharges = Column(Float)
    Churn = Column(BINARY)
    prediction = Column(Float)
    prediction_proba = Column(Float)
    prediction_time = Column(DateTime(timezone=True), server_default=func.now())
    
