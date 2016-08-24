import os
import urllib
import urllib.error
import requests

from . import SAVE_DIR

URL = 'https://bingapis.azure-api.net/api/v5/images/search'
API_FILE = '.average_pixels_api'
API_ENVIRON = 'AVERAGE_PIXELS_API'

def search_images(term, count, api_key):
    params = {"q": term, "count": count}
    headers = {'ocp-apim-subscription-key': api_key}
    response = requests.request("GET", URL,
                                headers=headers,
                                params=params)
    return response.json()['value']

def download_image(url, filename):
    urllib.request.urlretrieve(url, filename)

def get_api_key():
    try:
        api_key_file = os.path.join(
            os.path.expanduser('~'), API_FILE)
        with open(api_key_file, 'r') as f:
            api_key = f.read().replace('\n','')
    except FileNotFoundError:
        try:
            api_key = os.environ[API_ENVIRON]
        except KeyError:
            api_key = input("Please insert your API key: ")

    return api_key


def save_images(term, count):
    api_key = get_api_key()
    images = search_images(term, count, api_key)
    filenames = []

    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    for i, img in enumerate(images):
        if img['encodingFormat'] == 'unknown':
            continue
        name = "{path}/{filename}.{ext}".format(
                path=SAVE_DIR,
                filename="_".join(term.split()) + str(i),
                ext=img['encodingFormat'])
        try:
            download_image(img['thumbnailUrl'], name)
            filenames.append(name)
        except urllib.error.HTTPError:
            pass

    return filenames
