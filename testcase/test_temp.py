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
        page.into_page('https://www.baidu.com/')
        self.dr.type('id->kw','中国')






        # page = login_page.IndexPage(self.dr)
        # page.into_page('http://192.168.0.68:9090/')
        # page.input_username_key('admin')
        # page.input_password_key('123456')
        # page.input_code_key('0')
        # page.click_button()
        # self.dr.sleep(7)
        # # self.assertEqual(u'旅游公共信息服务平台', page.return_title())
        # # self.dr.take_screenshot('C:\\Users\\zk\\PycharmProjects\\web_final_version\\report\\img\\123.png')    #success
        # # self.dr.take_screenshot(r'C:/Users/zk/PycharmProjects/web_final_version/report/img/111.png')      #success
        # # get_img(self.dr,'321.png')        #Failed
        # A = self.dr.get_elements('id->template')
        # A[1].click()
        # self.dr.sleep(3)
        # B = self.dr.get_elements('')
        # B[0].click()
        # self.dr.sleep(10)


