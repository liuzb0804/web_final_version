# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_px_htgl_006(mytest.MyTest):
    '''
    用例编号：
    模块：门票
    功能点：
    测试点描述：
    测试步骤：

    预期结果：

    '''
    def test_login_page(self):
        """ login """
        #************************** login ************************
        page = login_page.IndexPage(self.dr)
        page.into_page()
        page.input_username_key('')
        page.input_password_key('')
        page.input_code_key('')
        page.click_button()
        time.sleep(7)
        self.assertEqual(u'', page.return_title())

        #************************** porject ***********************
        self.dr.click('id->')
        time.sleep(1)

        self.dr.click('xpath->')
        time.sleep(3)

        self.dr.click('id->')
        time.sleep(2)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('id->')
        time.sleep(3)

        #************************* before check ********************
        #TODO

        #************************** actions ************************
        #actions:查询，重置，添加，编辑，上架，下架，复制，开启PC商场销售，关闭PC商场销售，开启微商城销售，关闭微商城销售，设置验票人，批量同步分销商品
        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[1]')#添加
        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[2]')#编辑
        self.dr.click('id->shelvesButton')#上架
        self.dr.click('id->underButton')#下架
        self.dr.click('id->copyButton')#复制
        self.dr.click('id->openPc')#开启PC商场销售
        self.dr.click('id->closedPc')#关闭PC商场销售
        self.dr.click('id->openB2c')#开启微商城销售
        self.dr.click('id->closedB2c')#关闭微商城销售
        self.dr.click('id->selectCheckTicketMember')#设置验票人
        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[11]')#批量同步分销商品

        #搜索：
        self.dr.type('name->productName','******')#景区名称/商品名称
        self.dr.type('name->productSn')#商品ID
        self.dr.type('name->areaName')#所在区域
        self.dr.type('name->supplierName')#商户名称/账号

        self.dr.click('xpath->//*[@id="listForm"]/div[1]/p/select[1]')#销售渠道
        time.sleep(2)
        self.dr.click('xpath->//*[@id="listForm"]/div[1]/p/select[1]/option[2]')#第二个选项：微商城

        self.dr.click('xpath->//*[@id="listForm"]/div[1]/p/select[2]')#是否上架
        time.sleep(2)
        self.dr.click('xpath->//*[@id="listForm"]/div[1]/p/select[2]/option[2]')#第二选项，已上架

        self.dr.click('xpath->//*[@id="listForm"]/div[1]/p/button[1]')#查询
        self.dr.click('xpath->//*[@id="listForm"]/div[1]/p/button[2]')#重置

        #设置页面显示数：
        self.dr.click('name->pageSize')
        time.sleep(2)
        self.dr.click('xpath->//*[@id="pageSize"]/option[2]')#第二个选项：20条/页

        #指定页：
        self.dr.type('id->pageNumber','****')   #第**页

        #上一页，下一页，
        self.dr.click('xpath->//*[@id="listForm"]/div[4]/span/span[1]')#首页
        self.dr.click('xpath->//*[@id="listForm"]/div[4]/span/span[2]')#上一页
        self.dr.click('xpath->//*[@id="listForm"]/div[4]/span/span[3]')#1
        #后面的参数存在变化

        #全选
        self.dr.click('id->selectAll')

        #获取信息：[产品名]，所在区域，销售渠道，今日售价，商户名称（账号），是否上架，创建日期，操作
        self.dr.click('xpath->//*[@id="listTable"]/tbody/tr[2]/td[1]')#勾选
        #tr[2]:表示面板列表，第一个门票信息，第一个是信息栏
        #td[1]:表示该信息的第几个字段：
        self.dr.click('xpath->//*[@id="listTable"]/tbody/tr[2]/td[9]/a')#操作：下单







        #上传文件
        #同上传图片一样处理

        #上传图片
        #上传图片，正常上传
        self.dr.click('id->')#点击上传button
        time.sleep(2)
        #1:本地上传
        value = 'AUTO.exe （执行文件），内容为图片流'
        os.system(value)
        time.sleep(3)
        #2:选择
        self.dr.click('')#选择目标
        time.sleep(2)
        self.dr.click('')#点击确认
        time.sleep(3)
        try:
            self.dr.get_element('')#此处为图片名
        except:raise SystemError

        #上传图片，选择不支持格式的图片
        self.dr.click('id->')#点击上传button
        time.sleep(2)
        value = 'AUTO.exe （执行文件），内容为非图片流，路径'
        os.system(value)
        time.sleep(3)
        try:
            self.dr.get_element('')#此处为图片名
            #1：如果该次操作为第一次操作，则此处为报错

            #2：如果该次操作为第二次操作，则此处为上次的信息
        except:raise SystemError

        #上传图片，再次上传图片
        self.dr.click('id->')
        time.sleep(2)
        value = 'AUTO.exe （执行文件），内容为图片流'
        os.system(value)
        time.sleep(3)
        self.dr.click('id->')
        time.sleep(2)
        value = 'AUTO_1.exe （执行文件），内容为图片流'
        os.system(value)
        time.sleep(3)




        #新增功能
        #单独作为处理

        #修改(受限于账号权限，不同账户管理不同信息，拥有归属关系才可被操作)
        self.dr.type('name->supplierName','admin')  #搜索拥有‘账号admin’的信息
        time.sleep(1)
        self.dr.click('xpath->//*[@id="listForm"]/div[1]/p/button[1]')  #查询
        time.sleep(2)
        text = self.dr.get_text('xpath->//*[@id="listForm"]/div[4]')    #获取‘共 * 条记录’判断是否拥有归属关系
        # print text
        text_code = text.encode('utf-8')    #转换
        # print text_code
        list = text_code.split(' ')[1]      #提取 “ * ” * >= 3 即为存在两个。* = 2 需检查其他元素条件 * = 1 为提示栏
        print list


        A = int(list) + 1
        for i in range(1, A):
            xpath = '//*[@id="listTable"]/tbody/tr[' + str(i) + ']'



            text_1 = self.dr.get_text('xpath->//*[@id="listTable"]/tbody/tr[2]/td[6]/span')




        #保存

        #删除

        #查询

        #查询

        #列表上分页













        #************************ check after ************************
        #TODO
