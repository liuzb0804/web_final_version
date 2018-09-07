# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_px_htgl_001(mytest.MyTest):
    '''
    用例编号：px_htgl_001
    模块：门票
    功能点：进入门票页面
    测试点描述：进入门票页面
    测试步骤：
        1、鼠标放在右上角的系统选择下拉框处
        2、点击“电商运营子系统”
        3、点击“产品管理”
        4、点击“门票”
    预期结果：
        1、下拉框显示各系统名称如:建站子系统、业务组件系统等
        2、进入电商运营子系统页面
        3、显示管理菜单栏目
        4、进入门票页面
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************
        page = login_page.IndexPage(self.dr)
        page.into_page('http://192.168.0.65:8010/')
        page.input_username_key('admin')
        page.input_password_key('123456')
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
        text_before = self.dr.get_text('xpath->//*[@id="listForm"]/div[4]')
        print text_before

        #************************** actions ************************
        pass

        #************************ check after ************************
        pass
