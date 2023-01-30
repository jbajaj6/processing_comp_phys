from Optimization import *
from Engine import *
from Sphere import Sphere
from vector import Vector3D

scal = 2.3

def prep():
    frameRate(5000)
    scale(1, -1)
    translate(20, -(height-200))
    background(120,160,255)
    rect(200*scal,3.048*scal,20,50)

def scene():
    fill(100,200,100)
    rect(-100,0,1400,-200)#ground
    fill(255)

def create_balls():
    global balls
    for i in population:
        mass = 0.6
        rad = 0.12
        h = Vector3D(i.dis,100.0,0.0)
        v = 60.0
        a = Vector3D(0.0,0.0,0.0)
        spin = None
        spin_attr = None
        b = Sphere(rad,mass,0.01, h,Vector3D(v*cos(deg_to_rad(0.0)),v*sin(deg_to_rad(0.0)),0.0),a, spin, spin_attr,i.id)
        balls.append(b)


def draw_ball(s):
    fill(0,0,0)
    ellipse(s.pos.x*scal,s.pos.y*scal,20,20)

def new_gen():
    global generation
    for i in population:
        i.fit = abs(fin[i.id][0]-200)
        i.t = fin[i.id][1]
    fin.clear()
    del balls[:]
    populations(50, generation)
    create_balls()
    generation += 1
    
balls = []
fin = {}
g = Vector3D(0.0,-9.8,0.0)

generation = 0

def render():
    global generation
    global balls
    global g
    if generation == 0:
        populations(50,generation)
        create_balls()
        generation += 1
    if len(fin) == 50:
        new_gen()
    for i in balls:
        draw_ball(i)
        wind = Vector3D(-10.0,0.0,0.0)
        if i.pos.y < 3.048 and i.id not in fin.keys():
            fin[i.id] = (i.pos.x, i.t)
        elif i.pos.y < 3.048:
            continue
        air_vel = i.vel - wind
        Fw = weight(i.mass,g)
        Fd = drag(air_vel,air_vel.normalize(),i.cross_section(),1.2,0.5)
        Ft = Fw + Fd
        update(Ft, air_vel, i, wind)

        
        
            
    
    
