# LW 1-4

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

# ---

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
