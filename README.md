# 🐱🐶 Cat vs Dog Image Classifier

## Overview

This project is a Convolutional Neural Network (CNN) based image classification web app that predicts whether an uploaded image is of a **Cat** or a **Dog**. It uses TensorFlow/Keras for model training and **Streamlit** for deployment, providing a simple and interactive interface.

## Dataset

The model was trained on a labeled dataset of cat and dog images. The dataset includes:

* Cat Images
* Dog Images

Each image is resized to 150x150 pixels before being passed into the model.

## Model Architecture

The CNN model includes:

* Conv2D and MaxPooling Layers
* Flatten Layer
* Dense Layer with ReLU
* Dropout Layer
* Output Dense Layer with Sigmoid (for binary classification)

The model was trained with:

* Optimizer: Adam
* Loss Function: Binary Crossentropy
* Epochs: 20
* Validation Split: 0.2

The trained model is saved as:
'best_model.h5'


## Streamlit Web App

### How to Run the App

1. Open the App.py file form project folder in **PyCharm** or your preferred IDE.
2. Make sure the file `best_model.h5` is in the same directory.
3. Open the terminal and run:
4. streamlit run App.py



## Prediction Output

The app allows users to upload an image and get instant classification:

### 🐱 Cat Prediction

![Cat Prediction](https://github.com/M-MAHAD1/Cat-Dog-Classifier/blob/main/images/cat_prediction.jpg)

### 🐶 Dog Prediction

![Dog Prediction](https://github.com/M-MAHAD1/Cat-Dog-Classifier/blob/main/images/dog_prediction.jpg)

(📌 Make sure to include the above images in your GitHub repo in an `images` folder.)

## Libraries Used

- TensorFlow / Keras
- Numpy
- Streamlit
- Pillow


## Author

Developed by **Muhammad Mahad**

📧 Email: muhammadmahad.cs@gmail.com  
🔗 LinkedIn: [https://www.linkedin.com/in/muhammadmahad.cs](https://www.linkedin.com/in/muhammadmahad.cs)
