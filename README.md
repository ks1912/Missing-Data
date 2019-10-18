# Missing-Data-In-CSV File-Through-R-AND-PYTHON

# IDE USED-> For R -> R Studios, For Python -> Spyder

# DATASET 

Country	Age	Salary	Purchased

France	44	72000	    No

Spain	  27	48000	    Yes

Germany	30	54000	    No

Spain	  38	61000	    No

Germany	40		NaN     Yes

France	35	58000	    Yes

Spain		NaN 52000     No

France	48	79000	    Yes

Germany	50	83000	    No

France	37	67000	    Yes

# PYTHON CODE
-------------------------------------------------------------------
#DATA PREPROCESSING
#Importing the libraries 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#IMPORTING DATA SET
dataset = pd.read_csv('editeddata.csv')
X = dataset.iloc[:,:-1].values # Creating independent variable vector
#print(X)
Y = dataset.iloc[:,3].values # Creating dependent variable vector
#print(Y)

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN",strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------
Where dataset.iloc[:,:-1].values means-> The Left side of the comma represents the rows that have to be taken where as Right Side of the Comma represents the number of column's.

Syntax of Imputer(missing_values = "NaN", Strategy = "mean", axis = "0", varbose = 0, copy = True)

Imputer(missing_values = "NaN",strategy = 'mean', axis = 0)

Where in missing_values="NaN" where in place of NaN we have to write what is there in the place of missing values.

Strategy means what u choose to find the missing values u can choose from Mean,Median,Mode

Axis represents weather u have to perform operations in rows or columns

imputer.fit(X[:, 1:3])

Here " fit " represents weather you want to update your dataset with the values you have calculated or not

imputer.transform(X[:,1:3])

Impute all missing values in X.

----------------------------------------------------------------------------------
R CODE
--------------------------------------------------------------------------------

