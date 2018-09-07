# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_006(mytest.MyTest):
    '''
    用例编号：text_PX_Common_006
    模块：
    功能点：
    测试点描述：测试是否对重复值进行了判断？
    测试步骤：
        执行新增操作，关键字段与数据库中已存在的值重复。
    预期结果：
        给予‘XX已存在，请重新输入’的提示信息。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

