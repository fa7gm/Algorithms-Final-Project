__author__ = 'Amy Shi, Amber Lee, Fred Ayi-Quaye'

from tkinter import *
import random
import math
import time
import doctest
from itertools import permutations
from PIL import Image
from voronoiCell import Point, Line
from matplotlib.tri import Triangulation, UniformTriRefiner,CubicTriInterpolator
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.patches import RegularPolygon
import numpy as np
#from voronoi_python import voronoi as voronoi


voronoiLines = [] #This will contain all of the lines that were generated from the Green and Gibson algorithm
voronoiCells = []

#This draws a perpendicular line between all points that are closest to each other.
def nearestDistanceConnect(points, w):
    for point in points:
        closestDist = float("inf")
        closestX = 0;
        closestY = 0;
        for pointee in points: #For each point, find the point that is closest to it.
            dist = distance(point, pointee)
            if((dist < closestDist) & (dist > 0)):
                closestDist = dist
                closestX = pointee.x
                closestY = pointee.y
        print("The closest point to ", point.x, point.y, " is ", closestX, closestY)
        w.create_line(point.x, point.y, closestX, closestY, fill="#476042", width=1) #Draw a line between the closest points
        drawPerpendicular(point, Point(closestX, closestY), w) #Draw the line's perpendicular.
    return 0

#This code is most likely not going to be used, but it is a filler for now.
def drawPerpendicular(pt1, pt2, w):
    centerX = (pt1.x + pt2.x) / 2
    centerY = (pt1.y + pt2.y) / 2
    leftsize = 10
    rightsize = 10
    start = Point(0, 0)
    end = Point(0, 0)
    if pt1.y - pt2.y != 0:
        start.x = centerX - leftsize
        start.y = centerY + leftsize*((pt1.x-pt2.x)/(pt1.y-pt2.y))
        end.x = centerX + rightsize
        end.y = centerY - rightsize*((pt1.x-pt2.x)/(pt1.y-pt2.y))
        #print(centerX - 1, centerY + ((pt1.x-pt2.x)/(pt1.y-pt2.y)), " to ", centerX + 1, centerY - ((pt1.x-pt2.x)/(pt1.y-pt2.y)))
    else:
        start.x = centerX
        start.y = centerY + leftsize
        end.x = centerX
        end.y = centerY - rightsize
    w.create_line(start.x, start.y, end.x, end.y, fill="red", width=1)
    voronoiLines.append(Line(start, end))

def drawPerpendicularBisector(pt1, pt2, beginning, finish):
    centerX = (pt1.x + pt2.x) / 2
    centerY = (pt1.y + pt2.y) / 2
    start = Point(0, 0)
    end = Point(0, 0)
    if pt1.y - pt2.y != 0:
        start.x = beginning.x
        start.y = centerY + (centerX - beginning.x)*((pt1.x-pt2.x)/(pt1.y-pt2.y))
        end.x = finish.x
        end.y = centerY - (finish.x - centerX)*((pt1.x-pt2.x)/(pt1.y-pt2.y))
    else:
        start.x = centerX
        start.y = beginning.y
        end.x = centerY
        end.y = end.y
    voronoiLines.append(Line(start, end))
    return Line(Point(start.x, start.y), Point(end.x, end.y))


def distance(pt1, pt2):
    return math.hypot(pt2.x-pt1.x, pt2.y-pt1.y)

class Window():
    def __init__(self):
        #Let's create a text button
        self.T = Text(root, height=2, width=50)
        self.T.pack()
        Label(text="Welcome to the Voronoi Painter.").pack(side=TOP, padx=10, pady=10)

        #Let's create a textbox
        Label(text='Please enter an image file to use and press button.').pack(side=TOP,padx=10,pady=10)
        self.entry = Entry(root, width=50)
        self.entry.pack(side=TOP,padx=10,pady=10)
        def onok():
            imageName = self.entry.get()
            print(imageName)
            reload(self, imageName)
            #self.w.after(100, onok)
        Button(root, text='Exit', command=window_close).pack(side=BOTTOM)
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
    #Just a testing data structure. Don't use this.
    all_pixels = []
    #Use this one when doing calculations.
    points = []
    xarray = []
    yarray = []
    color = ["red", "orange", "yellow", "green", "blue", "violet"]
    #loop(self, points, pixels, all_pixels, width, height)
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            foo = random.randint(1, 7)
            if (round(sum(cpixel)) / float(len(cpixel)) > 127) & (x%foo == 0) & (y%foo == 0):
                all_pixels.append(255)
                points.append(Point(x*2, y*2))
                xarray.append(x*2)
                yarray.append(1000 - y*2)
                #self.w.create_oval(x*2, y*2, x*2+1, y*2+1, fill="black")
            else:
                all_pixels.append(0)

    triangulation = Triangulation(xarray, yarray)
    triangles = triangulation.get_masked_triangles()

    polygons = []

    for triangle in triangles:
        self.w.create_polygon([xarray[triangle[0]], 1000 - yarray[triangle[0]]], [xarray[triangle[1]], 1000 - yarray[triangle[1]]], [xarray[triangle[2]], 1000 - yarray[triangle[2]]], fill=random.choice(color))
        #print(triangle)
    #plt.figure()
    #plt.gca().set_aspect('equal')
    #plt.triplot(triangulation)
    #plt.title("Triangulation")
    #plt.show()
    #nearestDistanceConnect(points, self.w)
    #for line in voronoiLines:
    #    print("(",line.start.x,",", line.start.y, ") to (", line.end.x, ",", line.end.y,")")


def intersects(l1, l2):
    l1_start = l1.start
    l1_end = l1.end
    l2_start = l2.start
    l2_end = l2.end

    l1_startx = l1_start.x
    l1_starty = l1_start.y

    l2_startx = l2_start.x
    l2_starty = l2_start.y

    l1_endx = l1_end.x
    l1_endy = l1_end.y

    l2_endx = l2_end.x
    l2_endy = l2_end.y

    m1 = (l1_starty - l1_endy) / (l1_startx - l1_endx)
    m2 = (l2_starty - l2_endy) / (l2_startx - l2_endx)

    b1 = l1_starty - m1*l1_startx
    b2 = l2_starty - m2*l2_startx

    if m1==m2 and b1 != b2:
        return False
    else:
        return True


def window_close():
    root.destroy()

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

