import re

info="姓名:tongtong1998.生日:1964年8月16日.本科:1963年4月12日"

#findall太粗暴了，没有group功能，不好
print(re.findall("\d{4}",info))

#match是从字符串的开始匹配的
match_result=re.match(".*生日.*\d{4}",info)
#姓名:tongtong1998.生日:1964年8月16日.本科:1963 贪婪模式会匹配最后的\d{4}
print(match_result.group())

match_result=re.match(".*生日.*?\d{4}",info)
#姓名:tongtong1998.生日:1964非贪婪模式会匹配第一个的\d{4}
print(match_result.group())

match_result=re.match(".*生日.*?(\d{4}).*本科.*?(\d{4})",info)
print(match_result.group(1)) #匹配第一组的(\d{4})
print(match_result.group(2)) #匹配第二组的(\d{4})

#sub方法是替换字符串，返回字符串，不改变原值
sub_result=re.sub("\d{4}","2019",info)
#把四位数字都变成2019
print(sub_result)

#search不会从字符串的一开始就匹配了
search_result=re.search("生日.*?\d{4}",info)
#姓名:tongtong1998.生日:1964非贪婪模式会匹配第一个的\d{4}
print(search_result.group())

#模式

a="I am a Bobby man"
#忽略大小写,re.I
print(re.search("bobby",a,re.I).group())

b='''I am a 
bobby 
man
'''
#match是逐行搜索的，re.DOTALL可以无视逐行搜索
print(re.match(".*bobby",b,re.DOTALL).group())