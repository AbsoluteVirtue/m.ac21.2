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

# Testing
curl -d '{"username":"value1", "email":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:2022/user

https://medium.com/it-dead-inside/docker-containers-and-localhost-cannot-assign-requested-address-6ac7bc0d042b
https://techoverflow.net/2021/08/06/how-i-fixed-python-oserror-errno-99-cannot-assign-requested-address/
Trying to bind the specific IP address 192.168.1.100, the computer running the script did not have said IP address configured on any interface. Need to change the bind IP address to either 0.0.0.0 to listen to ANY IP address or to change it to the IP address of the host computer running the script on. For Docker containers, either you need to run them in network_mode: host to use the host’s network systemd, or you need to bind to the container’s IP address. You can not bind to the host’s IP address from the container unless using network_mode: host! But you can forward the ports from the host, binding to a specific IP address.

https://stackoverflow.com/a/64330227
This error will also appear if you try to connect to an exposed port from within a Docker container, when nothing is actively serving the port.

On a host where nothing is listening/bound to that port you'd get a No connection could be made because the target machine actively refused it error instead when making a request to a local URL that is not served, eg: localhost:5000. However, if you start a container that binds to the port, but there is no server running inside of it actually serving the port, any requests to that port on localhost will result in:

    [Errno 99] Cannot assign requested address (if called from within the container), or
    [Errno 0] Error (if called from outside of the container).

https://stackoverflow.com/a/49650286
To let other computers on the LAN connect to your service just use 0.0.0.0 address in app.run() function and expose desired port from your docker container to your host PC.

To expose port you need to

1) specify EXPOSE directive in Dockerfile

2) run container with -p <port_on_host>:<port_in_container> parameter.

For example, Dockerfile:

    FROM ubuntu:17.10

    RUN apt-get update && apt-get install -y apache2

    EXPOSE 80

    ENTRYPOINT ["/usr/sbin/apache2ctl"]
    CMD ["-D", "FOREGROUND"]

Build:

    docker build -t image_name .

Run:

    docker run -d -p 80:80 image_name

Check:

    curl http://localhost

P.S. make sure that 80 port is not used by another app on your host PC before running container. If this port is already in use - specify another port, for example 8080:

    docker run -d -p 8080:80 image_name

And then check:

    curl http://localhost:8080

https://github.com/aio-libs/aiohttp/issues/4554#issuecomment-582420968
This was the change I've done in Python. Tuple actually contains information about scope Id (4 - is the interface index of your network interface eth0). So, %eth0 is superfluous. Actually, the first tuple element should be a sequence of 16 bytes, not a string in IPv6 address form, but unfortunately, by compatibility reasons, it uses this form.

Possibly, you should use getnameinfo():

    In [16]: socket.getnameinfo(('fe80::841e:8fff:fea4:4f19', 456, 0, 3), socket.AI_NUMERICHOST)
    Out[16]: ('fe80::841e:8fff:fea4:4f19%wlp2s0', '456')

https://github.com/ray-project/ray/issues/7084#issuecomment-583805520
Does adding --webui-host 0.0.0.0 to ray start work to mitigate this? Solved it by adding

    ray.init(webui_host='127.0.0.1')
    
at the beginning of the python file. It seems like hostname '::1' or 'localhost' are sometimes not recognized.

https://support.prodi.gy/t/oserror-errno-99-cannot-assign-requested-address/89/3
We’re convinced this is a quirk of docker networking. Obviously when running these tools in production you’ll either need to bind to 0.0.0.0 or setup some kind of gateway like nginx.
