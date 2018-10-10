import cv2
import numpy as np
import math


class Warper:
    def __init__(self):
        self.x1 = 20
        self.x2 = 625
        self.y = 230
        self.h = 30
        self.Ot = math.radians(21)

        self.a = self.x1 + (self.h / math.tan(self.Ot))
        self.b = self.x2 - (self.h / math.tan(self.Ot))
        self.src = np.float32([
            [self.a, self.y - self.h],
            [self.b, self.y - self.h],
            [self.x2, self.y],
            [self.x1, self.y],
        ])

        self.dst = np.float32([[0, 0],[640, 0],[640, 480],[0, 480]])

        self.M = cv2.getPerspectiveTransform(self.src, self.dst)
        self.Minv = cv2.getPerspectiveTransform(self.dst, self.src)

    def warp(self, img):
        return cv2.warpPerspective(
            img,
            self.M,
            (img.shape[1], img.shape[0]),
            flags=cv2.INTER_LINEAR
        ), self.src, self.dst

    def unwarp(self, img):
        return cv2.warpPersective(
            img,
            self.Minv,
            (img.shape[1], img.shape[0]),
            flags=cv2.INTER_LINEAR
        )
