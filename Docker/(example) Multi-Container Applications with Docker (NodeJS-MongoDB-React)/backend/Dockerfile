FROM node
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
EXPOSE 80
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=secret
CMD [ "npm", "start" ]
