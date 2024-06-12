"""
Author: Luis Miguel Gómez Meneses
Email: luisgomez251811@correo.itm.edu.co
Date: 12/06/2024
Version: 1.0

Description:
This script normalizes the features from a CSV file.

Dependencies:
- pandas (version 2.0.3)
- Python (version 3.10.12)

Usage:
Example of how to use the function in this file:
>>> csv_path = 'Cyclist-Detection/data/processed/cyclist_detection_data.csv'
>>> normalize_features(csv_path)

Additional Information:
- Make sure to have the dependencies installed before running the code.
- This function reads a CSV file, normalizes specified features, and prints the first few rows of the normalized DataFrame.
"""

import pandas as pd

def normalize_features(csv_path):
    """
    Normalize specified features in a CSV file.

    Parameters:
    csv_path (str): Path to the input CSV file.

    Returns:
    None
    """
    df = pd.read_csv(csv_path)
    input_features = ['avg_angle', 'avg_distance', 'texture', 'contrast']
    for feature in input_features:
        df[feature] = (df[feature] - df[feature].mean()) / df[feature].std()
    print(df.head())
    # Uncomment to save dataframe as a .csv file
    df.to_csv('Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv', index=False)
