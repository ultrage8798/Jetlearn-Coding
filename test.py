import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Adults=pd.read_csv("adult.csv")

Adults.columns=["age","workclass","fnlwgt","education","educational-num","marital-status","occupation","relationship","race","gender","capital-gain","capital-loss","hour-per-week","native-country","income"]
Adults.rename(columns = {"age":"Age","occupation":"Work","capital-gain":"Gain","hour-per-week":"Weekly Hours"},inplace = True)

print(Adults.isnull().sum())

# print(Adults.head(5))
# print(Adults.info())