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
    用例编号：px_htgl_006
    模块：门票
    功能点：添加
    测试点描述：正常添加
    测试步骤：
        1、进入门票添加页
        2、信息填写正确完整
        3、点击“保存”
    预期结果：
        1、提示保存成功，返回到列表页
        2、列表上和数据库中存在已保存的信息
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

        self.dr.click('id->792')#门票
        time.sleep(3)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        #************************* before check ********************
        text_before = self.dr.get_text('xpath->//*[@id="listForm"]/div[4]')

        #************************** actions ************************
        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[1]')#点击添加
        time.sleep(2)

        #基本信息
        self.dr.click('id->companyName')
        time.sleep(1)
        self.dr.click('xpath->/html/body/div[5]/div[2]/table/tbody/tr[1]')#选择景区
        time.sleep(1)

        self.dr.click('id->companyType')
        time.sleep(2)
        self.dr.click('xpath->//*[@id="companyType"]/option[2]')#选择票型
        time.sleep(1)

        self.dr.type('name->name','123321')#产品名称

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/span/label')#服务特色

        self.dr.click('id->appkeyType')
        time.sleep(2)
        self.dr.click('xpath->//*[@id="appkeyType"]/option[2]')
        time.sleep(1)
        self.dr.type('name->outSn','123')#对接接口

        self.dr.click('id->supplierName')
        time.sleep(2)
        self.dr.click('xpath->/html/body/div[6]/div[2]/table/tbody/tr[1]')#商户
        time.sleep(1)

        self.dr.click('id->selectCheckTicketMember')#其他验票人
        time.sleep(2)
        self.dr.click('xpath->//*[@id="listTable"]/tbody/tr[2]')#验票人
        time.sleep(1)

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/div/div[2]/ul/li/div/a')
        time.sleep(2)
        os.system('D:\WinClick4.exe')#商品头图
        time.sleep(2)

        self.dr.click("id->logoUploadBox_1_1")
        time.sleep(2)
        os.system('D:\WinClick4.exe')#商品封面图
        time.sleep(2)

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[11]/td/label[1]/label[1]')#销售渠道
        time.sleep(1)

        #预订设置
        self.dr.type('name->autoCancelTime','3')#取消设置

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label[3]')#联系人信息   【3】:拼音

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/th/label')#客人信息

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/label[2]/label')#时间限制

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[17]/th/label/label')#手机限制

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[18]/th/label/label')#身份证限制

        self.dr.click('name->displayWay')#出售时间 *

        #入园设置
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[2]')#兑换凭证 *

        self.dr.click('name->passType')#入园方式 *

        self.dr.type('name->passAddress','*******')#入园地址 *

        self.dr.click('id->smsThemeId')
        time.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[24]/td/div/ul/li[1]')#短信模板
        time.sleep(2)

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[25]/td/label[2]')#入园次数

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[26]/td/label[2]')#入园人数

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[27]/th/label')#入园时间限制
        time.sleep(2)
        self.dr.type('name->enterSightDelayBookHour','1')#小时
        time.sleep(1)
        self.dr.type('name->enterSightDelayBookMinute','1')#分钟

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[28]/th/label')#入园时间
        time.sleep(1)
        self.dr.type('name->useTimeRangeStart','18:00')#前
        time.sleep(1)
        self.dr.type('name->useTimeRangeEnd','18:30')#后

        #价格库存
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[30]/td/label[1]')#价格库存模式  1;日历模式  2：总库存模式
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[30]/td/label[2]')

        #验证消费日期
        self.dr.click('xpath->//*[@id="consumeAuthen"]/td/label[1]')

        #价格库存
        #TODO

        #商品调价
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/label[2]')

        #退款信息
        #退狂设置
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[36]/td/label[1]')#可以退款

        #退款审核
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[1]')#需要审核

        #退款日期
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[38]/td/label[1]')#限制

        #退款说明
        self.dr.type('name->refundInfo','*************')

        #产品说明
        #费用包含
        self.dr.type('name->feeInfo','************')

        #费用不含
        self.dr.type('name->feeExclude','**********')

        #使用说明
        self.dr.switch_to_frame('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[43]/td/div/div[2]/iframe')#iframe
        time.sleep(3)
        self.dr.type('xpath->/html/body','************')


        self.dr.switch_to_frame_out()
        time.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        #保存/返回
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[1]')


        #************************ check after ************************
        text = self.dr.get_element('xpath->//*[@id="listForm"]/div[4]')
        if text != None:
            text_after = text.text
            if text_after == text_before:
                pass
            else:raise SyntaxWarning
        else:raise SystemError