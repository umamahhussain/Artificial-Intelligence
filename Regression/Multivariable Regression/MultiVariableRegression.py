import pandas as pd
import statistics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

path_to_file = 'MR_data.csv'
df = pd.read_csv(path_to_file)

y=df.y
X1=df.X1
X2=df.X2

X1_Train, X1_test, X2_Train, X2_test ,Y_Train, Y_test = train_test_split(X1, X2, y, test_size = 0.2)

#MANUAL LEARNING
X1_SquaredSum=(sum(X1_Train**2))-(sum(X1_Train))**2/X1_Train.count()
X2_SquaredSum=(sum(X2_Train**2))-(sum(X2_Train))**2/X2_Train.count()
X1prodY=sum(X1_Train*Y_Train)-(sum(X1_Train)*sum(Y_Train))/X1_Train.count()
X2prodY=sum(X2_Train*Y_Train)-(sum(X2_Train)*sum(Y_Train))/X2_Train.count()
X1prodX2=sum(X1_Train*X2_Train)-(sum(X1_Train)*sum(X2_Train))/X1_Train.count()

b1=((X2_SquaredSum)*X1prodY-(X1prodX2)*(X2prodY))/((X1_SquaredSum)*(X2_SquaredSum)-(X1prodX2)**2)
print("\nValue of B1/X1 Manually: ",b1)

b2=((X1_SquaredSum)*(X2prodY)-(X1prodX2)*(X1prodY))/((X1_SquaredSum)*(X2_SquaredSum)-(X1prodX2**2))
print("Value of B2/X2 Manually: ",b2)

b0=statistics.mean(y)-b1*(statistics.mean(X1))-b2*(statistics.mean(X2))
print("Value of B0/Regressor Intercept Manually: ",b0)

Y_ManualPred=b0+b1*X1_test+b2*X2_test

#AUTOMATIC LEARNING
regressor = LinearRegression()
X_libtrain = df.loc[X1_Train.index, ['X1', 'X2']]
X_libTest = df.loc[X1_test.index, ['X1', 'X2']]
X_libtrain.shape

regressor = LinearRegression()
regressor.fit(X_libtrain, Y_Train)
feature_names = X_libtrain.columns

model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(data = model_coefficients,
                              index = feature_names,
                              columns = ['Coefficient value'])

print('\n\nUsing Library:\n',coefficients_df)
print("Value of B0/Regressor Intercept Library: ",regressor.intercept_)
Y_LibPred = regressor.predict(X_libTest)

df_preds = pd.DataFrame({'Actual': Y_test.squeeze(),'Manual':Y_ManualPred ,'Predicted': Y_LibPred.squeeze()})
print('\n\n',df_preds)

mae = mean_absolute_error(Y_test, Y_LibPred)
mse = mean_squared_error(Y_test, Y_LibPred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')



