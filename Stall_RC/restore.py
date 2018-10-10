import tensorflow as tf
import numpy as np

num_channels = 1
img_size0 = 640
img_size1 = 140
img_size_flat = img_size0 * img_size1 * num_channels
img_shape = (img_size0, img_size1)
classes = ['left', 'right', 'straight']
num_classes = len(classes)

batch_size = 50
train_data = np.load('states.npy')

test = train_data[-150:]
test_x = np.array([i[0] for i in test]).reshape(len(test),img_size_flat)
test_y = [i[1] for i in test]

with tf.Session() as sess:
	 	saver = tf.train.Saver()
	 	saver.restore(sess,'my_model')
	 	print(tf.global_variables())
	 	print (sess.run(tf.get_default_graph().get_tensor_by_name('Variable:0')))
   
   	 	
		 

	 		 
   
   
   
  	  
