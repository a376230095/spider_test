#qq服务器
# 1.转发消息
# 2.处理登录
# 3.处理退出
# 4.维护历史消息，维护在线用户和维护用户的连接
import socket
from collections import defaultdict
import threading
import json

# #defaultdict的作用可以让我们随便创建一个新的字典，就算key不存在也行
# a=defaultdict(dict)
# a=dict()
# a["a"]["b"]="c"
# print(a)  #defaultdict(<class 'dict'>, {'a': {'b': 'c'}})
# b=dict()
# print(b["a"]) #这样就会报错了，因为没有默认值了

#1.维护用户连接
online_user=defaultdict(dict)

#2.维护用户的历史消息
user_msgs=defaultdict(list)
server=socket.socket()

#绑定ip
server.bind(("0.0.0.0",8000))
server.listen()

def handle_sock(sock,addr):
    pass

while True:
    #阻塞等待连接
    socket,addr =server.accept()
    #启动一个线程去处理新的用户连接
    client_threading=threading.Thread(target=handle_sock,args=(sock,addr))