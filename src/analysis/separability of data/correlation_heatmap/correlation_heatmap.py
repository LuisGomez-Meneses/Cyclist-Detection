"""
Author: Luis Miguel Gómez Meneses
Email: luisgomez251811@correo.itm.edu.co
Date: 12/06/2024
Version: 1.0

Description:
This script reads a CSV file, calculates the correlation between input features and output features, and creates a heatmap of these correlations. The heatmap is displayed and can be saved as an image file.

Dependencies:
- pandas (version 2.0.3)  # Update with the correct version
- seaborn (version 0.13.1)  # Update with the correct version
- matplotlib (version 3.4.2)  # Update with the correct version
- Python (version  3.10.12)  # Update with the correct version

Usage:
Example of how to use the function in this file:
>>> import pandas as pd
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> path = 'Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'
>>> df = pd.read_csv(path)
>>> from correlation_heatmap import correlation_heatmap
>>> correlation_heatmap(df)

Additional Information:
- Make sure to have the dependencies installed before running the code.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = 'Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'
df = pd.read_csv(path)

def correlation_heatmap(df):
    """
    Creates a heatmap of correlations between input and output features and saves the plot as an image file.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    # Define input and output features
    input_features = ['avg_angle', 'avg_distance', 'texture', 'contrast']
    output_features = ['centroid_x', 'centroid_y', 'width', 'height']

    # Calculate the correlation matrix
    correlation_matrix = df[input_features + output_features].corr().loc[input_features, output_features]

    # Create the heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')

    # Save the heatmap as a PNG file
    plt.savefig('results/figure/correlation_heatmap.png', format='png', dpi=300)
    plt.show()

# Uncomment to generate and save the correlation heatmap as an image file
correlation_heatmap(df)