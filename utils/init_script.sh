#!/bin/bash

# Define the Docker image name
IMAGE_NAME="my-grpc-server"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Run the Docker container in detached mode (-d) and map port 50051
docker run -d -p 50051:50051 $IMAGE_NAME

docker ps -a
