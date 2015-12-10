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


"""
MANHATTAN DISTANCES
for x=(a,b) and y=(c,d), the Manhattan distance between them x and y is
abs(a-c) + abs(b-d)

Voronoi algorithm: given an input set of points called 'sites'
compute bounded regions called 'cell' for each site such that the site enclosed by
each cell is the closest site to all points within the cell

Boundaries between cells called 'voronoi edge' are line segments equidistant from two sites.
Intersection of three or more voronoi edges create a 'voronoi vertex'

Delaunay triangulation:

Triangulation(in R2): of a set of points P(R2) is a simplitial complex 'delta
"""

