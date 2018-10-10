import time
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
import os

from random import shuffle
from tqdm import tqdm

# Convolutional Layer 1.
filter_size1 = 4 
num_filters1 = 64
# Convolutional Layer 2.
filter_size2 = 4
num_filters2 = 128
# Convolutional Layer 3.
filter_size3 = 4
num_filters3 = 64
# Convolutional Layer 4
filter_size4 = 4
num_filters4 = 128
# Convolutional Layer 5
filter_size5 = 4
num_filters5 = 64
# Fully-connected layer.
fc_size = 512        
# Number of colo channels for the images: 1 channel for gray-scale.
num_channels = 1
# image dimensions (only squares for now)
img_size0 = 640
img_size1 = 140
# Size of image when flattened to a single dimension
img_size_flat = img_size0 * img_size1 * num_channels
# Tuple with height and width of images used to reshape arrays.
img_shape = (img_size0, img_size1)
# class info
classes = ['right', 'straight']
num_classes = len(classes)
# batch size
batch_size = 10
last_state = 0

checkpoint_dir = "models/"


def new_weights(shape):
    return tf.Variable(tf.truncated_normal(shape, stddev=0.05))
def new_biases(length):
    return tf.Variable(tf.constant(0.05, shape=[length]))

def new_conv_layer(input,num_input_channels,filter_size,num_filters,use_pooling=True):  

    shape = [filter_size, filter_size, num_input_channels, num_filters]
    weights = new_weights(shape=shape)
    biases = new_biases(length=num_filters)

    layer = tf.nn.conv2d(input=input,filter=weights,strides=[1, 1, 1, 1],padding='SAME')
    layer += biases

    if use_pooling:
        layer = tf.nn.max_pool(value=layer,ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1],padding='SAME')

    layer = tf.nn.relu(layer)

    return layer, weights

def new_fc_layer(input,num_inputs,num_outputs,use_relu=True): 

    weights = new_weights(shape=[num_inputs, num_outputs])
    biases = new_biases(length=num_outputs)

    layer = tf.matmul(input, weights) + biases
    
    if use_relu:
        layer = tf.nn.relu(layer)

    return layer

def flatten_layer(layer):
    
    layer_shape = layer.get_shape()
    num_features = layer_shape[1:4].num_elements()
    layer_flat = tf.reshape(layer, [-1, num_features])

    return layer_flat, num_features

x = tf.placeholder(tf.float32, shape=[None, img_size_flat], name='x')
x_image = tf.reshape(x, [-1, img_size0, img_size1, num_channels])
y_true = tf.placeholder(tf.float32, shape=[None, num_classes], name='y_true')
y_true_cls = tf.argmax(y_true, axis=1)

layer_conv1, weights_conv1 = new_conv_layer(input=x_image,num_input_channels=num_channels,filter_size=filter_size1,
                                            num_filters=num_filters1,use_pooling=True)
layer_conv2, weights_conv2 = new_conv_layer(input=layer_conv1,num_input_channels=num_filters1,filter_size=filter_size2,
                                            num_filters=num_filters2,use_pooling=True)
layer_conv3, weights_conv3 = new_conv_layer(input=layer_conv2,num_input_channels=num_filters2,filter_size=filter_size3,
                                            num_filters=num_filters3,use_pooling=True)
layer_conv4, weights_conv4 = new_conv_layer(input=layer_conv3,num_input_channels=num_filters3,filter_size=filter_size4,
                                            num_filters=num_filters4,use_pooling=True)
layer_conv5, weights_conv5 = new_conv_layer(input=layer_conv4,num_input_channels=num_filters4,filter_size=filter_size5,
                                            num_filters=num_filters5,use_pooling=True)

layer_flat, num_features = flatten_layer(layer_conv5)
layer_fc1 = new_fc_layer(input=layer_flat,num_inputs=num_features,num_outputs=fc_size,use_relu=True)
layer_fc2 = new_fc_layer(input=layer_fc1,num_inputs=fc_size,num_outputs=num_classes,use_relu=False)

y_pred = tf.nn.softmax(layer_fc2)
y_pred_cls = tf.argmax(y_pred, axis=1)
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=layer_fc2,labels=y_true)
cost = tf.reduce_mean(cross_entropy)

optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)
correct_prediction = tf.equal(y_pred_cls, y_true_cls)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

session = tf.Session()
saver = tf.train.Saver()
saver.restore(session,'my_model')
test_edge = []
cap=cv2.VideoCapture(1)
#out = cv2.VideoWriter('Videooutput.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 16.57, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    image = frame[200:480, 0:640]
    image = cv2.resize(image,(640,140))
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    median = cv2.GaussianBlur(gray,(1,1),0)
    edges = cv2.Canny(median,80,200)
    test_edge = np.array(edges)
    test_edge = test_edge.reshape(1,img_size_flat)

    Test_acc = session.run(y_pred, feed_dict={x:test_edge})
    state = session.run(y_pred_cls, feed_dict={x:test_edge})
    print('without',state)
    print('Test_acc',Test_acc)
    a = np.argmax(Test_acc)
    if  a <= 0.7:
        cur_state = last_state
    else :
        cur_state = state
        last_state = state

    #print('cur_state',cur_state)
    if cur_state == 0:
        lane_state = 'Right'
    elif cur_state == 1:
        lane_state = 'Straight'
    #print('arr',np.array(Test_acc))

    cv2.putText(frame,lane_state,(320,250),cv2.FONT_ITALIC,2,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)

    
    cv2.waitKey(1)
    #out.write(frame)

cap.release()
cv2.destroyAllWindows()
                                                        