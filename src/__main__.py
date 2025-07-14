from libs.interface import interface
import cv2 as cv

window = interface.Window("test.png")

while(True):
    if cv.waitKey(20) & 0xFF == 27:
        break;

cv.destroyAllWindows()


