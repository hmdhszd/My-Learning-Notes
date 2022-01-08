                                                                              
▶ docker network create --driver=overlay mydrupal

w5kqdo73xgyavvwzeskrppt0u






▶ docker network ls

NETWORK ID     NAME              DRIVER    SCOPE
cf48c2570c83   bridge            bridge    local
15ae298a3c38   docker_gwbridge   bridge    local
188758f09b6c   host              host      local
y5m8vln6qtni   ingress           overlay   swarm
w5kqdo73xgya   mydrupal          overlay   swarm
caaf36e2b595   none              null      local






▶ docker service create --name psql --network=mydrupal -e POSTGRES_PASSWORD=mypass postgres

yuf2ioa9f245t16v3zjlo1fnd
overall progress: 0 out of 1 tasks 
overall progress: 1 out of 1 tasks 
1/1: running   [==================================================>] 
verify: Service converged 





▶ docker service create --name drupal --network mydrupal -p 80:80 drupal
bffwe8iun6cvabwcixrw58guu
overall progress: 1 out of 1 tasks 
1/1: running   [==================================================>] 
verify: Service converged






▶ docker service ls        
ID             NAME      MODE         REPLICAS   IMAGE             PORTS
bffwe8iun6cv   drupal    replicated   1/1        drupal:latest     *:80->80/tcp
yuf2ioa9f245   psql      replicated   1/1        postgres:latest   





                                                                                                                                              
▶ docker service ps drupal 
ID             NAME       IMAGE           NODE      DESIRED STATE   CURRENT STATE                ERROR     PORTS
tjg4srb3fko3   drupal.1   drupal:latest   node1     Running         Running about a minute ago             





▶ docker service ps psql 
ID             NAME      IMAGE             NODE      DESIRED STATE   CURRENT STATE           ERROR     PORTS
vy3q76750iir   psql.1    postgres:latest   hamid     Running         Running 7 minutes ago             




