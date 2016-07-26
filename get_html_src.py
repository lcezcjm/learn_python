#encoding:utf-8
from bs4 import BeautifulSoup
import requests
import urllib

url='http://tieba.baidu.com/p/2460150866?pn=5'
wb_data=requests.get(url)
soup=BeautifulSoup(wb_data.text,'lxml')
pics=soup.select('img[class="BDE_Image"]')

x=0
for pic in pics:
    pic_src = pic['src']
    urllib.urlretrieve(pic_src,'C:/Users/chen/Desktop/Python/Learn_Python/two_basic_scrapy_pictures/'+'%s.jpg' % x)#输出图片所在文件夹
    x+=1
    print(pic_src)

'''
#zip之前，pics是列表，每个元组是class type
#zip之后，pics由列表变为字典，每个元素变为tuple元组，元组是不可修改的

for pic in zip(pics):
    data={
        pic:pic.get('src')
    }
    print(pic)
'''