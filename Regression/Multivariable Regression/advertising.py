import pandas as pd
import statistics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

path_to_file = 'advertising.csv'
df = pd.read_csv(path_to_file)

y = df['Sales']
X = df[['TV', 'Radio','Newspaper']]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)
X.shape

#AUTOMATIC LEARNING
regressor = LinearRegression()
regressor.fit(X_train, y_train)

feature_names = X.columns

model_coefficients = regressor.coef_
coefficients_df = pd.DataFrame(data = model_coefficients,
                              index = feature_names,
                              columns = ['Coefficient value'])

print('\n\nUsing Library:\n',coefficients_df)
print("Value of B0/Regressor Intercept Library: ",regressor.intercept_)
Y_LibPred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze() ,'Predicted': Y_LibPred.squeeze()})
print('\n\n',df_preds)

mae = mean_absolute_error(y_test, Y_LibPred)
mse = mean_squared_error(y_test, Y_LibPred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')