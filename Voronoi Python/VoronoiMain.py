__author__ = 'Amy Shi, Amber Lee, Fred Ayi-Quaye'

from tkinter import *
import random
import math
from PIL import Image

def angle(pt1,pt2):
    m1 = (pt1.getY() - pt1.getY())/1
    m2 = (pt2.getY() - pt1.getY())/(pt2.getX()-pt1.getX())
    tnAngle = (m1-m2)/(1+(m1*m2))
    return math.atan(tnAngle)

class Window():
    def __init__(self):
        #Let's create a text button
        self.T = Text(root, height=2, width=50)
        self.T.pack()
        self.T.insert(END, "Welcome to the Voronoi Painter.\n")

        #Let's create a textbox
        Label(text='Please enter an image file to use.').pack(side=TOP,padx=10,pady=10)
        self.entry = Entry(root, width=50)
        self.entry.pack(side=TOP,padx=10,pady=10)
        def onok():
            imageName = self.entry.get()
            print(imageName)
            reload(self, imageName)
        Button(root, text='Add image file', command=onok).pack(side=BOTTOM)
        self.w = Canvas(root, width=1000, height=1000)
        self.w.pack()



def reload(self, imageName):
    #Let's create a canvas
    self.w.pack()
    self.w.delete("all")
    #Let's create an image
    image = Image.open(imageName)
    pixels = image.load()
    width, height = image.size
    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            foo = random.randint(1, 7)
            if (round(sum(cpixel)) / float(len(cpixel)) > 127) & (x%foo == 0) & (y%foo == 0):
                all_pixels.append(255)
                self.w.create_oval(x, y, x+1, y+1, fill="black")
                print(x, ", ", y, " white")

            else:
                print(x, ", ", y, " Black")
                all_pixels.append(0)
    print(all_pixels.__len__())
    print(all_pixels)
root = Tk()
Window()
root.title("Voronoi Painting")
root.geometry("500x500")
root.mainloop()
