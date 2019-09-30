import re
import ast
from urllib import parse
from datetime import datetime
import requests

from scrapy import Selector
from csdn_spider.model import Topic
#根目录url
domain="https://bbs.csdn.net"
#获取主模块url的json
def get_js_json():
    #先通过url获取js的内容
    left_menu_text=requests.get("https://bbs.csdn.net/dynamic_js/left_menu.js?csdn").text
    #用正则把我们需要的json格式提取出来
    nodes_str_match=re.search("forumNodes: (.*])",left_menu_text)
    #如果json的字符串存在，才进行下一步
    if nodes_str_match:
        #这个是将里面的null转化成None，才可以是python的格式
        nodes_str=nodes_str_match.group(1).replace("null","None")
        #由于本身这个是字符串，比如"[1,2,3]",并不是列表，所以用ast的literal_eval转化成列表
        nodes_list=ast.literal_eval(nodes_str)
        return nodes_list
    return []

#由于下面的方法用了递归，所以url_list放在最外层
#这个方法是获取全部的url
url_list=[]
def process_nodes_list(nodes_list):
    for item in nodes_list:
        #如果有url，就把url的内容加载到list上
        if "url" in item:
            url_list.append(item["url"])
            #如果第第一层出现了children，用递归的方式加入list，看不懂啊
            if "children" in item:
                process_nodes_list(item["children"])
    return url_list

#这个方法是获取第一层的url，由于第二层的url已经可以覆盖全了
#为了降低请求量，把第一层的url给去掉，因此先提取第一层的url
def get_first_url(nodes_list):
    first_url=[]
    for item in nodes_list:
        if "url" in item:
            first_url.append(item["url"])
    return first_url

#获取最终的url
def get_last_url():
    last_url=[]
    nodes_list=get_js_json()
    url_list=process_nodes_list(nodes_list)
    first_url=get_first_url(nodes_list)
    for i in url_list:
        #这里是去除掉第一层的url的做法
        if i not in first_url:
            last_url.append(i)
    all_url=[]
    for i in last_url:
        #parse.urljoin方法可以让我们判断如果有i只是相对路径，就会加入domain
        #如果i是绝对路径，就忽略domain了
        all_url.append(parse.urljoin(domain,i))
        all_url.append(parse.urljoin(domain,i+"/recommend"))
        all_url.append(parse.urljoin(domain,i+"/closed"))
    return all_url


def get_topic(url):
    #获取帖子信息和回复
    pass

def get_author(url):
    #获取用户的详细信息
    pass


def parse_list(url):
    #获取主页的信息
    re_text=requests.get(url).text
    sel=Selector(text=re_text)
    all_trs=sel.xpath("//table[@class='forums_tab_table']/tbody//tr")[2:]
    for td in all_trs:
        if "topic" in td.xpath(".//td[3]/a[1]/@href").extract()[0] :
            topic_url=parse.urljoin(domain,td.xpath(".//td[3]/a[1]/@href").extract()[0])
            topic_title=td.xpath(".//td[3]/a[1]/text()").extract()[0]
            static = td.xpath(".//td[1]/span/text()").extract()[0]
            socre = td.xpath(".//td[2]/em/text()").extract()[0]
            author_url=parse.urljoin(domain,td.xpath(".//td[4]/a/@href").extract()[0])
            author_id=author_url.split("/")[-1]
            create_time_str=td.xpath(".//td[4]/em/text()").extract()[0]
            create_time=datetime.strptime(create_time_str,"%Y-%m-%d %H:%M")
            answer_info=td.xpath(".//td[5]/span/text()").extract()[0]
            answer_nums=answer_info.split("/")[0]
            click_nums=answer_info.split("/")[1]
            last_time_str=td.xpath(".//td[6]/em/text()").extract()[0]
            last_time=datetime.strptime(last_time_str,"%Y-%m-%d %H:%M")

            topic=Topic()
            topic.id=int(topic_url.split("/")[-1])
            topic.author=author_id
            topic.title=topic_title
            topic.create_time=create_time
            topic.last_answer_time=last_time
            topic.answer_nums=int(answer_nums)
            topic.click_nums=int(click_nums)
            topic.socre=int(socre)
            topic.status=static

            topic_exist=Topic.select().where(Topic.id==topic.id)
            if topic_exist:
                topic.save()
            else:
                topic.save(force_insert=True)
            print("ok")

        # get_topic(topic_url)
        # get_author(author_url)
    next_page=sel.xpath("//a[@class='pageliststy next_page']/@herf").extract()
    print("next")

    if next_page:
        next_page_url=parse.urljoin(domain,next_page[0])
        parse_list(next_page_url)


if __name__=="__main__":
    for url in get_last_url():
        parse_list(url)













