from Celestial import *
from Vectors import *
from Time import *
import datetime

n = 20

mass = 2e35/n

celestials = []

for _ in range(n):
    pos = Vec(random(-7.4e12, 7.4e12), random(-7.4e12, 7.4e12), random(-7.4e12, 7.4e12))
    # abs of velocity has to be under 100 km per sec (100e3 m/s)
    # gets a random direction (norm functiton)
    # gets a random speed
    vel = Vmult(Norm(Vec(random(-1, 1), random(-1, 1), random(-1, 1))), random(0, 100e3))
    c = Celestial(1, mass, pos, vel)
    celestials.append(c)

x = Time(datetime.datetime(2022, 3, 8))

dt = 1e4

# universal gravitational constant
ugc = 6.67e-11

# reciprcol of ppm to get mpp times radius
collision_radius = 1/3e-11 * 8

def check_collision(p1, p2):
    if abs(Vmag(Vsub(p1.p, p2.p))) <= collision_radius * (p1.r + p2.r)/2:
        return True
    return False

def create_combo(p1, p2):
    # average vel and pos
    vel = Vmult(Vadd(Vmult(p1.v, p1.m), Vmult(p2.v, p2.m)), 1/(p1.m+p2.m))
    pos = Vmult(Vadd(p1.p, p2.p), 0.5)
    
    # combine radii and mass
    rad = ((p1.r*p1.r*PI + p2.r*p2.r*PI)/PI) ** 0.5
    mass = p1.m + p2.m
    
    return Celestial(rad, mass, pos, vel)

# returns the force from p1 on p2
def fg(p1, p2):
    dist = Vsub(p1.p, p2.p)
    r = Vmag(dist)
    return Vmult(Norm(dist), ugc * p1.m * p2.m / (r * r))

def move():
    global x
    
    d = {}

    for celestial in range(len(celestials)):
        F = Vec(0, 0, 0)
        for pull in range(len(celestials)):
            if celestials[pull] == celestials[celestial]:
                continue
            s = str(pull) + " " + str(celestial)
            if s in d:
                force = Vmult(d.get(s), -1)
            else:
                force = fg(celestials[pull], celestials[celestial])
                d[str(celestial) + " " + str(pull)] = force
            F.plus(force)
        a = Vdiv(F, celestials[celestial].m)
        celestials[celestial].updateVel(a, dt)
        celestials[celestial].move(dt)
        
        

        
    for p1 in celestials:
        for p2 in celestials:
            if p1 != p2:
                if check_collision(p1, p2):
                    celestials.remove(p1)
                    celestials.remove(p2)
                    celestials.append(create_combo(p1, p2))
                    break
    
    x.update(dt)

     
