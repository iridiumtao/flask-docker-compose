FROM python:3.8.15-slim

WORKDIR /visual

ADD . /visual

RUN pip install -r requirements.txt

CMD ["python", "visual-generating-server.py"]