# Average Pixels [![Build Status](https://travis-ci.org/liviu-/average-pixels.svg?branch=develop)](https://travis-ci.org/liviu-/average-pixels)

Command line tool which takes a bunch of images, and outputs a JPEG combining the images using a weighted average where the weights are samples drawn from the Dirichlet distribution.

## Installation

```sh
$ git clone https://github.com/liviu-/average-pixels
$ pip3 install average_pixels/
```
    
## Configuration
The application in `download` mode uses [Bing Search API](https://www.microsoft.com/cognitive-services/en-us/bing-image-search-api) to search for images so it requires the user to have an API key activated for Bing's search service. To obtain one:

- [Create a Microsoft account](https://signup.live.com/signup) if you don't have one
- Get an API key for the [Bing Image Search Service](https://www.microsoft.com/cognitive-services/en-us/bing-image-search-api)
    
    
Once obtained, the key may be provided through various methods:

- When prompted by the application
- By storing it in `~/.average_pixels_api`
- Or via the `AVERAGE_PIXELS_API` environment variable (e.g. `$ export AVERAGE_PIXELS_API=$key`)

## Example usage:

The application has 2 modes:

- `local`: Combines local files and outputs the combined image
- `download`: Takes keywords from the user, and combines images from Bing Image Search

```sh
$ average_pixels download "black cats"
```
    
![black_cats](img/black_cats.jpg)

```sh
$ average_pixels download "green field blue sky"
```
    
![green_field_blue_sky](img/green_field_blue_sky.jpg)

```sh
$ average_pixels download "just give me some random photo"
```

![just_give_me_some_random_photo](img/just_give_me_some_random_photo.jpg)

```sh
$ average_pixels download "no"
```

![no](img/no.jpg)

```sh
$ average_pixels download "insects" --count 30
```

![insects](img/insects.jpg)

```sh
$ average_pixels local /tmp/average_images --offset 40
```

![existing_dir](img/existing_dir.jpg)

```sh
$ average_pixels download "turner" --count 20
```

![turner](img/turner.jpg)

```sh
$ average_pixels download "jackson pollock painting" --count 10 --offset 30
```

![jackson_pollock](img/jackson_pollock_painting.jpg)

```sh
$ average_pixels download "green" --count 100
```

![green](img/green.jpg)

```sh
$ average_pixels local img/
```

![local_dir](img/output.jpg)

