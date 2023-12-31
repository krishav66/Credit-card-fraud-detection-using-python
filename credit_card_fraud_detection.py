# -*- coding: utf-8 -*-
"""Credit_card_fraud_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12LMSMNDP3Qn-EpF5YQxX605RV8_t7Upe
"""



"""Improting the Dependencies"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#loading the dataset to a panda dataframe
credit_card_data = pd.read_csv('/content/creditcard.csv')

#print first five from data set
credit_card_data.head()

#print last 5 data sets
credit_card_data.tail()

#check the information of data sets
credit_card_data.info()

#check if missing value is present or not
credit_card_data.isnull().sum()

# distribution of legit and fraud transactions
credit_card_data['Class'].value_counts()

"""140438 is legit transaction and 264 is fraud transaction here. dikh jata hai saf saf with vlue. count wale function se"""

#separating the data for better analysis
legit= credit_card_data[credit_card_data.Class==0]
fraud= credit_card_data[credit_card_data.Class==1]

print(legit.shape)
print(fraud.shape)

#getting the statistical measures of the data that is present in amount
legit.Amount.describe()

fraud.Amount.describe()

#compare the values for the transactions
credit_card_data.groupby('Class').mean()



"""method of under sampling"""



"""build a sample dataset containig the similar distribution of normal and fraud transaction"""

legit_sample= legit.sample(n=264)



"""concatenating two data frames"""

new_dataset=pd.concat([legit_sample, fraud],axis=0)

new_dataset.head()

new_dataset.tail()

new_dataset.groupby('Class').mean()

X= new_dataset.drop('Class',axis=1)
Y=new_dataset['Class']

print(X)

print(Y)

#splitting data into training data and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)



"""Model Training
Logistic Reression
"""

model = LogisticRegression()

#Trainig the Logistic regression model with Training data
model.fit(X_train,Y_train)

#accuracy on training data
X_train_prediction= model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction, Y_train)

print('Accuracy on train data :', training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction, Y_test)

print('Accuracy score on test data :', test_data_accuracy)

