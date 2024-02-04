FROM node:lts-alpine

RUN mkdir /app
WORKDIR /app

COPY package*.json /app/
RUN npm install

COPY . /app/

#RUN mv /app/docker/env /app/.env.production && npm run build
RUN mv /app/docker/env /app/.env.production && npm run build
RUN chmod +x  /app/docker/replace-vars.sh
RUN /app/docker/replace-vars.sh
#COPY /app/dist /static
