FROM ubuntu:focal

RUN apt update -y && apt install -y python3 && apt install -y pip
RUN pip install numpy && pip install matplotlib && pip install scipy
WORKDIR /app
COPY CalcPermeability.py .
CMD ["python3", "CalcPermeability.py"]
