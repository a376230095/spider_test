#http服务器

import socket
import json
import threading
server=socket.socket()
server.bind(('0.0.0.0',8000))
server.listen()


def handle_sock(sock,addr):
    while True:
        # recv方法是阻塞的
        tmp_data = sock.recv(1024)
        print(tmp_data.decode("utf8"))
        response_template='''HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin:http://localhost:63342

{}

'''
        data = [
            {
                "name":"django打造在线教育",
                "teacher":"bobby",
                "url":"https://coding.imooc.com/class/78.html_test"
            },
            {
                "name": "python高级编程",
                "teacher": "bobby",
                "url": "https://coding.imooc.com/class/200.html_test"
            },
            {
                "name": "scrapy分布式爬虫",
                "teacher": "bobby",
                "url": "https://coding.imooc.com/class/92.html_test"
            },
            {
                "name": "django rest framework打造生鲜电商",
                "teacher": "bobby",
                "url": "https://coding.imooc.com/class/131.html_test"
            },
            {
                "name": "tornado从入门到精通",
                "teacher": "bobby",
                "url": "https://coding.imooc.com/class/290.html_test"
            },
        ]
        sock.send(response_template.format(json.dumps(data)).encode("utf8"))
        sock.close()
        break

while True:
    sock,addr=server.accept()
    client_thread=threading.Thread(target=handle_sock,args=(sock,addr))
    client_thread.start()