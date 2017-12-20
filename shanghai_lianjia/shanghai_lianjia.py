# -*- coding:utf-8 -*-
# Filename: shanghai_lianjia.py
# CreateTime: 2017.04.28
# Author : Adair
# EditTime: 2017.12.19
# Rewriter: Amy


# [数据库表结构]
# [lianjia_hefei数据库表结构]
# CREATE TABLE `lianjia_hefei` (
# `id` int(11) NOT NULL AUTO_INCREMENT,
# `area` varchar(30) DEFAULT NULL,
# `fangxing` varchar(10) DEFAULT NULL,
# `allhouse` int(10) DEFAULT NULL,
# `createdate` datetime DEFAULT NULL,
# PRIMARY KEY (`id`)
# ) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=gbk;

import urllib.request #导入整个模块
import io, sys, string #import同时导入多个模块，可以使用逗号分隔
import time, re
import requests
from bs4 import BeautifulSoup #从bs4模块中导入bs4.BeautifulSoup,且作用域内BeautifulSoup = bs4.BeautifulSoup
import pymysql
import numpy as np #导入numpy模块，并给numpy一个别称np
import matplotlib.pyplot as plt
#解决中文显示问题

'''import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False'''


# DateTime = time.strftime("%Y-%m-%d", time.localtime())
# OutFile = open("shanghai_lianjia_0_"+DateTime+".txt", "a", encoding='utf-8')
# OutFile1 = open("shanghai_lianjia_1_"+DateTime+".txt", "a", encoding='utf-8')
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


#爬链家数据1
def spider_shanghai_lianjia_A1():
    area = {''''pudong': '浦东',
            'minhang': '闵行',
            'baoshan': '宝山',
            'xuhui': '徐汇',
            'putuo': '普陀','''
            'yangpu': '杨浦'
           }
    fangxing = {#'l1': '一室',
                #'l2': '二室',
                #'l3': '三室',
                #'l4': '四室',
                'l5': '五室'
                #'l6': '五室以上'
        }
    urls = ['http://hf.lianjia.com/ershoufang/']
    spider(area, fangxing, urls)



#爬链家数据2
# def spider_shanghai_lianjia_A2():
#     area = {'changning': '长宁',
#             'songjiang': '松江',
#             'jiading': '嘉定',
#             'huangpu': '黄埔',
#             'jingan': '静安',
#             'zhabei': '闸北'
#            }
#     fangxing = {'l1': '一室',
#                 'l2': '二室',
#                 'l3': '三室',
#                 'l4': '四室',
#                 'l5': '五室',
#                 'l6': '五室以上'
#                }
#     urls = ['http://hf.lianjia.com/ershoufang/']
#     spider(area, fangxing, urls)


#爬链家数据3
# def spider_shanghai_lianjia_A3():
#     area = {'hongkou': '虹口',
#             'qingpu': '青浦',
#             'fengxian': '奉贤',
#             'jinshan': '金山',
#             'chongming': '崇明',
#             'shanghaizhoubian': '上海周边'
#            }
#     fangxing = {'l1': '一室',
#                 'l2': '二室',
#                 'l3': '三室',
#                 'l4': '四室',
#                 'l5': '五室',
#                 'l6': '五室以上'
#                }
#     urls = ['http://hf.lianjia.com/ershoufang/']
#     spider(area, fangxing, urls)

