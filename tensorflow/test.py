#print(100 + 210)
#print("100 + 200 = ",100+200)


import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
hello = tf.constant('66666666666')
sess = tf.Session()
print(sess.run(hello))
