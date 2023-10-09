# Car-Plate-Number-Detection-using-ANPR

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction

**Car Plate Number Detection** is a Python-based project that utilizes Haar Cascade classifiers, OpenCV, and Tesseract-OCR to detect and extract license plate numbers from images or video streams. This project serves as a practical example of applying computer vision and OCR techniques for real-world applications, such as automated toll collection or parking management.

## Prerequisites

Before you get started, make sure you have the following prerequisites installed on your system:

- Python 3.x
- OpenCV (cv2)
- Tesseract-OCR
- pytesseract
- Haar Cascade XML classifier file for license plate detection

You can install the required Python libraries using pip:

```bash
pip install opencv-python
pip install pytesseract


Installation
Clone this repository to your local machine:


git clone https://github.com/your-username/car-plate-detection.git
cd car-plate-detection


Download the Haar Cascade XML classifier file for license plate detection and place it in the project directory.

Install Tesseract-OCR. You can download it from the official website or use a package manager specific to your operating system.

Usage
Run the Car Plate Number Detection script:

python car_plate_detection.py --image input_image.jpg

Project Structure
The project directory structure is organized as follows:

car-plate-detection/
├── nb.py  # Main script for license plate detection
├── model
      └─── haarcascade_plate.xml    # Haar Cascade classifier for plate detection
├── Requirements               # Project requirements
│
└─── Resources/               # Output folder (generated during script execution)
    ├── plate_img/    # Detected license plates (images)
    └── detected_plate_numbers.txt         # Text file containing extracted plate numbers
