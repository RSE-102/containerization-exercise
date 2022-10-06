# CalcPermeability Container image

With this Python script the intrinsic permeability of a sample with given grain size distribution can be calculated. There are multiple empirical and semi-empirical approaches available dependent on the soil type.

## Build the docker image

Clone this repository and create the the docker-image for this application with:
`docker build --tag calcperm_dockerimage`

## Run the docker image
To run the image use:
`docker run -it calcperm_dockerimage`

If you want to not run the container, but go into it do:
`docker run -it calcperm_dockerimage /bin/bash `
There you can run the script with:
`python3 CalcPermeability.py`

## Exit and rerun
To exit the container after work is done just do:
`exit`

If you want to restart the container do:
`docker container ls -a`
to get the ID of the container. Then do:
`docker start CONTAINERID && docker attach CONTAINERID`