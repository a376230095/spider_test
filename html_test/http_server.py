#http的server
import threading
import json
import socket
server=socket.socket()
server.bind(('0.0.0.0',8000))
server.listen()

def handle_sock(sock,addr):
    while True:
        tmp_data=sock.recv(1024)
        tmp_data=tmp_data.decode("utf8")
        request_line=tmp_data.splitlines()[0]
        print("1")
        if request_line:
            method=request_line.split()[0]
            path=request_line.split()[1]
            if method=="GET":
                print("2")
                response_template='''HTTP/1.1 200 OK
Access_Control-Allow-Origin: http://localhost:63342

<!DOCTYPE html_test>
<html_test lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/" method="POST" >
    <input type="text" name="name"/>
    <input type="password" name="password">
    <input type="submit" value="登录">
</form>
</body>
</html_test>

                '''
                print(3)
                sock.send(response_template.encode("utf8"))

            elif method=="POST":
                response_template='''HTTP/1.1 200 OK
Content-Type: application/json

{}

                '''

                data = [
                    {
                        "name": "django打造在线教育",
                        "teacher": "bobby",
                        "url": "https://coding.imooc.com/class/78.html_test"
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

                break



while True:
    sock,addr=server.accept()
    server_thread=threading.Thread(target=handle_sock,args=(sock,addr))
    server_thread.start()