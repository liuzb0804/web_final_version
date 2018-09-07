# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_016(mytest.MyTest):
    '''
    用例编号：text_PX_Common_016
    模块：
    功能点：
    测试点描述：测试在多行文本框中，是否允许存在回车符？
    测试步骤：
        在多行文本框中输入文字及回车进行保存，存在一个或多个回车键。
    预期结果：
        能够正常进行保存及回显
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

