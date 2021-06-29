FROM node:14-alpine
WORKDIR /frontend
COPY package.json package-lock.json /frontend/

ENV NODE_ENV=development
RUN npm install

COPY . /frontend
