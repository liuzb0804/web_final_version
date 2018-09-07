# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_007(mytest.MyTest):
    '''
    用例编号：text_PX_Common_007
    模块：
    功能点：
    测试点描述：测试是否对各字段的长度进行了限制。
    测试步骤：
        执行新增操作（各输入的值都大于表中定义的长度）
    预期结果：
        在各输入框中，输入的内容达到所定义的长度时，则限制无法输入了。（如果输入的为中文字符，则控制到一半的长时就够了）
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

