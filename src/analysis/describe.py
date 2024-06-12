"""
Author: Luis Miguel Gómez Meneses
Email: luisgomez251811@correo.itm.edu.co
Date: 12/06/2024
Version: 1.0

Description:
This script reads a CSV file, computes the statistical description of its data, and optionally saves the result as a new CSV file.

Dependencies:
- pandas (version 2.0.3)  # Update with the correct version
- Python (version  3.10.12)  # Update with the correct version

Usage:
Example of how to use the function in this file:
>>> import pandas as pd
>>> path = '/content/Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'
>>> from your_script_name import describe
>>> df = describe(path)
>>> print(df)

Additional Information:
- Make sure to have the dependencies installed before running the code.
"""

import pandas as pd

path = '/content/Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'

def describe(path):
    """
    Reads a CSV file and returns a DataFrame with the statistical description of the data.
    
    Parameters:
    path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: A DataFrame with the descriptive statistics of the data,
                  including a renamed 'statistic' column for the indices.
    """
    # Read the CSV file
    df = pd.read_csv(path)
    # Get the statistical description of the DataFrame
    df2 = df.describe()
    # Reset the index of the description DataFrame
    df2 = df2.reset_index()
    # Rename the index column
    df2 = df2.rename(columns={'index': 'statistic'})
    return df2

# Call the function and store the result in df
df = describe(path)
print(df)

# Uncomment to save the DataFrame as a CSV file
df.to_csv('results/tables/statistical description/statistical description of Normalized data.csv', index=False)
