import cv2
from math import sqrt
from numpy import ndarray  # used for type checking
from typing import NoReturn
from constants import *


class ContourInfo(object):
    def __init__(self, contour: ndarray):
        self.contour = contour
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0
        self.calc_angle()
    
    def calc_angle(self) -> NoReturn:
        moments = cv2.moments(self.contour)
        self.x = int(moments['m10'] / moments['m00'])
        self.y = int(moments['m01'] / moments['m00'])
        
        midway = CAMERA_RESOLUTION[0] / 2
        if self.x < midway:
            self.angle = DEGREES_PER_PIXEL * (midway - self.x)
        else:
            self.angle = -1 * (DEGREES_PER_PIXEL * (self.x - 320))


def get_nearness_to_center(contour: ContourInfo) -> float:
    coords = (contour.x, contour.y)
    center = (CAMERA_RESOLUTION[0] / 2, CAMERA_RESOLUTION[1] / 2)
    
    dist_x = abs(coords[0] - center[0])
    dist_y = abs(coords[1] - center[1])
    
    return sqrt((dist_x ** 2) + (dist_y ** 2))
