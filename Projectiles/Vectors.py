#from math import sqrt
import math

class Vec:
    # initializes class
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    # adds however many vectors to the given vector
    # syntax --> x.plus(vec1, vec2, vec3...) --> x + sum(vec1, vec2, vec3...)
    def plus(self, *vecs):
        for i in vecs:
            self.x += i.x
            self.y += i.y
            self.z += i.z
            
        
    
    # multiplies a constant to the given vector
    def times(self, coeff):
        self.x *= coeff
        self.y *= coeff
        self.z *= coeff
    
    # subtracts however many vectors from the given vector
    # syntax --> x.minus(vec1, vec2, vec3...) --> x - sum(vec1, vec2, vec3...)
    def minus(self, *vecs):
        for i in vecs:
            self.x -= i.x
            self.y -= i.y
            self.z -= i.z
           
    # divides a constant to the given vector 
    def dividedBy(self, divisor):
        self.x /= divisor
        self.y /= divisor
        self.z /= divisor

# calculates & returns magnitude for a given vector
# synatx --> Vmag(x)
def Vmag(vec):
    # with extensive testing i found that -->
    # math.sqrt(n) is ~4/3x as fast as n**0.5
    # n*n is ~5 times faster n**2
    return math.sqrt(vec.x*vec.x + vec.y*vec.y + vec.z*vec.z)
        
# prints vector
def Vprint(vec):
    print(vec.x, vec.y, vec.z)
    
# adds any number of vectors together and returns the sum without changing the given vectors
def Vadd(*vecs):
    v = Vec(0, 0, 0)
    for i in vecs:
        v.x += i.x
        v.y += i.y
        v.z += i.z
    return v

# returns difference of 2 vectors (the second one subtracted from the first one)
def Vsub(vec1, vec2):
    return Vec(vec1.x - vec2.x, vec1.y - vec2.y, vec1.z - vec2.z)

# returns the value of a vector multiplied by a scalar
def Vmult(vec1, coeff):
    return Vec(vec1.x * coeff, vec1.y * coeff, vec1.z * coeff)

# returns a vector which is the given vector divided by a scalar
def Vdiv(vec, divisor):
    return Vec(vec.x / divisor, vec.y / divisor, vec.z / divisor)
   
# returns the normalized vector
def Norm(vec):
    return Vdiv(vec, Vmag(vec))

# sets to normalized vector
def SetNorm(vec):
    vec = Norm(vec)

# returns dot product of two vectors
def Vdprod(vec1, vec2):
    return (vec1.x * vec2.x) + (vec1.y * vec2.y) + (vec1.z * vec2.z)

# returns cross product of two vectors
def Vcprod(vec1, vec2):
    return Vec(vec1.y * vec2.z - vec1.z * vec2.y, vec1.z * vec2.x - vec1.x * vec2.z, vec1.x * vec2.y - vec1.y * vec2.x)

# cross multiplies vec2 to vec1
def Vcmult(vec1, vec2):
    vec1 = Vcprod(vec1, vec2)
