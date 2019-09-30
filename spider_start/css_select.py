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


#获取一个html的css
sel=Selector(text=html)

##info是通过id找到tap
teahcer=sel.css("#info")

#.teacher_info来找到class的tap
teahcer_info=sel.css(".teacher_info")

#通过id找到子元素，然后::text就是获取string
child_p=sel.css("div#info > p::text").extract()[0]

#通过nth-child(n)获取第几个tap元素
child_three=sel.css(".teacher_info > p:nth-child(3)::text").extract()[0]

#获取相邻的tap，同辈的,通过+ p获取邻居p信息
teacher_near=sel.css(".teacher_info  + p::text").extract()[0]

#获取相邻同辈的tap元素
teacher_near_all=sel.css(".teacher_info  ~ p::text").extract()

#通过属性值找到tap
a=sel.css("a[href='https://coding.imooc.com/class/200.html']::text").extract()[0]


#通过属性值模糊查询找到tap,就是*
b=sel.css("a[href*='imooc']::text").extract()

