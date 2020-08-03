# Base Image
FROM python:3.8

# create and set working directory
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# Install system dependencies
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3-pip

# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv==2018.11.26

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

EXPOSE 8000
CMD gunicorn muzyka_niezalezna.wsgi:application --bind 0.0.0.0:8000