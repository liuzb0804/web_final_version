# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_003(mytest.MyTest):
    '''
    用例编号：text_PX_Common_003
    模块：
    功能点：
    测试点描述：测试界面上必填字段控制与数据库必填控制是否一致？
                （测试界面上必填字段控制是否满足数据库必填控制？）
    测试步骤：
        只填写界面上标识的必填字段（即标识*号）号的字段。
    预期结果：
        能够正常进行保存。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

