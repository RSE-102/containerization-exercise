FROM ubuntu:22.04

RUN apt update -y && apt install -y neofetch
# install the basic dependencies
RUN apt update \
    && apt-get install -y \
    vim \
    python3-dev \
    python3-pip \
    git \
    pkg-config \
    build-essential \
    cmake \
    doxygen \
    wget \
    && apt clean
RUN pip install numpy matplotlib
WORKDIR /app
COPY diffusion2d.py .
CMD ["/bin/bash"]