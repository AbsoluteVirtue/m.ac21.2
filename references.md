# OAuth
https://aaronparecki.com/oauth-2-simplified/
https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2

https://redis.com/blog/json-web-tokens-jwt-are-dangerous-for-user-sessions/
https://betterprogramming.pub/stop-using-json-web-tokens-for-authentication-use-stateful-sessions-instead-c0a803931a5d
- store stateful session tokens (like a UUID string) in HTTP-Only Cookies
- set HTTP-only, and the Secure flag to true (the browser won't put the cookie if the request is not HTTPS)
- Same-Site flag should be set to "strict"
- GET requests should only retrieve data
- using an Anti-CSRF Token ensures the server can verify the POST request sent by the client originated from the actual website

1. When the user clicks the sign-in button, a request is sent to the server to verify the user's credential using the database.
2. The server creates a token (UUID), maps it to the user's database ID, and stores it.
3. The server attaches the Cookie to the HTTP response sent to the browser.
4. The browser sends a GET request to the server endpoint that handles user session data. Since the Cookie provides the server with this info, this request requires no parameters.
5. The front-end can now store the session data in the application without keeping the actual Token.
6. The HTTP-Only Cookie is sent automatically on every request. The Token will be valid until it expires. However, the server can revoke it on demand.
7. Refresh Tokens.

    Auth tokens can then be short-lived, for example, 1–2 days. The browser will constantly be checking while the user is actively using their sessions to see if the auth token expires soon. When it detects this, it uses the refresh token, with has a longer-lived expiration, to request a new auth token before the previous one expires.

https://aliev.me/aioauth/
https://github.com/aliev/aioauth-fastapi/tree/master/aioauth_fastapi_demo

https://developers.google.com/identity/protocols/oauth2

# Security
https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
https://pages.nist.gov/800-63-3/sp800-63b.html

# Docker
https://docs.docker.com/ci-cd/best-practices/
https://code.visualstudio.com/docs/containers/quickstart-python

Dockerfile example:

    FROM alpine
    CMD ["echo", "Hello World!!"]

https://docs.rancherdesktop.io/tutorials/working-with-images

    docker build -t TAG .

if TAG = "expressapp:v1.0", launch Kubernetes cluster manager:

    kubectl run --image expressapp:v1.0 expressapp
    kubectl port-forward pods/expressapp 3000:3000

    docker run -d -p 8080:80 nginx

then: "http://localhost:8080/"

-d "detached"
-p "port binding"
for more flags: https://docs.docker.com/engine/reference/commandline/run/

    docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

to remove image:

    docker rmi IMAGE

    docker run -it --rm alpine

    docker build -t helloworld:v1.0 .
    docker images | grep helloworld
    docker run --rm helloworld:v1.0
    docker rmi helloworld:v1.0 #To remove the image

---

    mkdir ../nginx
    cd ../nginx
    echo "<h1>Hello World from NGINX!!</h1>" > index.html

    FROM nginx:alpine
    COPY . /usr/share/nginx/html

    docker build -t nginx-helloworld:v1.0 .
    docker images | grep nginx-helloworld
    docker run -d -p 8080:80 --name my-site nginx-helloworld:v1.0

    docker stop <container-id>
    docker rm <container-id>

or

    docker rm -f <container-id>

where: -f "force stop"

    docker ps   # to verify nothing is running 
    docker rmi nginx-helloworld:v1.0 # to remove the image

    docker run -d ubuntu bash -c "shuf -i 1-10000 -n 1 -o /data.txt && tail -f /dev/null"
    docker exec <container-id> cat /data.txt

    docker scan getting-started

    docker image history (--no-trunc) getting-started

--no-trunc is optional

# Testing
curl -d '{"username":"value1", "email":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:2022/user

# MongoDB
1. Register mongodb repo

    wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

or prereq: sudo apt-get install gnupg

2. Create Ubuntu list file

    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

3. Reload system package database

    sudo apt-get update

4. Install 

    sudo apt-get install -y mongodb-org

5. Run service

check system init process: ps --no-headers -o comm 1 

    sudo systemctl start mongod

in case of error reload service: sudo systemctl daemon-reload

check status: sudo systemctl status mongod

6. Stop service

    sudo systemctl stop mongod

7. Restart service

    sudo systemctl restart mongod

8. Mongo shell
https://www.mongodb.com/docs/mongodb-shell/run-commands/

    mongosh

 equivalent to: mongosh "mongodb://localhost:27017"

 To specify port:

    mongosh --port 28015

To connect remotely:

    mongosh "mongodb://mongodb0.example.com:28015"

or

    mongosh --host mongodb0.example.com --port 28015

Authentication:

    mongosh "mongodb://mongodb0.example.com:28015" --username alice --authenticationDatabase admin

Create DB:

    use pis_auth
