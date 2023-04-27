# pull offical base image
FROM python:3.11.3-alpine

# set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip

ENV PATH="/usr/src/app:${PATH}"

# copy requirements file
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# Makemigrations and migrate
# RUN python manage.py migrate
# RUN python manage.py collectstatic

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application" ]