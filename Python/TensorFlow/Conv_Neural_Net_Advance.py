import cifar10
import cifar10_input
import tensorflow as tf
import numpy as np
import time



# 训练轮数
max_steps = 3000
batch_size = 128
# 下载CIFAR-10默认路径
data_dir = '/tmp/cifar10_data/cifar-10-batches-bin'


def variable_with_weight_loss(shape, stddev, wl):
    var = tf.Variable(tf.truncated_normal(shape, stddev=stddev))
    if wl is not None:
        weight_loss = tf.multiply(tf.nn.l2_loss(var), wl, name='weight_loss')
        tf.add_to_collection('losses', weight_loss)

    return var

