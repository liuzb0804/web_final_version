# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_009(mytest.MyTest):
    '''
    用例编号：text_PX_Common_009
    模块：
    功能点：
    测试点描述：测试对日期数据的溢出进行了控制？
    测试步骤：
        存在日期型数据，
        输入的值为1899-01-01或2999-01-01
    预期结果：
        给予提示信息，不允许提交。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

