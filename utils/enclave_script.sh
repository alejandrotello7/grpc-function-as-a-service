#!/bin/sh
ip addr add 127.0.0.1/32 dev lo
ip link set dev lo up

HOST_PORT=5000
DOCKER_PORT=50051

# Route traffic from host port 5000 to Docker container port 50051 using vsock
socat vsock-listen:$HOST_PORT,reuseaddr,fork tcp-connect:127.0.0.1:$DOCKER_PORT &
#socat tcp-listen:$HOST_PORT,reuseaddr,fork tcp-connect:127.0.0.1:$DOCKER_PORT &

python3 server.py