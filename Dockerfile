# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN apt-get update && \
    apt-get install -y perl socat iproute2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY utils/enclave_script.sh .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Make port 50051 available to the world outside this container
EXPOSE 50051

RUN chmod +x enclave_script.sh

# Run server.py when the container launches
CMD ["./enclave_script.sh"]