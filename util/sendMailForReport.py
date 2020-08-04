# -*- coding:utf-8 -*-
'''
@project:newProject
@file:sendMailForReport.py
@ide:PyCharm
@author:lvy
@time:2020-07-27 10:46:32
@month:七月
'''

import yagmail

class SendMailWithReport(object):
    '''发送邮件'''

    @staticmethod
    def send_mail(smtp_server, from_user, from_pass_word, to_user, subject, contents, file_name):
        # 初始化服务器等信息
        yag = yagmail.SMTP(from_user,from_pass_word,smtp_server)

        # 发送邮件
        yag.send(to_user,subject,contents,file_name)

if __name__ == '__main__':
    SendMailWithReport.send_mail('smtp.qq.com',
                                 '账号@qq.com',
                                 'mhxvqpewblldbjhf',
                                 '1315516044@qq.com',
                                 'python自动化测试',
                                 '邮件正文',
                                 '17_12_07.html')