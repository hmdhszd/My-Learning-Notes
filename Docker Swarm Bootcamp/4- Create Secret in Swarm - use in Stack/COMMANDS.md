




▶ docker stack deploy -c docker-compose.yml mydb

Creating network mydb_default
Creating secret mydb_psql_user
Creating secret mydb_psql_password
Creating service mydb_psql






▶ docker secret ls

ID                          NAME                 DRIVER    CREATED          UPDATED
dlndhhewthnew1aoqgmbqebxd   mydb_psql_password             26 seconds ago   26 seconds ago
hw3a2bfk415u1up43i4qr0yan   mydb_psql_user                 26 seconds ago   26 seconds ago






▶ docker service ls

ID             NAME        MODE         REPLICAS   IMAGE             PORTS
hcqg3plp20f5   mydb_psql   replicated   1/1        postgres:latest  








--------------------------------------------------------------------------------







▶ docker stack rm mydb 
Removing service mydb_psql
Removing secret mydb_psql_password
Removing secret mydb_psql_user
Removing network mydb_default





▶ docker secret ls           
ID        NAME      DRIVER    CREATED   UPDATED





▶ docker service ls          
ID        NAME      MODE      REPLICAS   IMAGE     PORTS

