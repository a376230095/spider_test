import socket
server=socket.socket()
server.bind(("0.0.0.0",8000))
server.listen()
sock,addr=server.accept()
print(addr)
data=sock.recv(1024).decode("utf8")
print("----------------")
print(data)
print("----------------")
server.close()