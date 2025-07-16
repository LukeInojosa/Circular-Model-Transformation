from libs.interface import interface
from libs.operations.point import Point
from libs.operations.matrix import Matrix
from datetime import datetime
import cv2 as cv
import numpy as np
from tqdm import tqdm
import time
import sys

def fit(matrix,point):
    inverse = matrix.inverse()
    v = inverse*point
    diag = Matrix.diagonal(v)
    return matrix*diag

if __name__ == "__main__":
    
    if(len(sys.argv) == 2):
        window = interface.Window(sys.argv[1])

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
            
            print("from: ", points[1][0], "to: ", window.sphere.project_in_plane(transform*points[1][0]) )
            print("from: ", points[1][1], "to: ", window.sphere.project_in_plane(transform*points[1][1]) )
            print("from: ", points[1][2], "to: ", window.sphere.project_in_plane(transform*points[1][2]) )
            print("from: ", points[1][3], "to: ", window.sphere.project_in_plane(transform*points[1][3]) )

            image = window.image
            rows, cols, _ = image.shape
            dest_image = np.zeros((rows,cols,3), np.uint8)

            with tqdm(total=(rows+1)*(cols+1), desc="Processando...", unit="tarefa") as barra_progresso:
                for i in range(rows):
                    for j in range(cols):
                        point = window.sphere.raise_to_sphere(Point(i,j))
                        point_transform = transform*point
                        point_in_plane = window.sphere.project_in_plane(point_transform)
                        dest_image[j][i] = image[point_in_plane.y][point_in_plane.x] 
                        barra_progresso.update(1)

            print("Conversão realizada com sucesso!")
            
            for point in window.dest_point:
                cv.circle(dest_image,center = point,radius = 10,color = (0,255,0),thickness=-1)
            window.dest_point =[]
            name = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            cv.imwrite("data/"+name+".png",dest_image)

    cv.destroyAllWindows()


