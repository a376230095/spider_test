
import requests

r=requests.get("https://bbs.csdn.net/forums/ios").text
print(r)