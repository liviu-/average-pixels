#!/usr/bin/env python3

import glob
import argparse
import shutil

import numpy as np
import scipy.misc

from .get_images import save_images
from . import SAVE_DIR

WIDTH = 500
HEIGHT = 500
EXTENSION = "jpg"
MAX_INTENSITY = 255


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
    output = args.output or '_'.join(args.terms.split())
    filename = '{output_filename}.{ext}'.format(
            output_filename = output,
            ext=EXTENSION)
    scipy.misc.imsave(filename, new_image)
    return filename


def get_args():
    parser = argparse.ArgumentParser( description="Average multiple images")
    subparsers = parser.add_subparsers(dest='mode',
            help='Use images from a local dir or download new images')
    subparsers.required = True

    parser_local = subparsers.add_parser('local', help='Directory to combine images from')
    parser_local.add_argument( 'dir', type=str,
        help='dir to fetch images from')

    parser_download = subparsers.add_parser('download',
            help="Keywords for images to search for and filename")
    parser_download.add_argument(
            "terms", type=str,
            help="Keywords for images to search for and filename")
    parser_download.add_argument(
        '--count', '-c', type=int,
        default=10, help='number of photos to be combined')
    parser_download.add_argument(
        '--offset', '-o', type=int,
        default=0, help='odd a value to all pixels')

    parser.add_argument(
        '--output', '-o', type=str,
        help='file to output the image to')

    return parser.parse_args()


def offset_image(image, offset):
    return np.clip(image + offset, 0, MAX_INTENSITY)

def delete_images():
    shutil.rmtree(SAVE_DIR)

def main():
    args = get_args()
    if args.mode == 'local':
        filenames = glob.glob(args.dir + "*")
    else:
        filenames = save_images(args.terms, args.count)
    new_image = average_images(filenames)
    new_image = offset_image(new_image, args.offset)
    filename = save_image(new_image, args)
    delete_images()
    print("{} saved in current directory.".format(filename))

if __name__ == '__main__':
    main()
