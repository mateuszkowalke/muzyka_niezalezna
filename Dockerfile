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
RUN apt-get install -y nodejs
RUN apt-get install -y npm

# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv==2018.11.26

# Install project dependencies
RUN pipenv install --skip-lock --system --dev
WORKDIR /app/frontend
RUN npm install
RUN (npm run dev&)
WORKDIR /app/frontend/static/frontend
RUN (sass --watch styles.scss:styles.css --style compressed&)


WORKDIR /app
EXPOSE 8000
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000
# for production use:
# gunicorn muzyka_niezalezna.wsgi:application --bind 0.0.0.0:8000