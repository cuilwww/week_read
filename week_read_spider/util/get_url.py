"""
    @Author:sumu
    @Date:2020-01-09 15:10
    @Email:xvzhifeng@126.com

"""

from lxml.html import etree

def get_first_url(url,Bcount,Ecount):
    """

    http://www.ireadweek.com/sdfesfwsf.php?m=list&a=index&id=6
    :param url:初始url
    :param Bcount: 开始页
    :param Ecount: 结束页
    :return: 返回url的列表
    """

    url_list = []

    for i in range(Bcount,Ecount):
        url_list.append(url+str(i))
    return url_list


def get_seconde_url(url,count):
    """
    http://www.ireadweek.com/sdfesfwsf.php?g=portal&m=list&a=index&id=6&p=2
    :param url: 上一层的url
    :param count: 爬的页数
    :return: 返回一个url列表
    """
    url_list = []

    for i in range(1,count):
        url_list.append(url+"&p="+str(i))
    return url_list


def get_three_url(content,url='http://www.ireadweek.com'):
    """
    :param url: 原始url:http://www.ireadweek.com/
    :param content: 上一层网页的内容
    :return: url
    <div class="hanghang-content">
    """
    name_tree = etree.HTML(content)
    path = '//div[@class="hanghang-content"]/ul/a/@href'
    sub_url = name_tree.xpath(path)
    #print(len(sub_url))
    #print(sub_url)
    return sub_url
