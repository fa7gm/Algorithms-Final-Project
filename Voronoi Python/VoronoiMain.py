__author__ = 'Amy Shi, Amber Lee, Fred Ayi-Quaye'

from tkinter import *

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

context = Context()

#For reading coordinates from a text file
with open('points.txt') as f:
    w, h = [int(x) for x in f.readline().split()]
    array = [[int(x) for x in line.split()] for line in f]
for p in array:
    print(p)


#Graphics (Currently just a sample at the moment.)
root = Tk()
w = Canvas(root, width=200, height=100)
w.pack()
w.create_line(0,0,200,100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4,4))
w.create_rectangle(50,25,150,75,fill="blue")
root.title("Voronoi Painting")
root.geometry("500x500")

root.mainloop()