#爬数据函数
def spider(area, fangxing, urls):
    for u in urls:
        for key, val in area.items():
            for key1, val1 in fangxing.items():
                url = str(u)+ str(key)+'/'+ str(key1)+'/'
                time.sleep(20)
                print('End:' + '\t' +time.ctime())
                content_a = urllib.request.urlopen(url).read()
                print(type(content_a))
                content_a = content_a.decode('UTF-8', 'ignore') #解码utf-8，忽略其中有异常的编码，仅显示有效的编码
                print(content_a)
                # soup = BeautifulSoup(contentA,'html.parser') #创建BeautifulSoup对象,使用内置Python标准库解析器
                # for content3 in soup.select('.house-lst-page-box'):#通过css类名查找
                #     #pr   int(content3)
                #     searchObj = re.search(r'totalPage.*.,', str(content3))
                #     if searchObj:
                #        #print(searchObj.group())
                #        num = regexNum(searchObj.group())
                #        print(num)
                #     else:
                #        print("Nothing found!!")
                #     for i in range(1,int(num)+1):
                #         url = str(u)+ str(key)+'/'+ str('pg'+str(i))+str(key1)+'/'
                #         print(url)
                #         content = urllib.request.urlopen(url).read()
                #         content = content.decode('UTF-8', 'ignore')
                #         #print(content)
                #         soup = BeautifulSoup(content,'html.parser')
                #         #print(soup)
                #         #OutFile1.write(str(soup)+"\t"+"\n")
                #         if(i == 1):
                #             #获取各区总套数
                #             for content1 in soup.select('.resultDes'):
                #                 #print(content)
                #                 total = content1.select('.total')[0].text[3:]
                #                 print(val,val1,total)
                #                 OutFile.write(str(key)+"\t"+str(val)+"\t"+str(key1)+"\t"+\
                #                 str(val1)+"\t"+str(total)+"\n")
                #         else:
                #             #获取各区二手房详细信息
                #             for content2 in soup.find_all('ul', {'class' : 'sellListContent'}):
                #                 #print(content2)
                #                 for item in content2.find_all('li'):
                #                     #万振逍遥苑四期 2室2厅 145万房主自荐
                #                     #万振逍遥苑四期  | 2室2厅 | 85.27平米 | 南 | 其他
                #                     #低楼层(共34层)  -  周谷 堆
                #                     #8人关注 / 共0次带看 / 1个月以前发布
                #                     #145万
                #                     #单价17005元/平米
                #                     title = item.select('.title')[0].text
                #                     houseInfo = item.select('.houseInfo')[0].text.split("|")
                #                     xiaoqu = houseInfo[0]
                #                     fangxing = houseInfo[1]
                #                     mianji = houseInfo[2]
                #                     chaoxiang = houseInfo[3]
                #                     zhuangxiu = houseInfo[4]
                #                     #print(title,xiaoqu,fangxing,mianji,chaoxiang,zhuangxiu)
                #                     floor = item.select('.positionInfo')[0].text
                #                     followInfo = item.select('.followInfo')[0].text
                #                     #print(followInfo)
                #                     followInfo1 = ''.join(followInfo).split("/")
                #                     #print(followInfo1)
                #                     guanzhu = followInfo1[0]
                #                     daikan = followInfo1[1]
                #                     fabu = followInfo1[2]
                #                     #print(positionInfo,guanzhu,daikan,fabu)
                #                     totalPrice = item.select('.totalPrice')[0].text
                #                     unitPrice = item.select('.unitPrice')[0].text
                #                     #print(totalPrice,unitPrice)
                #                     #print(title+"\t"+xiaoqu+"\t"+fangxing+"\t"+\mianji+"\t"\
                #                     # +chaoxiang+"\t"+zhuangxiu+"\t"+floor+"\t"+guanzhu+"\t"\
                #                     # +daikan+"\t"+fabu+"\t"+totalPrice+"\t"+unitPrice)
                #                     OutFile1.write(str(title)+"\t"+str(xiaoqu)+"\t"\
                #                     +str(fangxing)+"\t"+str(mianji)+"\t"+str(chaoxiang)+\
                #                     "\t"+str(zhuangxiu)+"\t"+str(floor)+"\t"+str(guanzhu)+\
                #                     "\t"+str(daikan)+"\t"+str(fabu)+"\t"+str(totalPrice)+"\t"\
                #                     +str(unitPrice)+"\t"+str(key)+"\t"+str(key1)+"\t"\
                #                     +str(val)+"\t"+str(val1)+"\t"+"\n")


#数据库连接
# def connLinajia():
#     global conn, sql
#     conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='lagou', charset='utf8')
#     cur = conn.cursor()


