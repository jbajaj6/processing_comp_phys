from vector import Vec
from Sphere import Sphere
from math import sin,cos

def weight(mass, gravity):
    return gravity * mass

def drag(velocity, vdr, csection, density,drag_co):
    import math
    const = csection * density * drag_co * -0.5 * (velocity.magnitude()**2)
    return vdr*const

def lift(lift_co, spin_vec, air_vel):
    const = lift_co
    vec = spin_vec.cross(air_vel)
    return vec * const

def deg_to_rad(theta):
    import math
    return (theta * math.pi)/180

def update(Ft, air_vel,s, wind):
    s.a = Ft * (1 / s.mass)
    s.vel += s.a * s.dt
    s.pos += (air_vel + wind) * s.dt
    s.t += s.dt
    s.veldr = s.vel.normalize()
    # if s.spin.z > 0:
    #     s.spin += s.spin_attr * s.dt
    # else:
    #     s.spin.z = 0.0
