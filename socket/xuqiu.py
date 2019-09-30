"""
    需求：
        1.实现聊天服务器
        2.实现聊天客户的
    功能：
        1.登录
        2.退出
        3.发送信息
        4.获取离线消息
        5.获取在线用户
"""
#登录
login_template = {
    "action":"login",
    "user":"bobby1"
}
#给某个用户发送信息
send_date_template = {
    "action":"send_msg",
    "to":"user",
    "from":"user",
    "data":"i am bobby"
}
#历史消息
offline_msg_template = {
    "action":"history_msg",
    "user":"user",
}
#退出
exit_template = {
    "atcion":"exit",
    "user":"user"
}