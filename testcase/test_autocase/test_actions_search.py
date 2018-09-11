# coding:utf-8

from selenium import webdriver
import unittest
import time, os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory


class test_actions_search(mytest.MyTest):

    def test_actions_search_001(self):
        """
        用例编号：actions_search_001
        模块：search
        功能点：搜索（指定）
        """
        # ****************************** login ******************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        # ****************************** login check ******************************
        self.assertEqual(u'', page.return_title())


        # ****************************** porject ******************************
        self.dr.click('')
        self.dr.sleep(3)


        # ****************************** 切换frame ******************************
        self.dr.switch_to_frame('')
        self.dr.sleep(3)


        # ****************************** actions search ******************************
        """actions_search"""
        # ****************************** 精确匹配查找信息，检查信息数据 ******************************
        # 根据信息的关键数据查找
        # TODO



