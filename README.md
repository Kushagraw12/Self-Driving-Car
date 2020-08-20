# Self-Driving-Car

A Self-Driving Car, also known as an autonomous vehicle (AV), connected and autonomous vehicle (CAV), driverless car, robo-car, or robotic car is a vehicle that is capable of sensing its environment and moving safely with little or no human input.

[Source](https://en.wikipedia.org/wiki/Self-driving_car)

## My Experience

The problem seems to be quite complex, and that is truth as well. This project focuses only on predicting the steering angle for the car. We will be feeding sequences of images from dashcam and this model will predict the steering angle in degrees.

## Dataset

The link to dataset is [here](https://drive.google.com/file/d/1PZWa6H0i1PCH9zuYcIh5Ouk_p-9Gh58B/view?usp=sharing). The dataset contains around 64k images and corresponding steering angles.

## Model

The model was designed with basic CNN, Flatten, Dense and Dropout Layers.

Dropout layers were added for regularization and to prevent overfitting. 

Read about my Model in [Detail](https://github.com/Kushagraw12/Self-Driving-Car/blob/master/About.md)


## Sample Video
 
![alt text][gif]
 
[gif]: https://github.com/Kushagraw12/Self-Driving-Car/blob/master/Recording-gif.gif "GIF"


*The visualization is strictly on Test Data
 
