__author__ = 'Amy Shi, Amber Lee, Fred Ayi-Quaye'

from tkinter import *
import tkinter
import math
from PIL import Image

def angle(pt1,pt2):
    m1 = (pt1.getY() - pt1.getY())/1
    m2 = (pt2.getY() - pt1.getY())/(pt2.getX()-pt1.getX())
    tnAngle = (m1-m2)/(1+(m1*m2))
    return math.atan(tnAngle)

#Just a functionality to make the button click work. It's not even all that necessary.
def onok():
    imageName = entry.get()
    print(imageName)
    reload(imageName)
root = Tk()



#Let's create a text button
T = Text(root, height=2, width=50)
T.pack()
T.insert(END, "Welcome to the Voronoi Painter.\n")





#Let's create a textbox
Label(text='Please enter an image file to use.').pack(side=TOP,padx=10,pady=10)
entry = Entry(root, width=10)
entry.pack(side=TOP,padx=10,pady=10)

Button(root, text='Add image file', command=onok).pack(side=LEFT)





def reload(imageName):
    #Let's create a canvas
    w = Canvas(root, width=1000, height=1000)
    w.pack()
    #Let's create an image
    image = Image.open(imageName)
    pixels = image.load()
    width, height = image.size
    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            if round(sum(cpixel)) / float(len(cpixel)) > 127:
                all_pixels.append(255)
                w.create_oval(x, y, x+1, y+1, fill="white")
                print(x, ", ", y, " white")

            else:
                print(x, ", ", y, " Black")
                all_pixels.append(0)
    print(all_pixels.__len__())



root.title("Voronoi Painting")
root.geometry("500x500")
root.mainloop()
