FROM ubuntu:22.04

# alternative for mpich: openmpi-bin / openmpi-dev \
RUN apt-get update -y && apt-get install -y \
    git \
    hdf5-tools \
    libboost-dev \
    mpich \
    python3 \
    scons \
    && rm -rf /var/lib/apt/lists/*


# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir distutils


RUN git clone https://github.com/SGpp/DisCoTec.git
WORKDIR ./DisCoTec
RUN . ./compile.sh
WORKDIR ./distributedcombigrid/tests/
CMD mpiexec.mpich -n 9 ./test_distributedcombigrid_boost