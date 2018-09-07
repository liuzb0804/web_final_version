# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_004(mytest.MyTest):
    '''
    用例编号：text_PX_Common_004
    模块：
    功能点：
    测试点描述：测试当因任何原因无法提交时，原输入的内容是否保存？
    测试步骤：
        制造提交失败的数据，输入相关数据后，进行保存。
    预期结果：
        提交失败后，界面的数据仍保留，不会清空。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

