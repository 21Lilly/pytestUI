# -*- coding:utf-8 -*-
'''
@project:newProject
@file:basePage.py
@ide:PyCharm
@author:lvy
@time:2020-07-27 10:35:54
@month:七月
'''

import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException,TimeoutException,NoAlertPresentException,NoSuchFrameException

from util.clipboard import ClipBoard
from util.keyboard import KeyBoard
from util.parseConFile import ParseConfile
from util.parseExcelFile import ParseExcel

class BasePage(object):
    '''结合显示等待封装一些selenium内置方法'''

    cf = ParseConfile()
    excel = ParseExcel()

    def __init__(self,driver,outTime=30):
        self.byDic = {
            'id':By.ID,
            'name':By.NAME,
            'class_name':By.CLASS_NAME,
            'xpath':By.XPATH,
            'link_text':By.LINK_TEXT
        }
        self.driver = driver
        self.outTime = outTime

    def find_element(self,by,locator):
        '''
        find alone element
        :param by:
        :param locator:
        :return: element object
        '''

        try:
            print('[Info:Starting find the element "{}" by "{}" !]'.format(locator,by))
            element = wd(self.driver,self.outTime).until(lambda x:x.find_element(by,locator))
        except TimeoutException as t:
            print('error:found "{}" timeout !'.format(locator,t))
        except NoSuchWindowException as e:
            print('error: no such "{}"'.format(locator), e)
        except Exception as e:
            raise e
        else:
            # print('[Info:Had found the element "{}" by "{}"!]'.format(locator, by))
            return element

    def find_elements(self,by,locator):
        '''
        find group elements
        :param by:
        :param locator:
        :return: elements object
        '''
        try:
            print('[Info:Had found the elements "{}" by "{}" !]'.format(locator,by))
            elements = wd(self.driver,self.outTime).until(lambda x:x.find_element(by,locator))
        except TimeoutException as t:
            print('error:found "{}" timeout !'.format(locator),t)
        except NoSuchWindowException as e:
            print('error:no such "{}" '.format(locator),e)
        except Exception as e:
            raise e
        else:
            return elements

    def is_element_exist(self,by,locator):
        '''
        assert element if exist
        :param by: id,name,xpath ,css......
        :param locator: eg:id,name,xpath for str
        :return: if element return True else return false
        '''
        if by.lower() in self.byDic:
            try:
                wd(self.driver,self.outTime).until(ec.invisibility_of_element_located(self.byDic[by],locator))
            except TimeoutException as t:
                print('error:found "{}" timeout !'.format(locator), t)
                return False
            except NoSuchWindowException as e:
                print('error:no such "{}" '.format(locator), e)
                return False
            return True
        else:
            print('the "{}" error!'.format(by))

    def is_click(self,by,locator):
        '''
        判断是否可点击 没返回元素对象
        :param by:
        :param locator:
        :return:
        '''
        if by.lower() in self.byDic:
            try:
                element = wd(self.driver, self.outTime).until(ec.element_to_be_clickable(self.byDic[by], locator))
            except TimeoutException:
                print('元素不可以点击')
            else:
                return element
        else:
            print('the "{}" error!'.format(by))

    def is_alert(self):
        '''
        assert alsrt if exsit
        :return:alert obj
        '''
        try:
            re = wd(self.driver,self.outTime).until(ec.alert_is_present())
        except (TimeoutException,NoAlertPresentException):
            print('error:no found alert')
        else:
            return re



    def switch_to_frame(self,by,locator):
        '''
        判断frame是否存在，存在就跳到frame
        :param by:
        :param locator:
        :return:
        '''
        print('info:switching to iframe "{}"'.format(locator))
        if by.lower() in self.byDic:
            try:
                wd(self.driver, self.outTime).until(ec.frame_to_be_available_and_switch_to_it(self.byDic[by], locator))
            except TimeoutException as t:
                print('error: found "{}" timeout！切换frame失败'.format(locator), t)
        else:
            print('the "{}" error!'.format(by))

    def switch_to_default_frame(self):
        '''返回默认的frame'''
        print('info:switch back to default iframe')
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    def get_alert_text(self):
        '''获取alert的提示信息'''
        alert = self.is_alert()
        if alert:
            return alert.text
        else:
            return None

    def get_element_text(self,by,locator,name=None):
        '''获取某个元素的text信息'''
        print('info:get element text')
        try:
            element = self.find_element(by,locator)
            if name:
                return element.get_attribute(name)
            else:
                return element.text
        except AttributeError:
            print('get"{}" text failed return None'.format(locator))

    def load_url(self,url):
        '''加载url'''
        print('info:string upload url "{}" '.format(url))
        self.driver.get(url)

    def get_source(self):
        '''获取页面源码'''
        return self.driver.page_source()

    def send_keys(self,by,locator,value=''):
        '''输入数据'''
        print('info:input "{}" '.format(value))
        try:
            element = self.find_element(by,locator)
            element.send_keys(value)

        except AttributeError as e:
            print(e)

    def clear(self,by,locator):
        '''清理数据'''
        print('info:clearing value')
        try:
            element = self.find_element(by,locator)
            element.clear()

        except AttributeError as e:
            print(e)

    def click(self,by,locator):
        '''点击某个元素'''
        print('info:click "{}" '.format(locator))
        element = self.is_click(by,locator)
        if element:
            element.click()
        else:
            print('the "{}" unclickable!')

    @staticmethod
    def sleep(num=0):
        '''强制等待'''
        print('info:sleep "{}" minutes'.format(num))
        time.sleep(num)

    def ctrl_v(self,value):
        '''ctrl + v 粘贴'''
        print('info:pasting "{}" '.format(value))
        ClipBoard.setText(value)
        self.sleep(3)
        KeyBoard.twoKeys('ctrl','v')

    @staticmethod
    def enter_key():
        """enter 回车键"""
        print('info:keydown enter')
        KeyBoard.one_key('enter')

    def wait_element_to_be_located(self, by, locator):
        """显示等待某个元素出现，且可见"""
        print('info:waiting "{}" to be located'.format(locator))
        try:
            return wd(self.driver, self.outTime).until(ec.presence_of_element_located((self.byDic[by], locator)))
        except TimeoutException as t:
            print('error: found "{}" timeout！'.format(locator), t)

    def get_page_source(self):
        return self.get_source()

if __name__ == '__main__':
    pass