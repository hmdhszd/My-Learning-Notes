
▶ docker node update --label-add dmz=true node1
node1




▶ docker service create --name dmz-nginx --constraint node.labels.dmz==true --replicas 2 nginx
s80483f91r08cefre43h4ncio
overall progress: 2 out of 2 tasks 
1/2: running   
2/2: running   
verify: Service converged 





▶ docker service ps dmz-nginx
ID             NAME          IMAGE          NODE      DESIRED STATE   CURRENT STATE            ERROR     PORTS
bvp1g8t5pir7   dmz-nginx.1   nginx:latest   node1     Running         Running 15 seconds ago             
7g0hlyxsv6kz   dmz-nginx.2   nginx:latest   node1     Running         Running 15 seconds ago             
