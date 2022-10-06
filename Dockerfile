FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Setup: update, install prerequisites
RUN apt-get update \
    && apt-get install --no-install-recommends --yes \
    ca-certificates \
    python3-dev \
    python3-pip \
    git \
    pkg-config \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Install numpy, matplotlib, pytest
RUN pip3 install numpy matplotlib pytest


# Clone the python testing repo
RUN cd /home \
	&& git clone https://github.com/ampdes/diffusion2D-testing-exercise.git

