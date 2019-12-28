# 1. docker build . -t smarthome-webui:0.8
# 2. docker run -dit -p 80:80 -v /home/elie/Workspace/smarthome/:/config/ smarthome-webui:0.8
FROM httpd:latest
COPY ./build/ /usr/local/apache2/htdocs/
RUN chmod 755 -R /usr/local/apache2/htdocs/
EXPOSE 80