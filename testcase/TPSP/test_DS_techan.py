# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_techan(mytest.MyTest):
    '''
    用例编号：
    模块：
    功能点：
    测试点描述：
    测试步骤：

    预期结果：

    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************
        page = login_page.IndexPage(self.dr)
        page.into_page('http://192.168.0.65:8010/')
        page.input_username_key('admin')
        page.input_password_key('123456')
        page.click_button()
        time.sleep(7)
        self.assertEqual(u'旅游公共信息服务平台', page.return_title())

        #************************** porject ***********************
        self.dr.click('id->systemName')
        time.sleep(1)

        self.dr.click('xpath->/html/body/div[1]/ul/li[2]/ul/li[7]')
        time.sleep(3)

        self.dr.click('id->790')#产品管理
        time.sleep(2)

        self.dr.click('id->794')#特产
        time.sleep(3)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[1]')
        self.dr.sleep(3)

        # ********************** actions *****************************

        # 商品名称（1-60字）
        self.dr.type('name->name''***') #商品名称


        #商品卖点 *
        self.dr.type('name->sellingPoint','***')

        #商品属性
        #品牌
        self.dr.click('id->specialtyBrand')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="specialtyBrand"]/option[2]')
        #生成许可证编号
        self.dr.type('name->licenseNo','*****')
        #厂名
        self.dr.type('name->factoryName','***')
        #厂家联系方式
        self.dr.type('name->contactWay','***')
        #进货日期
        self.dr.type('name->inStockStartDate','***')    #可以直接输入也可以按照日期的方式选择。
        #产地
        self.dr.click('name->areaCity_select')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="id_propertytable"]/tbody/tr[1]/td[2]/span/select/option[2]')#第二个选项
        #产品标准号
        self.dr.type('name->standardNo','***')
        #厂址
        self.dr.type('name->factoryAddress','***')
        #特产类型
        self.dr.click('id->productClassId')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="id_propertytable"]/tbody/tr[4]/td[2]/div/ul/li[2]')#第二个选项
        #添加类型
        self.dr.click('xpath->//*[@id="id_propertytable"]/tbody/tr[4]/td[2]/a')
        #生产日期
        self.dr.type('name->inStockStartDate','***')    #可以直接输入也可以按照日期的方式选择。

        #发货地址 *
        self.dr.click('name->startAreaCity_select')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/select/option[2]') #第二个选项
        #省级目标选择后，才会出现下级列表选择
        self.dr.click('name->startAreaCity_select')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/select[2]/option[2]')#第二个选项
        #市级目标选择后，出现最后一级目标
        self.dr.click('name->startAreaCity_select')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/select[3]/option[2]')#第二个选项

        #商户
        self.dr.click('id->supplierName')
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[3]/div[2]/table/tbody/tr[1]')

        #验票人
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[7]/td/label')#默认是勾选装填
        self.dr.click('id->selectCheckTicketMember')
        #切frame
        #选择
        #确定
        #切回frame

        #销售驱动
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label[1]/label[1]')#C端
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label[2]')#PC商场

        #特产图片 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/div/div[2]/ul/li/div/a')
        self.dr.sleep(3)
        os.system('D:\WinClick4.exe')   #AUTO执行文件
        self.dr.sleep(3)

        #商品封面图
        self.dr.click('id->logoUploadBox_1_1')
        self.dr.sleep(3)
        os.system('D:\WinClick3.exe')   #AUTO执行文件
        self.dr.sleep(3)

        #取消设置
        self.dr.type('id->autoCancelTime','***')

        #联系人信息(默认三个勾选)

        #手机限制
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/th/label')
        self.dr.sleep(2)
        self.dr.type('name->limitAmountNum_MOBILE','***')

        #出售时间 * (默认勾选：1)
        #1
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/td/label[1]')
        #2
        self.dr.click('name->displayWay')
        self.dr.sleep(1)
        self.dr.click('id->saleStartTime')#起始
        #时间选择
        self.dr.click('id->saleEndTime')#截止
        #时间选择

        #短信模板 *
        self.dr.click('id->smsThemeId')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/div/ul/li[1]')#第二个选项
        #新增
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/a')

        #运费模板 *
        self.dr.click('id->deliverTemplateId')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[17]/td/div/ul/li[1]')
        #新增
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[17]/td/a')

        #商品规格 *
        #一级规格
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/table/tbody/tr[1]/td/select')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/table/tbody/tr[1]/td/select/option[2]')
        #二级规格
        self.dr.type('id->sku_tagsinput','***')

        #价格库存 *
        self.dr.click('id->batchset')
        self.dr.sleep(2)
        self.dr.type('id->marketPrice_2','***') #市场价
        self.dr.type('id->stockNum_2','***')    #整体库存
        self.dr.type('id->sellPrice_2','***')  #售卖价
        self.dr.type('id->minimum_2','***')  #最少购买
        self.dr.type('id->maximum_2','***')  #最多购买
        self.dr.click('xpath->//*[@id="skuStock"]/div[2]/div[4]/input[1]')  #保存
        self.dr.click('xpath->//*[@id="skuStock"]/div[2]/div[4]/input[2]')  #取消

        #商品调价
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[1]')  #是（默认）
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[2]')  #否

        #退款设置
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[23]/td/label[1]')  #可以退款（默认）
        #列表：1
        self.dr.click('name->partRefund')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[23]/td/select[1]/option[1]')#默认
        #列表：2
        self.dr.click('id->refundChargeType')
        time.sleep(2)
        self.dr.click('xpath->//*[@id="refundChargeType"]/option[1]')#默认
        #输入：
        self.dr.type('id->refundCharge','***')
        #不可退款
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[23]/td/label[2]')

        #退款审核(选择不可退款后，无此项)
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[1]')  #需要审核
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[2]')  #不需要审核（默认）

        #售后服务（可多选）
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[25]/td/label[1]')  #第一个：提供发票。label[1]:依次

        #商品描述
        self.dr.switch_to_frame('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[27]/td/div/div[2]/iframe')
        self.dr.sleep(3)
        self.dr.type('xpath->/html/body','***')

        #保存
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[1]')
        #返回
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[2]')

















