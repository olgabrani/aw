FROM debian

RUN apt-get update && apt-get install -y python-pip python-dev libjpeg-dev zlib1g-dev
RUN apt-get install -y ruby-full
RUN gem install compass

ADD . /src
WORKDIR /src

RUN cd aw/static && compass compile

RUN pip install -r requirements.txt

RUN python manage.py syncdb --noinput
RUN python manage.py migrate

RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '    admin@example.com', '1234')" | python manage.py shell

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