#文件写入数据库表
# def insertLianjia(fileName, flag):
#     print(fileName, flag)
#     flag = 2
#     f = open(fileName, 'rb') # 打开文件
#     #f = file('poem.txt')
#     # if no mode is specified, 'r'ead mode is assumed by default
#     while True:
#         line = f.readline().decode('UTF-8', 'ignore')
#         if len(line) == 0: # Zero length indicates EOF
#             break
#         if int(flag) == 1:
#             areaEn = line.split('\t')[0]
#             areaKey = line.split('\t')[1]
#             fangxingEn = line.split('\t')[2]
#             fangxingKey = line.split('\t')[3]

#             #p = re.compile(r'\D')
#             #amount= p.split((line.split('\t')[4]))[1]
#             amount = regexNum(line.split('\t')[4])
#             #print(areaKey,fangxingKey,amount)
#             connLinajia()
#             DateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#             sql = "INSERT IGNORE INTO `lianjia_hefei` (`area`,`area_en`,`fangxing`,`fangxing_en`,`allhouse`,`createdate`) VALUES (%s,%s,%s,%s,%s,%s)"
#             try:
#                 with conn.cursor() as cursor:
#                     print(areaKey, fangxingKey, amount)
#                     cursor.execute(sql, (areaKey, areaEn, fangxingKey, fangxingEn, amount, DateTime))
#                     conn.commit()
#                     cursor.close()
#             finally:
#                 pass
#         else:

#             title = line.split('\t')[0]
#             xiaoqu = line.split('\t')[1]
#             fangxing = line.split('\t')[2]
#             mianji = regexNum(line.split('\t')[3])
#             chaoxiang = line.split('\t')[4]
#             zhuangxiu = line.split('\t')[5]
#             floor = line.split('\t')[6]
#             guanzhu = regexNum(line.split('\t')[7])
#             daikan = regexNum(line.split('\t')[8])
#             fabu = regexNum(line.split('\t')[9])
#             totalPrice = regexNum(line.split('\t')[10])
#             unitPrice = regexNum(line.split('\t')[11])
#             areaEN = regexNum(line.split('\t')[12])
#             area = regexNum(line.split('\t')[13])
#             fxEN = regexNum(line.split('\t')[14])
#             fx = regexNum(line.split('\t')[15])



#             #print(unitPrice)
#             connLinajia()
#             DateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#             sql = "INSERT IGNORE INTO `lianjia_hefei_info` (`title`,`xiaoqu`,`fangxing`,`mianji`,`chaoxiang`,`zhuangxiu`,`floor`,`guanzhu`,`daikan`,`fabu`,`totalPrice`,`unitPrice`,`area`,`areaEN`,`fx`,`fxEN`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#             try:
#                 with conn.cursor() as cursor:
#                     #print(title+"\t"+xiaoqu+"\t"+fangxing+"\t"+mianji+"\t"+chaoxiang+"\t"+zhuangxiu+"\t"+floor+"\t"+guanzhu+"\t"+daikan+"\t"+fabu+"\t"+totalPrice+"\t"+unitPrice)

#                     cursor.execute(sql, (title, xiaoqu, fangxing, mianji, chaoxiang, zhuangxiu, floor, guanzhu, daikan, fabu, totalPrice, unitPrice, area, areaEN, fx, fxEN))
#                     conn.commit()
#                     cursor.close()
#             finally:
#                 pass
#     f.close() # close the file


# def  regexNum(text):

#     num = re.sub(r'\D', "", text)
#     return num


# #清空数据库表
# def truncate(tableName):
#     connLinajia()
#     try:
#         with conn.cursor() as cursor:
#             cursor.execute('truncate table '+tableName)
#             conn.commit()
#             cursor.close()
#     finally:
#         pass



