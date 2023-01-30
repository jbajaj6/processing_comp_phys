from Optimization import *
from Engine import *
from Sphere import Sphere
from vector import Vec

scal = 3

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
        mass = 0.042
        rad = .021335
        h = Vec(0,0,0.0) #ask if length of cannon changes initial position based on angle
        #h = Vec(0.0,0.0,0.0)
        v = 20.0
        a = Vec(0.0,0.0,0.0)
        spin = None
        spin_attr = None
        b = Sphere(rad,mass,0.01, h, Vec(v*cos(deg_to_rad(i.angle)),v*sin(deg_to_rad(i.angle)),0.0),a,i.id)
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
g = Vec(0.0,-1.62,0.0)

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
        if i.pos.x > 100:
            if i.pos.y <= (tan(25*PI/180)*i.pos.x-100*tan(25*PI/180)) and i.id not in fin.keys():
                fin[i.id] = i.pos.x
            elif i.pos.y <= (tan(25*PI/180)*i.pos.x-100*tan(25*PI/180)):
                continue
        else:
            if i.pos.y < 0 and i.id not in fin.keys():
                fin[i.id] = i.pos.x
            elif i.pos.y < 0:
                continue
        Fw = weight(i.mass,g)
        Ft = Fw
        update(Ft, i)

        
        
            
    
    
