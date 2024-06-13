"""
Author: Luis Miguel Gómez Meneses
Email: luisgomez251811@correo.itm.edu.co
Date: 12/06/2024
Version: 1.0

Description:
This script reads a CSV file and creates a KDE (Kernel Density Estimate) plot for the input features. The plot is displayed and can be saved as an image file.

Dependencies:
- pandas (version 2.0.3)  # Update with the correct version
- seaborn (version 0.11.2)  # Update with the correct version
- matplotlib (version 3.4.2)  # Update with the correct version
- Python (version  3.10.12)  # Update with the correct version

Usage:
Example of how to use the function in this file:
>>> import pandas as pd
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> path = 'Cyclist-Detection/data/processed/cyclist_detection_Normalized_data.csv'
>>> df = pd.read_csv(path)
>>> from kde_plot_input_features import kde_plot_input_features
>>> kde_plot_input_features(df)

Additional Information:
- Make sure to have the dependencies installed before running the code.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = 'data/processed/cyclist_detection_Normalized_data.csv'
df = pd.read_csv(path)

def kde_plot_input_features(df):
    """
    Creates a KDE plot for the input features and saves the plot as an image file.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    input_features = ['avg_angle', 'avg_distance', 'texture', 'contrast']

    # Create the KDE plot
    sns.kdeplot(data=df[input_features])
    plt.xlabel('Values')

    # Save the KDE plot as a PNG file
    plt.savefig('results/figure/normalized_input_features_distribution/normalized_input_features_distribution.png', format='png', dpi=300)
    plt.show()

# Uncomment to generate and save the KDE plot as an image file
kde_plot_input_features(df)