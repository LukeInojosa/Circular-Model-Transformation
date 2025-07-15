from numbers import Number
from libs.operations.point import Point 

ZERO_ARRAY = [[0,0,0],[0,0,0],[0,0,0]]

class Matrix:
    def __init__(self,array = ZERO_ARRAY):
        self.matrix = array
    
    
    @classmethod
    def diagonal(cls,p1):
        array = [
                [p1.x ,0, 0],
                [0, p1.y, 0],
                [0, 0, p1.z]
                ]
        return cls(array)


    @classmethod
    def from_points(cls,p1,p2,p3):
        array = [
                [p1.x,p2.x,p3.x],
                [p1.y,p2.y,p3.y],
                [p1.z,p2.z,p3.z]
                ]
        return cls(array)
        
    def inverse(self):
        inverse_det = 1/self.det()
        adj = self.adj()
        return inverse_det*adj
    
    def __mul__(self,value):
        # multiplicação por escalar
        if(isinstance(value,Number)):
            lista = list(map(lambda row: list(map(lambda e: value*e, row)),self.matrix))
            result = Matrix(lista)
            return result
        # multiplicação por outra matrix
        if(type(value) == type(self)):
            value_transp = value.transpose()  
            r1 = Point.from_list(self.matrix[0])
            r2 = Point.from_list(self.matrix[1])
            r3 = Point.from_list(self.matrix[2]) 

            c1 = Point.from_list(value_transp.matrix[0])
            c2 = Point.from_list(value_transp.matrix[1])
            c3 = Point.from_list(value_transp.matrix[2])

            return Matrix([
                [r1*c1, r1*c2, r1*c3],
                [r2*c1, r2*c2, r2*c3],
                [r3*c1, r3*c2, r3*c3]
                ])
        # multiplicação por ponto
        if(type(value) == type(Point())):
            x = Point.from_list(self.matrix[0])*value
            y = Point.from_list(self.matrix[1])*value
            z = Point.from_list(self.matrix[2])*value
            return Point(x,y,z) 

        return NotImplemented
    
    def __rmul__(self,value):
        # multiplicação por escalar
        if isinstance(value,Number):
            lista = list(map(lambda row: list(map(lambda e: value*e, row)),self.matrix))
            result = Matrix(lista)
            return result
        # multiplicação por outra matrix
        if(type(value) == type(self)):
            value_transp = value.transpose()  
            r1 = Point.from_list(self.matrix[0])
            r2 = Point.from_list(self.matrix[1])
            r3 = Point.from_list(self.matrix[2]) 

            c1 = Point.from_list(value_transp.matrix[0])
            c2 = Point.from_list(value_transp.matrix[1])
            c3 = Point.from_list(value_transp.matrix[2])

            return Matrix([
                [r1*c1, r1*c2, r1*c3],
                [r2*c1, r2*c2, r2*c3],
                [r3*c1, r3*c2, r3*c3]
                ])
        return NotImplemented

    def transpose(self):
        result = Matrix()
        for i in range(3):
            for j in range(3):
                result.matrix[j][i] = self.matrix[i][j]
        return result


    def det(self):  
        a,b,c = self.matrix[0]
        d,e,f = self.matrix[1]
        g,h,i = self.matrix[2]

        return (a*e*i + b*f*g + c*d*h) - (c*e*g + a*f*h + b*d*i)

    def cof(self):
        a,b,c = self.matrix[0]
        d,e,f = self.matrix[1]
        g,h,i = self.matrix[2]
        
        return Matrix([
            [e*i-f*h, f*g-d*i, d*h-e*g ],
            [c*h-b*i, a*i-c*g, b*g-a*h ],
            [b*f-c*e, c*d-a*f, a*e-b*d ]
            ])

    def adj(self):
        return self.cof().transpose()

    def __repr__(self):
        return "|{} {} {}|\n".format(self.matrix[0][0],self.matrix[0][1],self.matrix[0][2])+"|{} {} {}|\n".format(self.matrix[1][0],self.matrix[1][1],self.matrix[1][2])+"|{} {} {}|\n".format(self.matrix[2][0],self.matrix[2][1],self.matrix[2][2])
