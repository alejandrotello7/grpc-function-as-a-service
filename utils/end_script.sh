#!/bin/bash

# Define the Docker image name
IMAGE_NAME="my-grpc-server"

# Find and stop all containers based on the specified image name
container_ids=$(docker ps -q --filter "ancestor=$IMAGE_NAME")

if [ -z "$container_ids" ]; then
  echo "No containers found based on image $IMAGE_NAME."
else
  echo "Stopping containers based on image $IMAGE_NAME..."
  docker stop $container_ids
  echo "Containers stopped."
fi
