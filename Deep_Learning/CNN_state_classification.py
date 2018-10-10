import time
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
import os

from random import shuffle
#from tqdm import tqdm

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
num_filters4 = 256
# Convolutional Layer 5
filter_size5 = 4
num_filters5 = 128
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
classes = ['left', 'right', 'straight']
num_classes = len(classes)
# batch size
batch_size = 50


TRAIN_DIR = 'train'
TEST_DIR = 'test'

def label_img(img):
  word_label = img.split('.')[-3]
  if word_label == 'cat': return [1,0]
  elif word_label == 'dog': return [0,1]

train_data = np.load('states.npy')


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

layer_flat, num_features = flatten_layer(layer_conv3)
layer_fc1 = new_fc_layer(input=layer_flat,num_inputs=num_features,num_outputs=fc_size,use_relu=True)
layer_fc2 = new_fc_layer(input=layer_fc1,num_inputs=fc_size,num_outputs=num_classes,use_relu=False)

y_pred = tf.nn.softmax(layer_fc2)
y_pred_cls = tf.argmax(y_pred, axis=1)
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=layer_fc2,labels=y_true)
cost = tf.reduce_mean(cross_entropy)

optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)
correct_prediction = tf.equal(y_pred_cls, y_true_cls)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

train = train_data[:-150]
test = train_data[-150:]

x_batch = np.array([i[0] for i in train]).reshape(len(train),img_size_flat)
y_true_batch = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(len(test),img_size_flat)
test_y = [i[1] for i in test]

saver = tf.train.Saver()
session = tf.Session()
session.run(tf.global_variables_initializer())
total_iterations = 0

def optimize(num_iterations):
    
    global total_iterations
    start_time = time.time()
    b =0

    for i in range(total_iterations,total_iterations + num_iterations):
    	a = 0
    	for __ in range(int(len(train)/batch_size)):
        	feed_dict_train = {x: x_batch[a:a+batch_size,:],y_true: y_true_batch[a:a+batch_size]}
        	session.run(optimizer, feed_dict=feed_dict_train)
        	a = a + batch_size

    	duration = time.time() - start_time
 		
    	if i % 2 == 0: 
            print("Test Accuracy = ", session.run(accuracy, feed_dict={x:test_x[b:b+batch_size,:], y_true: test_y[b:b+batch_size]}))
            print("Iteration = ", i, "Loss = ", session.run(cost, feed_dict=feed_dict_train))
            print("Train Accuracy = ", session.run(accuracy, feed_dict=feed_dict_train))
            print("Duration = %.1f sec" % duration)
            if (b+batch_size == 150):
              b=0
            b = b + batch_size
    saver.save(session,'my_model')        

optimize(num_iterations=50)                                                        