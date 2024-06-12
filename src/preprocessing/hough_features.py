"""
Author: [Your Name]
Email: [Your Email]
Date: [Creation Date]
Version: 1.0

Description:
This file contains functions to calculate features using the Hough Transform.

Dependencies:
- numpy (version x.x.x)
- cv2 (version x.x.x)
- skimage (version x.x.x)

Usage:
Example of how to use the functions in this file:
>>> import cv2
>>> from hough_features import calculate_hough_features
>>> image = cv2.imread('path/to/image.jpeg')
>>> avg_angle, avg_dist = calculate_hough_features(image)

License:
[License Name]

Additional Information:
- Make sure to have the dependencies installed before running the code.
- The file is optimized for images in JPEG format.
"""

import numpy as np
import cv2
from skimage.transform import hough_line, hough_line_peaks

def calculate_hough_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    h, theta, d = hough_line(edges)
    _, angles, dists = hough_line_peaks(h, theta, d)
    avg_angle = np.mean(angles)
    avg_dist = np.mean(dists)
    return avg_angle, avg_dist
