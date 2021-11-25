FROM python:3.9

MAINTAINER Yen Le <ngocyenle08@gmail.com>

# install dependencies
RUN apt-get update -y && \
    apt-get install -y \
    unzip wget

# install chrome
RUN apt-get update -y && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# setup working directory and install requirements
WORKDIR /behave-webdriver-api
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
