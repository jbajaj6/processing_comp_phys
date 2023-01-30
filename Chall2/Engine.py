from vector import Vec
from Sphere import Sphere
from math import sin,cos

def weight(mass, gravity):
    return gravity * mass

def deg_to_rad(theta):
    import math
    return (theta * math.pi)/180

def update(Ft, s):
    s.a = Ft * (1 / s.mass)
    s.vel += s.a * s.dt
    s.pos += s.vel * s.dt
    s.t += s.dt
    # s.veldr = s.vel.normalize()
