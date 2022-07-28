# ColorGenAPI

## Overview

| **Try it out -** [**https://colorgenapi.herokuapp.com/docs**](https://colorgenapi.herokuapp.com/docs) |

ColorGenAPI is a REST API for generating color palettes. It takes an image as a request and returns a list of colors with their hex values. The API is built with FastAPI, and can be accessed using the following endpoints:

- https://colorgenapi.herokuapp.com/upload with a POST request along with the image.

The API is used for the [ColorGenUI](https://github.com/keshavsharma25/ColorGenUI) which is deployed on Netlify (Link - [ColorGen](https://colorgen-ai.netlify.app)).

The [route.py](route/route.py) contains the endpoints for the API and the [palette_gen.py](model\palette_gen.py) contains the KMeans model which helps in creating the hex colors.

The docker instance of the same can be created using the following command after cloning the repository:

```bash
docker-compose build
docker-compose up -d
```
