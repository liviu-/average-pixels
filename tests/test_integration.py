import os
import sys
import tempfile
from pathlib import Path
from subprocess import Popen, PIPE

from average_pixels.version import __version__


# Extract it from setup.py?
TOOL = 'average-pixels'
IMAGES_DIR = 'images'


def run_tool(args):
    p = Popen(args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = (out.decode('utf-8') for out in p.communicate())
    return p, stdout, stderr

def get_images_dir():
    return str(Path(sys.path[0]).parent / IMAGES_DIR)

def test_fails_with_help_no_args():
    p, stdout, stderr = run_tool(TOOL)
    assert p.returncode == 2
    assert 'usage:' in stderr.lower()


def test_fails_with_help_when_running_mode_no_args():
    for mode in ['download', 'local']:
        p, stdout, stderr = run_tool([TOOL, mode])
        assert p.returncode == 2
        assert 'usage:' in stderr.lower()


def test_fails_when_dir_inexistent():
    f = tempfile.TemporaryDirectory()
    os.rmdir(f.name)
    p, stdout, stderr = run_tool([TOOL, 'local', f.name])
    assert p.returncode == 1
    assert 'not found' in stderr.lower()


def test_fails_when_dir_has_no_images():
    f = tempfile.TemporaryDirectory()
    p, stdout, stderr = run_tool([TOOL, 'local', f.name])
    assert p.returncode == 1
    assert 'no images' in stderr.lower()
    os.rmdir(f.name)


def test_fails_when_dir_is_a_file():
    f = tempfile.NamedTemporaryFile()
    p, stdout, stderr = run_tool([TOOL, 'local', f.name])
    assert p.returncode == 1
    assert 'not a directory' in stderr.lower()
    os.unlink(f.name)


def test_version_displays_correctly():
    p, stdout, stderr = run_tool([TOOL, '--version'])
    assert p.returncode == 0
    assert __version__ in stdout

def test_output_filename_igores_user_extension():
    p, stdout, stderr = run_tool(
        [TOOL, 'local', get_images_dir(), '--output', 'filename.ext'])
    assert 'ext' not in stdout

def test_output_filename_adds_jpg():
    p, stdout, stderr = run_tool(
        [TOOL, 'local', get_images_dir(), '--output', 'filename.ext'])
    assert 'jpg' in stdout

