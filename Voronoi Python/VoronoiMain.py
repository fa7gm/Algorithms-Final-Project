__author__ = 'Amy Shi, Amber Lee, Fred Ayi-Quaye'

from tkinter import *
import random
import math
import time
import doctest
from itertools import permutations
from PIL import Image
import voronoiCell

voronoiLines = []

#This code currently finds the closest point out of all the points.
def nearestDistanceConnect(points, w):
    for point in points:
        closestDist = float("inf")
        closestX = 0;
        closestY = 0;
        for pointee in points:
            #w.create_line(point[0], point[1], pointee[0], pointee[1], fill="#476042", width=3)
           # print("created a line at (", point[0], ", ", point[1], ") to (", pointee[0], ", ", pointee[1], ")")
            dist = distance(point, pointee)
            if((dist < closestDist) & (dist > 0)):
                closestDist = dist
                closestX = pointee.x
                closestY = pointee.y
        print("The closest point to ", point.x, point.y, " is ", closestX, closestY)
        w.create_line(point.x, point.y, closestX, closestY, fill="#476042", width=3)
        drawPerpendicular(point, [closestX, closestY], w)
    return 0

#This code draws a perpendicular line given two points
def drawPerpendicular(pt1, pt2, w):
    leftsize = 10
    rightsize = 10
    centerX = (pt1.x + pt2.x) / 2
    centerY = (pt1.y + pt2.y) / 2
    if(pt1.y - pt2.y != 0):
        w.create_line(centerX - leftsize, centerY + leftsize*((pt1.x-pt2.x)/(pt1.y-pt2.y)), centerX + rightsize, centerY - rightsize*((pt1.x-pt2.x)/(pt1.x-pt2.x)), fill="red", width=1)
        print(centerX - 1, centerY + ((pt1[0]-pt2[0])/(pt1[1]-pt2[1])), " to ", centerX + 1, centerY - ((pt1[0]-pt2[0])/(pt1[1]-pt2[1])))
    else:
        w.create_line(centerX, centerY + leftsize, centerX, centerY - rightsize, fill="red", width=1)

def angle(pt1,pt2):
    if(pt2[0]-pt1[0] == 0):
        #Something happens
        return 0
    else:
        m1 = (pt1[1] - pt1[1]/1)
        m2 = (pt2[1] - pt1[1]/(pt2[0]-pt1[0]))
        tnAngle = (m1-m2)/(1+(m1*m2))
        return math.atan(tnAngle)

def distance(pt1, pt2):
    return math.hypot(pt2[0]-pt1[0], pt2[1]-pt1[1])

def total_distance(points):
    return sum([distance(point, points[index+1]) for index, point in enumerate(points[:-1])])

#def bruteForceTravellingSalesman(points, start=None):
#    if start is None:
#        start=points[0]
#    return min([perm for perm in permutations(points) if perm[0] == start], key=total_distance)

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
    #Just a testing data structure. Don't use this.
    all_pixels = []
    #Use this one when doing calculations.
    points = []
    #loop(self, points, pixels, all_pixels, width, height)
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            foo = random.randint(1, 7)
            if (round(sum(cpixel)) / float(len(cpixel)) > 127) & (x%foo == 0) & (y%foo == 0):
                all_pixels.append(255)
                pt = Point(x*2, x*2)
                pt.x = x*2
                pt.y = y*2
                points.append(pt)
                self.w.create_oval(x*2, y*2, x*2+1, y*2+1, fill="black")
                #print(x, ", ", y, " white")
            else:
                #print(x, ", ", y, " Black")
                all_pixels.append(0)
            #self.w.after(1000, delay(self))

    #print(all_pixels.__len__())
    #print(all_pixels)
    #print(points)
    #value = distance(points[0], points[1])
    #ang = angle(points[0], points[1])
    #print(value)
    #rint(total_distance(points))
    #print(ang)
    nearestDistanceConnect(points, self.w)
    #example1 = [0, 0]
    #example2 = [500, 500]
    #self.w.create_line(0, 0, 500, 500, fill="blue")
    #drawPerpendicular(example1, example2, self.w)

    #self.w.after(20, reload(self, imageName))

def delay(self):
    print("Animated")

root = Tk()
Window()
root.title("Voronoi Painting")
root.geometry("500x500")
root.mainloop()
