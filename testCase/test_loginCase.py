# -*- coding:utf-8 -*-
'''
@project:newProject
@file:test_loginCase.py
@ide:PyCharm
@author:lvy
@time:2020-07-27 10:40:29
'''

import pytest
from data.loginData import LoginData

@pytest.mark.loginTest
class TestLogin(object):
    '''登录'''
    loginData = LoginData

    @pytest.mark.parametrize('username,password,except',loginData.login_success_data)
    def test_login(self,open_url,username,password,expect):
        login_page = open_url
        login_page.login(username,password)
        login_page.switch_default_frame()
        actual = login_page.get_login_success_account()
        assert expect in actual,"登录成功，断言失败"

    @pytest.mark.parametrize('username, password, expect', loginData.login_fail_data)
    def test_fail(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        actual = login_page.get_error_text()
        assert expect == actual, "登录失败, 断言失败"


if __name__ == "__main__":
    pytest.main(['-v', 'test_loginCase.py'])