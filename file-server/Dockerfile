FROM python:3.8.15-slim

WORKDIR /files

ADD . /files

RUN pip install -r requirements.txt

CMD ["python", "file-server.py"]