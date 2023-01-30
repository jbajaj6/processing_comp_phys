from vector import Vec

class Sphere:
    def __init__(self, radius, mass, dt, pos, vel, a, id):
        self.r = radius
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.t = 0
        self.dt = dt
        self.a = a
        self.id = id


    def cross_section(self):
        import math
        return math.pi * (self.r ** 2)
