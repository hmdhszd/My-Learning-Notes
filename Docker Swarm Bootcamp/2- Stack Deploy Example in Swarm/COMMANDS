

▶ docker stack deploy -c example-voting-app-stack.yml voteapp
Creating network voteapp_frontend
Creating network voteapp_backend
Creating config voteapp_redis-healthcheck
Creating config voteapp_postgres-healthcheck
Creating service voteapp_result
Creating service voteapp_worker
Creating service voteapp_redis
Creating service voteapp_db
Creating service voteapp_vote





▶ docker stack ls
NAME      SERVICES   ORCHESTRATOR
voteapp   5          Swarm





▶ docker stack ps voteapp 
ID             NAME               IMAGE                                       NODE      DESIRED STATE   CURRENT STATE                  ERROR     PORTS
ncjvl2swfmc8   voteapp_db.1       postgres:9.6                                hamid     Running         Preparing about a minute ago             
tbst3nf9z12m   voteapp_redis.1    redis:latest                                node1     Running         Preparing about a minute ago             
nre94ravfb06   voteapp_result.1   bretfisher/examplevotingapp_result:latest   node1     Running         Preparing about a minute ago             
vxb7o2yfo68q   voteapp_vote.1     bretfisher/examplevotingapp_vote:latest     hamid     Running         Preparing 56 seconds ago                 
66ejckvhu2z5   voteapp_worker.1   bretfisher/examplevotingapp_worker:latest   node1     Running         Preparing about a minute ago             
nrfr0jlvz7fk   voteapp_worker.2   bretfisher/examplevotingapp_worker:latest   hamid     Running         Preparing about a minute ago             





▶ docker stack services voteapp
ID             NAME             MODE         REPLICAS   IMAGE                                       PORTS
thrpw2ebgx69   voteapp_db       replicated   1/1        postgres:9.6                                
vv8dr49mhfj5   voteapp_redis    replicated   1/1        redis:latest                                
ca4cm3wlrbt0   voteapp_result   replicated   1/1        bretfisher/examplevotingapp_result:latest   *:5001->80/tcp
ikaipsmemkn7   voteapp_vote     replicated   1/1        bretfisher/examplevotingapp_vote:latest     *:5000->80/tcp
n1kwop2bmk3o   voteapp_worker   replicated   2/2        bretfisher/examplevotingapp_worker:latest  







