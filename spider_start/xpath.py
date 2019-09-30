from scrapy import Selector

html='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>bobby基本信息</title>
</head>
<body>
    <div id="info">
        <p style="color: blue">讲师信息</p>
        <div class="teacher_info info">
            python全栈工程师，7年工作经验，喜欢钻研python技术，对爬虫、
            web开发以及机器学习有浓厚的兴趣，关注前沿技术以及发展趋势。
            <p class="age">年龄: 29</p>
            <p class="name">姓名: bobby</p>
            <p class="work_years">工作年限: 7年</p>
            <p class="position">职位: python开发工程师</p>
        </div>
        <p style="color: aquamarine">课程信息</p>
        <table class="courses">
          <tr>
            <th>课程名</th>
            <th>讲师</th>
            <th>地址</th>
          </tr>
          <tr>
            <td>django打造在线教育</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/78.html">访问</a></td>
          </tr>
          <tr>
            <td>python高级编程</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/200.html">访问</a></td>
          </tr>
          <tr>
            <td>scrapy分布式爬虫</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/92.html">访问</a></td>
          </tr>
          <tr>
            <td>django rest framework打造生鲜电商</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/131.html">访问</a></td>
          </tr>
          <tr>
            <td>tornado从入门到精通</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/290.html">访问</a></td>
          </tr>
        </table>
    </div>

</body>
</html>
'''
#xpath定位一个tap并不是唯一的，可以用很多xpath定位一个tap

#获取一个html的xpath
sel=Selector(text=html)

#xpath是让整个tap都是可配置的
#因为tap可能会随时变，这样通过改变量，方便管理
age_name_xpath="//div[1]/div/p[1]/text()"
age_name_tap=sel.xpath(age_name_xpath).extract()
#加个if是防止报错
if age_name_tap:
    name=age_name_xpath[0]

#使用class时，需要把全部的class都包含了才行
teacher_tap=sel.xpath("//div[@class='teacher_info info']/p/text()").extract()[0]

#可以使用contains方法
teacher_tap=sel.xpath("//div[contains(@class,'teacher_info')]/p/text()").extract()[0]

#找到class元素,用@class
teacher_class=sel.xpath("//div[contains(@class,'teacher_info')]/@class").extract()[0]
print(teacher_class)

#用或 | 找到两个tap
teacher_info=sel.xpath("//p[@class='age'] | //p[@class='name']").extract()
print(teacher_info)


#获取一个tag，sel.xptah是获取一个tap列表，因为可能定位的tap是多个
#text()是获取直接获取文字
#extract是把抽象的xpath变成一个不抽象的列表，[0]就是把列表转化成string
#tag=sel.xpath("//div[1]/div/p[1]/text()").extract()[0]


