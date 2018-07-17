FROM python:3.6-alpine
MAINTAINER Rushal Verma<rusrushal13@gmail.com>
COPY . /app
WORKDIR /app
CMD python GameOfLife.py && cat output.txt