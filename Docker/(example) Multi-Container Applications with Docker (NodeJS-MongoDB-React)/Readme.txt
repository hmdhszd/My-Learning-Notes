NETWORK:


create a network to connect all containers:


docker network create goals-net


---------------------------------------------
MONGODB:


docker run --rm -d --name mongodb -v data:/data/db --network goals-net -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=secret mongo



---------------------------------------------
BACKEND:


change mongodb url in the app.js file in BACKEND:

mongoose.connect(
  `mongodb://${process.env.MONGODB_USERNAME}:${process.env.MONGODB_PASSWORD}@mongodb:27017/course-goals?authSource=admin`,





Rebuild the image after changes:

docker build -t goals-node backend/.


docker run --rm --name goals-backend -d -v "/home/hamid/Documents/My-Learning-Notes/Docker/(example) Multi-Container Applications with Docker (NodeJS-MongoDB-React)/backend/:/app" -v logs:/app/logs -v /app/node_modules --network goals-net -p 80:80 goals-node


---------------------------------------------
FRONTEND:



change src/app.js in the frontend:

      try {
        const response = await fetch('http://localhost/goals');







Rebuild the image after changes:

docker build -t goals-react frontend/.

docker run --name goals-frontend --rm  -p 3000:3000 -it goals-react




---------------------------------------------


