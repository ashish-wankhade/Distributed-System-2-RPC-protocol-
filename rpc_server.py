from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.server

PORT = 8080


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


server = SimpleXMLRPCServer(("localhost", PORT))
print(f"Listening on port {PORT} ...")

server.register_multicall_functions()
server.register_function(add, 'add')
server.register_function(sub, 'sub')
server.serve_forever()
