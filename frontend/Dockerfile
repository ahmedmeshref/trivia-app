FROM node:14-alpine
WORKDIR /frontend
COPY package.json package-lock.json /frontend/
ENV NODE_ENV=development
RUN npm install
#EXPOSE 3000
COPY . /frontend
#CMD ["npm", "start", "--host", "0.0.0.0", "--disable-host-check"]