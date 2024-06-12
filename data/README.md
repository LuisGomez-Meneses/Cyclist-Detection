# data
This section of the repository contains all the data files and scripts related to the cyclist detection project.

## Table of Contents
- [File Description](#file-description)
- [Folder Structure](#folder-structure)
- [Usage Instructions](#usage-instructions)
- [Requirements](#requirements)
- [Contact](#contact)

## File Description

This section details the files and folders present in the `data` directory.

- `raw/`: Contains raw images obtained through web scraping techniques and from the COCO and KITTY databases.
  - `nocturnosjpeg/`: Contains images of cyclists taken at night.
    - `txt/`: `.txt` files corresponding to each image, representing cyclist detections in YOLO format.
  - `simplesjpeg/`: Contains images of cyclists taken during the day.
    - `txt/`: `.txt` files corresponding to each image, representing cyclist detections in YOLO format.
- `weights/`: Contains the YOLO NAS weight files for cyclist detection.
  - `part_1.pth`, `part_2.pth`, `part_3.pth`: The original weight file `.pth` split into three parts due to GitHub's file size restrictions.

## Folder Structure

The folder structure of the data section is as follows:
```bash
data/
│
├── raw/
│ ├── NocturnosJPEG/
│ │ ├── Nocturnos (1).jpeg
│ │ ├── Nocturnos (2).jpeg
│ │ ├── .
│ │ ├── .
│ │ ├── Nocturnos (19).jpeg
│ │ └── txt/
│ │ ├── Nocturnos (1).txt
│ │ ├── Nocturnos (2).txt
│ │ ├── .
│ │ ├── .
│ │ ├── Nocturnos (19).txt
│ ├── SimplesJPEG/
│ │ ├── Simples (1).jpeg
│ │ ├── Simples (2).jpeg
│ │ ├── .
│ │ ├── .
│ │ ├── Simples (19).jpeg
│ │ └── txt/
│ │ ├── Simples (1).txt
│ │ ├── Simples (2).txt
│ │ ├── .
│ │ ├── .
│ │ ├── Simples (19).txt
├── weights/
│ ├── part_1.pth
│ ├── part_2.pth
│ ├── part_3.pth
└── README.md
```


## Usage Instructions

To use the data and scripts in this section, follow these steps:

1. Download and combine the YOLO NAS weight files:

    ```bash
    cat weights/part_1.pth weights/part_2.pth weights/part_3.pth > weights/yolo_weights.pth
    ```

2. Use the image and annotation files to train your YOLO NAS model with cyclist detections both during the day and at night.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- PyTorch
- SuperGradients 3.1.3
- PyParsing 2.4.7
- Roboflow
- Ultralytics

You can install the necessary dependencies with:

```bash

pip install super_gradients==3.1.3
pip uninstall pyparsing
pip install pyparsing==2.4.7
pip install -q roboflow
pip install ultralytics
'''

## Contact
   ```bash
   email:luismiguelgomez0821@gmail.com
   '''