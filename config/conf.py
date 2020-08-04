# -*- coding:utf-8 -*-
'''
@project:newProject
@file:conf.py
@ide:PyCharm
@author:lvy
@time:2020-07-27 10:34:20
'''

from datetime import datetime
import os

#项目根目录
ROOT_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#报告目录
REPORT_Dir = os.path.join(ROOT_Dir,'report')

#ui对象库config.ini文件所在目录
CONF_Path = os.path.join(ROOT_Dir,'config','config.ini')

#测试数据所在目录
DATA_Path = os.path.join(ROOT_Dir,'data','tcdata.xlsx')

#当前时间
CURRENT_Time = datetime.now().strftime('%H_%M_%S')

#邮件配置信息
#邮件服务器
SMTP_Server = 'smtp.qq.com'
#发送者
FROM_User = '账号@qq.com'
#发送者密码
FROM_Password = 'mhxvqpewblldbjhf'

#接收者
TO_User = ['账号@qq.com'] #可以同时发送给多人，追加到列表中
#邮件标题
SUBJECT = 'xx项目自动化测试报告'
#邮件正文
CONTENTS = '测试报告正文'
#报告名称
HTML_NAME = 'testReport{}.html'.format(CURRENT_Time)
print(HTML_NAME)