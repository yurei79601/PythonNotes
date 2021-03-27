"""
create data for classification tasks
1. MNIST data
2. cifar 10 data
"""
import numpy as np


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


def one_hot_array(arr: np.array) -> np.array:
    '''
    Transform array with labels to one-hot array
    '''
    num_classes = len(np.unique(arr))
    num_sample = arr.shape[0]
    return np.eye(num_classes)[arr].reshape(num_sample, num_classes)


class DataManager:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data_loader = {
            'mnist': self.load_mnist_data,
            'cifar10': self.load_cifar10_data
        }

    def load_mnist_data(self, mode):
        from tensorflow.examples.tutorials.mnist import input_data

        mnist = input_data.read_data_sets(self.data_path, one_hot=True)
        if mode == "train":
            x_train = np.expand_dims(
                np.concatenate((mnist.train.images, mnist.validation.images), axis=0), 2
                )
            y_train = np.concatenate((mnist.train.labels, mnist.validation.labels), axis=0)
            return x_train, y_train
        elif mode == "test":
            x_test, y_test = \
                np.expand_dims(mnist.test.images, 2),\
                mnist.test.labels
            return x_test, y_test

    def load_cifar10_data(self, mode):
        '''
        Get cifar10 datasets from Keras
        '''
        import tensorflow as tf

        if mode == 'train':
            (x_train, y_train), (_, _) = tf.keras.datasets.cifar10.load_data()
            n, h, w, c = x_train.shape
            return np.reshape(x_train, (n, h*w, c)), one_hot_array(y_train)
        elif mode == 'test':
            (_, _), (x_valid, y_valid) = tf.keras.datasets.cifar10.load_data()
            n, h, w, c = x_valid.shape
            return np.reshape(x_valid, (n, h*w, c)), one_hot_array(y_valid)
