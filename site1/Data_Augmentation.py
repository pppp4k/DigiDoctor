import tensorflow as tf
import cv2
 
a = tf.truncated_normal([16,128,128,3])
sess = tf.Session()
sess.run(tf.initialize_all_variables())
sess.run(tf.shape(a))
