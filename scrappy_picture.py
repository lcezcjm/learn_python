#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print(imglist)
    '''
    x = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
'''
html = getHtml("http://tieba.baidu.com/p/2460150866?pn=1")

print getImg(html)

# 当前已抓取前五页图片，后续抓取需要改变x参量的值和网页地址，pn=5，x=165