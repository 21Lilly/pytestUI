# -*- coding:utf-8 -*-
'''
@project:newProject
@file:clipboard.py
@ide:PyCharm
@author:lvy
@time:2020-07-27 10:45:27
'''

import win32con
import  win32clipboard as WC

class ClipBoard(object):
    '''设置剪切板内容和获取剪切板内容'''

    @staticmethod
    def getText():
        '''获取剪切板内容'''
        WC.OpenClipboard()
        value = WC.GetClipboardData(win32con.CF_TEXT)
        WC.CloseClipboard()
        return value

    @staticmethod
    def setText(value):
        '''设置剪切板内容'''
        WC.OpenClipboard()
        WC.EmptyClipboard()
        WC.SetClipboardData(win32con.CF_UNICODETEXT,value)
        WC.CloseClipboard()

if __name__ == '__main__':
    # from selenium import webdriver
    #
    # value = 'python'
    # driver = webdriver.Chrome("E:\\tool\chromedriver.exe")
    # driver.get('http://www.baidu.com')
    # query = driver.find_element_by_id('kw')
    # ClipBoard.setText(value)
    # clvalue = ClipBoard.getText()
    # query.send_keys(clvalue.decode('utf-8'))

    pass