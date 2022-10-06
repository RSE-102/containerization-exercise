# Docker image to solve the diffusion equation in 2D

## How to build image and run the application
Build the image:

`docker build --tag diffusion2d-image .`

Instantiate a container:

`docker run -it diffusion2d-image /bin/bash`

Inside the container, run the application:

`python3 diffusion2d.py`

Then it will crate output data into files in the naming format `output[index of corresponding timestamp]`.