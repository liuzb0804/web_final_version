# coding:utf-8

from selenium import webdriver
import unittest
import time, os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory


class test_actions_delete(mytest.MyTest):

    def test_actions_delete_001(self):
        """
        用例编号：actions_delete_001
        模块：delete
        功能点：删除（指定）
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

        # ****************************** before check(获取信息总数) ******************************
        text_before = self.dr.get_text('')
        # print text_before

        # ****************************** actions delete ******************************
        """actions_delete"""
        # TODO

        # ****************************** check after（操作后check总数变化） ******************************
        text_after = self.dr.get_text('')
        # print text_before

        # compare text_before and text_after
        # TODO





