from Celestial import *
from Vectors import *
from Time import *
import datetime


# init pos and vel on march 8
# asteroid initial pos
aip = Vec(-3.005962561795256e12, 4.038952915479552e12, -1.492794252572341e12)


# sun, mercury, venus, earth (with moon), mars, jupiter, saturn, uranium, neptune

# create new celestial object for each celestial (mass, position, velocity)
sun = Celestial(3, "Sun", 1988500e24, Vec(-1.313521631827818e9, 4.165494865584964e8, 2.727350484357949e7), Vec(-4.695794865686246e0, -1.494332707948341e1, 2.326766798669477e-1), 253, 184, 19)
asteroid = Celestial(1, "Asteroid", 1, aip, Vec(5.683734402456867e2, 7.506989468425318e2, 3.131585861735725e1), 200, 200, 200)
mercury = Celestial(0.8, "Mercury", 3.302e23, Vec(6.906266519516132e9, -6.758191938853790e10, -6.283448846695736e9), Vec(3.858651435738656e4, 8.330718843762895e3, -2.857625453889960e3), 173, 168, 165)
venus = Celestial(0.8, "Venus", 48.685e23, Vec(-1.010050465950096e11, -4.070919240512995e10, 5.215165238148943e10), Vec(1.311149010770386e4, -3.254932090697576e4, -1.203209679906598e3), 255, 198, 73)
earth = Celestial(1, "Earth", 5.97219e24, Vec(-1.460284448215014e11, 3.359107209201963e10, 2.644291526326910e7), Vec(-7.137140953958247e3, -2.917199196426223e4, 6.723603368019582e-1), 40, 122, 184)
moon = Celestial(0.3, "Moon", 7.349e22, Vec(-1.457738097235724e11, 3.389790029178204e10, 2.381901821419969e7), Vec(-7.863044411347168e3, -2.851533220243849e4, 8.702818179782312e1), 254, 252, 215)
mars = Celestial(0.8, "Mars", 6.4171e23, Vec(4.362574396476334e9, -2.167325809296497e11, -4.662925287737712e9), Vec(2.512824547194639e4, 2.702250681768545e3, -5.593312399203167e2), 188, 39, 50)
jupiter = Celestial(2, "Jupiter", 189818722e19, Vec(7.177857129365799e11, -1.936751255821390e11, -1.525515099580573e10), Vec(3.248006583427828e3, 1.322690866890178e4, -1.275639321280826e2), 188, 175, 178)
saturn = Celestial(1.5, "Saturn", 5.6834e26, Vec(1.075407753899379e12, -1.017433698815629e12, -2.512573207994366e10), Vec(6.098121183594531e3, 6.998363541981655e3, -3.650586384174681e2), 171, 96, 74)
uranus = Celestial(1.2, "Uranus", 86.813e24, Vec(2.125553155431122e12, 2.043246615197367e12, -1.994823528146613e10), Vec(-4.769342676217716e3, 4.592281962103117e3, 7.893554528023361e1), 79, 208, 231)
neptune = Celestial(1.2, "Neptune", 102.409e24, Vec(4.435713952610410e12, -5.805469379064959e11, -9.027022756118616e10), Vec(6.700757125145634e2, 5.422133394724042e3, -1.271340558810616e2), 75, 112, 221)


# create array of celesitals
celestials = [sun, asteroid, mercury, venus, earth, moon, mars, jupiter, saturn, uranus, neptune]

# create initial time object
x = Time(datetime.datetime(2022, 3, 8))

# set delta time
dt = 10e5

# universal gravitational constant
ugc = 6.67e-11

# returns the force from p1 on p2
def fg(p1, p2):
    # d --> distance (dist is a keyword)
    d = Vsub(p1.p, p2.p)
    r = Vmag(d)
    return Vmult(Norm(d), ugc * p1.m * p2.m / (r * r))

def move():
    global x, dt
    
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

     
