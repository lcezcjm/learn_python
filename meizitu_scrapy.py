#!bin/python
# -*- coding: UTF-8 -*-

'''
妹子图网站 spider
URL: www.meizitu.com
抓取网站所有图片
'''

import re
import string
import urllib, urllib2
import os, sys
import multiprocessing


def getImageUrls(page):
    '''获取每个模块下的图片链接'''
    image_items = {}

    url_index = 'http://www.meizitu.com/a/list_1_%s.html' % page

    prog_index = r'<h3 class="tit"><a href="(.*)".*</a></h3>'
    prog_pages = r'<img alt=.*src="(.*)" /><br />'

    index_items = re.findall(prog_index, urllib2.urlopen(url_index).read())

    for index, item in enumerate(index_items):
        image_item = re.findall(prog_pages, urllib2.urlopen(item).read())
        image_items[index] = image_item

    return image_items


def downloadImage(image, store_file):
    urllib.urlretrieve(image, store_file, call_back)


def BeginDownload(page):
    pool = multiprocessing.Pool(24)
    store_dir = 'C:/Users/chen/Desktop/Python/Learn_Python/two_basic_scrapy_pictures/%s/' % page

    image_items = getImageUrls(page)
    for index in image_items:
        for i, image in enumerate(image_items[index]):
            if os.path.exists(store_dir):
                store_file = store_dir + str(index) + '-' + str(i) + '.jpg'
                pool.apply_async(downloadImage, (image, store_file))
            else:
                store_file = store_dir + str(index) + '-' + str(i) + '.jpg'
                os.makedirs(store_dir)
                pool.apply_async(downloadImage, (image, store_file))
    pool.close()
    pool.join()


def call_back(a, b, c):
    per = 100 * a * b / c
    if per < 100:
        sys.stdout.write('%.2f%%\r' % per)
        sys.stdout.flush()
    else:
        print 'download finish!'


if __name__ == '__main__':

    print '''
             *************************************
             **       Welcome to use Spider     **
             **      Created on  2016-07-18     **
             **           @author: cjm          **
             *************************************
          '''
    page = raw_input('Pleae enter your page to download(1-88 or all): ')

    #这里的if-选择怎么写需要再思考
    #pa_ge=int(page)

    if '0'< page<= '88':
        BeginDownload(page)
        print 'All done!'
    elif page == 'all':
        for i in range(1, 89):
            BeginDownload(i)
            print 'Page %s done!' % i
        print 'All done!'
    else:
        print 'Error input!'
        sys.exit(-1)