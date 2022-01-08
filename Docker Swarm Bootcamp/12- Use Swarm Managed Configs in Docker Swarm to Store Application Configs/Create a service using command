▶ cat > index.html << EOF
<html>
  <body>
    Hello, World!
  </body>
</html>
EOF






▶ docker config create nginx_root_doc index.html
15xasf8xwuiop38j7aijs02t8






▶ docker config ls
ID                          NAME                           CREATED          UPDATED
15xasf8xwuiop38j7aijs02t8   nginx_root_doc                 24 seconds ago   24 seconds ago
odht5mplo8r143edqp5i5mcjd   voteapp_postgres-healthcheck   18 hours ago     18 hours ago
nw7feywpxevc16dcpsz7otjb3   voteapp_redis-healthcheck      18 hours ago     18 hours ago






▶ docker service create --name web \
  --config source=nginx_root_doc,target=/usr/share/nginx/html/index.html \
  --publish 8080:80 nginx:alpine

m5cpemqrt3bbdjp048kt4c5eu
overall progress: 1 out of 1 tasks 
1/1: running   
verify: Service converged 





▶ curl  http://localhost:8080/  
<html>
  <body>
    Hello, World!
  </body>
</html>
