# Model

1. The steering angle was in degrees and it was converted into radians first.
2. The model was designed with basic CNN, Flatten, Dense and Dropout Layers.
3. The activation used in inner layers was 'relu'
4. The activation used in output layer was 'tanh'. (I tried for Linear Activation as well but tanh produced someway better results)
5. Dropout layers were added for regularization and to prevent overfitting.
6. The model predicted the value of steering angle in radians so later it was converted back to degrees (for visualization).

# Model Architecture (in Brief)

1. 5 Convolutional Layers, each followed by a MaxPooling Layer.
2. I chose the input_size as (100, 100) and kernel_size as (3, 3). Since they gave me the best results!
3. Flatten the layers
4. 4 Dense Layers, followed by 3 Dropout Layers to avoid over-fitting.
5. The images were read in 'grayscale' mode for better results. 

# Loss Function

Loss function used is general: 'mae'

The loss is the mean overseen data of the absolute differences between true and predicted values

Formula: 

![alt text][formula]

[formula]: https://github.com/Kushagraw12/Self-Driving-Car/blob/master/mae-formula.png "Formula"

 # Training
 
 I trained my model on google colab. This is the most critical part. One needs to be very patient while training one's model. It took me around 6-7 hours of training while I was trying for different hyper_parameters. 
 
 # Testing
 
 Driver.py containes code for testing the model and its performance. This output video is on testing data (not on training data) which can be verified from code itself.
