from Vectors import *

class Celestial:
    # initializes class
    # mass, pos, velocity
    def __init__(self, r, m, p, v):
        self.r = r
        self.m = m
        self.p = p
        self.v = v
    
    def updateVel(self, a, dt):
        self.v = Vadd(self.v, Vmult(a, dt))

    def move(self, dt):
        self.p = Vadd(self.p, Vmult(self.v, dt))
