import random
import numpy as np
import tensorflow as tf
import cv2
import os

from random import shuffle
from tqdm import tqdm

train_dir = 'lanes'
test_dir = 'test'

def label_folder(folders):
    if folders == 'left': return [1,0,0]
    elif folders == 'right': return [0,0,1]
    elif folders == 'straight': return [0,1,0]

def create_train_data():
    training_data = []
    dirs = os.listdir( train_dir )
    for folders in dirs:
        label = label_folder(folders)
        req_train_dir = os.path.join(train_dir,folders)
        for img in tqdm(os.listdir(req_train_dir)):
            path = os.path.join(req_train_dir,img)
            img = cv2.imread(path,1)
            #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            training_data.append([np.array(img),np.array(label)])
    shuffle(training_data)
    np.save('states_rgb.npy', training_data)
    return training_data

def process_test_data():
    testing_data = []
    for img in tqdm(os.listdir(test_dir)):
        path = os.path.join(test_dir,img)
        img_num = img.split('.')[0]  #image id
        img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (img_size,img_size))
        testing_data.append([np.array(img), img_num])
        
    shuffle(testing_data)
    np.save('flower_test_data.npy', testing_data)
    return testing_data

train_data = create_train_data()
#test_data = process_test_data()