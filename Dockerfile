FROM debian

RUN apt-get update && apt-get install -y python-pip python-dev libjpeg-dev zlib1g-dev

ADD . /src
WORKDIR /src

RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
