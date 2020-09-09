# Base Image
FROM python:3.8

# create and set working directory and environment
WORKDIR /app
ENV PYTHONUNBUFFERED 1
RUN pip3 install pipenv==2018.11.26
ADD Pipfile /app
RUN pipenv install --skip-lock --system --dev

# Add current directory code to working directory
ADD . /app

EXPOSE 8000