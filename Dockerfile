FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update --fix-missing
RUN apt-get install -y \
	build-essential \
	git-core \
	pkg-config \
	unzip \
	software-properties-common

RUN apt install -y gdal-bin python-gdal python3-gdal

RUN mkdir /code
WORKDIR /code
RUN mkdir /static
ADD requirements.txt /code/
RUN pip install uwsgi
RUN pip install -r requirements.txt
ADD ./infuy /code/
RUN python manage.py collectstatic --noinput