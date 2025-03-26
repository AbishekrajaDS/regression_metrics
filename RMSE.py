import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    square_value = np.square(y_true - y_pred)
    mse = np.mean(square_value)
    rmse_res = np.sqrt(mse)
    return round(rmse_res,3)