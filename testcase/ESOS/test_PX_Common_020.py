# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class text_PX_Common_020(mytest.MyTest):
    '''
    用例编号：text_PX_Common_020
    模块：
    功能点：
    测试点描述：测试在任何情况下，是否可取消保存
    测试步骤：
        点击‘新增’按钮，在弹出的页面中，输入及选择相应信息，在弹出的提示中，选择取消按钮
    预期结果：
        回到原记录所在页面，不更新任何值。
    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************


        #************************** porject ***********************


        #************************ 切换frame **********************


        #************************* before check ********************


        #************************** actions ************************


        #************************ check after ************************

