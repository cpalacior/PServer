import grpc
import Service_pb2
import Service_pb2_grpc
import os
from dotenv import load_dotenv
load_dotenv()


def run(file):
    print("Client active...")
    with grpc.insecure_channel(os.getenv('URL_Request')) as channel:
        stub = Service_pb2_grpc.ProductServiceStub(channel)
        response = stub.getResource(Service_pb2.Resource(resourceName=file))
    print("Greeter client received: " + response.Response)
    return response.Response
