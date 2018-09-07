# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_012(mytest.MyTest):
    '''
    用例编号：text_PX_Common_012
    模块：
    功能点：
    测试点描述：测试是否对数值型数据进行了格式化输入
    测试步骤：
        1、输入正整数、0、负整数（3/0/5）
        2、输入小数
        3、输入超大值（超出该字段定义范围）
        4、输入非数值（如数值+字符；字符+数值；纯字符）
    预期结果：
        进行了格式化输入控制：
        1、能够正常输入
        2、不允许输入
        3、给予提示信息
        4、不允许输入或提交给予提示信息。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

