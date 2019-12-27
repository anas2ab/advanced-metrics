FROM python:latest

RUN useradd -ms /bin/bash webapp

WORKDIR /home/webapp

COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt
RUN pip install gunicorn


COPY app app
COPY config.py private.py ./


ENV FLASK_APP app/__init__.py

RUN chown -R webapp:webapp ./

USER webapp

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
