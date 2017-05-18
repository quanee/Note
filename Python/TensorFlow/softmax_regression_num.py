import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

'''
Softmax Regression识别手写数字
训练数据特征: 55000x784(28x28)的Tensor
训练数据Label: 55000x10

'''


mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 训练集(55000)