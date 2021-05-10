
▶  docker network create favorites-net


▶ docker network ls
NETWORK ID     NAME            DRIVER    SCOPE
76a1a0eb6dae   bridge          bridge    local
e31e27cd6f48   favorites-net   bridge    local









▶  docker run --name mongodb -d  --rm --network favorites-net mongo


▶ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS       NAMES
d732488aadd7   mongo     "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds   27017/tcp   mongodb









the use the name (mongodb) of mongodb container in our nodejs program

mongoose.connect(
  'mongodb://mongodb:27017/swfavorites',
  { useNewUrlParser: true },









build and run nodejs container:


▶  docker build -t favorites-node .










▶  docker run --name favorites -d --rm --network favorites-net -p 3000:3000  favorites-node


CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS                                       NAMES
ebb961ff6716   favorites-node   "docker-entrypoint.s…"   4 seconds ago        Up 2 seconds        0.0.0.0:3000->3000/tcp, :::3000->3000/tcp   favorites
d732488aadd7   mongo            "docker-entrypoint.s…"   About a minute ago   Up About a minute   27017/tcp                                   mongodb







▶  docker 