import math


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def raise_to_sphere(self, point):
        diff_center = point - self.center
        mod = diff_center & diff_center
        if math.sqrt(mod) <= self.radius:
            diff_center.z = math.sqrt(self.radius**2 - mod)
        return diff_center

    def __repr__(self):
        return "Esphere(center = {}, radius = {})".format(self.center,self.radius)

class Point:
    def __init__(self,x = 0,y = 0,z = 0):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_tuple(cls,t):
        return cls(*t)
        

    def __add__(self, point):
        return Point( self.x + point.x, self.y + point.y, self.z + point.z)

    def __sub__(self, point):
        return Point( self.x - point.x, self.y - point.y, self.z - point.z)
    
    def __neg__(self):
        return Point(-self.x,-self.y,-self.z)

    def __mul__(self,value):
        return Point(self.x*value, self.y*value, self.z*value)

    def __and__(self,point):
        return self.x*point.x + self.y*point.y + self.z*point.z
    
    def __xor__(self,point):
        x = self.y*point.z-self.z*point.y
        y = self.x*point.z - self.z*point.x
        z = self.x*point.y - self.y*point.x
        return Point(x,y,z)
    
    def dot(self, point):
        return self.x*point.x + self.y*point.y + self.z*point.z
    
    def cross(self,point):
        x = self.y*point.z-self.z*point.y
        y = self.x*point.z - self.z*point.x
        z = self.x*point.y - self.y*point.x
        return Point(x,y,z)
    
    def module(self):
        return math.sqrt(self & self)

    def __abs__(self):
        return math.sqrt(self & self)

    def __repr__(self):
        return "Point({},{},{})".format(self.x,self.y,self.z)
