import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data


'''Convolutional Neural Network(CNN)卷积神经网络'''


mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
sess = tf.InteractiveSession()


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 卷积层 池化层