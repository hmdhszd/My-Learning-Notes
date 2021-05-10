▶ docker build -t my-node-volume .

Sending build context to Docker daemon  11.78kB
Step 1/7 : FROM node:14
 ---> d6602e31594f
Step 2/7 : WORKDIR /app
 ---> Using cache
 ---> bf44009d292f
Step 3/7 : COPY package.json .
 ---> Using cache
 ---> 621ea50b63c0
Step 4/7 : RUN npm install
 ---> Using cache
 ---> 753e5a922571
Step 5/7 : COPY . .
 ---> b993ce88013e
Step 6/7 : EXPOSE 80
 ---> Running in 3d335d256005
Removing intermediate container 3d335d256005
 ---> f58f076a9fb2
Step 7/7 : CMD [ "node","server.js" ]
 ---> Running in 096f403390a0
Removing intermediate container 096f403390a0
 ---> 441acbdf8adc
Successfully built 441acbdf8adc
Successfully tagged my-node-volume:latest






▶  docker run -d -p 3000:80 --name node-feedback-volume -v "/home/hamid/Documents/My-Learning-Notes/Docker/volumes in dockerizing a Node.js app/:/app" -v /app/node_modules   my-node-volume

58815ce5b9bfb13e99a8df6dd30fb592753a9db0d7bf613c31c2eeaf2a6d6d51





 
▶ docker volume ls

DRIVER    VOLUME NAME
local     feedback-volume-in-host





 
▶ docker ps

CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS                                   NAMES
58815ce5b9bf   my-node-volume   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:3000->80/tcp, :::3000->80/tcp   node-feedback-volume