version: "3.1"
services:
  db:
    images: mysql:5.7
    deploy:
      placement:
        constraints:
          - node.labels.disk == ssd



-----------------------------------



node attribute			matches						example
node.id					Node ID						node.id==2ivku8v2gvtg4
node.hostname			Node hostname				node.hostname!=node-2
node.role				Node role (manager/worker)	node.role==manager
node.platform.os		Node operating system		node.platform.os==windows
node.platform.arch		Node architecture			node.platform.arch==x86_64
node.labels				User-defined node labels	node.labels.security==high
engine.labels			Docker Engine’s labels		engine.labels.operatingsystem==ubuntu-14.04