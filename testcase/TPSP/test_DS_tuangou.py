# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_tuangou(mytest.MyTest):
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

        self.dr.click('id->798')#团购
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

        #推荐理由
        self.dr.type('name->reason','***')

        #服务特色 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[4]/td/span/label')#随时退
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[4]/td/span/span')

        #商品图片 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/div/div[2]/ul/li/div/a')
        self.dr.sleep(3)
        os.system('D:\WinClick4.exe')
        self.dr.sleep(3)

        #商品封面图
        self.dr.click('id->logoUploadBox_1_1')
        self.dr.sleep(3)
        os.system('D:\WinClick4.exe')
        self.dr.sleep(3)

        #商户
        self.dr.click('id->supplierName')
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[6]/div[2]/table/tbody/tr[1]')
        self.dr.sleep(2)

        #验票人
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label')

        self.dr.click('id->selectCheckTicketMember')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->/html/body/div[9]/div[3]/div/iframe')
        self.dr.sleep(3)
        self.dr.click('id->selectAll')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('xpath->/html/body/div[9]/div[4]/input[1]')
        self.dr.sleep(2)

        #销售渠道
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[1]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[2]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[3]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[4]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[5]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[2]')

        #取消设置
        self.dr.type('name->autoCancelTime','***')

        #联系人信息
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/label[3]')

        #客人信息
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/th/label')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/span/label[1]')#默认
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/span/label[2]')#不需要

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[1]')#姓名
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[2]')#拼音
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[3]')#手机

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[4]')#身份证
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[5]')#护照
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[6]')#台胞证
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[7]')#港澳通行证

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[8]/input[1]')
        self.dr.type('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[8]/input[2]','***')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[9]/input[1]')
        self.dr.type('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/div/label[9]/input[2]','***')

        #预订限制
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label[1]')#默认

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label[2]/input[1]')
        self.dr.type('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label[2]/input[2]','***')
        self.dr.click('name->enterSightAdvanceHour')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')
        self.dr.click('name->enterSightAdvanceMinute')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')

        #生效时间
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/th/label')

        self.dr.type('name->enterSightDelayBookHour','***')

        #手机限制
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/th/label')

        self.dr.click('name->limitTimeType_MOBILE')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/select[1]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->limitTimeNum_MOBILE')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/select[2]/option[1]')
        self.dr.sleep(2)
        self.dr.type('name->limitAmountNum_MOBILE','***')

        #身份证限制
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[17]/th/label')

        self.dr.click('name->limitTimeType_IDCARD')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[17]/td/select[1]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->limitTimeNum_IDCARD')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[17]/td/select[2]/option[1]')
        self.dr.sleep(2)
        self.dr.type('name->limitAmountNum_IDCARD','***')

        #出售时间 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[18]/td/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[18]/td/label[2]/input[1]')
        self.dr.click('id->saleStartTime')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div/div[6]/input[2]')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[18]/td/label[2]/input[3]')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(3)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #短信模板 *
        self.dr.click('id->smsThemeId')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/div/ul/li[1]')

        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/a')

        #价格库存模式 *
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[1]')

        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[2]')

        #验证消费日期 *
        self.dr.click('xpath->//*[@id="consumeAuthen"]/td/label[1]/label')

        self.dr.click('xpath->//*[@id="consumeAuthen"]/td/label[2]/label')
        self.dr.click('id->consumeStartDate')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->/html/body/div[7]/iframe')
        self.dr.sleep(2)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('id->consumeEndDate')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[18]/td/label[3]')

        #价格库存 *
        #批量上架
        self.dr.click('id->batchset')
        self.dr.sleep(2)
        self.dr.click('id->startDate_1')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(2)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(3)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('id->endDate_1')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(3)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[1]')#星期1
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[2]')#星期2
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[3]')#星期3
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[4]')#星期4
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[5]')#星期5
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[6]')#星期6
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[7]')#星期7

        self.dr.type('id->marketPrice_1', '100')#票面价
        self.dr.type('id->stockNum_1', '100')#每日库存
        self.dr.type('id->sellPrice_1', '100')#售卖价
        self.dr.type('id->minimum_1', '100')#最少购买
        self.dr.type('id->maximum_1', '100')#最多购买

        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[4]/input[1]')#保存
        # self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[4]/input[2]')#取消
        self.dr.sleep(2)
        # 批量下架
        self.dr.click('id->batchunset')
        self.dr.sleep(3)
        self.dr.click('id->startDate_3')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(2)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[2]/div/label[2]')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[1]')#1
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[2]')#2
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[3]')#3
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[4]')#4
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[5]')#5
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[6]')#6
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[7]')#7

        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[4]/input[1]')#确定
        # self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[4]/input[2]')#取消
        self.dr.sleep(2)
        #全部下架
        self.dr.click('id->clearall')

        #商品调价
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[25]/td/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[25]/td/label[2]')

        #退款设置
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[27]/td/label[1]/input[1]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[27]/td/label[1]/select[1]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[27]/td/label[1]/select[1]/option[1]')
        self.dr.sleep(2)
        self.dr.click('id->refundChargeType')
        self.dr.sleep(2)
        self.dr.type('id->refundCharge','***')

        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[27]/td/label[2]')

        #退款审核
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[1]')

        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[2]')

        #退款说明 *
        self.dr.type('name->refundInfo','***')

        #所属商家 * （类型：餐饮，旅游，生活。。选择不同显示选项不同。此为旅游）
        self.dr.click('id->businessOfTeamName')
        self.dr.sleep(3)
        self.dr.click('xpath->//html/body/div[5]/div[2]/table/tbody/tr[7]')
        self.dr.sleep(3)

        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[31]/td/a')#添加商家

        #所属分类 *
        #根据商家

        #商品头图
        self.dr.click('xpath->//*[@id="headImage"]/td/div/div/ul/li/div/a')
        self.dr.sleep(3)
        os.system('D:\WinClick4.exe')#********
        self.dr.sleep(3)

        #性别
        # self.dr.click('xpath->//*[@id="sex"]/td/label[1]')

        self.dr.click('xpath->//*[@id="sex"]/td/label[2]')

        #相关证件号
        self.dr.type('name->certificate','***')

        #特色服务
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="specialty"]/td/div/div[2]/iframe')
        self.dr.sleep(3)
        self.dr.type('xpath->/html/body','***')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #费用说明
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="feeInfo"]/td/div/div[2]/iframe')
        self.dr.sleep(3)
        self.dr.type('xpath->/html/body','***')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #温馨提示
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="memo"]/td/div/div[2]/iframe')
        self.dr.sleep(3)
        self.dr.type('xpath->/html/body','***')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #套餐详情
        self.dr.switch_to_frame('xpath->//*[@id="detail"]/td/div/div[2]/iframe')
        self.dr.sleep(3)
        self.dr.type('xpath->/html/body','***')
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #保存
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[1]')

        #返回
        # self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[2]')

