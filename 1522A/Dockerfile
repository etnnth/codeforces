from ubuntu:focal-20210416 as raifml
run apt-get update && apt-get install -y \
  fish \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*
copy requirements.txt requirements.txt
run pip3 install -r requirements.txt
workdir /raifml
volume /raifml
