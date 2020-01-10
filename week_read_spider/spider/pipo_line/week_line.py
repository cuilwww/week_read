"""
    @Author:sumu
    @Date:2020-01-09 15:04
    @Email:xvzhifeng@126.com

"""

from lxml.html import etree
from util.get_url import *
from spider.my_spider import *
import re
from spider.my_spider.weekRead_spider import *
from util.file_tools import *
from datetime import datetime

def get_end_page(content):
    """
    <li><a href="/sdfesfwsf.php?g=portal&m=list&a=index&id=9&p=8">尾页</a> </li>
    :param content:
    :return:
    """
    rex = re.compile(r'p=(\d+)">*尾页')
    num = re.findall(rex,content)
    #print(len(num))
    n = int(num[0]) if len(num)!=0 else 1
    #print(n)
    #print(n)
    return n

#[@href="/sdfesfwsf.php?m=list&a=index&id={i}]"
def get_bookKinds(content,i):
    page = etree.HTML(content)
    #print(page,content)
    kinds = page.xpath(f'//div[@class="hanghang-za"]/div[@class="hanghang-shupu-content"]/a[@href="/sdfesfwsf.php?m=list&a=index&id={i}"]/li')
    if len(kinds) == 0:
        kind = f'类型出错页面为{i}'
    else:
        kind = kinds[0].text
    #print(kinds[0].text)
    # for j in kinds:
    #     print(kinds[i].text)
    #print(kinds.text)
    kind = kind.replace(' ','_')
    return kind
####-----------------------------------------------------结果数据
def get_bookName(content):
    name_tree = etree.HTML(content)
    bookname = name_tree.xpath('//ul/a/li/div[@class="hanghang-list-name"]')
    # if len(bookname) == 0:
    #     bookname = '书籍名出错'
    # else:
    #     bookname = bookname[0].text
    return bookname

def get_doubanpf(content):
    name_tree = etree.HTML(content)
    bookdbpf = name_tree.xpath(f'//ul/a/li/div[@class="hanghang-list-num"]')
    # if len(bookdbpf) == 0 :
    #     bookdbpf = 0
    # else :
    #     bookdbpf = bookdbpf[0].text
    #print(f'dbpf------{len(bookdbpf)}')
    return bookdbpf
    #return float(bookdbpf)

def get_auther(content):
    name_tree = etree.HTML(content)
    book_auther = name_tree.xpath(f'//ul/a/li/div[@class="hanghang-list-zuozhe"]')
    # if len(book_auther) == 0 :
    #     book_auther = '作者未知'
    # else :
    #     book_auther = book_auther[0].text
    #print(book_auther)
    return book_auther

def get_baiduwpurl(content):
    url_list = get_three_url(content)
    bdurl = []
    for i in range(0,len(url_list)):
        content,e = getThreeHtml("http://www.ireadweek.com"+url_list[i])
        name_tree =etree.HTML(content)
        baiduwpurl = name_tree.xpath('//div[@class="hanghang-shu-content-btn"]/a/@href')
        #print(baiduwpurl[0])
        if len(baiduwpurl) != 0:

            bdurl.append(baiduwpurl[0])
        else:
            bdurl.append('')

    #print(bdurl)
    return bdurl


def get_baiduwptqm(content):
    url_list = get_three_url(content)
    bdtqm = []
    for i in range(0,len(url_list)):
        #print(url_list[i])
        content,e = getThreeHtml("http://www.ireadweek.com"+url_list[i])
        name_tree = etree.HTML(content)
        baiduwpurl = name_tree.xpath('//div[@class="hanghang-shu-content-btn"]/a/div')
        if len(baiduwpurl) != 0 :

            bdtqm.append(baiduwpurl[0].text)
        else :
            bdtqm.append('')


    #print(bdtqm)
    return bdtqm

def handle_data(content,n):
    list_data = []
    bn = get_bookName(content)
    ga = get_auther(content)
    pf = get_doubanpf(content)

    urlbd = get_baiduwpurl(content)
    tqmbd = get_baiduwptqm(content)
    for i in range(0,len(bn)):
        dic = {}
        dic['书名'] = bn[i].text
        dic['作者'] = ga[i].text
        dic['分类'] = get_bookKinds(content,n)
        dic['豆瓣评分'] = pf[i].text
        dic['百度网盘提取码'] = tqmbd[i]
        dic['百度云盘链接']  = urlbd[i]
        list_data.append(dic)
        print(dic)
        # print(bn[i].text)
        # print(ga[i].text)
        # print(pf[i].text)
        # print(tqmbd[i])
        # print(urlbd[i])
    save_csv(f"./handle_Data/book_kind/book_{get_bookKinds(content,n)}_{datetime.now().date()}.csv",list_data)