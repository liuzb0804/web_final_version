# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_015(mytest.MyTest):
    '''
    用例编号：text_PX_Common_015
    模块：
    功能点：
    测试点描述：测试对各输入框中，输入内容的前后空格是否进行了处理？
    测试步骤：
        在各输入框中输入相应的值进行新增保存。
        1、前面存在空格
        2、后面存在空格
        3、前/后都存在空格
        4、中间存在空格
    预期结果：
        1、2、3能够正常去掉空格保存；4连同空格一起进行保存。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

