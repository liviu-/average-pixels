#!/usr/bin/env python3

import os
import sys
import shutil

import numpy as np
import scipy.misc

from .get_images import save_images
from .parse_args import get_args
from . import SAVE_DIR


WIDTH = 500
HEIGHT = 500
EXTENSION = "jpg"
MAX_INTENSITY = 255
OUTPUT_DEFAULT = 'output'
IMAGE_EXTENSIONS = ('jpg', 'jpeg', 'png')


def average_images(filenames, weighted=True):
    images = []
    for filename in filenames:
        try:
            images.append(scipy.misc.imread(filename, mode="RGB"))
        # Some images are corrupted
        except OSError:
            pass
    if not images:
        sys.exit('No images found in the directory')
    resized_images = resize_images(images)
    weights = np.random.dirichlet(np.ones(len(resized_images))) if weighted else None
    return np.average(resized_images, axis=0, weights=weights)


def resize_images(images):
    return [scipy.misc.imresize(img, (WIDTH, HEIGHT)) for img in images if img.shape]


def save_image(new_image, args):
    output = args.output or '_'.join(args.terms.split()) or OUTPUT_DEFAULT
    filename = '{output_filename}.{ext}'.format(
        output_filename=output,
        ext=EXTENSION)
    scipy.misc.imsave(filename, new_image)
    return filename


def offset_image(image, offset):
    return np.clip(image + offset, 0, MAX_INTENSITY)


def delete_images():
    try:
        shutil.rmtree(SAVE_DIR)
    except FileNotFoundError:
        pass


def get_local_files(directory):
    """Return only files that may be images

    Only checks for extension -- no magic.

    Yields:
        str: path to an image
    """
    try:
        dir_contents = os.listdir(directory)
    except FileNotFoundError:
        sys.exit('Directory not found')
    except NotADirectoryError:
        sys.exit('Argument provided is not a directory')

    for f in dir_contents:
        if f.lower().endswith(IMAGE_EXTENSIONS):
            yield os.path.join(directory, f)


def main():
    args = get_args()
    if args.mode == 'local':
        filenames = get_local_files(args.dir)
    else:
        filenames = save_images(args.terms, args.count)
    new_image = average_images(filenames, args.weighted)
    new_image = offset_image(new_image, args.offset)
    filename = save_image(new_image, args)
    delete_images()
    print("{} saved in current directory.".format(filename))

if __name__ == '__main__':
    main()
