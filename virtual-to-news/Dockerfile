FROM python:3.8.15-slim

WORKDIR /vtn

ADD . /vtn

RUN pip install -r requirements.txt

CMD ["python", "virtual-to-news-server.py"]