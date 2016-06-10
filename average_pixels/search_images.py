import requests
import urllib

from api_key import API_KEY

from IPython import embed as qq

URL = "https://bingapis.azure-api.net/api/v5/images/search"
NUMBER_OF_IMAGES = 10
DIR = "img"

def search_images(term):
    params = {"q": term, "count":NUMBER_OF_IMAGES}
    headers = {'ocp-apim-subscription-key': API_KEY}
    response = requests.request("GET", URL,
                                headers=headers,
                                params=params)

    return response.json()['value']

def download_image(url, filename):
    urllib.request.urlretrieve(url, filename)

def save_images(term):
    images = search_images(term)
    for i, img in enumerate(images):
        name = "{path}/{filename}.{ext}".format(
                path=DIR,
                filename=term + str(i),
                ext=img['encodingFormat'])
        download_image(img['contentUrl'], name)
