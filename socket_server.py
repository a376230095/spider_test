import socket
server=socket.socket()
server.bind(("0.0.0.0",8000))
server.listen()
sock,addr=server.accept()
data=""
while True:
    sock.send("welcome to server!".encode("utf8"))
    #recv方法是阻塞的
    tmp_data=sock.recv(1024).decode("utf8")
    print(tmp_data)
    input_date=input()
    sock.send(input_date.encode("utf8"))

    # if tmp_data:
    #     data+=tmp_data
    #     if tmp_data.endswith("#"):
    #         break
    # else:
    #     break
print(data)
server.close()