import grpc
import service_pb2 as pb2
import service_pb2_grpc as pb2_grpc

def run_client():
    channel = grpc.insecure_channel('ec2-18-157-185-42.eu-central-1.compute.amazonaws.com:50051')
    stub = pb2_grpc.FunctionServiceStub(channel)

    # Define the code and its arguments
    code = """
def client_function():
    print("Hello from server")
    return "Hello from client!"
"""
    args = []

    request = pb2.FunctionRequest(code=code, args=args)
    response = stub.ExecuteFunction(request)
    print("Function Result:", response.result)

if __name__ == '__main__':
    run_client()

