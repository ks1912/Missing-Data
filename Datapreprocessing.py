# -*- coding: utf-8 -*-
# DATA PREPROCESSING
# Importing the libraries 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# IMPORTING DATA SET'S
dataset = pd.read_csv('editeddata.csv')
X = dataset.iloc[:,:-1].values # Creating independent variable vector
# print(X)
Y = dataset.iloc[:,3].values # Creating dependent variable vector
# print(Y)

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN",strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:,1:3] = imputer.transform(X[:,1:3])