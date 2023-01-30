from Optimization import *
from Engine import *
from Sphere import Sphere
from vector import Vec

scal = .7

def prep():
    frameRate(5000)
    scale(1, -1)
    translate(20, -(height-200))
    background(120,160,255)

def scene():
    fill(100,200,100)
    rect(-100,0,1400,-200) #ground

def create_balls():
    global balls
    for i in population:
        mass = 4.2
        rad = .125
        h = Vec(30.48*cos(deg_to_rad(35)),30.48*sin(deg_to_rad(35)),0.0) #ask if length of cannon changes initial position based on angle
        #h = Vec(0.0,0.0,0.0)
        v = 330.0
        a = Vec(0.0,0.0,0.0)
        spin = None
        spin_attr = None
        b = Sphere(rad,mass,0.01, h,Vec(v*cos(deg_to_rad(35)),v*sin(deg_to_rad(35)),0.0),a, i.wind, spin, spin_attr,i.id)
        balls.append(b)


def draw_ball(s):
    fill(0,0,0)
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
g = Vec(0.0,-9.8,0.0)

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
        if i.pos.y < 0 and i.id not in fin.keys():
            fin[i.id] = i.pos.x
        elif i.pos.y < 0:
            continue
        air_vel = i.vel - i.wind
        Fw = weight(i.mass,g)
        Fd = drag(air_vel,air_vel.normalize(),i.cross_section(),0.97,0.3)
        # Fm = lift(0.00005, i.spin, air_vel)
        Ft = Fw + Fd
        update(Ft, air_vel, i, i.wind)

        
        
            
    
    
