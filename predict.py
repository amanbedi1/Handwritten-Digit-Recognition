import tensorflow as tf
import numpy as np
import cv2

#loading the Digit Recognizer Model
model = tf.keras.models.load_model("digit_classifier.h5")

#Function for preprocessing the image
def preProcess(image):
    #converting image into gray color
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #resizing image into 28*28 pixel matrix
    resized_image = cv2.resize(gray_image,(28,28),interpolation=cv2.INTER_AREA)

    #Normalizing image so their pixel value ranges between (0 - 1)
    normalized_image=resized_image/255.0

    #converting image to 4d array to make it suitable for the input in model
    final_image = np.array(normalized_image).reshape(-1,28,28,1)  

    return final_image


#Function for predicting digit
def predictDigit(image):
    #PreProcessing the image
    image = preProcess(image)

    #Predicting the image using our Model
    res=model.predict(image)

    print("Predicted Digit is: ",np.argmax(res))
