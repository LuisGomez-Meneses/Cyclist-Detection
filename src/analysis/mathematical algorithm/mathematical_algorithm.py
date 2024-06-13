"""
Author: Luis Miguel Gómez Meneses
Email: luisgomez251811@correo.itm.edu.co
Date: 12/06/2024
Version: 1.0

Description:
This script reads a CSV file, creates a regression model to predict output features from input features, and evaluates the model using Mean Squared Error (MSE) and Mean Absolute Error (MAE).

Dependencies:
- pandas (version 2.0.3)  # Update with the correct version
- scikit-learn (version 1.2.2)  # Update with the correct version
- Python (version  3.10.12)  # Update with the correct version

Usage:
Example of how to use the code in this file:
>>> import pandas as pd
>>> from sklearn.model_selection import train_test_split
>>> from sklearn.linear_model import LinearRegression
>>> from sklearn.metrics import mean_squared_error, mean_absolute_error
>>> path = 'Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'
>>> df = pd.read_csv(path)
>>> X = df[['avg_angle', 'avg_distance', 'texture', 'contrast']]
>>> y = df[['centroid_x', 'centroid_y', 'width', 'height']]
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
>>> model = LinearRegression()
>>> model.fit(X_train, y_train)
>>> y_pred = model.predict(X_test)
>>> mse_cx = mean_squared_error(y_test['centroid_x'], y_pred[:, 0])
>>> mse_cy = mean_squared_error(y_test['centroid_y'], y_pred[:, 1])
>>> mse_width = mean_squared_error(y_test['width'], y_pred[:, 2])
>>> mse_height = mean_squared_error(y_test['height'], y_pred[:, 3])
>>> print("Mean Squared Error for centroid_x:", mse_cx)
>>> print("Mean Squared Error for centroid_y:", mse_cy)
>>> print("Mean Squared Error for width:", mse_width)
>>> print("Mean Squared Error for height:", mse_height)
>>> mae_cx = mean_absolute_error(y_test['centroid_x'], y_pred[:, 0])
>>> mae_cy = mean_absolute_error(y_test['centroid_y'], y_pred[:, 1])
>>> mae_width = mean_absolute_error(y_test['width'], y_pred[:, 2])
>>> mae_height = mean_absolute_error(y_test['height'], y_pred[:, 3])
>>> print("Mean Absolute Error for centroid_x:", mae_cx)
>>> print("Mean Absolute Error for centroid_y:", mae_cy)
>>> print("Mean Absolute Error for width:", mae_width)
>>> print("Mean Absolute Error for height:", mae_height)

Additional Information:
- Make sure to have the dependencies installed before running the code.
"""

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Define the path to the CSV file
path = 'Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(path)

# Define input features and output labels
X = df[['avg_angle', 'avg_distance', 'texture', 'contrast']]
y = df[['centroid_x', 'centroid_y', 'width', 'height']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the output labels for the test set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE) for each output label
mse_cx = mean_squared_error(y_test['centroid_x'], y_pred[:, 0])
mse_cy = mean_squared_error(y_test['centroid_y'], y_pred[:, 1])
mse_width = mean_squared_error(y_test['width'], y_pred[:, 2])
mse_height = mean_squared_error(y_test['height'], y_pred[:, 3])

# Print the Mean Squared Error for each output label
print("Mean Squared Error for centroid_x:", mse_cx)
print("Mean Squared Error for centroid_y:", mse_cy)
print("Mean Squared Error for width:", mse_width)
print("Mean Squared Error for height:", mse_height)

# Calculate Mean Absolute Error (MAE) for each output label
mae_cx = mean_absolute_error(y_test['centroid_x'], y_pred[:, 0])
mae_cy = mean_absolute_error(y_test['centroid_y'], y_pred[:, 1])
mae_width = mean_absolute_error(y_test['width'], y_pred[:, 2])
mae_height = mean_absolute_error(y_test['height'], y_pred[:, 3])

# Print the Mean Absolute Error for each output label
print("Mean Absolute Error for centroid_x:", mae_cx)
print("Mean Absolute Error for centroid_y:", mae_cy)
print("Mean Absolute Error for width:", mae_width)
print("Mean Absolute Error for height:", mae_height)
