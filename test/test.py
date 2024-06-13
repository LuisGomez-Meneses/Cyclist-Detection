"""
Author: Luis Miguel Gómez Meneses
Email: luisgomez251811@correo.itm.edu.co
Date: 12/06/2024
Version: 1.0

Description:
This script demonstrates the general behavior of the algorithms used for preprocessing, analyzing, and visualizing cyclist detection data.

Dependencies:
- numpy==1.25.2
- pandas==2.0.3
- matplotlib==3.7.1
- seaborn==0.13.1
- scikit-learn==1.2.2
- opencv-python==4.8.0
- scikit-image==0.19.3

Usage:
Run this script to see an example of data preprocessing, analysis, and visualization.
"""

import os
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from skimage.feature import greycomatrix, greycoprops
from skimage.transform import hough_line, hough_line_peaks
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import sys

# Load the dataset
path = 'Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'
df = pd.read_csv(path)

# Add paths to custom modules
sys.path.append('/content/Cyclist-Detection/src/visualization')
sys.path.append('/content/Cyclist-Detection/src/preprocessing')
sys.path.append('/content/Cyclist-Detection/src/analysis/statistical description of data')
sys.path.append('/content/Cyclist-Detection/src/analysis/separability of data/correlation_heatmap')
sys.path.append('/content/Cyclist-Detection/src/analysis/feature vs centroid_x')
sys.path.append('/content/Cyclist-Detection/src/analysis/feature vs centroid_y')
sys.path.append('/content/Cyclist-Detection/src/analysis/feature vs width')
sys.path.append('/content/Cyclist-Detection/src/analysis/feature vs height')

# Import custom functions
from kde_plot_input_features import kde_plot_input_features
from hough_features import calculate_hough_features
from texture_contrast_features import calculate_texture_contrast_features
from normalize_features import normalize_features
from statistical_description_of_data import statistical_description_of_data
from correlation_heatmap import correlation_heatmap
from scatter_plots_feature_vs_centroid_x import scatter_plots_feature_vs_centroid_x
from scatter_plots_feature_vs_centroid_y import scatter_plots_feature_vs_centroid_y
from scatter_plots_feature_vs_width import scatter_plots_feature_vs_width
from scatter_plots_feature_vs_height import scatter_plots_feature_vs_height

# Define the base path for raw data
base_path = "Cyclist-Detection/data/raw"
data = []

# Iterate through each folder in the base path
folders = os.listdir(base_path)
for folder in folders:
    cyclist_type_path = os.path.join(base_path, folder)
    if os.path.isdir(cyclist_type_path):
        files = os.listdir(cyclist_type_path)
        for file in files:
            file_path = os.path.join(cyclist_type_path, file)
            if file.lower().endswith('.jpeg'):
                image = cv2.imread(file_path)
                avg_angle, avg_dist = calculate_hough_features(image)
                texture, contrast = calculate_texture_contrast_features(image)
                txt_file = os.path.splitext(file)[0] + ".txt"
                txt_file_path = os.path.join(cyclist_type_path, "txt", txt_file)
                if os.path.exists(txt_file_path):
                    with open(txt_file_path, 'r') as txt_file:
                        lines = txt_file.readlines()
                        for line in lines:
                            parts = line.strip().split()
                            if len(parts) == 5:
                                class_id, cx, cy, w, h = parts
                                data.append({
                                    'avg_angle': avg_angle,     # Average angle from Hough Transform
                                    'avg_distance': avg_dist,   # Average distance from Hough Transform
                                    'texture': texture,         # Texture
                                    'contrast': contrast,       # Contrast
                                    'class': int(class_id),     # Class
                                    'centroid_x': cx,           # Centroid x
                                    'centroid_y': cy,           # Centroid y
                                    'width': w,                 # Detection width
                                    'height': h                 # Detection height
                                })

# Create a DataFrame from the collected data
df = pd.DataFrame(data)
print(df)

# Normalize features and update DataFrame
df2 = normalize_features('Cyclist-Detection/data/processed/cyclist_detection_data.csv')

# Perform statistical description of data
statistical_description_of_data(df2)

# Generate correlation heatmap
correlation_heatmap(df2)

# Generate scatter plots for different features
scatter_plots_feature_vs_centroid_x(df2)
scatter_plots_feature_vs_centroid_y(df2)
scatter_plots_feature_vs_width(df2)
scatter_plots_feature_vs_height(df2)

# Select input features and output labels
input_features = ['avg_angle', 'avg_distance', 'texture', 'contrast']
output_labels = ['centroid_x', 'centroid_y', 'width', 'height']

# Split the data into training and testing sets
X = df[input_features]
y = df[output_labels]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the output labels for the test set
y_pred = model.predict(X_test)

# Evaluate the model with Mean Squared Error (MSE) and Mean Absolute Error (MAE)
mse_cx = mean_squared_error(y_test['centroid_x'], y_pred[:, 0])
mse_cy = mean_squared_error(y_test['centroid_y'], y_pred[:, 1])
mse_width = mean_squared_error(y_test['width'], y_pred[:, 2])
mse_height = mean_squared_error(y_test['height'], y_pred[:, 3])

print("Mean Squared Error for centroid_x:", mse_cx)
print("Mean Squared Error for centroid_y:", mse_cy)
print("Mean Squared Error for width:", mse_width)
print("Mean Squared Error for height:", mse_height)

mae_cx = mean_absolute_error(y_test['centroid_x'], y_pred[:, 0])
mae_cy = mean_absolute_error(y_test['centroid_y'], y_pred[:, 1])
mae_width = mean_absolute_error(y_test['width'], y_pred[:, 2])
mae_height = mean_absolute_error(y_test['height'], y_pred[:, 3])

print("Mean Absolute Error for centroid_x:", mae_cx)
print("Mean Absolute Error for centroid_y:", mae_cy)
print("Mean Absolute Error for width:", mae_width)
print("Mean Absolute Error for height:", mae_height)