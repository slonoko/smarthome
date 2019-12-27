# 1. docker build . -t smarthome-api:0.8
# 2. docker run -dit -p 8000:8000 smarthome-api:0.8
FROM python:latest
ADD . /app
ADD config.json /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV app_config config.json
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]