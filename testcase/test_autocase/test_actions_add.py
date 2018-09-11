# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class test_actions_add(mytest.MyTest):

    def test_actions_add_001(self):
        """
        用例编号：actions_add_001
        模块：add
        功能点：新增（全）
        """
        #****************************** login ******************************
        page = login_page.IndexPage(self.dr)
        page.into_page('')  #URL
        page.input_username_key('') #账户
        page.input_password_key('') #密码
        page.input_code_key('')     #验证码
        page.click_button()     #登录
        time.sleep(7)
        #****************************** login check ******************************
        self.assertEqual(u'', page.return_title())  #网站title


        #****************************** porject ******************************
        self.dr.click('')
        self.dr.sleep(3)


        #****************************** 切换frame ******************************
        self.dr.switch_to_frame('')
        self.dr.sleep(3)


        #****************************** before check(获取信息总数) ******************************
        text_before = self.dr.get_text('')  #共 * 条记录 共*页
        # print text_before

        #****************************** actions add ******************************
        """actions_add"""
        #TODO
        #1： input
        self.dr.type('***->***','***') #原来的文本中有数据使用：clear_type

        #2： list
        self.dr.click('***->***') #点击list 触发下拉列表然后在选择
        self.dr.sleep(2) #此处的 sleep = time.sleep(2)
        self.dr.click('***->***')
        self.dr.sleep(2)

        #3:  select
        self.dr.click('***->***') #已有选择项，使用此方法，需新增的需先增加选择

        #4.1： upload （本地上传）
        self.dr.click('***->***') #上传按键
        self.dr.sleep(3)
        os.system('') #AutoIt   此处输入autoIt转化的执行文件
        self.dr.sleep(3)
        #4.2: upload(非本地)
        self.dr.click('***->***')   #一般情况会触发弹窗，然后让用户选择
        self.dr.sleep(3)
        self.dr.click('***->***')   #选择某个目标后，有可能需要，点击确定，也有可能选择即生效，具体看网站

        #5; download
        #TODO

        #6.1: date(输入式)
        self.dr.type('***->***')
        #6.2: date(选择式)
        self.dr.click('***->***') #一般为年月日，依次选择，固需执行多次。

        #7: frame
        self.dr.switch_to_frame('***->***') #此处跳新frame
        self.dr.sleep(3)
        #******** 操作
        #TODO 在新frame下执行对应操作,操作完成后，需退出，重新回到原来的frame,或之后要操作元素所在的frame
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('***->***')#回到之前的frame，或之后要操作元素所在的frame
        self.dr.sleep(3)


        #****************************** check after（操作后check总数变化） ******************************
        text_after = self.dr.get_text('')
        # print text_before

        # compare text_before and text_after
        #TODO


        #****************************** 精确匹配查找新增信息，检查信息数据 ******************************
        #根据新增信息的关键数据查找，比对数据添加正确性
        #TODO



