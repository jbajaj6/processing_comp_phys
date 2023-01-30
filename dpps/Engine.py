from Vectors import *
from math import sin, radians, cos
from Ball import Ball

balls = []

launch_height = 96.952
launch_speed = 60

pi = 3.14159265359

num_balls = 40

for i in range(num_balls):
    # inputs
    # launch_angle = random(0, 90)
    dd = random(0, 500)

    # v = Vec(launch_speed * cos(radians(launch_angle)), launch_speed * sin(radians(launch_angle)), 0)
    v = Vec(launch_speed, 0, 0)
    launch_height = 96.952
    
    ball = Ball(launch_height, v, dd)
    balls.append(ball)

g = Vec(0, -9.8, 0)

m = 0.6
Fg=Vmult(g,m)

dt = 0.05

t = 0

counter = 0

radius = 0.12

airdrag_coeff = 0.5
front_facing_area = radius * radius * PI
air_density = 1.2

wind = Vec(-10, 0, 0)

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

def move():
    global t, dt, max_height, record_balls, balls, new_balls, counter, launch_height
    
    if len(balls) == 0:
        # sort balls in order of greatest to least distance
        sorted_balls = sorted(record_balls, key=lambda x:x[1])
            
        new_balls = []
        
        # get 5 best performing balls
        for i in range(5):
            dd = sorted_balls[i][0]
            # v = Vec(launch_speed * cos(radians(ang)), launch_speed * sin(radians(ang)), 0)
            new_balls.append(Ball(launch_height, Vec(60, 0, 0), dd))
        
        for i in range(5):
            std = 10 - counter * 0.5
            old = new_balls[i].drop
            launch_height = 96.952
            # make 7 kids per ball
            for j in range(num_balls//5-1):
                # using inverse standard normal distribution
                new = sqrt(-2 * log(random(0, 1))) * cos(2 * pi * random(0, 1)) * std + old
                # ang = random(theta-3+counter*0.6, theta+3-counter*0.4)
                v = Vec(60, 0, 0)
                new_balls.append(Ball(launch_height, v, new))
                
        balls = [x for x in new_balls]
        
        counter += 1

        print("Generation: " + str(counter))
        print("Height: " + str(launch_height))
        print("Drop: " + str(sorted_balls[0][0]))
        print("Time: " + str(sorted_balls[0][0]/60))
        print("Dist From 200: " + str(sorted_balls[0][1]))
        print(" ")
        
        # print(len(balls))
        
    # print(len(balls))
    
    # actually applies force and moves each ball
    for ball in balls:
    
        # F = Vadd(Fg, airdrag(ball.vel, airdrag_coeff, front_facing_area, air_density), magnus_force(magnus_coeff, launch_spin, ball.vel))
        F = Vadd(Fg, airdrag(ball.vel, airdrag_coeff, front_facing_area, air_density))
        a = Vdiv(F, m)
        ball.updateVel(a, dt)
        ball.move(dt)
        
        t += dt
        
        # if ball is on ground remove from list and record it
        if ball.pos.y <= 0:
            record_balls.append([ball.drop, abs(200-ball.pos.x)])
            balls.remove(ball)
            
    return balls
            
    