#伪装浏览器访问
# def lianjia2():
#     area1 = {'baohe': '包河',
#              'shushan': '蜀山',
#              'luyang': '庐阳',
#              'yaohai': '瑶海',
#              'zhengwu': '政务',
#              'binhuxinqu': '滨湖新区',
#              'jingkai2': '经开',
#              'gaoxin8': '高新',
#              'xinzhan': '新站',
#              'feidong': '肥东',
#              'feixi': '肥西',
#              'changfeng': '长丰'
#          }
#     fangxing1 = {'l1': '一室',
#                  'l2': '二室',
#                  'l3': '三室',
#                  'l4': '四室',
#                  'l5': '五室'
#          }
#     urls = ['http://hf.fang.lianjia.com/loupan/', 'http://hf.lianjia.com/ershoufang/']
#     for u in urls:
#         #print (url)
#         for key, val in area1.items():
#             #print(name, address)
#             for key1, val1 in fangxing1.items():
#                 #print(name, address)
#                 #print (u,key,key1);
#                 url = str(u)+ str(key)+'/'+ str(key1)+'/'
#                 #print(url)
#                 #content = urllib.request.urlopen(url).read()
#                 #headers = {'User-Agent':'Mozilla / 5.0(X11;Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 50.0.2661.102 Safari / 537.36'}
#                 headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
#                 content = requests.get(url, headers = headers).content
#                 content = content.decode('UTF-8', 'ignore')
#                 #print(content)
#                 soup = BeautifulSoup(content,'html.parser')
#                 #print(soup.prettify())

#                 for content1 in soup.select('.resultDes'):
#                     #print(content)
#                     total = content1.select('.total')[0].text[3:]
#                     print(val,val1,total)
#                     OutFile.write(str(val)+"\t"+str(val1)+"\t"+str(total)+"\n")






# #画图
# def makepie():
#     global la,da,num
#     la = ''
#     da = ''
#     ta = ''
#     ca = ''
#     num = 0

#     connLinajia()
#     cursor = conn.cursor()

#     sql1 ='select area,sum(allhouse)as alls,date_format(createdate, "%Y-%m-%d")  from lianjia_hefei  GROUP BY area,date_format(createdate, "%Y-%m-%d") order by sum(allhouse) desc '
#     cursor.execute(sql1)
#     data1 = cursor.fetchall()

#     for k in range(0,len(data1)):
#         #print(data1[k][0])
#         la = la + ',' + "'" +data1[k][0] + "'"
#         da = da + ','+  str(data1[k][1])
#         num = num+data1[k][1]
#         if(k == 0):
#             ca = ca + ','+  str(0.1)
#         else:
#             ca = ca + ','+  str(0)

#     for k in range(0,len(data1)):
#         #print(data1[k][1],num)
#         ta = ta + ',' + str(round( (data1[k][1]/num)*100) )


#     print(tuple(eval(la[1:])) , list(eval(da[1:])) ,num,ta[1:],tuple(eval(ca[1:])))
#         # Pie chart, where the slices will be ordered and plotted counter-clockwise:


#     #plt.figure()
#     lab = tuple(eval(la[1:]))
#     labels = lab
#     #print(len(lab),type(lab))
#     #print(len(labels),type(labels))
#     sizes = list(eval(ta[1:]))
#     explode = tuple(eval(ca[1:]))  # only "explode" the 2nd slice (i.e. 'Hogs')

#     fig1, ax1 = plt.subplots()
#     ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#             shadow=True, startangle=90)
#     ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#     plt.title('', fontsize=20)
#     plt.suptitle(u'链家合肥二手房'+str(data1[k][2]), fontsize=18)

#     plt.show()
#     figname=str(data1[k][2])+'.png'
#     plt.savefig(figname)
#     plt.clf()#清除图形


#入口函数
if __name__ == '__main__':


    spider_shanghai_lianjia_A1()
    #time.sleep(60)
    #spider_shanghai_lianjia_A2()
    #time.sleep(60)
    #spider_shanghai_lianjia_A3()
    #truncate(tableName='shanghai_lianjia')
    #truncate(tableName='shanghai_lianjia_info')
    #insertLianjia("lianjia_hefei_1_"+DateTime+".txt",flag=1)
    #insertLianjia("lianjia_hefei_2_"+DateTime+".txt",flag=2)