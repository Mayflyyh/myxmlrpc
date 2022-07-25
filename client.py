import myrpc.client

server = myrpc.client.ServerProxy('http://127.0.0.1:8000')

a = server.rand(100,100)
b = server.rand(100,100)

print(server.add(1,2))
print(server.add(a,b))

