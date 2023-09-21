
# Digit Recognition Neural Network

This project is an implementation of a digit recognition neural network using PyTorch. The neural network architecture is inspired by the VGG neural network architecture. The goal of this project is to recognize handwritten digits with high accuracy
## Project Overview

* Neural Network Architecture: I have built my own neural network architecture inspired by the VGG neural network. The network consists of multiple convolutional layers followed by fully connected layers. The architecture is designed to extract features from input images and make accurate predictions.

* Training Accuracy: During the training process, I achieved an approximate accuracy of 98% on the training dataset. This indicates that the neural network has learned to recognize handwritten digits effectively.

* Graphical User Interface (GUI): To provide an easy-to-use interface for digit recognition, I have built a graphical user interface (GUI) using Gradio. The GUI includes a sketchpad where users can draw digits, and the neural network will predict the drawn digit.
## Screenshots

####  This is gradio GUI for prediciton

![image](https://github.com/Abhi-vish/notex/assets/109618783/f9505974-e81f-45c3-afa0-754d52f1dac4)


![image](https://github.com/Abhi-vish/notex/assets/109618783/0b76ec7c-b67e-4969-ab96-cf7e8c0aa9ec)
# Usage
To use this digit recognition project, follow these steps:

### 1. Clone the Repository:

To clone the repository to your local machine, use the following command:

git clone `https://github.com/Abhi-vish/Handwritten_Digit_Recognizer.git`

If you prefer to run it in Google Colab, you can directly open the Colab notebooks mentioned below.

### 2. Training the Model:

Open the `MNISTDigitRecognition.ipynb` notebook in Colab.
Run all the cells in the notebook to retrain the model if needed.
### 3. Running the Gradio App:

To use the Gradio app for digit recognition, open the `gradio_app.ipynb` notebook in Colab.
Run all the cells in this notebook to start and run the Gradio app.
By following these steps, you can both retrain the model and use the Gradio app for digit recognition.

#### Note : Change the `checkpoint = "Model\DigitRecognitionCNNModel.pth"`. This path with model's orginal path on Colab.

Note: Ensure you have the required dependencies installed before running the notebooks. You can typically install dependencies using `pip install -r requirements.txt`.
## 🚀 About Me
I'm a student...


## Lessons Learned

While building this project, I learned several key concepts and faced various challenges. Here are the details:


### Data Handling:

* Converting images to tensors.
* Using data loaders for efficient data handling.
### Model Development:

* Creating a custom neural network architecture.
### Training and Testing:

* Building effective training and testing loops.
### Hardware Flexibility:

* Writing code that works on both CPU and GPU.
### GUI Development:

* Developing user-friendly interfaces using Gradio.
### Model Evaluation:

* Assessing model performance with accuracy metrics.
