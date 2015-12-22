FROM debian

RUN apt-get update && apt-get install -y python-pip python-dev libjpeg-dev zlib1g-dev
RUN apt-get install -y ruby-full
RUN gem install compass

RUN pip install Django==1.6 django-mptt==0.7.4 feedparser==5.2.1 FeinCMS==1.11.3
RUN pip install Pillow==3.0.0 pytz==2015.7 South==1.0.2 wheel==0.24.0

ADD . /src
WORKDIR /src

RUN cd aw/static && compass compile

RUN python manage.py syncdb --noinput
RUN python manage.py migrate

RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '    admin@example.com', '1234')" | python manage.py shell

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
