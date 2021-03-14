"""
configuation setting for neural network model
"""

img_h = img_w = 28  # MNIST images are 28x28

img_size_flat = img_h * img_w  # 28x28=784, the total number of pixels

n_channels = 1

h1 = 200  # number of nodes in the 1st hidden layer

n_classes = 10  # Number of classes, one class per digit

epochs = 10  # Total number of training epochs

batch_size = 64  # Training batch size

display_freq = 100  # Frequency of displaying the training results

learning_rate = 0.001  # The optimization initial learning rate

model_path = './'

data_path = 'MNIST_data'