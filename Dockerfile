# Build Stage
FROM python:3.8-slim AS build
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime Stage
FROM python:3.8-slim
WORKDIR /app
COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY . .
RUN apt-get update && \
    apt-get install -y apt-utils socat iproute2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
EXPOSE 50051
EXPOSE 5000
CMD ["./enclave_script.sh"]
