import cv2
import numpy as np
import matplotlib.pyplot as plt
from warper import Warper
from fitting import Fitter

if __name__ == '__main__':
    warp_object = Warper()
    fitt_object = Fitter()
    img = cv2.imread('img.jpg')
    # print img.shape
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    transformed, src, dst = warp_object.warp(img)
    src = src.astype(np.int32)

    cv2.polylines(img, [src], True, (255, 255, 255))
    cv2.imshow('Input', img)
    cv2.imshow('Perspective Transform', transformed)

    # transformed = cv2.GaussianBlur(transformed, (7, 7), 0)
    ret, threshold = cv2.threshold(transformed, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((7, 7), np.int8)
    threshold = cv2.erode(threshold, kernel, iterations=3)

    hist = np.sum(threshold, axis=0)
    np.reshape(hist, (-1, 1))
    print hist

    n = np.arange(1, hist.shape[0] + 1, 1)
    n = n[:, np.newaxis]
    print n.shape
    plt.plot(n, hist)

    cv2.imshow('Perspective Transform', transformed)
    cv2.imshow('threshold', threshold)
    cv2.waitKey(0)

plt.show()
cv2.destroyAllWindows()
