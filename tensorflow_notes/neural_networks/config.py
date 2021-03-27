"""
configuation setting for neural network model
"""

hidden_dimension_list = [512, 256, 128, 64] # number of nodes in hidden layers

epochs = 10  # Total number of training epochs

batch_size = 64  # Training batch size

learning_rate = 0.001  # The optimization initial learning rate

model_path = 'model_weights'

data_path = 'MNIST_data'

data_source = 'mnist'

data_description = {
    'mnist': {
        'img_w': 28,
        'img_h': 28,
        'n_channels': 1,
        'image_size_flat': 28 * 28,
        'n_classes': 10
    },
    'cifar10': {
        'img_w': 32,
        'img_h': 32,
        'n_channels': 3,
        'image_size_flat': 32 * 32,
        'n_classes': 10
    }
}
