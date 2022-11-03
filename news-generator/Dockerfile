FROM python:3.8.15-slim

WORKDIR /news

ADD . /news

RUN pip install -r requirements.txt

CMD ["python", "news-generating-server.py"]