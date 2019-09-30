from peewee import *


db=MySQLDatabase("spider",host="127.0.0.1",port=3306,user="root",password="")

class BaseModel(Model):
    class Meta:
        database = db
#设置表的注意事项
'''
char类型一般可以设置一个最大值
不知道内容多大的时候可以用text类型
设计表的时候，采集到的数据尽量先做格式化处理，比如date就是date
如果数据可能为空，先default一下，不然数据库会报错
'''


class Topic(BaseModel):
    title=CharField() #标题
    content=TextField(default="") #内容
    id=IntegerField(primary_key=True) #url的用户id
    author=CharField() #创作用户名
    create_time=DateTimeField #创建时间
    answer_nums=IntegerField(default=0) #回答数
    click_nums=IntegerField(default=0) #点击数
    parised_nums=IntegerField(default=0) #点赞数
    jtl=FloatField(default=0.0) #结帖率
    socre=IntegerField(default=0) #赏分
    status=CharField() #状态
    last_answer_time = DateTimeField()


class Answer(BaseModel):
    topic_id=IntegerField()
    authod=CharField()
    content=TextField()
    create_time=DateTimeField()
    parised_nums=IntegerField(default=0)


class Author(BaseModel):
    name=CharField()
    id = CharField(primary_key=True)
    click_nums=IntegerField(default=0)   #访问数
    original_nums=IntegerField(default=0) #原创数
    forward_nums=IntegerField(default=0)  #转发数
    rate=IntegerField(default=0)         #排名
    answer_nums=IntegerField(default=0)  #评论数
    parised_nums=IntegerField(default=0) #获赞数
    desc=TextField(null=True)
    industry=CharField(null=True)
    location=CharField(null=True)
    follower_nums=IntegerField(default=0) #粉丝数
    following_nums=IntegerField(default=0) #关注数


if __name__=="__main__":
    db.create_tables([Topic,Answer,Author])