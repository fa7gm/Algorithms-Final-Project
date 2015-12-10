__author__ = 'Amy Shi, Amber Lee, Fred Ayi-Quaye'

from tkinter import *
import random
import math
import time
import doctest
from itertools import permutations
from PIL import Image


# A point has an x and a y coordinate
# x and y must be numbers
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# A line has a start point and an end point
# The start and end points are of class Point
class Line:
	def __init__(self, start, end):
		self.start = start
		self.end = end

# A cell has a center, adjacent cells, and walls
# The center is a Point object
# The adjacent cells list is a list of cells
# The walls are of class Line
class Cell:
	def __init__(self, center, adjacent, walls):
		self.center = center
		self.adjacent = adjacent
		self.walls = walls