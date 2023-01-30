from Vectors import *

class Ball:
    # initializes class
    # launch height, velocity, theta (angle)
    def __init__(self, h, v, t):
        self.pos = Vec(0, h, 0)
        self.vel = v
        self.angle = t
    
    def updateVel(self, a, dt):
        self.vel = Vadd(self.vel, Vmult(a, dt))

    def move(self, dt):
        self.pos = Vadd(self.pos, Vmult(self.vel, dt))
