FROM python:3.9-alpine

RUN mkdir /web-app

WORKDIR /web-app

ADD requirements.txt /web-app

ADD app.py /web-app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
