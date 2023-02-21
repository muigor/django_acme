FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code 
COPY requirements.txt /code/
#RUN python -m pip install django-cors-headers
RUN pip install -r requirements.txt
RUN pip install psycopg2==2.8.6
COPY . /code/