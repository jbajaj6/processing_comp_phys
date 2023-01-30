from vector import Vector3D

class Sphere:
    def __init__(self, radius, mass, dt, pos, vel, a, spin, spin_attr, id):
        self.r = radius
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.t = 0
        self.dt = dt
        self.a = a
        self.veldr = self.vel.normalize()
        self.spin = spin
        self.spin_attr = spin_attr
        self.id = id


    def cross_section(self):
        import math
        return math.pi * (self.r ** 2)

    def area(self):
        import math
        return 4 * math.pi * (r**2)
