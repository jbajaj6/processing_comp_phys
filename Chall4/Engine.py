from vector import Vector3D
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

def density(h):
    import math
    if h <= 11000.0:
        t = 15.04 - (.00649 * h)
        p = 101.29 * (((t+273.1)/288.08)**5.256)
        roe = p / (.2869 * (t + 273.1))
        return roe
    elif h > 11000.0 and h <= 25000:
        t = -56.46
        p = 22.65 * math.exp(1.73-(.000157*h))
        roe = p / (.2869 * (t + 273.1))
        return roe
    else:
        t = -131.21 + (.00299*h)
        p = 2.488 * (((t+273.1)/216.16)**(-11.388))
        roe = p / (.2869 * (t + 273.1))
        return roe

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
