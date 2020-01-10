# base image
FROM node:slim

COPY . /app
# set working directory
WORKDIR /app

# install and cache app dependencies
RUN npm install

EXPOSE 3000
CMD ["npm", "start"]