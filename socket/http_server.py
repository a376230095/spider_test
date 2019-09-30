#http服务器
import json
import socket
import threading
server=socket.socket()
server.bind(('0.0.0.0',8000))
server.listen()

def http_handle(sock,addr):
    tmp_data=sock.recv(1024)
    response_template='''HTTP/1.1 200 OK

<!DOCTYPE html_test>
<html_test lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Build A web Server</title>
    </head>
    <body>
        Hello World,this is a very simple HTML doument
    </body>
</html_test>
'''
    sock.send(response_template.encode("utf8"))

if __name__=="__main__":
    sock,addr=server.accept()
    http_thread=threading.Thread(target=http_handle,args=(sock,addr))
    http_thread.start()