"""
Author: Luis Miguel Gómez Meneses
Email: luisgomez251811@correo.itm.edu.co
Date: 12/06/2024
Version: 1.0

Description:
This script reads a CSV file, selects specific columns, and creates scatter plots of these features against the 'width' column. The plots are displayed and can be saved as image files.

Dependencies:
- pandas (version 2.0.3)  # Update with the correct version
- matplotlib (version 3.4.2)  # Update with the correct version
- Python (version  3.10.12)  # Update with the correct version

Usage:
Example of how to use the function in this file:
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> path = 'Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'
>>> df = pd.read_csv(path)
>>> from scatter_plots_feature_vs_width import scatter_plots_feature_vs_width
>>> scatter_plots_feature_vs_width(df)

Additional Information:
- Make sure to have the dependencies installed before running the code.
"""

import pandas as pd
import matplotlib.pyplot as plt

path = 'Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'
df = pd.read_csv(path)
selected_columns = ['avg_angle', 'avg_distance', 'texture', 'contrast']

def scatter_plots_feature_vs_width(df):
    """
    Creates scatter plots of selected features vs 'width' and saves the plots as an image file.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    # Convert 'width' column to numeric type
    df['width'] = pd.to_numeric(df['width'])

    # Set up the figure and axes for the scatter plots
    plt.figure(figsize=(12, 8))

    # Loop through selected columns and create scatter plots
    for i, feature in enumerate(selected_columns):
        plt.subplot(2, 2, i + 1)
        plt.scatter(df[feature], df['width'], alpha=0.5)
        plt.title(f'Scatter Plot of {feature} vs width')
        plt.xlabel(feature)
        plt.ylabel('width')
        plt.ylim(df['width'].min() - 0.1, df['width'].max() + 0.1)

    # Adjust layout and save the figure as a PNG file
    plt.tight_layout()
    plt.savefig('results/figure/scatter plots/scatter_plots_feature_vs_width.png', format='png', dpi=300)
    plt.show()

# Uncomment to generate and save the scatter plots as an image file
scatter_plots_feature_vs_width(df)