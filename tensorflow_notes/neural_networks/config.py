"""
configuation setting for neural network model
"""

img_h = img_w = 32  # MNIST images are 28x28

n_channels = 3

hidden_dimension_list = [512, 256, 128, 64] # number of nodes in hidden layers

n_classes = 10  # Number of classes, one class per digit

epochs = 10  # Total number of training epochs

batch_size = 64  # Training batch size

learning_rate = 0.001  # The optimization initial learning rate

model_path = './'

data_path = 'MNIST_data'