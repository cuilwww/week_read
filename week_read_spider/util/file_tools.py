"""
    @Author:sumu
    @Date:2020-01-06 14:27
    @Email:xvzhifeng@126.com

"""



import csv
import requests
from functools import singledispatch


def read_file(filepath):
    """
    :param filepath: 文件的路径
    :return: 文件的内容
    """
    with open(filepath) as fp :
        content = fp.read()
    return content


def read_file_layout(filepath):
    """
    :param filepath: 文件的路径
    :return: 文件的内容
    """
    str = ""
    fp = open(filepath)
    content = fp.readlines()
    for c in content:
        str += c.replace('\n', '\n')
    fp.close()
    return str

def write_file_str(filepath,mode,content,encoding1='utf-8'):
    """
    :param filepath: 文件的路劲
    :param mode: 打开的方式
    :param content: 写入的内容
    :return: 返回值
    """
    with open(filepath, mode,encoding=encoding1) as rwf:
        rwf.write(content)
    return "successful"

def write_file_list(filepath,mode,content=list):
    """
    :param filepath: 文件的路劲
    :param mode: 打开的方式
    :param content: 写入的内容
    :return: 返回值
    """
    print("list")
    with open(filepath, mode) as rwf:
        for i in content:
            rwf.write(str(i)+'\n')
        #rwf.write(content)
    return "successful"


# stu1 = [lid, k, pre_count_data[k]]
# # 打开文件，写模式为追加'a'
# out = open('../results/write_file.csv', 'a', newline='')
# # 设定写入模式
# csv_write = csv.writer(out, dialect='excel')
# # 写入具体内容
# csv_write.writerow(stu1)

def write_cvs_file(filepath,mode,t1,t2,t3,t4,t5,t6):
    """
    功能：把51同城搜索只有网页的源码的数据清理之后的数据整理成表格的形式写入csv表中；进行存储，备份。
    :param filepath: 文件存放的路径
    :param mode: 写入方式例如；'w','a'等
    :param t1: 职位列表
    :param t2: 公司列表
    :param t3: 地区列表
    :param t4: 最小薪资列表
    :param t5: 最大薪资列表
    :param t6: 发布的日期
    :return:
    """
    f = open(filepath,mode,newline='', encoding='utf-8')
    # 2. 基于文件对象构建 csv写入对象
    print(len(t1),len(t2),len(t3),len(t4),len(t5),len(t6))
    csv_writer = csv.writer(f)
    for i in range(len(t1)):
        csv_writer.writerow([str(t1[i]),str(t2[i]),str(t3[i]),str(t4[i]),str(t5[i]),str(t6[i])])
    f.close()


def save_csv(filepath,data,encoding='utf-8'):
    """
    :param filepath: 文件最后保存的路径
    :param data: 51job的工作信息的字典的列表
    :param encoding: 编码格式，默认utf-8，
    :return:
    """
    with open(filepath,'a+') as fp:

        # 获取表头列表
        headers = data and list(data[0].keys())
        print(headers)
        # 定义writer
        writer = csv.DictWriter(fp,fieldnames=headers)
        # 如果程序没有指向表头，依旧以为程序为空，没有表头，则添加表头，否则不添加表头
        if fp.tell() == 0:
            writer.writeheader()
        # print(data)
        # for i in range(0,len(data)):
        #     print(list(data[i].values()))
            #writer()
        # 可以直接写入字典类型的数据，但是数据的keys必须和表头的keys相等，否则会出错。
        writer.writerows(data)


if __name__ == '__main__':
    filepath ='../handled_data/test.csv'

    data= [
        {'1':1,'3':'kjl'},
        {'1':1,'3':'kljk'}
    ]
    save_csv(filepath,data)

