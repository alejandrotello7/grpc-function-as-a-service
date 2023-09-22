#!/bin/bash

# Pull the alpine/socat:latest Docker image
docker pull alpine/socat:latest

# Set the desired port number
PORT_NUMBER=50051

# Run the Docker container with socat
docker run -d -p $PORT_NUMBER:$PORT_NUMBER --name socat_$PORT_NUMBER alpine/socat tcp-listen:$PORT_NUMBER,fork,keepalive,reuseaddr vsock-connect:16:5000,keepalive

