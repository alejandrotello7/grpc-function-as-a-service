#!/bin/bash

# Define the container name to stop
CONTAINER_NAME="my-grpc-server"

# Stop the Docker container with the specified name
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker ps
