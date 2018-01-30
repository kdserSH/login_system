#！/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Mario Gong
''''
#col1=data.col_values(0) #获取第一列数据
#col2=data.col_values(1) #获取第二列数据
#row1=data.row_value(0)#获取第一行数据
#nrows=data.nrows #获取sheet行数
#ncols=data.ncols #获取sheet列数
'''

#import getpass
import xlrd
import xlwt
f=xlrd.open_workbook('user.xlsx','r')  #xlrd打开excel
data=f.sheets()[0]  #根据sheet索引打开sheet
usr=data.col_values(0,1) #获取用户名列表,除去表头
pwd=data.col_values(1,1) #获取密码列表，除去表头
pwd1=[]
for i in pwd:
    pwd1.append(str(int(i)))#以上为新建一个列表pwd1，将密码设置为字符串格式
dict1=dict(map(lambda x,y:[x,y],usr,pwd1))#dict2=dict(zip(usr,pwd))#以上两种均可将两个列表映射为一个字典。
count=0
while True:
    usrname = input('login>>>:')
    password = input('password>>>:')
    passwd = dict1.get(usrname)
    if passwd== password:
        print('welcom to login',usrname)
        break
    else:
        print('incorrect usrname or password,please try again')
    count+=1
    if count==3:
        print('your acount has been blocked')
        locked_usr=xlwt.Workbook() #创建工作簿
        locked_sheet=locked_usr.add_sheet('locked',True) #创建sheet
        locked_sheet.write(0,0,usrname)
        locked_sheet.write(0,1,'locked')
        locked_usr.save('locked_usr_list.xls')
        exit()


