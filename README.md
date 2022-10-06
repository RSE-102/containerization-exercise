## Dockerfile for DisCoTec

This Dockerfile installs DisCoTec's dependencies, compiles DisCoTec and its tests, and automatically runs the tests with MPI.

To install docker, consider [this guide](https://github.com/RSE-102/Lecture-Material/tree/main/05_containerization#readme).

With docker set up, you can run

```
docker build containerization-exercise/
```
to instantiate DisCoTec.