docker-compose.yml:




version: "3.9"
services:
  web:
    image: nginx:alpine
    ports:
      - 8080:80
    networks:
      - net
    configs:
      - source: nginx_root_doc
        target: /usr/share/nginx/html/index.html

configs:
  nginx_root_doc:
    file: ./index.html

networks:
  net:
    driver: overlay






--------------------------------------------------------------------





▶ docker stack deploy -c docker-compose.yml apps

Creating network apps_net
Creating config apps_nginx_root_doc
Creating service apps_web






▶ curl  http://localhost:8080/

<html>
  <body>
    Hello, World!
  </body>
</html>



