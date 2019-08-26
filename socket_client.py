import socket
client=socket.socket()
client.connect(("192.168.66.158",8000))
client.send("tongtong".encode("utf-8"))
client.close()