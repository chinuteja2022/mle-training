# Median housing value prediction

The housing data can be downloaded from 
"https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

. The script has codes to download the data, train the models and calculate the MSE.
. We also used Random Search CV for hyper parameter tunning the models.

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## To excute the script
python nonstandardcode.py
