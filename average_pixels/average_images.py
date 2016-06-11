import glob
import argparse

import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

from get_images import save_images

from IPython import embed as qq

WIDTH = 500
HEIGHT = 500
EXTENSION = "JPEG"
DIR = "outputs"

def average_images(filenames):
    images = [cv2.imread(filename).astype('float')
              for filename in filenames]
    resized_images = resize_images(images)
    return np.mean(resized_images, axis=0)

def resize_images(images):
    return [scipy.misc.imresize(img, (WIDTH, HEIGHT)) for img in images]


def get_args():
    parser = argparse.ArgumentParser(
        description="Average multiple images")
    parser.add_argument(
            "terms", type=str,
            help="Keywords for images to search for")

    return parser.parse_args()

def save_image(new_image, args):
    scipy.misc.imsave("{save_dir}/{output_filename}.{ext}".format(
            save_dir=DIR,
            output_filename='_'.join(args.terms.split()),
            ext=EXTENSION),
        new_image)


def main():
    args = get_args()
    filenames = save_images(args.terms)
    new_image = average_images(filenames)
    save_image(new_image, args)
    print("Image saved in {}.".format(DIR))

if __name__ == '__main__':
    main()
    
