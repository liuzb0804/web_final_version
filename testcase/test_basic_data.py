# coding:utf-8

from selenium import webdriver
import unittest
import time,os
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
        #**************************login************************
        page = login_page.IndexPage(self.dr)
        page.into_page('http://192.168.0.65:8010/')
        page.input_username_key('admin')
        page.input_password_key('123456')
        page.click_button()
        time.sleep(7)
        # self.assertEqual(u'旅游行业管理平台3.0.0', page.return_title())

        #**************************porject***********************
        # project=u'资源管理'
        # page.project_number(project)
        self.dr.click('xpath->//*[@id="itemUl"]/li[5]')
        time.sleep(3)

        # type=u'景区'
        # page.type_number(type)
        self.dr.click('id->627')
        time.sleep(3)

        #**************************切换frame**********************
        self.dr.switch_to_frame('id->main')
        time.sleep(3)
        t1 = page.data_number()
        time.sleep(2)
        # self.dr.click('xpath->//*[@id="listForm"]/div/div/div[1]/div[4]/a[1]')
        # self.dr.switch_to_frame('id->layui-layer-iframe1')
        time.sleep(7)

        #**************************添加数据************************
        page.actions_type_add_all(type, '1')
        time.sleep(3)
        page.actions_type_add_all(type, '2')
        time.sleep(3)
        page.actions_type_add_all(type, '3')
        time.sleep(3)
        page.actions_type_add_all(type, '4')
        time.sleep(3)

        #*********************比对添加前后数据总数*******************
        self.dr.switch_to_frame_out()
        time.sleep(3)
        self.dr.switch_to_frame('id->main')
        time.sleep(3)
        t2 = page.data_number()
        # get_img(self.dr,'123.png')
        t3 = t2 - t1
        if t3 == 1:
            self.dr.my_print("Resources added successfully",)
        else:
            # print
            raise SystemError
            # raise self.dr.my_print("failed ,need help")


    def _search(self,data_values):
        """封装的函数"""
        page = login_page.IndexPage(self.dr)
        page.into_page()
        page.input_username_key(data_values[0])
        page.input_password_key(data_values[1])
        page.input_code_key(data_values[2])
        page.click_button()
        time.sleep(2)
        # self.assertIn(title, page.return_title())

    def test_search_excel(self):
        """使用数据驱动,进行测试"""
        datas = datainfo.get_excel_data('searKey_1.xlsx','Sheet1',1)
        # for data in datas:
        #     self._search(data)
        self._search(datas)


