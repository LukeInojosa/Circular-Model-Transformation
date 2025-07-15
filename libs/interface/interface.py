import cv2 as cv
import math
from datetime import datetime
from libs.operations.point import Sphere
from libs.operations.point import Point

class Window:
        
    EVENT_CTRLKEYACTIVE = 9

    def __init__(self,image_name = ""):
        # cria janela
        self.window_name = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv.namedWindow(self.window_name, cv.WINDOW_NORMAL) 
        # coloca imagem na janela
        self.put_image(image_name)
        # callback function para mouse
        cv.setMouseCallback(self.window_name, self.mouse_callback)
        # transformation points
        self.X = []
        self.Y = []
    
    def put_image(self,image_name):
        # carrega imagem
        image = cv.imread("data/"+image_name)
        if image.size == 0:
            raise ValueError("Nao foi possivel carregar imagem")

        rows, cols = image.shape[:2]

        # adiciona bordas a imagem carregada
        diagonal = int(math.sqrt(rows*rows + cols*cols))
        top = bottom = int(1.5*diagonal - rows)//2
        left = right = int(1.5*diagonal - cols)//2
        image_with_border = cv.copyMakeBorder(image, top, bottom, left, right, cv.BORDER_CONSTANT,None,value = 0)
        self.image = image_with_border.copy()

        # adiciona circulo na imagem
        rows, cols = image_with_border.shape[:2] 
        center = (rows//2,cols//2)
        radius = int(1.2*diagonal)//2
        self.sphere = Sphere(Point(*center),radius)
        cv.circle(image_with_border, center, radius, (255,0,0), thickness = 2)
        
        # adiciona imagem na janela
        cv.imshow(self.window_name,image_with_border)
    
    def get_points(self):
        if(len(self.X) == len(self.Y) == 4):
            result = (self.X,self.Y)
            self.X = []
            self.Y = []
            return result
        return []

    def mouse_callback(self,event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            if len(self.X) < 4:
                point = Point(x,y)
                point_in_sphere = self.sphere.raise_to_sphere(point)
                self.X.append(point_in_sphere)
                print(self.X)

        if event == cv.EVENT_LBUTTONDBLCLK and flags == Window.EVENT_CTRLKEYACTIVE:
            if len(self.Y) < 4:
                point = Point(x,y)
                point_in_sphere = self.sphere.raise_to_sphere(point)
                self.Y.append(point_in_sphere)
                print(self.Y)
