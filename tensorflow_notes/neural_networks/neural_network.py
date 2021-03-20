"""
main construction of neural network
"""
import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from model_utils import fc_layer, weight_variable
from data_manager import get_next_batch, randomize, DataManager
import config


class NeuralNetworkModel:
    def __init__(
        self,
        img_h,
        img_w,
        n_channels,
        hidden_dimension_list,
        n_classes,
        epochs,
        batch_size,
        display_freq,
        learning_rate,
        model_path,
        data_path
    ):
        self.img_h, self.img_w = img_h, img_w
        self.img_size_flat = self.img_h * self.img_w
        self.n_channels = n_channels
        self.hidden_dimension_list = hidden_dimension_list
        self.n_classes = n_classes
        self.epochs = epochs
        self.batch_size = batch_size
        self.display_freq = display_freq
        self.learning_rate = learning_rate
        self.model_path = model_path
        self.save_path = os.path.join(self.model_path, "twolayernetwork")
        self.session = tf.InteractiveSession()
        self.data_manager = DataManager(data_path)

        with self.session.as_default():
            (
                self.x,
                self.y,
                self.output_logits,
                self.loss,
                self.optimizer,
                self.accuracy,
                self.cls_prediction,
                self.init,
            ) = self.model()
            self.init.run()

        with self.session.as_default():
            self.saver = tf.train.Saver()
            ckpt = tf.train.latest_checkpoint(self.model_path)
            if ckpt:
                print("Checkpoint is valid")
                self.step = int(ckpt.split('/')[-1].split('-')[1])
                self.saver.restore(self.session, ckpt)


    def model(self):
        x = tf.placeholder(tf.float32,
                           shape=[None, self.img_size_flat, self.n_channels],
                           name="X")
        y = tf.placeholder(tf.float32, shape=[None, self.n_classes], name="Y")
        channel_matrix = weight_variable('channel_matrix', [self.n_channels, 1])
        hidden_layer = tf.squeeze(tf.matmul(x, channel_matrix), 2)
        # Create a fully-connected layer with h1 nodes as hidden layer
        for i, h in enumerate(self.hidden_dimension_list):
            hidden_layer = fc_layer(hidden_layer, h, f"FC{i+1}", use_relu=True)
        # Create a fully-connected layer with n_classes nodes as output layer
        output_logits = fc_layer(hidden_layer, self.n_classes, "OUT", use_relu=False)
        # Define the loss function, optimizer, and accuracy
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
                                labels=y,
                                logits=output_logits),
                              name="loss")
        optimizer = tf.train.AdamOptimizer(learning_rate=self.learning_rate,
                                           name="Adam-op").minimize(loss)
        correct_prediction = tf.equal(tf.argmax(output_logits, 1),
                                      tf.argmax(y, 1),
                                      name="correct_pred")
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32),
                                  name="accuracy")

        # Network predictions
        cls_prediction = tf.argmax(output_logits, axis=1, name="predictions")
        init = tf.global_variables_initializer()
        return x, y, output_logits, loss, optimizer, accuracy, cls_prediction, init

    def train(self):
        # x_data, y_data = self.data_manager.load_data('train')
        x_data, y_data = self.data_manager.load_cifar10_data('train')
        x_train, x_valid, y_train, y_valid = \
            train_test_split(
                x_data, y_data, test_size=0.1, random_state=123
            )
        # x_data, y_data, x_valid, y_valid = load_data("train")
        with self.session.as_default():
            print("Training")
            self.session.run(self.init)
            # Number of training steps in each epoch
            steps_per_epoch = int(len(y_data) / self.batch_size)
            for epoch in range(self.epochs):
                print("Training epoch: {}".format(epoch + 1))
                # Randomly shuffle the training data at the beginning of each epoch
                x_train, y_train = randomize(x_data, y_data)
                for step in range(steps_per_epoch):
                    start = step * self.batch_size
                    end = (step + 1) * self.batch_size
                    x_batch, y_batch = get_next_batch(
                        x_train, y_train, start, end
                    )

                    # Run optimization op (backprop)
                    feed_dict_batch = {self.x: x_batch, self.y: y_batch}
                    self.session.run(self.optimizer, feed_dict=feed_dict_batch)

                    if step % self.display_freq == 0:
                        # Calculate and display the batch loss and accuracy
                        loss_batch, acc_batch = self.session.run(
                            [self.loss, self.accuracy],
                            feed_dict=feed_dict_batch,
                        )

                        print(f"step {step:3d}:\t Loss={loss_batch:.2f}, \t"+\
                              f"Training Accuracy={acc_batch:.01%}")
                # Run validation after every epoch
                feed_dict_valid = {
                    self.x: x_valid,
                    self.y: y_valid,
                }
                loss_valid, acc_valid = self.session.run(
                    [self.loss, self.accuracy], feed_dict=feed_dict_valid
                )
                print("---------------------------------------------------------")
                print(f"Epoch: {epoch+1}, "+\
                      f"validation loss: {loss_valid:.2f}, "+\
                      f"validation accuracy: {acc_valid:.01%}")
                print("---------------------------------------------------------")

        self.saver.save(self.session, self.save_path, global_step=self.epochs)

    def test(self):
        with self.session.as_default():
            print("Testing")
            #x_test, y_test = self.data_manager.load_data("test")
            x_test, y_test = self.data_manager.load_cifar10_data('test')
            select_index = np.random.choice(range(10000), 1000)
            feed_dict_test = {
                self.x: x_test[select_index], self.y: y_test[select_index]
            }
            loss_test, acc_test, y_pred = \
                self.session.run(
                    [self.loss, self.accuracy, self.output_logits],
                    feed_dict=feed_dict_test)
        print('---------------------------------------------------------')
        print(f"Test loss: {loss_test:.2f}, "+\
              f"test accuracy: {acc_test:.01%}")
        print('---------------------------------------------------------')
        return np.argmax(y_pred, axis=1)


if __name__ == "__main__":
    NN_Model = NeuralNetworkModel(
        config.img_h,
        config.img_w,
        config.n_channels,
        config.hidden_dimension_list,
        config.n_classes,
        config.epochs,
        config.batch_size,
        config.display_freq,
        config.learning_rate,
        config.model_path,
        config.data_path)

    NN_Model.test()
