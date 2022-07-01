import sys 
from predict import predictDigit
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

directory = "TestImages"

#Function to read the image
def openImage(filepath):
    image=cv2.imread(filepath)
    return image

#Function to plot the image
def plot(image):
    plt.imshow(image)
    plt.show()

#Iterating over all test images and predicting them
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        image=openImage(f)
        plot(image)
        predictDigit(image)


































































# #Canvas Function
# lastx, lasty = 0, 0

# #Function to capture current location of x and y coordinates
# def xy(event):
#     "Takes the coordinates of the mouse when you click the mouse"
#     global lastx, lasty
#     lastx, lasty = event.x, event.y


# #Fucntion to draw a line
# def addLine(event):
#     """Creates a line when we drag the mouse
#     from the point where we clicked the mouse to where the mouse is now"""
#     global lastx, lasty
#     canvas.create_line((lastx, lasty, event.x, event.y))
#     # this makes the new starting point of the drawing
#     lastx, lasty = event.x, event.y


# #Function to capture digit drawn on canvas
# def save(event):
#     x=root.winfo_rootx()+canvas.winfo_x()
#     y=root.winfo_rooty()+canvas.winfo_y()
#     x1=x+canvas.winfo_width()
#     y1=y+canvas.winfo_height()
#     im = ImageGrab.grab((x, y, x1, y1))
#     im.save("image.png")
#     # return im
#     Hd = canvas.winfo_id() # to fetch the handle of the canvas
#     rect = win32gui.GetWindowRect(Hd) # to fetch the edges of the canvas
#     im = ImageGrab.grab(rect)
#     im.save("captured.png")



# #Function to clear the canvas
# def clear():
#     canvas.delete('all')


# #Function to predict image 
# def predict():
#     image=save()
#     predictDigit(image)

    
# #Initialising Tkinter object
# root = tk.Tk()

# #Setting Hieght and Width of Tkinter window
# root.geometry("400x400")
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)


# #Initialsing Canvas 
# canvas = tk.Canvas(root)
# canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# #Binding Events on canvas
# canvas.bind("<Button-1>", xy)
# canvas.bind("<B1-Motion>", addLine)

# #Defining Predict Button 
# predict_button = Button(root, text="Predict Digit", command=predict)

# #Defining Clear Canvas Button
# clear_button = Button(root, text="Clear Canvas",command = clear)

# #Rendering Buttons
# predict_button.grid(row=1, column=1)
# clear_button.grid(row=1, column=0)

# #Binding event to root element
# root.bind("<Control-s>", save)

# #Mainloop to render the tkinter window
# root.mainloop()