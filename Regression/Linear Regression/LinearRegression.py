import pandas as pd
import statistics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

path_to_file = 'student_scores.csv'
df = pd.read_csv(path_to_file)

X_Manual=df.Hours
Y_Manual=df.Scores

X_Manualtrain, X_test, Y_Manualtrain, Y_test = train_test_split(X_Manual, Y_Manual, test_size = 0.2)


#MANUAL LEARNING
X_mean=statistics.mean(X_Manualtrain)
Y_mean=statistics.mean(Y_Manualtrain)

XsubtractMean=X_Manualtrain-X_mean
YsubtractMean=Y_Manualtrain-Y_mean

ProdOfMeanDiff=XsubtractMean*YsubtractMean
SquareOfMeanDiffX=XsubtractMean**2

b1=sum(ProdOfMeanDiff)/sum(SquareOfMeanDiffX)
b0=Y_mean-b1*(X_mean)

print("B0 manually is: ",b0)
print("B1 manually is: ",b1)

Y_ManualRegression=b1*(X_Manualtrain)+b0
Y_ManualPred = b1 * X_test + b0

n=X_Manualtrain.count();
MSE=1/n*(Y_test-Y_ManualPred)**2
SSR=sum(Y_ManualPred-Y_mean)**2
SST=sum(Y_test-Y_mean)**2
DeterminationCoeff=SSR/SST


##USING LIBRARYYYY
X_libraryTrain = X_Manualtrain.values.reshape(-1, 1)
Y_LibraryTrain = Y_Manualtrain.values.reshape(-1, 1)
X_test_reshaped = X_test.values.reshape(-1, 1)

regressor = LinearRegression()
regressor.fit(X_libraryTrain, Y_LibraryTrain)

print("From Library: ",regressor.intercept_)
print("From Library: ",regressor.coef_)
Y_libPrediction = regressor.predict(X_test_reshaped)


df_preds = pd.DataFrame({'Actual': Y_test.squeeze(),'Manual':Y_ManualPred ,'Predicted': Y_libPrediction.squeeze(),
                         'MSE Manual': MSE})
print(df_preds)
print("Determination of Coefficient Manually is: ",DeterminationCoeff)

