from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from math import sqrt

y_predict = model.predict(X_test)

y_predict_orig = scaler.inverse_transform(y_predict)
y_test_orig = scaler.inverse_transform(y_test)

RMSE = float(format(np.sqrt(mean_squared_error(y_test_orig, y_predict_orig)),'.3f'))
MSE = mean_squared_error(y_test_orig, y_predict_orig)
MAE = mean_absolute_error(y_test_orig, y_predict_orig)
r2 = r2_score(y_test_orig, y_predict_orig)
adj_r2 = 1-(1-r2)*(n-1)/(n-k-1)

print('RMSE =',RMSE, '\nMSE =',MSE, '\nMAE =',MAE, '\nR2 =', r2, '\nAdjusted R2 =', adj_r2)

#Output:
""" RMSE = 896.711 
MSE = 804090.7268051868 
MAE = 631.7969626082855 
R2 = 0.7793582534689741 
Adjusted R2 = 0.7097865315898217 """