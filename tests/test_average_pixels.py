import os
import glob

import pytest

from average_pixels import average_pixels as ap
from average_pixels import get_images
from average_pixels import SAVE_DIR
from average_pixels.average_pixels import WIDTH, HEIGHT, MAX_INTENSITY


SAVE_DIR_TEST = SAVE_DIR + '_test'


def download_images(term='anything', count=10):
    return ap.save_images(term, count)


filenames = glob.glob(SAVE_DIR_TEST + "/*") if os.path.exists(SAVE_DIR_TEST) else download_images()
image = ap.average_images(filenames)


def test_default_average_images_size():
    assert WIDTH, HEIGHT == ap.average_images(filenames).shape


def test_modified_average_images_size():
    global WIDTH
    global HEIGHT
    WIDTH += 100
    HEIGHT += 100
    assert WIDTH, HEIGHT == ap.average_images(filenames).shape


def test_modified_average_images_size_not_square():
    global WIDTH
    global HEIGHT
    WIDTH -= 100
    assert WIDTH, HEIGHT == ap.average_images(filenames).shape


def test_offset_image_over_max_intensity():
    new_intensity = MAX_INTENSITY + 100
    assert ap.offset_image(image, new_intensity).max() <= MAX_INTENSITY

