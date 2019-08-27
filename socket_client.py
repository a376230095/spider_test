import socket
client=socket.socket()
client.connect(("192.168.66.158",8000))
server_data = client.recv(1024)
print("server_date: {}".format(server_data.decode("utf8")))
while True:
    input_str=input()
    #if input_str!="q":
    client.send(input_str.encode("utf8"))
    server_data=client.recv(1024)
    print("server_date: {}".format(server_data.decode("utf8")))
#client.close()