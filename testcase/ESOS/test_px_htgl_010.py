# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_px_htgl_010(mytest.MyTest):
    '''
    用例编号：px_htgl_010
    模块：门票
    功能点：添加
    测试点描述：保存时，连续点击按钮
    测试步骤：
        1、进入门票添加页
        2、信息填写正确完整
        3、连续点击“保存”
    预期结果：
        1、提示保存成功，返回到列表页
        2、列表上和数据库中只保存了一条数据
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************
        page = login_page.IndexPage(self.dr)
        page.into_page()
        page.input_username_key('admin')
        page.input_password_key('123456')
        page.input_code_key('0')
        page.click_button()
        time.sleep(7)
        self.assertEqual(u'旅游公共信息服务平台', page.return_title())

        #************************** porject ***********************
        self.dr.click('id->systemName')
        time.sleep(1)

        self.dr.click('xpath->/html/body/div[1]/ul/li[2]/ul/li[7]')
        time.sleep(3)

        self.dr.click('id->790')#产品管理
        time.sleep(2)

        self.dr.click('id->792')#门票
        time.sleep(3)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        #************************* before check ********************
        pass

        #************************** actions ************************
        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[1]')
        time.sleep(2)

        #************************ check after ************************
        #TODO
