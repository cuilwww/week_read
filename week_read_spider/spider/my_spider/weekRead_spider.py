"""
    @Author:sumu
    @Date:2020-01-09 15:03
    @Email:xvzhifeng@126.com

"""

import random

import requests



def getFirstHtml(url):
    """
    :param url:  想要爬取的网址地址
    :return: 源文件和响应码
    """

    # 让机器访问网址，模拟浏览器访问，具体请求头，可以在谷歌浏览器F12进入检查模式可以查看
    # 一下就是各种机型访问网站的的标志
    agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    ]
    # 模拟一个请求头，由下面的字典组成，random.choice（）就是从agents中随机取出一个来，以达到不同人访问的目的
    # 当然除了这个方法以外还可以减慢访问的速度，因为人在访问时不可能一直点一直点，没有那么快的访问速度，所以每访问一次最好可以间隔一段时间

    # 还有一个问题及时由于我们访问的ip一直是一个也可能导致会被网站察觉到，所以我们可以使用代理服务器的方式。
    hs = {"User-Agent" : random.choice(agents)}
    # 利用request库发出一个get请求
    response = requests.get(url,headers =hs)

    # 解决乱码问题
    # 修改编码格式
    response.encoding  = response.apparent_encoding

    return response.text,response.status_code


def getSecondeHtml(url):
    """
        :param url:  想要爬取的网址地址
        :return: 源文件和响应码
        """

    # 让机器访问网址，模拟浏览器访问，具体请求头，可以在谷歌浏览器F12进入检查模式可以查看
    # 一下就是各种机型访问网站的的标志
    agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'
    ]
    # 模拟一个请求头，由下面的字典组成，random.choice（）就是从agents中随机取出一个来，以达到不同人访问的目的
    # 当然除了这个方法以外还可以减慢访问的速度，因为人在访问时不可能一直点一直点，没有那么快的访问速度，所以每访问一次最好可以间隔一段时间

    # 还有一个问题及时由于我们访问的ip一直是一个也可能导致会被网站察觉到，所以我们可以使用代理服务器的方式。
    hs = {"User-Agent" : random.choice(agents)}
    # 利用request库发出一个get请求
    response = requests.get(url, headers=hs)

    # 解决乱码问题
    # 修改编码格式
    response.encoding = response.apparent_encoding

    return response.text, response.status_code


def getThreeHtml(url):
    """
        :param url:  想要爬取的网址地址
        :return: 源文件和响应码
        """

    # 让机器访问网址，模拟浏览器访问，具体请求头，可以在谷歌浏览器F12进入检查模式可以查看
    # 一下就是各种机型访问网站的的标志
    agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    ]
    # 模拟一个请求头，由下面的字典组成，random.choice（）就是从agents中随机取出一个来，以达到不同人访问的目的
    # 当然除了这个方法以外还可以减慢访问的速度，因为人在访问时不可能一直点一直点，没有那么快的访问速度，所以每访问一次最好可以间隔一段时间

    # 还有一个问题及时由于我们访问的ip一直是一个也可能导致会被网站察觉到，所以我们可以使用代理服务器的方式。
    hs = {"User-Agent" : random.choice(agents)}
    # 利用request库发出一个get请求
    response = requests.get(url, headers=hs)

    # 解决乱码问题
    # 修改编码格式
    response.encoding = response.apparent_encoding

    return response.text, response.status_code