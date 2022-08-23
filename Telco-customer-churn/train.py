import pandas as pd
import numpy as np
import pickle

from utils import save_model

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score


df = pd.read_csv('./data/Telco-Customer-Churn.csv')

df = df.drop(['customerID'], axis = 1)
df['TotalCharges'] = pd.to_numeric(df.TotalCharges, errors='coerce')
df.drop(labels=df[df['tenure'] == 0].index, axis=0, inplace=True)
df["SeniorCitizen"]= df["SeniorCitizen"].map({0: "No", 1: "Yes"})
df["InternetService"].describe(include=['object', 'bool'])
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

def object_to_int(dataframe_series):
    if dataframe_series.dtype=='object':
        dataframe_series = LabelEncoder().fit_transform(dataframe_series)
    return dataframe_series

df = df.apply(lambda x: object_to_int(x))

X = df.drop(columns = ['Churn'])
y = df['Churn'].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.30, random_state = 40, stratify=y)

# Divide the columns into 3 categories, one ofor standardisation, one for label encoding and one for one hot encoding
num_cols = ["tenure", 'MonthlyCharges', 'TotalCharges']
cat_cols_ohe =['PaymentMethod', 'Contract', 'InternetService'] # those that need one-hot encoding
cat_cols_le = list(set(X_train.columns)- set(num_cols) - set(cat_cols_ohe)) #those that need label encoding

scaler= StandardScaler()

X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])


############################

knn_model = KNeighborsClassifier(n_neighbors = 11) 
knn_model.fit(X_train,y_train)
predicted_y = knn_model.predict(X_test)
accuracy_knn = knn_model.score(X_test,y_test)
print("KNN accuracy:",accuracy_knn)

# save the model to disk
filename = 'knn_model.sav'
pickle.dump(knn_model, open(filename, 'wb'))

############################

svm_model = SVC(random_state = 1)
svm_model.fit(X_train,y_train)
predict_y = svm_model.predict(X_test)
accuracy_svc = svm_model.score(X_test,y_test)
print("SVM accuracy is :",accuracy_svc)

# save the model to disk
filename = 'svm_model.sav'
pickle.dump(svm_model, open(filename, 'wb'))

############################

rf_model = RandomForestClassifier(n_estimators=500 , oob_score = True, n_jobs = -1,
                                  random_state =50, max_features = "auto",
                                  max_leaf_nodes = 30)
rf_model.fit(X_train, y_train)

# Make predictions
prediction_test = rf_model.predict(X_test)
print ("Random Forest accuracy is : ", metrics.accuracy_score(y_test, prediction_test))

# save the model to disk
filename = 'rf_model.sav'
pickle.dump(rf_model, open(filename, 'wb'))

############################

lr_model = LogisticRegression()
lr_model.fit(X_train,y_train)
accuracy_lr = lr_model.score(X_test,y_test)
print("Logistic Regression accuracy is :",accuracy_lr)

# save the model to disk
filename = 'lr_model.sav'
pickle.dump(lr_model, open(filename, 'wb'))