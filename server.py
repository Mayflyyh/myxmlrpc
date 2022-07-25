from myrpc.server import SimpleXMLRPCServer
from myrpc.server import SimpleXMLRPCRequestHandler
from socketserver import ThreadingMixIn
import torch

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_introspection_functions()
        self.register_function(self.quit)
    def quit(self):
        self._BaseServer__shutdown_request = True
        return 0

# Create server
with ThreadXMLRPCServer(('0.0.0.0', 8000),
                        requestHandler=RequestHandler) as server:
    
    for funcs in torch.__all__ :
        if(hasattr(getattr(torch,funcs),"__name__")):
            server.register_function(getattr(torch,funcs))
    
    
    def adder_function(x, y):
        return x + y
    def echo(x):
        return x

    server.register_function(adder_function)
    server.register_function(adder_function,"echo")

    class MyFuncs:
        def mul(self, x, y):
            return x * y

    server.register_instance(MyFuncs())

    server.serve_forever()
    
    print("close")