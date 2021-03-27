import argparse
import config
from neural_network import NeuralNetworkModel


def parse_arguments():
    args = argparse.ArgumentParser(description="Train or test the linear NN model")

    args.add_argument(
            "--mode",
            type=str,
            help="Decide the model is either train or test"
        )
    return args.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    NN_Model = NeuralNetworkModel(
        config.hidden_dimension_list,
        config.epochs,
        config.batch_size,
        config.learning_rate,
        config.model_path,
        config.data_path,
        config.data_source
    )
    if args.mode == 'train':
        NN_Model.train()
    elif args.mode == 'test':
        NN_Model.test()
    else:
        raise NameError('Please choose either train or test')
