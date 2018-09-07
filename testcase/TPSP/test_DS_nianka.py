# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_nianka(mytest.MyTest):
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

        self.dr.click('id->885')#年卡
        time.sleep(3)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        #************************* before check ********************
        text_before = self.dr.get_text('xpath->//*[@id="listForm"]/div[4]') #获取当前页面条数显示信息
        print text_before

        #************************** actions ************************
        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[1]') #点击添加
        self.dr.sleep(3)


        #产品名称 *
        self.dr.type('name->name','***')

        #年卡内容
        self.dr.type('id->zy','***')#资源
        self.dr.click('name->companyType_')#票型
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[2]/td/select/option')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[2]/td/button')#重置

        self.dr.type('name->price_','***')#价格

        self.dr.type('name->remind_','***')#使用细则

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td/span/label[1]')#无限次

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td/span/label[2]')#免一次

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td/span/label[3]/label')#免
        self.dr.type('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td/span/label[3]/input','***')#**次

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td/span/label[4]/label')#特惠
        self.dr.type('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td/span/label[4]/input','***')#***元/次

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td/span/label[5]/label')#特惠
        self.dr.type('name->specialPrice_','***')#***元/次

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td/span/label[5]/input[2]','***')#限***次

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td/div/input')#增加年卡内容
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td/div/label[2]/b')#删除
        #商户
        self.dr.click('id->supplierName')
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[4]/div[2]/table/tbody/tr[1]')

        #验票人 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/label')

        self.dr.click('id->selectCheckTicketMember')

        #商品头图 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/div/div/ul/li/div/a')
        self.dr.sleep(3)
        os.system('D:\WinClick2.exe')#********
        self.dr.sleep(3)

        #商品封面图
        self.dr.click('id->logoUploadBox_1_1')
        self.dr.sleep(3)
        os.system('D:\WinClick3.exe')#****
        self.dr.sleep(3)

        #销售渠道
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label[1]/label[1]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label[1]/label[2]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label[1]/label[3]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label[1]/label[4]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label[1]/label[5]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label[2]')

        #取消设置
        self.dr.type('name>autoCancelTime','***')

        #联系人信息
        #客人信息
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/th/label')#客人信息

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/span/label[1]')#仅需要
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/span/label[2]')#需要
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/span/label[3]/label')#每
        self.dr.type('id->passengerInfoPerNumInput','***')#***个

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/div/label[1]')#姓名
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/div/label[2]')#手机

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/div/label[3]')#身份证
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/div/label[4]')#护照
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/div/label[5]')#台胞证
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/div/label[6]')#港澳通行证

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/div/label[7]/label')
        self.dr.type('name->needPassengerInfoOther1','***')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/div/label[8]/label')
        self.dr.type('name->needPassengerInfoOther2','***')

        #地区限制
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/input[1]')
        self.dr.sleep(2)
        self.dr.click('name->areaLimit_select')

        #时间限制
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[1]/td/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[1]/td/label[2]/label')
        self.dr.type('name->enterSightAdvanceDay','***')
        self.dr.click('name->enterSightAdvanceHour')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->enterSightAdvanceMinute')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')
        self.dr.sleep(2)

        #手机限制
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[2]/th/label')

        self.dr.click('name->limitTimeType_MOBILE')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[2]/td/select[1]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->limitTimeNum_MOBILE')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[2]/td/select[2]/option[1]')
        self.dr.sleep(2)
        self.dr.type('name->limitAmountNum_MOBILE','***')

        #身份证限制
        self.dr.sleep('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[3]/th/label')

        self.dr.click('name->limitTimeType_IDCARD')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[3]/td/select[1]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->limitTimeNum_IDCARD')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[3]/td/select[2]/option[1]')
        self.dr.sleep(2)
        self.dr.type('name->limitAmountNum_IDCARD','***')

        #出售时间 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[4]/td/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[4]/td/label[2]/input[1]')
        self.dr.click('id->saleStartTime')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(3)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('name->saleEndTime')
        self.dr.sleep(1)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('xpath->/html/body/div/div[6]/input[2]')
        self.dr.sleep(1)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[4]/td/label[3]')

        #兑换凭证 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[6]/td/label[1]')#确认短信
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[6]/td/label[2]')#身份证
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[6]/td/label[3]')#短信和身份证
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[6]/td/label[4]')#电子邮件

        #使用方式 *
        self.dr.type('name->pickupAddress','***')

        self.dr.type('name->pickupTime','***')

        #使用地址 *
        self.dr.type('name->passAddress','***')

        #短信模板 *
        self.dr.click('id->smsThemeId')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[9]/td/div/ul/li[1]')

        #价格库存模式（默认） *
        #价格库存 *
        #编辑价格
        self.dr.click('id->modifyprice')
        self.dr.sleep(2)
        self.dr.click('id->startDate_2')
        #TODO
        self.dr.click('id->endDate_2')
        #TODO
        self.dr.type('id->marketPrice_2','***')#票面价
        self.dr.type('id->stockNum_2','***')#整体库存
        self.dr.type('id->sellPrice_2','***')#售卖价
        self.dr.type('id->minimum_2','***')#最少购买
        self.dr.type('id->maximum_2','***')#最多购买
        self.dr.click('xpath->//*[@id="totalStock"]/div[2]/div[4]/input[1]')#保存
        self.dr.click('xpath->//*[@id="totalStock"]/div[2]/div[4]/input[2]')#取消
        #价格库存 *

        #商品调价
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[14]/td/label[1]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[14]/td/label[2]')

        #退款设置
        #可以退款：
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[16]/td/label[1]/input[1]')
        #列表1：
        self.dr.click('name->partRefund')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[16]/td/label[1]/select[1]/option[1]')
        #列表2：
        self.dr.click('id->refundChargeType')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="refundChargeType"]/option[1]')
        #输入
        self.dr.type('id->refundCharge','***')
        #不可退款
        self.dr.click('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[16]/td/label[2]')

        #退款审核
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[1]')
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[2]')

        #退款说明 *
        self.dr.type('name->refundInfo','***')

        #购买条款 *
        self.dr.switch_to_frame('xpath->//*[@id="inputForm"]/table[3]/tbody/tr[20]/td/div/div[2]/iframe')
        self.dr.sleep(3)
        self.dr.type('xpath->/html/body','***')
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')

        #保存
        self.dr.click('xpath->//*[@id="inputForm"]/table[4]/tbody/tr/td/input[1]')

        #返回
        self.dr.click('xpath->//*[@id="inputForm"]/table[4]/tbody/tr/td/input[2]')
