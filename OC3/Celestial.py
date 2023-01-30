from Vectors import *

class Celestial:
    # initializes class
    # radius, name, mass, pos, velocity, r, g, b (for color)
    def __init__(self, radius, name, m, p, v, r, g, b):
        self.radius = radius
        self.name = name
        self.m = m
        self.p = p
        self.v = v
        self.r = r
        self.g = g
        self.b = b
    
    def updateVel(self, a, dt):
        self.v = Vadd(self.v, Vmult(a, dt))

    def move(self, dt):
        self.p = Vadd(self.p, Vmult(self.v, dt))
