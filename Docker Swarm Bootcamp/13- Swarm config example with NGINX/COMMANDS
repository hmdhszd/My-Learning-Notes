





▶ docker stack deploy -c example-voting-app-stack.yml vote
Creating network vote_backend
Creating network vote_frontend
Creating service vote_vote
Creating service vote_result
Creating service vote_worker
Creating service vote_redis
Creating service vote_db





▶ docker config create vote-nginx-v1 ./nginx-app.conf
sfbtcl6n0j8wsgefd16dv9nf1





▶ docker config ls
ID                          NAME            CREATED          UPDATED
sfbtcl6n0j8wsgefd16dv9nf1   vote-nginx-v1   14 seconds ago   14 seconds ago






▶ docker service create --config source=vote-nginx-v1,target=/nginx/conf.d/default.conf -p 9000:80 --network vote_frontend --name proxy nginx
q9zrcahv3z2i0jk57dapo3qj3
overall progress: 1 out of 1 tasks 
1/1: running   
verify: Service converged 








---------------------------------------------------------------






update the config:





▶ docker config create vote-nginx-v2 ./nginx-app.conf        
z1nz4s04h9j595k7ua2ly06jc





▶ docker service update --config-rm vote-nginx-v1 --config-add source=vote-nginx-v2,target=/nginx/conf.d/default.conf proxy
proxy
overall progress: 1 out of 1 tasks 
1/1: running   
verify: Service converged




