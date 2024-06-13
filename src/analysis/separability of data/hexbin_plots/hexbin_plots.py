"""
Author: Luis Miguel Gómez Meneses
Email: luisgomez251811@correo.itm.edu.co
Date: 12/06/2024
Version: 1.0

Description:
This script reads a CSV file and creates hexbin plots for each combination of input features and output labels. The plots are displayed and can be saved as image files.

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
>>> from hexbin_plots import hexbin_plots
>>> hexbin_plots(df)

Additional Information:
- Make sure to have the dependencies installed before running the code.
"""

import pandas as pd
import matplotlib.pyplot as plt

path = 'Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'
df = pd.read_csv(path)

def hexbin_plots(df):
    """
    Creates hexbin plots for each combination of input features and output labels and saves the plots as image files.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    # Define input features and output labels
    input_features = ['avg_angle', 'avg_distance', 'texture', 'contrast']
    output_features = ['centroid_x', 'centroid_y', 'width', 'height']
    fig, axs = plt.subplots(len(output_features), len(input_features), figsize=(12, 10))
    for i, output_label in enumerate(input_features):
        for j, input_feature in enumerate(output_features):
            axs[i, j].hexbin(df[input_feature], df[output_label], gridsize=20, cmap='viridis')
            axs[i, j].set_xlabel(input_feature)
            axs[i, j].set_ylabel(output_label)
    plt.tight_layout()
    plt.savefig('results/figure/The hexbin plot/The hexbin plot.png', format='png', dpi=300)
    plt.show()

# Uncomment to generate and save the hexbin plots as image files
hexbin_plots(df)