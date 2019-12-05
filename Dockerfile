FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /code

# set working dir
WORKDIR /code
ADD . /code/

# system and dependencies
RUN pip install -r requirements.txt

EXPOSE 8000

#environment variables

# run server
CMD ["/code/codecamp/manage.py", "migrate", "--run-syncdb"]
CMD ["/code/codecamp/manage.py", "makemigrations"]
CMD ["/code/codecamp/manage.py", "runserver", "0.0.0.0:8000"]