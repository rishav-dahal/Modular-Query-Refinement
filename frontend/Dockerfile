FROM node:22-bullseye

WORKDIR /frontend

COPY package*.json ./

RUN npm install --legacy-peer-deps

COPY . .

RUN npm run build 




 