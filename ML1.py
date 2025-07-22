import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#split data into training and testing
from sklearn.model_selection import train_test_split
#algorithim we use
from sklearn.tree import DecisionTreeClassifier
#find accuracy
from sklearn import metrics

#get data into program
data = pd.read_csv('data.csv')

#verify data has been successfully imported
print(data.head())
print(data.info())

#data preprocessing 
data["species"] = data["species"].replace({"setosa":0,"versicolor":1,"virginica":2})

#basic data-analysis
Y = data["species"]

X = data.drop("species",axis = 1)
#print(X.head())

X_train, x_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 1)

print(X_train.shape)
print(X_test.shape)

model = DecisionTreeClassifier(max_depth = 3, random_state = 1)

model = fit(X_train, Y_train)

predictions = model.predict(X_test)

print("Accuracy ", metrics.accuracy_score(predictions, Y_test))