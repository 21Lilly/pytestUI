# -*- coding:utf-8 -*-
'''
@Project:newProject
@File:RunTestCase.py
@IDE:PyCharm
@Author:lvy
@Time:2020-08-04 14:59:49
'''

import sys
import pytest

from config.conf import ROOT_Dir, HTML_NAME

# from util.sendMailForReprot import SendMailWithReport


def main():
    if ROOT_Dir not in sys.path:
        sys.path.append(ROOT_Dir)
    # 执行用例
    args = ['--reruns', '1', '--html=' + './report/' + HTML_NAME]
    pytest.main(args)
    # 发送邮件 这里我屏蔽了 自己添加自己的邮箱信息
    # SendMailWithReport.send_mail(
    #     smtpServer, fromUser, fromPassWord,
    #     toUser, subject, contents,
    #     htmlName)


if __name__ == '__main__':
    main()