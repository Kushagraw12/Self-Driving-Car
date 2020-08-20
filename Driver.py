import pandas
import numpy as np
from keras.preprocessing import image
from keras.layers import Conv2D,Flatten, Dense, Dropout, MaxPool2D
from keras.optimizers import Adam
from keras.models import Sequential
from keras import regularizers
from keras.optimizers import Adam
import scipy.misc
import tensorflow as tf
import cv2
from subprocess import call
import os


adam = Adam(0.0001)
model = tf.keras.models.Sequential([
                                    tf.keras.layers.Conv2D(16, (3,3), activation = 'relu', input_shape=(100, 100, 1)),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                 
                                    tf.keras.layers.Conv2D(32, (3,3), activation = 'relu'),
                                    tf.keras.layers.MaxPooling2D(2,2),
                                 
                                    tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                 
                                    tf.keras.layers.Conv2D(256, (3,3), activation = 'relu'),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                 
                                    tf.keras.layers.Conv2D(512,(3,3), activation = 'relu'),
                                    tf.keras.layers.MaxPooling2D(2,2),
                                    
                                    tf.keras.layers.Flatten(),
                                    
                                    tf.keras.layers.Dense(512, activation = 'relu'),
                                    tf.keras.layers.Dropout(0.2),
                                 
                                    tf.keras.layers.Dense(256, activation = 'relu'),
                                    tf.keras.layers.Dropout(0.2),
                                 
                                    tf.keras.layers.Dense(128, activation = 'relu'),
                                    tf.keras.layers.Dropout(0.2),
                                 
                                    tf.keras.layers.Dense(1, activation='tanh')
])

model.summary()
model.compile(optimizer = Adam(lr = 0.0001), loss = 'mse', metrics = ['mae'])

model.load_weights('./z-1-weights-0.0521.h5')

img_str = cv2.imread('s1.jpg',0)
rows,cols = img_str.shape

smoothed_angle = 0


i = 52123
while(cv2.waitKey(10) != ord('q') and i < 63825):
	img1 = image.load_img("new_data/data/" + str(i) + ".jpg",color_mode='grayscale')
	img1 = image.img_to_array(img1) / 255.0
	img = image.load_img("new_data/data/" + str(i) + ".jpg", color_mode = 'grayscale', target_size = [100, 100])
	img = image.img_to_array(img) / 255.0
	img_resh = np.reshape(img,[1, 100, 100, 1])
	degrees = con.predict(img_resh) * 180.0 / scipy.pi
	print("Predicted steering angle: " + str(degrees) + " degrees")
	cv2.imshow("frame", cv2.cvtColor(img1, cv2.COLOR_RGB2BGR))
	smoothed_angle += 0.2 * pow(abs((degrees - float(smoothed_angle))), 2.0 / 3.0) * (degrees - smoothed_angle) / abs(degrees - smoothed_angle)
	M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -float(smoothed_angle), 1)
	dst = cv2.warpAffine(img_str, M, (cols, rows))
	cv2.imshow("steering wheel", dst)
	i += 1

cv2.destroyAllWindows()
