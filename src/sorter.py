import argparse
from algorithm import SortingAlgorithm
from image import Image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-sorter',
        help='supported algorithms: quick, bubble, heap',
        required=True
    )
    args = parser.parse_args()

    image = Image()
    image.initialize()
    image.randomize()
    algorithm = SortingAlgorithm.factory(args.sorter)
    image.make_frames(algorithm)
