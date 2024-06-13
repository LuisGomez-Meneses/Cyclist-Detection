"""
Author: Luis Miguel Gómez Meneses
Email: luisgomez251811@correo.itm.edu.co
Date: 12/06/2024
Version: 1.0

Description:
This script extracts texture, contrast, and Hough Transform features from images and creates a database with these features.

Dependencies:
- numpy (version 1.25.2)
- cv2 (version 4.8.0)
- pandas (version: 2.0.3)  # Update with the correct version
- skimage (version 0.19.3)
- Python (version  3.10.12)  # Update with the correct version

Usage:
Example of how to use the functions in this file:
>>> import cv2
>>> from hough_features import calculate_hough_features
>>> from texture_contrast_features import calculate_texture_contrast_features
>>> image = cv2.imread('path/to/image.jpeg')
>>> avg_angle, avg_dist = calculate_hough_features(image)
>>> texture, contrast = calculate_texture_contrast_features(image)


Additional Information:
- Make sure to have the dependencies installed before running the code.
- The file is optimized for images in JPEG format.
"""

import os
import cv2
import pandas as pd
import sys

# Ensure the path to the custom modules is added
sys.path.append('src/preprocessing')

from hough_features import calculate_hough_features
from texture_contrast_features import calculate_texture_contrast_features
from normalize_features import normalize_features
# Define the base path for raw data
base_path = "data/raw"
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
                    with open(txt_file_path, 'r') as file:
                        lines = file.readlines()
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
# Uncomment to save dataframe as a .csv file
df.to_csv('data/processed/cyclist_detection_data.csv', index=False)
normalize_features('data/processed/cyclist_detection_data.csv')

