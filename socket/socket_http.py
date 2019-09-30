#get和post的http_server
import threading
import json
import socket
http_client=socket.socket()
http_client.connect(("127.0.0.1",8000))
http_client.send("""GET /HTTP/1.1
""")


while True:
    sock,arr=http_client.accept()