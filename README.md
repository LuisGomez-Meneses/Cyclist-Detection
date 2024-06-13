# Cyclist-Detection
##Contetx
According to research from the World Health Organization (WHO), it has been observed that cyclists have a significant impact on global traffic accident fatality statistics, contributing 3% to the total number of deaths. In Colombia, this figure is even higher, reaching 5% (World Health Organization, 2018). This highlights the importance of effectively addressing the safety challenges faced by cyclists on the roads, recognizing the need to implement preventive and protective measures. Additionally, it is crucial to consider that detecting and preventing collisions between autonomous vehicles (AVs) and cyclists represent a significant challenge. The environments in which cyclists travel are often dynamic and changing, making it difficult to anticipate their movements and behaviors.
![Contetx](image/deathsbyroad.PNG)
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
