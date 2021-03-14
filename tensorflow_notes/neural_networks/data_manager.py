"""
create data for classification tasks
1. MNIST data
"""
import numpy as np


class DataManager:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self, mode):
        from tensorflow.examples.tutorials.mnist import input_data

        mnist = input_data.read_data_sets(self.data_path, one_hot=True)
        if mode == "train":
            x_train = np.concatenate((mnist.train.images, mnist.validation.images), axis=0)
            y_train = np.concatenate((mnist.train.labels, mnist.validation.labels), axis=0)
            return x_train, y_train
        elif mode == "test":
            x_test, y_test = mnist.test.images, mnist.test.labels
            return x_test, y_test


def randomize(x, y):
    """ Randomizes the order of data samples and their corresponding labels"""
    permutation = np.random.permutation(y.shape[0])
    shuffled_x = x[permutation, :]
    shuffled_y = y[permutation]
    return shuffled_x, shuffled_y


def get_next_batch(x, y, start, end):
    x_batch = x[start:end]
    y_batch = y[start:end]
    return x_batch, y_batch
