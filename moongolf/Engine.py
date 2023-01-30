from Vectors import *
from math import sin, radians, cos
from Ball import Ball

balls = []

launch_height = 0
launch_speed = 20

pi = 3.14159265359

num_balls = 40

for i in range(num_balls):
    # inputs
    launch_angle = random(0, 90)

    v = Vec(launch_speed * cos(radians(launch_angle)), launch_speed * sin(radians(launch_angle)), 0)
    
    ball = Ball(launch_height, v, launch_angle)
    balls.append(ball)

g = Vec(0, -1.62, 0)

m = 0.045
Fg=Vmult(g,m)

dt = 0.05

t = 0

counter = 0

radius = 0.021335

airdrag_coeff = 0.2
front_facing_area = radius * radius * PI
air_density = 1.15

wind = Vec(0, 0, 0)

record_balls = []

magnus_coeff = 5e-5
launch_spin = Vec(0, 0, 200)


def magnus_force(mc, spin, vel):
    relative_velocity = Vsub(vel, wind)
    fl = Vmult(Vcprod(spin, relative_velocity), mc)
    return fl

def airdrag(velocity, adc, ffa, ad):
    relative_velocity = Vsub(velocity, wind)
    fd = -0.5 * adc * ffa * ad * Vmag(relative_velocity) * Vmag(relative_velocity)
    return Vmult(Norm(velocity), fd)

def isLanded(x, y):
    if y <= (5 * x)/18 - (250/9):
        return True
    return False

def move():
    global t, dt, max_height, record_balls, balls, new_balls, counter, launch_height
    
    if len(balls) == 0:
        # sort balls in order of greatest to least distance
        sorted_balls = sorted(record_balls, key=lambda x:-x[1])
            
        new_balls = []
        
        # get 5 best performing balls
        for i in range(5):
            ang = sorted_balls[i][0]
            v = Vec(launch_speed * cos(radians(ang)), launch_speed * sin(radians(ang)), 0)
            new_balls.append(Ball(launch_height, v, ang))
        
        for i in range(5):
            std = 3-counter*0.5
            theta = new_balls[i].angle
            # make 7 kids per ball
            for j in range(num_balls//5-1):
                # using inverse standard normal distribution
                ang = sqrt(-2 * log(random(0, 1))) * cos(2 * pi * random(0, 1)) * std + theta
                # ang = random(theta-3+counter*0.6, theta+3-counter*0.4)
                v = Vec(launch_speed * cos(radians(ang)), launch_speed * sin(radians(ang)), 0)
                new_balls.append(Ball(launch_height, v, ang))
                
        balls = [x for x in new_balls]

        print("Height: " + str(launch_height))
        print("Angle: " + str(sorted_balls[0][0]))
        print("Range: " + str(sorted_balls[0][1]))
        print(" ")
        
        # print(len(balls))
        
    # print(len(balls))
    
    # actually applies force and moves each ball
    for ball in balls:
    
        # F = Vadd(Fg, airdrag(ball.vel, airdrag_coeff, front_facing_area, air_density), magnus_force(magnus_coeff, launch_spin, ball.vel))
        # F = Vadd(Fg, airdrag(ball.vel, airdrag_coeff, front_facing_area, air_density))
        F = Fg
        a = Vdiv(F, m)
        ball.updateVel(a, dt)
        ball.move(dt)
        
        t += dt
        
        # if ball is on ground remove from list and record it
        if isLanded(ball.pos.x, ball.pos.y):
            record_balls.append([ball.angle, ball.pos.x])
            balls.remove(ball)
            
    return balls
            
    
