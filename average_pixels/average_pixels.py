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
    images = []
    for filename in filenames:
        try:
            images.append(scipy.misc.imread(filename, mode="RGB"))
        # Some images are corrupted
        except OSError:
            pass
    resized_images = resize_images(images)
    weights = np.random.dirichlet(np.ones(len(resized_images)))
    return np.average(resized_images, axis=0, weights=weights)


def resize_images(images):
    return [scipy.misc.imresize(img, (WIDTH, HEIGHT)) for img in images if img.shape]


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
            help="Keywords for images to search for and filename")
    parser.add_argument(
        '--count', '-c', type=int,
        default=10, help='number of photos to be combined')
    parser.add_argument(
        '--dir', '-d', type=str,
        help='dir to fetch images from')
    parser.add_argument(
        '--offset', '-o', type=int,
        default=0, help='odd a value to all pixels')

    return parser.parse_args()


def offset_image(image, offset):
    return image + offset

def main():
    args = get_args()
    if args.dir:
        filenames = glob.glob(args.dir + "*")
    else:
        filenames = save_images(args.terms, args.count)
    new_image = average_images(filenames)
    new_image = offset_image(new_image, args.offset)
    save_image(new_image, args)
    print("Image saved in current directory.")

if __name__ == '__main__':
    main()
    
