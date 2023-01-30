from Vectors import *

class Ball:
    # initializes class
    # launch height, velocity, drop distance
    def __init__(self, h, v, dd):
        self.pos = Vec(dd, h, 0)
        self.vel = v
        self.drop = dd
    
    def updateVel(self, a, dt):
        self.vel = Vadd(self.vel, Vmult(a, dt))

    def move(self, dt):
        self.pos = Vadd(self.pos, Vmult(self.vel, dt))
