# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_002(mytest.MyTest):
    '''
    用例编号：text_PX_Common_002
    模块：新增
    功能点：新增功能
    测试点描述：测试是前端否对提交操作做单次点击控制，后端是否做事务控制
    测试步骤：
        输入能够正确新增成功的表单数据，连续多次快速点击提交按钮
    预期结果：
        只发送一次请求，操作流程正确，新增数据成功
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

