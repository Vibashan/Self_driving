import random
import numpy as np
#import tensorflow as tf
import cv2
import os

from random import shuffle
from tqdm import tqdm

train_dir = 'train'
test_dir = 'test'

def label_img(img):
    word_label = img.split('.')[-3]
    if word_label == 'right': return [1,0]
    elif word_label == 'straight': return [0,1]

def create_train_data():
    training_data = []
    dirs = os.listdir( train_dir )
    for img in tqdm(os.listdir(train_dir)):
        label = label_img(img)
        path = os.path.join(train_dir,img)
        img = cv2.imread(path,0)
        img = img[200:480, 0:640]
        img = cv2.resize(img ,(640,140))
        #cv2.imshow('img',img)
        #cv2.waitKey(80)
        training_data.append([np.array(img),np.array(label)])
    shuffle(training_data)
    np.save('states_gray.npy', training_data)
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
