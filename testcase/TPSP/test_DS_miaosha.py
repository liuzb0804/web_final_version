# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_miaosha(mytest.MyTest):
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

        self.dr.click('id->890')#秒杀
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

        #商品名称 *
        self.dr.type('name->name','***')

        #所属地区 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/span/select[1]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/span/select/option[4]')#省
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/span/select[2]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/span/select[2]/option[2]')#市
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/span/select[3]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/span/select[3]/option[2]')#县

        #对接接口
        self.dr.click('id->appkeyType')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="appkeyType"]/option[2]')
        self.dr.type('name->outSn','***')

        #商户
        self.dr.click('id->supplierName')
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[6]/div[2]/table/tbody/tr[1]')

        #验票人
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/label')

        self.dr.click('id->selectCheckTicketMember')

        #商品图片 *
        self.dr.click('xpath->/html/body/div[8]')
        self.dr.sleep(2)
        os.system('D:\WinClick2.exe')#******
        self.dr.sleep(2)

        #商品封面图
        self.dr.click('id->logoUploadBox_1_1')
        self.dr.sleep(2)
        os.system('D:\WinClick4.exe')#******
        self.dr.sleep(2)

        #销售渠道
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[1]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[2]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[3]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[4]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[5]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[2]')

        #抢购时间 *
        self.dr.click('id->saleStartTime')
        self.dr.sleep(2)
        #TODO
        self.dr.click('id->saleEndTime')
        self.dr.sleep(2)
        #TODO

        #取消设置
        self.dr.type('name->autoCancelTime','***')

        #所需信息
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/label[3]')

        #手机限购
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/th/label')

        self.dr.click('name->limitTimeType_MOBILE')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label/select[1]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->limitTimeNum_MOBILE')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label/select[2]/option[1]')
        self.dr.sleep(2)
        self.dr.type('name->limitAmountNum_MOBILE','***')


        #身份证限购
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/th/label')

        self.dr.click('name->limitTimeType_IDCARD')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/td/label/select[1]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->limitTimeNum_IDCARD')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/td/label/select[2]/option[1]')
        self.dr.sleep(2)
        self.dr.type('name->limitAmountNum_IDCARD','***')

        #短信模板 *
        self.dr.click('id->smsThemeId')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/div/ul/li[1]')

        #运费模板
        self.dr.click('id->deliverTemplateId')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[17]/td/div/ul/li[2]')

        #价格库存 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[18]/td/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[18]/td/label[2]')

        #验证消费日期 *
        self.dr.click('xpath->//*[@id="consumeAuthen"]/td/label[1]')

        self.dr.click('id->consumeAuthenType_OUTSIDE_DATE')
        self.dr.click('name->beforeDay')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="consumeAuthen"]/td/label[2]/select[1]/option[2]')
        self.dr.sleep(2)
        self.dr.click('name->afterDay')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="consumeAuthen"]/td/label[2]/select[2]/option[2]')

        #价格库存 *
        #TODO

        #时间限制
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[22]/td/label[1]')

        self.dr.click('xpaht->//*[@id="inputForm"]/table[1]/tbody/tr[22]/td/label[2]/label')
        self.dr.type('name->enterSightAdvanceDay','***')
        self.dr.click('name->enterSightAdvanceHour')
        self.dr.sleep(2)
        self.dr.click('name->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->enterSightAdvanceMinute')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')

        #退款设置
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[23]/td/label[1]/input[1]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[23]/td/label[1]/select[1]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[23]/td/label[1]/select[1]/option[1]')
        self.dr.sleep(2)
        self.dr.click('id->refundChargeType')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="refundChargeType"]/option[1]')
        self.dr.sleep(2)
        self.dr.type('id->refundCharge','***')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[23]/td/label[2]')

        #退款审核
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[1]')

        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[2]')

        #退款说明 *
        self.dr.type('name->refundInfo','***')

        #抢购须知 *
        self.dr.switch_to_frame('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[27]/td/div/div[2]/iframe')
        self.dr.sleep(3)
        self.dr.type('xpath->/html/body','***')
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #商品描述 *
        self.dr.switch_to_frame('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[28]/td/div/div[2]/iframe')
        self.dr.sleep(3)
        self.dr.type('xpath->/html/body','***')
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #使用说明 *
        self.dr.switch_to_frame('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[29]/td/div/div[2]/iframe')
        self.dr.sleep(3)
        self.dr.type('xpath->/html/body','***')
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #保存
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[1]')

        #返回
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[2]')

