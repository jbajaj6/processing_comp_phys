from Optimization import *
from Engine import *
from Sphere import Sphere
from vector import Vector3D

scal = .01

def prep():
    frameRate(50000000000)
    scale(1, -1)
    translate(20, -(height-200))
    background(120,160,255)

def scene():
    fill(100,200,100)
    rect(-100,0,1400,-200) #ground

def create_balls():
    global balls
    for i in population:
        mass = 15.0
        rad = .08
        h = Vector3D(0.0,1.0,0.0) #ask if length of cannon changes initial position based on angle
        v = i.vel
        a = Vector3D(0.0,0.0,0.0)
        spin = None
        spin_attr = None
        b = Sphere(rad,mass,0.01, h,Vector3D(0.0,v*sin(deg_to_rad(90.0)),0.0),a, spin, spin_attr,i.id)
        balls.append(b)


def draw_ball(s):
    fill(255,0,0)
    ellipse(s.pos.x*scal,s.pos.y*scal,20,20)

def new_gen():
    global generation
    for i in population:
        i.fit = fin[i.id]
    fin.clear()
    del balls[:]
    populations(50, generation)
    create_balls()
    generation += 1
    
balls = []
fin = {}
g = Vector3D(0.0,-9.8,0.0)

m_d = 0

generation = 0

def render():
    global generation
    global balls
    global m_d
    global g
    if generation == 0:
        populations(50,generation)
        create_balls()
        generation += 1
    if len(fin) == 50:
        print(m_d)
        m_d = 0
        new_gen()
    for i in balls:
        draw_ball(i)
        wind = Vector3D(0.0,0.0,0.0)
        if (i.vel.y < 0) and i.id not in fin.keys():
            fin[i.id] = i.pos.y
        elif i.vel.y < 0:
            continue
        air_vel = i.vel - wind
        Fw = weight(i.mass,g)
        Fd = drag(air_vel,air_vel.normalize(),i.cross_section(),density(i.pos.y),0.5)
        m_d = max(m_d,-1*Fd.y)
        # Fm = lift(0.00005, i.spin, air_vel)
        Ft = Fw + Fd
        update(Ft, air_vel, i, wind)

        
        
            
    
    
