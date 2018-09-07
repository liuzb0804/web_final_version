# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_024(mytest.MyTest):
    '''
    用例编号：text_PX_Common_024
    模块：
    功能点：
    测试点描述：测试在新增情况下，如果提供了重置功能，重置后的数据是否正常？
    测试步骤：
        界面对应的有新增后默认生成的数据，点击新增按钮，再点击重置。
    预期结果：
        能够清空已输入的数据，但不清空新增时默认生成的数据。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

