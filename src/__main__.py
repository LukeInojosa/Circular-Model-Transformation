from libs.interface import interface
from libs.operations.point import Point
from libs.operations.matrix import Matrix
from datetime import datetime
import cv2 as cv
import numpy as np

def fit(matrix,point):
    inverse = matrix.inverse()
    v = inverse*point
    diag = Matrix.diagonal(v)
    return matrix*diag

if __name__ == "__main__":

    window = interface.Window("test.png")

    while(True):
        if cv.waitKey(20) & 0xFF == 27:
            break
        points = window.get_points()
        if(points):
            X = Matrix.from_points(*points[0][:3])
            x = points[0][3]

            Y  = Matrix.from_points(*points[1][:3])
            y = points[1][3]
            
            transform = fit(X,x)*(fit(Y,y).inverse())
            print("transform:", transform) 

            image = window.image
            rows, cols, _ = image.shape
            print("rows: " , rows)
            print("cols: ", cols)
            dest_image = np.zeros((rows,cols,3), np.uint8)

            for i in range(rows):
                for j in range(cols):
                    point = window.sphere.raise_to_sphere(Point(i,j))
                    point_transform = transform*point
                    point_in_plane = window.sphere.project_in_plane(point_transform)
                    dest_image[i][j] = image[point_in_plane.x][point_in_plane.y] 

            name = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            cv.imwrite("data/"+name+".png",dest_image)
            print("conversão realizada com sucesso")

    cv.destroyAllWindows()


