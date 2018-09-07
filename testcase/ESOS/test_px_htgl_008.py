# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_px_htgl_008(mytest.MyTest):
    '''
    用例编号：px_htgl_008
    模块：门票
    功能点：添加
    测试点描述：文本框长度是否限制
    测试步骤：
        1、进入门票添加页
        2、文本框输入超过一定字符长度（数据库字段的长度）
        3、点击“保存”
    预期结果：
        1、提示字段最大输入长度是XXX或者文本框输入达到一定长度，不能输入
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
