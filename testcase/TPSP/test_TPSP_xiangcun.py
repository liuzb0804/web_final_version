# coding:utf-8

from selenium import webdriver
import unittest
import time, os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory


class Test_basic(mytest.MyTest):
    '''
    用例编号：
    模块：
    功能点：
    测试点描述：
    测试步骤：

    预期结果：

    '''

    def test_basic_test(self):
        """演示脚本"""
        # ************************** login ************************
        page = login_page.IndexPage(self.dr)
        page.into_page('http://192.168.0.65:8010/')
        page.input_username_key('admin')
        page.input_password_key('123456')
        page.click_button()
        time.sleep(7)
        # self.assertEqual(u'旅游行业管理平台3.0.0', page.return_title())

        # ************************** porject ***********************
        self.dr.click('id->systemName')
        time.sleep(1)

        self.dr.click('xpath->/html/body/div[1]/ul/li[2]/ul/li[5]')
        time.sleep(3)

        self.dr.click('id->551')#基础数据配置
        time.sleep(2)

        self.dr.click('id->652')#乡村
        time.sleep(3)

        # ************************ 切换frame **********************
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        # ************************* before check ********************
        text_before = self.dr.get_text('xpath->/html/body/div[2]/div/div[2]/div[2]/div/span')

        # ************************** actions ************************
        self.dr.click('id->listAddButton')
        time.sleep(3)
        self.dr.type('name->name','xiangcun')#名称

        self.dr.click('xpath->//*[@id="regionSelector"]/div[3]')
        time.sleep(2)
        self.dr.click('xpath->//*[@id="regionSelector"]/div[3]/ul/li[2]')#所属地区

        self.dr.click('xpath->//*[@id="dataForm"]/div[2]/div/button')

        # ************************ check after ************************
        # check 1:数量变化
        text_fater = self.dr.get_text('xpath->/html/body/div[2]/div/div[2]/div[2]/div/span')
        # text_before equal text_fater
        if text_before == text_fater:
            pass
        else:
            raise SystemError

