"""
    @Author:sumu
    @Date:2020-01-09 11:35
    @Email:xvzhifeng@126.com

    http://www.ireadweek.com/sdfesfwsf.php?g=portal&m=index&a=index&p=1
    http://www.ireadweek.com/sdfesfwsf.php?m=list&a=index&id=6
    http://www.ireadweek.com/sdfesfwsf.php?g=portal&m=list&a=index&id=6&p=2
"""


"""


 <ul class="hanghang-list">
 
 
<a href="/sdfesfwsf.php?m=article&a=index&id=14189">
                    <li>
                        <div class="hanghang-list-name">了无痕：报人读史礼记五集</div>
                        <div class="hanghang-list-num">1</div>
                        <div class="hanghang-list-zuozhe">田东江</div>
                        <div class="clearFloat"></div>
                    </li>
                </a>
"""


from util.file_tools import *
from util.get_url import *

from spider.my_spider.weekRead_spider import *
from spider.pipo_line.week_line import *

def begin():
    url = "http://www.ireadweek.com/sdfesfwsf.php?m=list&a=index&id="
    bcount = 41
    ecount = 68

    count = 100
    countj = 100
    url_fl = get_first_url(url, bcount, ecount)
    for i in range(0, len(url_fl)) :
        url_sl = get_seconde_url(url_fl[i], count)
        for j in range(0, len(url_sl)) :
            print(url_sl[j])
            content, rsm = getSecondeHtml(url_sl[j])
            kind = get_bookKinds(content, bcount + i)
            print(f"正在爬取{kind}类，第{j + 1}页。")
            handle_data(content, bcount + i)
            if j == 0 :
                countj = get_end_page(content)
                countj -= 1
            elif j >= countj :
                break;

            write_file_str(f"./datas/book_kind/{kind}_{j + 1}.html", 'w', content)

if __name__ == '__main__':
    # 爬取数据加上分析数据
    begin()
        #getFirstHtml(url_fl[i])

