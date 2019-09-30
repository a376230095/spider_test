from bs4 import BeautifulSoup
import re
html='''
<!DOCTYPE html_test>
<html_test lang="en">
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
            <p class="name" id="hello world">姓名: bobby</p>
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
            <td><a href="https://coding.imooc.com/class/78.html_test">访问</a></td>
          </tr>
          <tr>
            <td>python高级编程</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/200.html_test">访问</a></td>
          </tr>
          <tr>
            <td>scrapy分布式爬虫</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/92.html_test">访问</a></td>
          </tr>
          <tr>
            <td>django rest framework打造生鲜电商</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/131.html_test">访问</a></td>
          </tr>
          <tr>
            <td>tornado从入门到精通</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/290.html_test">访问</a></td>
          </tr>
        </table>
    </div>

</body>
</html_test>
'''
#引擎是是使用html.parser，python的原生库
bs_html=BeautifulSoup(html,"html.parser")

#这是title的一个Tap,包含<title>bobby基本信息</title>全部的信息
#print(bs_html.title)

title=bs_html.title
#打印出text的内容
print(title.string)

#这种方式可以找到全部的div的Tap，但太蠢了
#print(bs_html.find_all("div"))

#搜索到div中，id=info的tag
#print(bs_html.find("div",id="info"))


#正则的用法一般适用于搜索的值是动态变化的，但有一定规律的
#print(bs_html.find("div",id=re.compile("\d+")))

#通过string，也就是text获取元素
#print(bs_html.find(string=re.compile("scrapy")))

div_info=bs_html.find("div",id="info")
#通过tag.contents来获取tag的子元素集合的列表
#但也会把回车换行符算一个子tab，需要注意
child_div_info=div_info.contents

#这里的孙元素包含子元素和孙元素，返回一个生成器对象，descendants方法
grandson_div_info=div_info.descendants

child=bs_html.find("p",{"class":"name"})
#获取全部的父元素，方法parents，也是一个生成器
father=child.parents


#next_sibling获取同辈下面的tap，也是生成器
next_sibling=child.next_siblings


#previous_sibling是获取同辈上面的tap，也是生成器
previous_sibling=child.previous_siblings

#获取属性

#class属性允许多class，所以无论是单还是多class，都返回列表
child_class=child["class"]

#非class属性都是字符串
child_id=child["id"]



