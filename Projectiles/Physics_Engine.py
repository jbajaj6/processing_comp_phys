from Vectors import *
from math import sin, radians, cos

pp = []

inputs = "5  80  10".split("  ")


# inputs
launch_height = float(inputs[0])
launch_speed = float(inputs[1])
launch_angle = radians(float(inputs[2]))

p = Vec(0, launch_height, 0)
v = Vec(launch_speed * cos(launch_angle), launch_speed * sin(launch_angle), 0)
m = 0.045

g = Vec(0, -9.8, 0)
Fg=Vmult(g,m)

dt = 0.01

t = 0

radius = 0.021335

airdrag_coeff = 0.2
front_facing_area = radius * radius * PI
air_density = 1.2

wind = Vec(-5, 0, 0)

magnus_coeff = 5e-5
launch_spin = Vec(0, 0, 272)

max_height = 0

def magnus_force(mc, spin, vel):
    relative_velocity = Vsub(vel, wind)
    fl = Vmult(Vcprod(spin, relative_velocity), mc)
    return fl

def airdrag(velocity, adc, ffa, ad):
    relative_velocity = Vsub(velocity, wind)
    fd = -0.5 * adc * ffa * ad * Vmag(relative_velocity) * Vmag(relative_velocity)
    return Vmult(Norm(velocity), fd)

def move():
    global t, dt, max_height
    
    F = Vadd(Fg, airdrag(v, airdrag_coeff, front_facing_area, air_density), magnus_force(magnus_coeff, launch_spin, v))
    a = Vdiv(F, m)
    v.plus(Vmult(a, dt))
    p.plus(Vmult(v, dt))

    past_pos = Vec(p.x, p.y, 0)
    pp.append(past_pos)
    
    if p.y > max_height:
        max_height = p.y
    
    t += dt
    
    if p.y < 0:

        
        dt = 0
        print("Range: " + str(p.x) + " m")
        print("\nTime: " + str(t) + " s")
        # print("\nVelocity: " + str(v.y) + " m/s")
        # print("\nX Vel: " + str(v.x) + " m/s")
        # print("\nY Vel: " + str(v.y) + " m/s")
        print("\nMax Height: " + str(max_height) + " m")
        p.y = 0
