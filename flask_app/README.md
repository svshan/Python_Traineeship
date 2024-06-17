### Task reference:
https://www.freecodecamp.org/news/build-secure-apis-with-flask-and-auth0/

### Docker:
docker build -t my-python-app .
docker run -p 5001:5000 --name my-python-app my-python-app

docker stop my-python-app
docker rm my-python-app

docker ps - list all containers
docker ps -a  - list all even stopped

### Requests from the task (in Docker):
curl -i http://127.0.0.1:5001/
curl -i -H "Authorization: bearer [access token]" http://127.0.0.1:5001/user
curl -i -H "Authorization: bearer [access token]" http://127.0.0.1:5001/admin
