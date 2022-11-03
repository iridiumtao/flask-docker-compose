FROM python:3.8.15-slim

WORKDIR /voice

ADD . /voice

RUN pip install -r requirements.txt

CMD ["python", "voice-generating-server.py"]