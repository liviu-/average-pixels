#!/usr/bin/env python3

import glob
import argparse

import numpy as np
import scipy.misc

from .get_images import save_images

WIDTH = 500
HEIGHT = 500
EXTENSION = "jpg"


def average_images(filenames):
    images = [scipy.misc.imread(filename, mode="RGB")
              for filename in filenames]
    resized_images = resize_images(images)
    weights = np.random.dirichlet(np.ones(len(filenames)))
    return np.average(resized_images, axis=0, weights=weights)


def resize_images(images):
    return [scipy.misc.imresize(img, (WIDTH, HEIGHT)) for img in images]


def save_image(new_image, args):
    scipy.misc.imsave("{output_filename}.{ext}".format(
            output_filename='_'.join(args.terms.split()),
            ext=EXTENSION),
        new_image)


def get_args():
    parser = argparse.ArgumentParser(
        description="Average multiple images")
    parser.add_argument(
            "terms", type=str,
            help="Keywords for images to search for")
    parser.add_argument(
        '--count', '-c', type=int,
        default=10, help='number of photos to be combined')

    return parser.parse_args()


def main():
    args = get_args()
    filenames = save_images(args.terms, args.count)
    new_image = average_images(filenames)
    save_image(new_image, args)
    print("Image saved in current directory.")

if __name__ == '__main__':
    main()
    
