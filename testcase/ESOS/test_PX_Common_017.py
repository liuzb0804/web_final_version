# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_017(mytest.MyTest):
    '''
    用例编号：text_PX_Common_017
    模块：
    功能点：
    测试点描述：测试针对特殊字段限制是否正常?
    测试步骤：
        1、主页地址中可输入\
        2、电话号码中可输入\-
        3、E-mail地址中中输入@
    预期结果：
        提示：你输入的内容错误，请重新输入，光标停留在第一个需输入的输入框处。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

