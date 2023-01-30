class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        xx = other.x + self.x
        yy = other.y + self.y
        zz = other.z + self.z
        return Vector3D(xx,yy,zz)

    def __sub__(self, other):
        xx = self.x - other.x
        yy = self.y - other.y
        zz = self.z - other.z
        return Vector3D(xx,yy,zz)

    def __mul__(self, other):
        xx = self.x * other
        yy = self.y * other
        zz = self.z * other
        return Vector3D(xx,yy,zz)

    def __truediv__(self, other):
        xx = self.x / other
        yy = self.y / other
        zz = self.z / other
        return Vector3D(xx,yy,zz)

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

    def magnitude(self):
        import math
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    def normalize(self):
        return self * (1/self.magnitude())

    def normalizeinplace(self):
        y = self * (1/self.magnitude())
        self.x = y.x
        self.y = y.y
        self.z = y.z

    def dot(self,v):
        xx = self.x * v.x
        yy = self.y * v.y
        zz = self.z * v.z
        return xx + yy + zz

    def cross(self,v):
        cx = (self.y * v.z) - (self.z * v.y)
        cy = (self.z * v.x) - (self.x * v.z)
        cz = (self.x * v.y) - (self.y * v.x)
        return Vector3D(cx,cy,cz)

    def crossinplace(self,v):
        cx = (self.y * v.z) - (self.z * v.y)
        cy = (self.z * v.x) - (self.x * v.z)
        cz = (self.x * v.y) - (self.y * v.x)
        self.x = cx
        self.y = cy
        self.z = cz
