FROM ubuntu:22.04

# alternative for mpich: openmpi-bin / openmpi-dev \
RUN apt-get update -y && apt-get install -y \
    git \
    hdf5-tools \
    libboost-dev \
    libboost-serialization-dev \
    libboost-test-dev \
    mpich \
    python3 \
    python3-pip \
    # scons \ # is installed from pip below!
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir scons

RUN git clone https://github.com/SGpp/DisCoTec.git

WORKDIR ./DisCoTec
RUN ls -l ./distributedcombigrid/tests/
# compile DisCoTec
# ...along the lines of
# RUN . ./compile.sh
RUN scons -j 8 ISGENE=0 VERBOSE=1 COMPILE_BOOST_TESTS=1 RUN_BOOST_TESTS=0 RUN_CPPLINT=0 BUILD_STATICLIB=0 CC=mpicc.mpich FC=mpifort.mpich CXX=mpicxx.mpich OPT=1 TIMING=0 UNIFORMDECOMPOSITION=1 ENABLEFT=0 DEBUG_OUTPUT=0

RUN ls -l ./lib/sgpp/
RUN ls -l ./distributedcombigrid/tests/

ENV LD_LIBRARY_PATH=$(pwd)/lib/sgpp:$(pwd)/glpk/lib:$LD_LIBRARY_PATH

# run DisCoTec tests explicitly, with mpi
WORKDIR ./distributedcombigrid/tests/
ENTRYPOINT mpiexec.mpich -np 9 ./test_distributedcombigrid_boost
