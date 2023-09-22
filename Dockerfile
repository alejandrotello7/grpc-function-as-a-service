#Use an official Python runtime as a parent image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN apt-get update && \
    apt-get install -y apt-utils perl socat iproute2

COPY utils/enclave_script.sh .
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Make port 50051, 5000 available to the world outside this container
EXPOSE 50051
EXPOSE 5000

RUN chmod +x enclave_script.sh

# Run server.py when the container launches
CMD ["./enclave_script.sh"]