import grpc
import service_pb2 as pb2
import service_pb2_grpc as pb2_grpc
import ast
from concurrent.futures import ThreadPoolExecutor  # Import ThreadPoolExecutor from concurrent.futures


# Server Implementation
class FunctionServiceServicer(pb2_grpc.FunctionServiceServicer):
    def ExecuteFunction(self, request, context):
        # Extract the code and arguments from the request
        code = request.code
        args = request.args
        output_file = open("/server_output.log", "w")

        # Execute the code dynamically
        try:
            # Parse the code
            code_module = ast.parse(code)
            # Create a namespace for the code to execute in
            code_namespace = {"__builtins__": {}}
            # Redirect stdout to the custom output file
            code_namespace["__builtins__"]["print"] = lambda *args, **kwargs: print(*args, file=output_file, **kwargs)
            # Execute the code in the created namespace
            exec(compile(code_module, '<string>', 'exec'), code_namespace)
            # Call the function
            result = code_namespace['client_function'](*args)
        except Exception as e:
            result = str(e)

        output_file.close()  # Close the custom output file
        return pb2.FunctionResponse(result=str(result))


def serve():
    executor = ThreadPoolExecutor(max_workers=10)  # Use ThreadPoolExecutor from concurrent.futures
    server = grpc.server(executor)
    pb2_grpc.add_FunctionServiceServicer_to_server(FunctionServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
