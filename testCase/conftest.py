# -*- coding:utf-8 -*-
'''
@project:newProject
@file:conftest.py
@ide:PyCharm
@author:lvy
@time:2020-07-27 10:39:46
@month:七月
'''

import pytest

from page.pageObject.loginPage import LoginPage
from page.pageObject.homePage import HomePage
from page.pageObject.contactPage import ContactPage
from page.pageObject.sendMailPPage import SendMailPage

from util.parseConFile import ParseConfile

do_conf = ParseConfile()
#从配置文件中获取正确的用户名和密码
userName = do_conf.get_locators_or_account('126LoginAccount','username')
passWord = do_conf.get_locators_or_account('126LoginAccount', 'password')

# @pytest.fixture(scope='function')
# def login(driver):
#     """除登录用例，每一个用例的前置条件"""
#     print('------------staring login------------')
#     login_action = LoginPage(driver, 30)
#     login_action.login(userName, passWord)
#     yield
#     print('------------end login------------')
#     driver.delete_all_cookies()


@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    contact_page = ContactPage(driver)
    send_mail_page = SendMailPage(driver)
    yield driver,login_page,home_page,contact_page,send_mail_page

@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    # login_page.open_url()
    yield login_page
    driver.delete_all_cookies()

@pytest.fixture(scope='class')
def login(ini_pages):
    driver, login_page, home_page, contact_page, send_mail_page = ini_pages
    login_page.login(userName,passWord)
    login_page.switch_default_frame()
    yield login_page, home_page, contact_page, send_mail_page
    driver.delete_all_cookies()

@pytest.fixture(scope='function')
def refresh_page(ini_pages):
    driver = ini_pages[0]
    yield
    driver.refresh()