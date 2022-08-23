# Telco-Customer-Churn-Project
## Problem Description
To reduce customer churn, telecom companies need to predict which customers are at high risk of churn.
To detect early signs of potential churn, one must first develop a holistic view of the customers and their interactions across numerous channels, including store/branch visits, product purchase histories, customer service calls, Web-based transactions, and social media interactions, to mention a few.
As a result, by addressing churn, these businesses may not only preserve their market position, but also grow and thrive. More customers they have in their network, the lower the cost of initiation and the larger the profit. As a result, the company's key focus for success is reducing client attrition and implementing effective retention strategy.
## Data Description
![image](https://user-images.githubusercontent.com/81258866/186208489-930f4e2e-a93b-449f-9068-50ed6a1d0805.png)
![image](https://user-images.githubusercontent.com/81258866/186208530-9a45a81f-e064-4d62-8729-c0d94ed1c5b6.png)
## Database Design
In the project, the database design was made as star schema. Thus, the data will not take up space on the fact table. The fact table will contain only 1 and 0 data.
We can import raw data in two different ways such as direct import of csv file and DDL operations. We’ve showed both methods and provide sql files.
### 1- Import source csv file into mysql database
![image](https://user-images.githubusercontent.com/81258866/186208716-1f914fbf-1108-4964-9d6a-2ca73f473bcd.png)

Successfully observed that import operation of raw data is completed
![image](https://user-images.githubusercontent.com/81258866/186208749-22c0678c-9325-4439-ac7a-cdae2df3959e.png)
### 2- DDL Operations
#### 2.1 Create table
![image](https://user-images.githubusercontent.com/81258866/186208909-3b9fe11a-812c-43a7-866f-38755c0d7d75.png)

#### 2.2 Insert data (Three examples are shown. Full code is provided in the .sql file)
• INSERT INTO crm.Telco_Customer_Churn (customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn) VALUES ('6713-OKOMC', 'Female', 0, 'No', 'No', 10, 'No', 'No phone service', 'DSL', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Month-to-month', 'No', 'Mailed check', 29.75, 301.9, 'No');
• INSERT INTO crm.Telco_Customer_Churn (customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn) VALUES ('7892-POOKP', 'Female', 0, 'Yes', 'No', 28, 'Yes',
'Yes', 'Fiber optic', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Month-to-month', 'Yes', 'Electronic check', 104.8, 3046.05, 'Yes');
• INSERT INTO crm.Telco_Customer_Churn (customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn) VALUES ('6388-TABGU', 'Male', 0, 'No', 'Yes', 62, 'Yes', 'No', 'DSL', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'One year', 'No', 'Bank transfer (automatic)', 56.15, 3487.95, 'No');
## Normalization and Data Modeling
As database design, we aim to have a star schema based database. In order to accomplish that we’ve done following:
#### 1.  Draw a ER-Diagram
![image](https://user-images.githubusercontent.com/81258866/186209556-d05c4233-b18f-4143-917f-a0bc2944970b.png)
#### 2.  Create a fact table from denormalized raw data
Add surrogate key “id” column and create fact table
![image](https://user-images.githubusercontent.com/81258866/186209710-fccf0738-c137-4975-a7b8-0308707cf3d1.png)

#### 3.  Create dimension table
#### 3.1. Generate random customer data
#### 3.1.1 Create customer dimension table:
![image](https://user-images.githubusercontent.com/81258866/186209868-151a76a8-1f5a-475a-ac14-291e67ff1073.png)
Insert generated customer data:
![image](https://user-images.githubusercontent.com/81258866/186209979-5401196e-646d-47d3-abf6-919b36946558.png)
We’ve generated 7500 customer information. Full script is available attached sql file.
However there were some duplicate rows. We handled them by deleting duplicates. Since we have only 7032 customer in source data getting rid of all duplicate was not an issue.
![image](https://user-images.githubusercontent.com/81258866/186210316-dc3af0f0-6b66-498e-be7e-ad7b818aba8c.png)
So, we have customer dimension that we can relate on id column. For example:
![image](https://user-images.githubusercontent.com/81258866/186210383-50611ce7-aff8-4192-8f0f-8b1357aa7949.png)
#### 3.1.2. Create tables from existing data:
Create multipleLines dimension table:
![image](https://user-images.githubusercontent.com/81258866/186210465-4962a8df-3a46-414c-910e-f1dd28153e98.png)
Updating the fact table with corresponding dimension id:
![image](https://user-images.githubusercontent.com/81258866/186210527-38cfa65b-ce5f-494d-849c-327a4b81d47a.png)
The other multiple lines dimension tables was created as like upper. The table names are d_internetservice, d_onlinesecurity, d_onlinebackup, d_onlinebackup, d_deviceprotection, d_techsupport, d_streamingtv, d_streamingmovies, d_paymentmethod, d_paperlessbilling.
In order to manipulate the data and then make churn analysis, the raw data was pulled from the SQL database as follows.
![image](https://user-images.githubusercontent.com/81258866/186210586-62224b3c-9f01-4e1a-92e3-4f1a5d51e320.png)
The details of the codes for data manipulation and modeling are given in the appendix as a code file.

#### 5.  Result of Application
We use accuracy metric for evaluating models. As can be seen below value, best models are Random Forest and Voting Classifier.
KNN accuracy: 0.7753554502369668
SVM accuracy: 0.8075829383886256
Random Forest accuracy: 0.8137440758293839
Logistic Regression accuracy: 0.8090047393364929
Decision Tree accuracy: 0.7255924170616114
AdaBoost Classifier accuracy: 0.8075829383886256
Gradient Boosting Classifier accuracy: 0.8080568720379147
Confusion matrix of Random Forest;
![image](https://user-images.githubusercontent.com/81258866/186210755-ccef46ef-6896-40f7-86d4-21583900dd9d.png)
ROC Curve of Random Forest;
![image](https://user-images.githubusercontent.com/81258866/186210806-44449f35-3655-4121-8ee9-b757733812d4.png)
Voting Classifier
Let's now predict the final model based on the highest majority of voting and check it's score.
Final Accuracy Score: 0.8170616113744076
![image](https://user-images.githubusercontent.com/81258866/186210887-ecf5f461-9624-432c-b9e1-6523e7a16627.png)
From the confusion matrix we can see that: There are total 1400+149=1549 actual non-churn values and the algorithm predicts 1400 of them as non churn and 149 of them as churn. While there are 237+324=561 actual churn values and the algorithm predicts 237 of them as non churn values and 324 of them as churn values.
#### 6. Sample User Interface via Fast API
We also try to develop a REST API in order to get prediction about new user in near real time. We’ve used Fast Api framework and test with a random user. For each model that we’ve trained, we created a post endpoint. When we post a new user in json format, our api takes the input json. Then makes necessary transformations like one hot encoding and scaling, fit into model and returns the churn result with probability.
![image](https://user-images.githubusercontent.com/81258866/186210992-0a7d459a-5df5-46a8-b27b-fbeb473ab2c2.png)
1. POST request is sent to an API of the running project on docker container
2. Prediction is evaluated on the same endpoint.
Code snippet:
![image](https://user-images.githubusercontent.com/81258866/186211070-d2a79dff-72b8-49dd-9ae5-9b57db2caf01.png)
Test from FastAPI UI:
![image](https://user-images.githubusercontent.com/81258866/186211120-990cf77f-11ef-4dba-b1a5-d36f4e50e0e6.png)
First let us send a Post request for KNN prediction:
![image](https://user-images.githubusercontent.com/81258866/186211165-c6ccbe40-0e22-497b-b868-b32e553fe83b.png)
Result prediction for KNN:
prediction(churn): 0 and probability: 0.45 for random sample data
![image](https://user-images.githubusercontent.com/81258866/186211282-fe5ac730-cab2-49e1-ac74-4f14436060bc.png)
Result prediction of Random Forest:
prediction(churn): 0 and probability: 0.10 for the same data
![image](https://user-images.githubusercontent.com/81258866/186211356-cf41e083-925b-47cc-abec-ec6d48b6783e.png)
![image](https://user-images.githubusercontent.com/81258866/186211389-fe104214-dbb0-418e-99cd-499cf067c4b4.png)
#### 6. Discussion
Customer churn is definitely bad to a firm ’s profitability. Various strategies can be implemented to eliminate customer churn. The best way to avoid customer churn is for a company to truly know its customers. This includes identifying customers who are at risk of churning and working to improve their satisfaction. Improving customer service is, of course, at the top of the priority for tackling this issue. Building customer loyalty through relevant experiences and specialized service is another strategy to reduce customer churn. Some firms survey customers who have already churned to understand their reasons for leaving in order to adopt a proactive approach to avoiding future customer churn.
#### 7. Results and Recommendation
In this study, churn analysis of telco customers was made. First of all, analyzes were made on the basis of variables. To reduce customer churn, telecom companies need to predict which customers are at high risk of churn. For this purpose, the data set is divided into train and test, and it is planned to establish a modeling for churn analysis by creating machine learning algorithms.
The metrics of the established algorithms were compared and the most ideal one was selected. Thus, it will be possible to predict whether a customer will be churn in the future according to his attitude.
