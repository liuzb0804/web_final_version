# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_014(mytest.MyTest):
    '''
    用例编号：text_PX_Common_014
    模块：
    功能点：
    测试点描述：测试是否对各输入框的非法字符进行了控制（请将此数据作为修改的一个用例）。
    测试步骤：
        在各输入框中，输入@#$%^&*()<p>~%[]-/’等。操作新增操作
    预期结果：
        1、不允许输入或提示‘你输入的  **中存在非法字符，请重新输入’，光标停留在待输入的输入框处。
        2、允许输入保存后，能够正常回显。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

