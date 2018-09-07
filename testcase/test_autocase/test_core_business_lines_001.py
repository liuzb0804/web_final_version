# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory




class test_core_business_lines_001(mytest.MyTest):
    '''
    用例编号：test_core_business_lines_001
    模块：login-proje-add-check
    功能点：核心业务线

    '''

    def test_login_001(self):
        """ login """
        #************************** login ************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        self.assertEqual(u'', page.return_title())


    # def test_project_001(self):
        """project"""
        #************************** porject ***********************
        # self.test_login_001()
        self.dr.click('')
        self.dr.sleep(3)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('')
        self.dr.sleep(3)


        #************************* before check(获取信息总数) ********************
        text_before = self.dr.get_text('')
        # print text_before


    # def test_actions_add_001(self):
        """actions_add"""
        #************************** actions ************************



    # def test_check(self):
        """check"""
        #************************ check after（操作后check总数变化） ************************

