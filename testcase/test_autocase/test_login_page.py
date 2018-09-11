# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class test_login_page(mytest.MyTest):

    def test_login_001(self):
        """
        用例编号：login_001
        模块：login
        功能点：正确的账户，密码，验证码登录验证
        """
        #******************************login******************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        #******************************check******************************
        self.assertEqual(u'', page.return_title())

    def test_login_002(self):
        """
        用例编号：login_002
        模块：login
        功能点：空账户，空密码，空验证码登录
        """
        #******************************login******************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        #******************************check******************************
        #1.登录失败check提示信息

    def test_login_003(self):
        """
        用例编号：login_003
        模块：login
        功能点：任一登录数据未输入
        """
        #******************************login******************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        #******************************check******************************
        #1.登录失败check提示信息

    def test_login_004(self):
        """
        用例编号：login_004
        模块：login
        功能点：正确账户，密码，无验证码
        """
        #******************************login******************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        #******************************check******************************
        #1.登录失败check提示信息

    def test_login_005(self):
        """
        用例编号：login_005
        模块：login
        功能点：正确但不配套的账户，密码
        """
        #******************************login******************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        #******************************check******************************
        #1.登录失败check提示信息

    def test_login_006(self):
        """
        用例编号：login_006
        模块：login
        功能点：账户或密码输入非法字段
        """
        #******************************login******************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        #******************************check******************************
        #1.登录失败check提示信息

    def test_login_007(self):
        """
        用例编号：login_007
        模块：login
        功能点：已被删除的用户登录
        """
        #******************************login******************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        #******************************check******************************
        #1.登录失败check提示信息
