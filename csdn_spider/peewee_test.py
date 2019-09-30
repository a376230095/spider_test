from peewee import *
from datetime import date
#创建一个连接的数据库
db=MySQLDatabase("spider",host="127.0.0.1",port=3306,user="root",password="")

#创建一个表Person
class Person(Model):
    #字段name是char类型，id也是char，生日是date类型
    name=CharField(max_length=20)
    id=CharField
    birthday=DateField()

    class Meta:
        database=db #this model users the "pepople.db" database
        # table_name = "users"


if __name__ == "__main__":
    print()
    #真正创建一个表Person
    #db.create_tables([Person])

    #生成数据
    #uncle_bob = Person(name='BoB',birthday=date(1961,1,15))
    #uncle_bob.save() #bob is now stored

    #这个只能获取单条数据，两种写法都ok,如果获取不到信息会抛出异常
    #相当于select * from person where name='BoB'
    #grandma = Person.select().where(Person.name == 'BoB').get()
    #grandma = Person.get(Person.name == 'BoB')
    #print(grandma.birthday)

    #这里少了一个get，会获取全部行的信息
    #query =Person.select().where(Person.name == 'BoB')
    #for pet in query:
        #print(pet.birthday)

    #虽然query并不是列表，但支持切片的操作方式
    #query = Person.select().where(Person.name == 'BoB')[0]
    #print(query.birthday)

    #修改数据
    #第一步先获取值
    #query = Person.select().where(Person.name == 'BoB')
    #for pet in query:
        #pet.birthday=date(1992,3,6)
        #通过save方法去修改值，相当于获取人名，修改生日
        #save方法，如果之前的值存在，就修改，没有存在，就新增
        #pet.save()

    #删除数据
    # 第一步先获取值
    #query = Person.select().where(Person.name == 'BoB')
    #for pet in query:
    #    pet.delete_instance()









