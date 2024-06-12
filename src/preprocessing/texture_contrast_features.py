"""
Author: [Your Name]
Email: [Your Email]
Date: [Creation Date]
Version: 1.0

Description:
This file contains functions to calculate texture and contrast features using Grey Level Co-occurrence Matrix (GLCM) and other related methods.

Dependencies:
- numpy (version 1.25.2)
- cv2 (version 4.8.0)
- skimage (version x.x.x)  # Update with the correct version

Usage:
Example of how to use the functions in this file:
>>> import cv2
>>> from texture_features import calculate_texture_contrast_features
>>> image = cv2.imread('path/to/image.jpeg')
>>> texture, contrast = calculate_texture_contrast_features(image)

License:
[License Name]

Additional Information:
- Make sure to have the dependencies installed before running the code.
- The file is optimized for images in JPEG format.
"""

import cv2
from skimage.feature import greycomatrix, greycoprops

def calculate_texture_contrast_features(image):
    """
    Calculate texture and contrast features of an image using GLCM.

    Parameters:
    image (numpy.ndarray): Input image in BGR format.

    Returns:
    tuple: A tuple containing texture and contrast values.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    glcm = greycomatrix(gray, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)
    contrast = greycoprops(glcm, 'contrast')[0][0]
    texture = greycoprops(glcm, 'dissimilarity')[0][0]
    return texture, contrast