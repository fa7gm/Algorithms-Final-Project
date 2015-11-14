__author__ = 'Amy Shi, Amber Lee, Fred Ayi-Quaye'

from tkinter import *
import math
from PIL import Image
import operator

class Context:
    def __init__(self):
        self.doPrint = 0
        self.debug = 0
        self.plot = 0
        self.triangulate = False
        self.vertices = []    # list of vertex 2-tuples: (x,y)
        self.lines = []    # equation of line 3-tuple (a b c), for the equation of the line a*x+b*y = c
        self.edges = []    # edge 3-tuple: (line index, vertex 1 index, vertex 2 index)   if either vertex index is -1, the edge extends to infiinity
        self.triangles = []    # 3-tuple of vertex indices
        self.polygons = {}    # a dict of site:[edges] pairs
    def circle(self, x, y, rad):
        pass
    def line(self,x0,y0,x1,y1):
        pass


def angle(pt1,pt2):
    m1 = (pt1.getY() - pt1.getY())/1
    m2 = (pt2.getY() - pt1.getY())/(pt2.getX()-pt1.getX())
    tnAngle = (m1-m2)/(1+(m1*m2))
    return math.atan(tnAngle)



context = Context()

#For reading coordinates from a text file
#with open('points.txt') as f:
#    w, h = [int(x) for x in f.readline().split()]
#    array = [[int(x) for x in line.split()] for line in f]
#for p in array:
#    print(p)


#Graphics (Currently just a sample at the moment.)
root = Tk()
w = Canvas(root, width=200, height=100)
w.pack()
#w.create_line(0,0,200,100)
#w.create_line(0, 100, 200, 0, fill="red", dash=(4,4))
#w.create_rectangle(50,25,150,75,fill="blue")


#Let's create an image
image = Image.open('sample.png')
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
           # w.create_oval(x, y, x + 1, y + 1, fill="white")
            all_pixels.append(0)

print(all_pixels.__len__())
root.title("Voronoi Painting")
root.geometry("500x500")

root.mainloop()
