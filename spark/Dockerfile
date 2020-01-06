FROM openjdk:8-alpine
COPY --from=python:3.7-alpine / /
COPY --from=alpine/git:latest / /
COPY --from=maven:slim / /
ADD *.py /app/
ADD requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python","spark_init.py"]
EXPOSE 4040