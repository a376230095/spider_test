import pymysql.cursors

#连接数据库的固定写法
connection =pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='spider',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        #记得非关键字都用``，不是用''，后面输入必须是%s
        sql="insert into `my_users` (`email`,`password`) values (%s,%s)"
        #需要插入的变量，后面必须是一个元祖
        cursor.execute(sql,('tong','1234'))
    #最终commit执行sql
    connection.commit()

    with connection.cursor() as cursor:
        sql = "select `id` `password` from `my_users` where `email`=%s"
        cursor.execute(sql, ('tong', ))
        result=cursor.fetchone()
        print(result)

    connection.commit()
finally:
    #关闭数据库连接
    connection.close()
