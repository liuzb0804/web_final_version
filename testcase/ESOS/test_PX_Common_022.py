# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_022(mytest.MyTest):
    '''
    用例编号：text_PX_Common_022
    模块：
    功能点：
    测试点描述：测试在任何情况下，点击取消（返回）按钮后，能否再保存信息
    测试步骤：
        点击‘新增’按钮，在弹出的页面，输入及选择相应信息，取消（返回）按钮，在弹出的提示框中，再选择确定按钮
    预期结果：
        提示‘保存成功！’返回到原页面首页首行显示新增的记录。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

