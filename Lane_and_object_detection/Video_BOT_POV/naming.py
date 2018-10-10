import random
import numpy as np
import tensorflow as tf
import cv2
import os

from random import shuffle
from tqdm import tqdm

TRAIN_DIR = 'right'
d = 1

for img in tqdm(os.listdir(TRAIN_DIR)):
    path = os.path.join(TRAIN_DIR,img)
    img = cv2.imread(path,1)
    img = cv2.flip(img,1)
    cv2.imwrite
    filename = "left.%d.jpg"%d
    cv2.imwrite(filename, img)
    d+=1
